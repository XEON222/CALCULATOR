import math
print("i am a calculator||||For square root type [square root] without big brackets")
a = float(input("First number?/Square root yr number?/Radius?/length?"))
b = float(input("second number?/power?/breath?/height?"))
c = str(input("operation?"))

if c == "+":
    print(a+b)

if c == "-":
    print(a-b)

if c == "*":
    print(a*b)

if c == "/":
    print(a/b)

if c == "square root":
    d = math.sqrt(a)
    print(d)

if c == "power":
    print(a**b)

if c == "divisible by":
    if a%b == 0:
        print(a, "is divisible by", b)
    else:
        print(a, "is not divisible by", b)

if c == "percentage":
    print((a/b)*100)

if c == "area cir":
    d = 22/7
    print("area of circle is", (a**2)*d, "cm square")

if c == "area tri":
    print("area of triangle is", (a*b)/2, "cm square")