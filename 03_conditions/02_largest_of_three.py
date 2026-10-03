def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("pehla number: "))
num2 = int(input("dusra number: "))
num3 = int(input("tisra number: "))

print("sabse bada number hai:", largest(num1, num2, num3))