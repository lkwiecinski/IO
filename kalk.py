def komentarz():
    print("Pozrowienia dla małżonki :)")
print(">>")
print("Wprowadź działanie")
a = input()
dzialanie = input()
b = input()
if(dzialanie == '+'):
    result = int(a) + int(b)
elif(dzialanie == '-'):
    result = int(a) - int(b)
else:
    result = "BŁĄÐ"
print("=")
print(result)
