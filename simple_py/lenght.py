from multiprocessing.spawn import old_main_modules


name = []
name.append(input("Name: "))

i = 0
while name[0] != '\0':
    print()
    i += 1

print(str(i))