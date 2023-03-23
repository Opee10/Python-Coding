'''a_dict = {'Yellow': 'Marigold', 'Red': 'Rose', 'White': 'Lilly'}

a_list = ['Black', 'Purple']

dict_copy = a_dict.copy()
a_list.append(dict_copy)

print(a_list)

'''
while True:
    Var = input("Guess the name of Tesla founder : ")
    if Var == "Elon":
        break
    print ("Length of the string is : ", len(Var))
print("Done")

val = [value%2 for value in range(1,10) ]
print(val)