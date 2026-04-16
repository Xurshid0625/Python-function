from random import randint

son = randint(1000,9999)

name = str(input('Mijoznoi ismi: '))
phone = str(input('Mijozni nomeri: '))

print(f"Sizning kodingiz: {son}")

def login(name,phone):
    cod = int(input('Kodingizni kiriting: '))
    if son == cod:
        with open('matn.txt',"a") as f:
            f.write(f"\nismi: {name}\nnomeri: {phone}")
            print("Xush kelibsiz")
            
login(name,phone)            