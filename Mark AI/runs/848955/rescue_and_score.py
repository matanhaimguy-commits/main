VAT=0.20
def gate(retail, landed):
    net=retail/(1+VAT); gp=net-landed; m=gp/net; x=net/landed
    return net,gp,m,x,(gp>=20 and m>=0.60 and x>=3)
print("OPP-2 RETAIL SENSITIVITY (landed midpoint GBP12.00) -- Chef Preserve US tier = $69.99 ~ GBP52")
print(f"{'retail':>7} {'net exVAT':>10} {'GP':>7} {'margin':>7} {'mult':>6}  gate")
for r in (39,43,45,47,49,52):
    net,gp,m,x,ok=gate(r,12.00)
    print(f"{r:7.2f} {net:10.2f} {gp:7.2f} {m*100:6.1f}% {x:5.2f}x  {'PASS' if ok else 'FAIL'}")
print("\nOPP-2 landed-band stress at retail GBP49:")
for l in (9,12,15):
    net,gp,m,x,ok=gate(49,l)
    print(f"  landed GBP{l:5.2f} -> GP GBP{gp:6.2f}  margin {m*100:5.1f}%  mult {x:4.2f}x  {'PASS' if ok else 'FAIL'}")
print("\nOPP-1 landed-band stress at retail GBP49:")
for l in (8,11,14):
    net,gp,m,x,ok=gate(49,l)
    print(f"  landed GBP{l:5.2f} -> GP GBP{gp:6.2f}  margin {m*100:5.1f}%  mult {x:4.2f}x  {'PASS' if ok else 'FAIL'}")

# STEP 10 - fixed rubric /100
R={"wedge":20,"money":15,"econ":20,"demand":10,"emotion":10,"source":10,"content":5,"avatar":5,"route":5}
def score(n,s,caps,notes):
    t=sum(s.values()); c=min(caps) if caps else 100; f=min(t,c)
    print(f"\n{n}\n  " + "  ".join(f"{k} {s[k]}/{R[k]}" for k in R))
    print(f"  raw {t}/100 | caps applied {caps} -> FINAL {f}/100")
    for x in notes: print(f"    - {x}")
    return f
print("\n"+"="*74+"\nSTEP 10 - COMPARISON (fixed rubric /100)\n"+"="*74)
a=score("OPP-1 TMJ jaw-tension relief pen (UK)",
  {"wedge":18,"money":13,"econ":18,"demand":8,"emotion":10,"source":5,"content":5,"avatar":5,"route":5},
  [70],["GB density 35 ads vs US 1,007 - genuine geo vacancy",
        "single dominant operator (yourTMJ 507 ads across 2 records)",
        "CAP 70: SOURCE-CONDITIONAL (no per-unit listing retrievable)"])
b=score("OPP-2 Cordless handheld vacuum sealer (UK)",
  {"wedge":10,"money":14,"econ":11,"demand":9,"emotion":8,"source":5,"content":5,"avatar":3,"route":4},
  [70],["GB already served: 412 active ads",
        "GBP10.99 GoGroopie anchor vs required GBP49 retail",
        "CAP 70: SOURCE-CONDITIONAL"])
print(f"\nRANK: 1) OPP-1 {a}/100   2) OPP-2 {b}/100")
