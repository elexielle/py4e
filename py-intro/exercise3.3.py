xs = input("Enter Score:")
try:
    fs = float(xs)
except:
    print("Error")
    quit()

if fs >= 0.9:
    print("A")
elif fs >= 0.8:
    print("B")
elif fs >= 0.7:
    print("C")
elif fs >= 0.6:
    print("D")
elif fs < 0.6:
    print("F")
else:
    print("Error")
