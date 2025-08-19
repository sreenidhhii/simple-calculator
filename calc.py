a=input("type a number ")
op=input("type an operator ")
b=input("type an another number ")
if op== "+":
    print(int(a)+int(b))
elif op=="-":
    print(int(a)-int(b))
elif op=="*":
    print(int(a)*int(b))
elif op=="/":
    print(int(a)/int(b))
else:
    print("error")
