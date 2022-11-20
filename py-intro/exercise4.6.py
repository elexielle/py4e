def computepay(h,r):
    if h <= 40:
        origp = h*r
        return origp
    if h > 40:
        origp = h*r
        exp = (xh/2)*r
        totalp = origp + exp
        return totalp


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
r = float(rate)
h = float(hrs)
xh = h - 40
p = computepay(h,r)
print("Pay",p)
