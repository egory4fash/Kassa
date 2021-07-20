import pickle

base = []
def starting():
    try:                #Trying to open a base if exists,appending() if not
        with open("base.pickle","rb") as file:
            base = pickle.load(file)
    except FileNotFoundError:
        print("База пустая")
        append()

    #return base


def append():       #adding new elements in base
    while True:
        line = input("Через пробелы:цена,№ нач,№ посл,количество")
        if not line:
            break             #running while input,adding packs in base
        a = line.split()
        base.append(a)

    if base[0] != float:            #checking money,adding if not
        money = float(input("Скока денег?"))
        base.insert(0,money)

    #with open("base.pickle","wb") as file:       #saving in pickle file
        #pickle.dump(base, file)

    return base



def selling():
    price, quantity= input("Через пробел цена и количество").split()
    for i in range(1,len(base)):
        if base[i][0] == price:
            if int(quantity) < int(base[i][3]):
                base[i][3] = int(base[i][3]) - int(quantity)
                base[i][1] = int(base[i][1]) + (int(base[i][1]) + int(quantity))
                base[0] += float(price) * int(quantity)
                return base
            elif int(quantity) == base[i][3]:
                base[0] += int(price) * int(quantity)
                del base[i]
                return base
            elif int(quantity) > base[i][3]:
                base[0] += int(price) * int(base[i][3])
                quantity = int(quantity) - int(base[i][3])
                base[i][3] = 0
                continue

    for i in range(1,len(base)):
        if base[i][3] == 0:
            del base[i]
            break

    return base

def saving():
    with open("base.pickle","wb") as file:       #saving in pickle file
        pickle.dump(base, file)

starting()
selling()
saving()
print(base)











