def khabar(quantity, *talikas):
    print("Khabar er Quantiuty :",quantity)
    for menu in talikas:
        print(menu)

def foodie(name, age, *foods):
    print("Hers : ",name)
    print("Old :",age)
    print("Her Favs : ")
    for food in foods:
        print(f"-",food.rstrip())
name = 'Farii'
age = 24
foodie(name,age,'Cashewnuts', 'Pasta', 'SimCurry','myLipie')