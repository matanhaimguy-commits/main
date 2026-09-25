#!/usr/bin/env python3
"""Orchestrator finalizer: merge -> gallery.html, source-notes.md, qa-notes.md, campaign-spec.json ads rows, campaign.zip, final audit. Read-only on fragments/ and ads/."""
import json,os,re,subprocess,glob,csv,zipfile,html,sys
B=os.path.dirname(os.path.abspath(__file__)); os.chdir(B)
SK='/root/.claude/skills/synced/ecbb512e-baad-4579-8fb7-650b733b4f86_5b0c7e87-40d3-427d-b2a8-b08eea6731f4/readymerce-ads-machine/scripts/audit_batch.py'
subprocess.run([sys.executable,'merge_batch.py'],check=True)
b=json.load(open('batch.json'))
caps={c['id']:c for c in b['captions']}
# pairing map: first CAP-## token on a line that names the ad id
pair={}
if os.path.exists('work/pairing-map.md'):
    for line in open('work/pairing-map.md'):
        for a in b['ads']:
            if a['id'] in line:
                m=re.search(r'CAP-0[1-5]',line)
                if m and a['id'] not in pair: pair[a['id']]=m.group(0)
# gallery
rows=[]
for a in b['ads']:
    img=a.get('image_file','')
    exists=os.path.exists(img)
    r=a.get('render',{}) or {}
    rows.append(f"""<div class="card"><h3>{html.escape(a['id'])} · {html.escape(a.get('vehicle',''))} · {html.escape(a.get('aspect',''))} · {html.escape(a.get('launch_status',''))}</h3>
{'<img src="'+html.escape(img)+'">' if exists else '<div class="missing">no local proof copy</div>'}
<p><b>persona</b> {html.escape(str(a.get('persona','')))}<br><b>angle</b> {html.escape(str(a.get('angle',''))[:220])}<br><b>hook</b> {html.escape(str(a.get('hook','')))}<br><b>subhead</b> {html.escape(str(a.get('subhead','')))}<br><b>body</b> {html.escape(str(a.get('body','')))}<br><b>proof</b> {html.escape(str(a.get('proof','')))}<br><b>CTA</b> {html.escape(str(a.get('cta_outcome','')))}<br><b>caption</b> {html.escape(pair.get(a['id'],'story (own primary text)' if a['id'].endswith('-V3') else 'CAP-01'))}<br><b>render</b> {html.escape(str(r.get('width','?')))}×{html.escape(str(r.get('height','?')))} · qa {html.escape(str(a.get('qa',{}).get('status','')))} · {('<a href="'+html.escape(r['rawUrl'])+'">full-res</a>') if r.get('rawUrl') else ''}</p></div>""")
open('gallery.html','w').write(f"""<!doctype html><meta charset="utf-8"><title>Readymerce batch-01 gallery</title><style>body{{font-family:system-ui;margin:16px;background:#F7F4EE;color:#1C1C1A}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}}.card{{background:#fff;border:1px solid #ddd;padding:12px}}img{{width:100%;height:auto}}.missing{{padding:40px;background:#eee;text-align:center}}h3{{font-size:14px;margin:0 0 8px}}p{{font-size:12px;line-height:1.4}}</style><h1>Readymerce ads batch-01</h1><p>{len(b['ads'])} ads · launch {sum(1 for a in b['ads'] if a.get('launch_status')=='launch')} · benched {sum(1 for a in b['ads'] if a.get('launch_status')=='benched')} · local images are 800 px proof copies; full-resolution renders via the links.</p><div class="grid">{''.join(rows)}</div>""")
# source notes
with open('source-notes.md','w') as fh:
    fh.write('# SOURCE NOTES — batch-01 (concatenated from each concept file; the full working copies with trace tags live in ads/C#.md)\n\n')
    for f in sorted(glob.glob('ads/C*.md')):
        t=open(f).read(); m=re.search(r'## SOURCE NOTES.*',t,re.S)
        fh.write(f'## {f}\n\n'+(m.group(0) if m else '(no SOURCE NOTES section found)')+'\n\n')
    if os.path.exists('work/captions-sources.md'): fh.write('## captions\n\n'+open('work/captions-sources.md').read())
# qa notes
imgs=json.load(open('fragments/images.json')) if os.path.exists('fragments/images.json') else {}
vid=json.load(open('videos/C1-V.json')) if os.path.exists('videos/C1-V.json') else {}
with open('qa-notes.md','w') as fh:
    fh.write('# QA NOTES — batch-01\n\n## Images (P4; local 800 px proof copies inspected with the Read tool; full-res in the Higgsfield workspace)\n\n| id | render px | aspect ok | qa | notes | repair_of |\n|---|---|---|---|---|---|\n')
    for a in b['ads']:
        i=imgs.get(a['id'],{}); q=i.get('qa',{})
        fh.write(f"| {a['id']} | {i.get('width','')}×{i.get('height','')} | {i.get('aspect_ok','')} | {q.get('status','pending')} | {str(q.get('notes','')).replace('|','/')[:300]} | {i.get('repair_of','')} |\n")
    fh.write(f"\nimages credits used: {imgs.get('spend_credits','?')} · balance after: {imgs.get('balance_after','?')}\n\n## Video C1 (P5)\n\n")
    fh.write('```\n'+json.dumps({k:vid.get(k) for k in ('shots','stitched','credits_used','balance_after','notes') if k in vid},indent=1,ensure_ascii=False)[:6000]+'\n```\n' if vid else '(no video json yet)\n')
# campaign spec ads rows
spec=json.load(open('campaign-spec.json'))
adsets={s['name']:s for s in spec['adsets']}
rowsc=[]
for a in b['ads']:
    if a.get('launch_status')!='launch': continue
    r=a.get('render',{}) or {}
    cid=a['concept_id'] if 'concept_id' in a else a['id'].split('-')[0]
    adset=[n for n in adsets if n.startswith(cid+'-')]
    rowsc.append({"name":a['id'],"adset":adset[0] if adset else cid,"image":{"rawUrl":r.get('rawUrl'),"job_id":r.get('job_id'),"local_proof":a.get('image_file'),"qa":a.get('qa',{}).get('status')},
        "primary_text": (a.get('primary_text') if a['id'].endswith('-V3') else caps.get(pair.get(a['id'],'CAP-01'),{}).get('text')),
        "text_options": ([h.get('text') if isinstance(h,dict) else h for h in a.get('story_hooks',[])] if a['id'].endswith('-V3') else None),
        "headline": a.get('headline'),"description":"","cta_button":"SHOP_NOW","destination":"https://readymerce.com","url_params":f"utm_source=meta&utm_campaign=RM-ABO-01&utm_content={a['id']}"})
spec['ads']=rowsc; spec['status']="SPEC ONLY — not built; ads rows filled from batch.json"
json.dump(spec,open('campaign-spec.json','w'),indent=1,ensure_ascii=False)
# zip
with zipfile.ZipFile('campaign.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in ['batch.json','ad-index.csv','captions.txt','headlines.txt','stories.txt','test-plan.md','campaign-spec.json','gallery.html','qa-notes.md','source-notes.md']:
        if os.path.exists(p): z.write(p)
    for d in ['images','prompts','contact-sheets','videos','ads']:
        for p in glob.glob(d+'/**/*',recursive=True):
            if os.path.isfile(p) and not p.endswith('.partial'): z.write(p)
print('gallery, notes, spec rows',len(rowsc),'zip',os.path.getsize('campaign.zip'),'bytes')
print(subprocess.run([sys.executable,SK,'batch.json','--final'],capture_output=True,text=True).stdout[-1800:])
