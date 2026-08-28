def route(name, reads, soph_shift, soph_label, fmt_override=False):
    s=sum(1 for v in reads.values() if v=="STATIC+"); n=sum(1 for v in reads.values() if v=="NATIVE+")
    z=sum(1 for v in reads.values() if v=="0")
    print("="*70); print(name); print("="*70)
    for k,v in reads.items(): print(f"  {k:26s} {v}")
    print(f"  tally: STATIC+ {s} | NATIVE+ {n} | NEUTRAL {z}")
    gap=abs(s-n); lead="STATIC" if s>n else ("NATIVE" if n>s else "TIE")
    base = 50 if lead=="TIE" else (80 if gap>=3 else 70)
    print(f"  base lead = {lead}, margin {gap} -> base split {base}/{100-base}")
    lead_share=base
    if lead=="STATIC": lead_share += soph_shift
    elif lead=="NATIVE": lead_share += soph_shift
    lead_share=min(lead_share,90)
    print(f"  sophistication {soph_label} -> shift {soph_shift:+d} toward {lead} -> {lead_share}/{100-lead_share} (cap 90)")
    print(f"  FORMAT-wedge override: {'APPLIED' if fmt_override else 'not applicable (FORMAT is not the primary wedge)'}")
    if 40<=lead_share<=60: verdict="MIXED"
    else: verdict = "STATIC_DR_LED" if lead=="STATIC" else "NATIVE_STORY_LED"
    print(f"  FINAL -> {verdict}  split {lead_share}/{100-lead_share}\n")

route("OPP-1  TMJ JAW-TENSION RELIEF PEN",
 {"Demonstrability":"NATIVE+","Trust burden":"NATIVE+","Consideration (GBP49>38)":"NATIVE+",
  "Problem privacy":"0","Buyer awareness mass":"STATIC+"}, 10, "L4 (mechanism language everywhere)")

route("OPP-2  CORDLESS VACUUM SEALER",
 {"Demonstrability":"STATIC+","Trust burden":"STATIC+","Consideration (GBP49>38)":"NATIVE+",
  "Problem privacy":"STATIC+","Buyer awareness mass":"STATIC+"}, 10, "L2 (few brands, same basic claim)")
