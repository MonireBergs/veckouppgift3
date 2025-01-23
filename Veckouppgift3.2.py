#1.A
answer = 0
for i in range(1,11):
    answer += i
print("summan av talen 1 till 10 är:" + str(answer))

#-------------------------------------------------------#

#1.B
answer_1 = 0
for i in range(1,101):
    answer_1 += i
print("Summan av talen 1 till 10 är:" + str(answer_1))

#---------------------------------------------------------#

#1.C
answer_2 = 0
i = 1
while i <= 100:
    answer_2 += i
    i += 1
print("summan av talen 1 till 100 är" + str(answer_2))

#-----------------------------------------------------------#

#2.2
numbers = [1, -2, 3, -2, 4, -3]
total = 0
for number in numbers:
    total += number
print(total)

#-----------------------------------------------------------#

#3.Skapa lista med namn på fyra filmer.
#
filmlista = ["film a", "film b", "film c", "film d"]
print (filmlista)

filmlista.append("Fellowship of the ring") #lagt till i listan
print(filmlista)

filmlista[0] = "The two towers" #lagt till filmen på indexplats 0
print(filmlista)

index = filmlista.index("Fellowship of the ring") #vilken indexplats den har
print(index)

filmlista.remove("film b") #tagit bort en film för att se om Fellowship of the ring har ändrat index, vilket den inte har gjort.
print(filmlista)

langd = len(filmlista) # tar reda på hur lång listan är
print(langd)

vand = list(reversed(filmlista)) #vänder på listan men först måste man göra om den till en lista först genom att skriva "list".
print(vand)

filmlista.sort()
print(filmlista)