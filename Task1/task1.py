import re

list = input("Enter your string:\n")

print("Your string:\n", list)


#функція знаходить числа та букви в рядочку
def find_list(find_list, poisk):
    if poisk == 0:
        list_int = re.findall(r'\d+', find_list)
        list_int = [int(i) for i in list_int]
        return list_int
    elif poisk == 1:
        list_str = re.findall(r'\D', find_list)
        list_str = [str(i) for i in list_str]
        list_str = ''.join(list_str)
        return list_str
    else:
        return "Error!"
#функція знаходить числа та букви в рядочку

list_int = find_list(list, 0)

print("String with numbers only:\n", list_int)

list_str = find_list(list, 1)

print("String with letters only:\n", list_str)

#функція замінює першу та останню букву на великі
def Bykvi(list_str):
    res = ""
    j = 0
    spl = str(list_str).split()
    for i in spl:
        for i in spl[j].split():
            a = ''.join(spl[j])
            if len(a) == 1:
                res += a[0].upper()+' '
            else:
                res += a[0].upper()+a[1:-1]+a[-1].upper() + ' '
            j += 1
    return res


print("A string with a big first and last letter:\n", Bykvi(list_str))

#фунція підносить цифри до степеню
def Stepen(list_int):
    maximum = max(list_int)
    res = []
    for i in range(len(list_int)):
        if list_int[i] != maximum:
            res.append(list_int[i]**(i+1))
        else:
            res.append(list_int[i])
    return res


print("Max value:\n", max(list_int))

print("String with numbers in degree:\n",Stepen(list_int))



