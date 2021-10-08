#list comprehension demo

int_list = [1, 2, 3, 4, 5]
str_list = ["Eeny", "Meeny", "Miney","Moe"]

print(int_list)
print(str_list)

odds = [x for x in int_list if (x % 2 != 0)]
evens = [x for x in int_list if (x % 2 == 0)]

print("Odds Are...", odds)
print("Evens are..", evens)
