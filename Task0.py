import random
random.seed()

spisok1=[]
spisok2=[]
schet=0
n_schet=0
biggest=-101

for i in range(30):
    spisok1.append(random.randint(-100, 100))
print("Список: \n", spisok1)

for number in spisok1:
    schet+=1
    if number>biggest:
        biggest=number
        n_schet=schet
print("Максимальное значение =", biggest, ". Номер по счёту =" , n_schet)

for i in range(len(spisok1)):
    if spisok1[i]%2!=0:
        spisok2.append(spisok1[i])
spisok2.sort(reverse=True)
print("Список с цифрами от больших к маленьким: \n", spisok2)
