start = int(input("B son:"))
end = int(input("T son:"))

def nimadir(start, end):
    for i in range(start, end):
        if i % 2 == 0:
            print(f"Juft Son: {i}")
        
nimadir(start,end)        