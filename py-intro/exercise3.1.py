hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    pay = h*r
else:
    newh = h-40
    newh = 5*(r*1.5)
    pay = (40*r)+newh
print(pay)
