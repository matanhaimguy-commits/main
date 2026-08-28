# CHECK 6 - PROFIT MATH (geo_mode=UK). All inputs printed. VAT line included.
VAT = 0.20
def block(name, retail, landed_lo, landed_hi, comps, budget=4000.0):
    landed = round((landed_lo+landed_hi)/2, 2)
    print("="*74); print(name); print("="*74)
    net = retail/(1+VAT)                      # UK: retail is VAT-inclusive
    gp   = net - landed
    marg = gp/net
    mult = net/landed
    print(f"retail (VAT-inc)      GBP {retail:.2f}")
    print(f"net revenue (ex-VAT)  GBP {net:.2f}   [retail/1.20 - UK VAT line]")
    print(f"landed COGS band      GBP {landed_lo:.2f}-{landed_hi:.2f}  -> midpoint GBP {landed:.2f}  [ASSUMPTION: SOURCE-CONDITIONAL]")
    print(f"gross profit          GBP {gp:.2f}")
    print(f"gross margin          {marg*100:.1f}%     multiple {mult:.2f}x")
    hard = (gp>=20) and (marg>=0.60) and (mult>=3)
    print(f"HARD GATE (GP>=GBP20 . margin>=60% . multiple>=3): {'PASS' if hard else 'FAIL'}")

    # Day-1 AOV model - DEFAULT take rates
    r = {"bump":0.40, "cart":0.25, "oto1":0.10, "oto2":0.08}
    print(f"\nDay-1 AOV model (DEFAULT take rates: bump {r['bump']:.0%}, cart {r['cart']:.0%}, OTO1 {r['oto1']:.0%}, OTO2 {r['oto2']:.0%} of OTO1 decliners)")
    aov = retail; cogs = landed
    for k,(nm,price,cst) in comps.items():
        take = r[k] if k!="oto2" else r["oto1"]*0  # placeholder, handled below
        if k=="oto2":
            take = (1-r["oto1"])*r["oto2"]
        else:
            take = r[k]
        aov  += price*take
        cogs += cst*take
        print(f"  {k:5s} {nm:34s} GBP {price:6.2f}  landed GBP {cst:5.2f}  take {take*100:5.2f}%")
    aov_net = aov/(1+VAT)
    fees    = 0.029*aov          # payment fees on gross
    refund  = 0.05*aov           # refund reserve on gross
    ship    = 2.50               # absorbed UK delivery [ASSUMPTION]
    cm      = aov_net - cogs - fees - refund - ship
    print(f"\n  blended AOV (VAT-inc)   GBP {aov:.2f}")
    print(f"  AOV ex-VAT              GBP {aov_net:.2f}")
    print(f"  weighted landed COGS    GBP {cogs:.2f}")
    print(f"  payment fees 2.9%       GBP {fees:.2f}")
    print(f"  refund reserve 5%       GBP {refund:.2f}")
    print(f"  shipping absorbed       GBP {ship:.2f}  [ASSUMPTION]")
    print(f"  CM / order              GBP {cm:.2f}")
    be  = cm
    anchor = min(aov/2, be)
    print(f"  breakeven CPA           GBP {be:.2f}")
    print(f"  cpa_anchor = min(AOV/2={aov/2:.2f}, breakeven={be:.2f}) = GBP {anchor:.2f}  [PROVISIONAL]")
    dev = (anchor-32)/32*100
    print(f"  vs UK sanity ref GBP32: {dev:+.1f}%  {'<-- FLAG >50% deviation' if abs(dev)>50 else '(within 50%)'}")
    od = budget/(30*anchor)
    lab = "FUNDABLE" if od>=2 else ("STRETCH" if od>=1 else "NOT FUNDABLE")
    print(f"\n  FUNDABILITY: GBP{budget:.0f}/mo / (30 x {anchor:.2f}) = {od:.2f} test orders/day -> {lab}")

    print(f"\n  SCALE SKETCH @ GBP800/day (UK)          | and @ client budget GBP{budget/30:.0f}/day")
    print(f"  {'CVR':>5} {'CPC':>6} {'clicks':>8} {'orders':>7} {'CPA':>8} {'rev/day':>9} {'CM/day':>8}")
    for cvr in (0.020,0.025,0.035):
        for cpc in (0.65,1.00,1.40):
            clicks=800/cpc; orders=clicks*cvr; cpa=800/orders
            print(f"  {cvr*100:4.1f}% {cpc:6.2f} {clicks:8.0f} {orders:7.1f} {cpa:8.2f} {orders*aov:9.0f} {orders*cm-800:8.0f}")
    d=budget/30
    print(f"  -- at client budget GBP{d:.0f}/day --")
    for cvr in (0.020,0.025,0.035):
        cpc=1.00; clicks=d/cpc; orders=clicks*cvr; cpa=d/orders if orders else 0
        print(f"  {cvr*100:4.1f}% {cpc:6.2f} {clicks:8.0f} {orders:7.1f} {cpa:8.2f} {orders*aov:9.0f} {orders*cm-d:8.0f}")
    print()
    return dict(retail=retail,net=round(net,2),landed=landed,gp=round(gp,2),margin=round(marg,4),
                multiple=round(mult,2),aov=round(aov,2),cm=round(cm,2),be=round(be,2),
                anchor=round(anchor,2),orders_day=round(od,2),fund=lab,hard=hard)

A = block("OPP-1  TMJ / JAW-TENSION RELIEF PEN  (retail GBP49)", 49.00, 8.00, 14.00, {
  "bump": ("Reusable jaw heat/cold gel pack", 14.99, 3.00),
  "cart": ("Trigger-point release ball set",  19.99, 4.00),
  "oto1": ("2nd pen (partner/gift)",          34.99, 11.00),
  "oto2": ("Travel case + spare tips",        12.99, 2.50)})

B = block("OPP-2  CORDLESS HANDHELD VACUUM SEALER  (retail GBP39)", 39.00, 9.00, 15.00, {
  "bump": ("30 reusable vacuum bags",   16.99, 4.00),
  "cart": ("3 vacuum containers S/M/L", 24.99, 7.00),
  "oto1": ("2nd sealer (gift)",         29.99, 12.00),
  "oto2": ("60-bag refill pack",        19.99, 5.00)})

import json; print(json.dumps({"OPP-1":A,"OPP-2":B}, indent=1))
