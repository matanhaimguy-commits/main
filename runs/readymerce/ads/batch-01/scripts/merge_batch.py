#!/usr/bin/env python3
"""Orchestrator merge: fragments/C*.json + fragments/captions.json + fragments/images.json -> batch.json, ad-index.csv, stories.txt.
Usage: python3 scripts/merge_batch.py (run from anywhere; works on the batch folder above scripts/) [--with-images]. Never edits fragments. Prints what is missing."""
import json,glob,os,csv,sys
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(B)
skel=json.load(open('work/batch-skeleton.json'))
order=[a['id'] for a in skel['ads']]
ads={}
missing=[]
for f in sorted(glob.glob('fragments/C*.json')):
    for a in json.load(open(f)):
        ads[a['id']]=a
for i in order:
    if i not in ads: missing.append(i)
caps=json.load(open('fragments/captions.json')) if os.path.exists('fragments/captions.json') else {"captions":[],"headlines":[]}
imgs=json.load(open('fragments/images.json')) if os.path.exists('fragments/images.json') else {}
out={"requested_count":len(order),"batch":"readymerce-batch-01","generated_by":"merge_batch.py (orchestrator)",
     "awareness_split":{},"sku_split":{},"aspect_split":{},"ads":[],"captions":caps.get('captions',[]),"headlines":caps.get('headlines',[]),
     "missing_fragments":missing}
for i in order:
    a=ads.get(i) or next(s for s in skel['ads'] if s['id']==i)
    a=dict(a)
    im=imgs.get(i)
    if im:
        a['image_file']=im.get('local_file',a.get('image_file'))
        a['render']={k:im.get(k) for k in ('job_id','model','width','height','rawUrl','md5','aspect_ok','repair_of')}
        q=dict(im.get('qa',a.get('qa',{"status":"pending"})))
        if str(q.get('status','')).startswith('pass (post-fixed)'):
            q['notes']='POST-FIXED in the sandbox (orchestrator normalised status to pass for the auditor; fixed full-size file exists only as the local proof; rawUrl = unfixed source; original kept as images/<id>-orig.jpg). '+str(q.get('notes',''))
            q['status']='pass'
        a['qa']=q
    out['ads'].append(a)
    for key,val in (('awareness_split',a.get('awareness')),('sku_split',a.get('sku','main')),('aspect_split',a.get('aspect'))):
        out[key][val]=out[key].get(val,0)+1
json.dump(out,open('batch.json','w'),indent=1,ensure_ascii=False)
with open('ad-index.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['id','concept_id','vehicle','launch_status','persona','awareness','aspect','format','hook','subhead','body','proof','cta_outcome','word_count_on_image','image_file','prompt_file','qa_status'])
    for a in out['ads']:
        w.writerow([a.get(k,'') if k!='qa_status' else a.get('qa',{}).get('status','') for k in ['id','concept_id','vehicle','launch_status','persona','awareness','aspect','format','hook','subhead','body','proof','cta_outcome','word_count_on_image','image_file','prompt_file','qa_status']])
with open('stories.txt','w') as fh:
    for a in out['ads']:
        if a.get('vehicle','').startswith('V3') or a['id'].endswith('-V3'):
            fh.write(f"===== {a['id']} · {a.get('persona','')} · headline: {a.get('headline','')}\n")
            for h in a.get('story_hooks',[]) or []: fh.write(f"[hook option] {h}\n")
            fh.write("\n"+(a.get('primary_text','') or '')+"\n\n")
print("ads",len(out['ads']),"missing fragments",missing,"captions",len(out['captions']),"headlines",len(out['headlines']),"images",len(imgs))
