'''
#Deafault
def home(name, found = 1999):
    print("House",name, "Found at ",found)
home('Parasite')
'''

def house(name, address):
    information = f"{name}, {address}"
    return information

no = house('Opee',"LLL")
print(no)

def person(fname, lname):
    person = { 'first' : fname, 'last' : lname }
    return person
var = person('Jimi', 'Handrix')
print(var)

def greet_user(names):
    for name in names:
     msg = f"Hello, {name.title()}"
     print(msg)
var = ['opee', 'kobi', 'noki']
greet_user(var)

def students(*names):
    for name in names:
        print(name)
var = ('Opee','Aush','Yobi','Vris')
students(*var)
var1 = ['kom','som',22,98]
students(*var1)



def students(size, weigth, *foods):
    print("Size is :",size)
    print("weigth is :",weigth)
    print("Foods are :")
    for food in foods:
        print(f"-",food)

students('ospps','shs''sks','vdsv')

def foodie(name, age, *foods):
    print("Hers : ",name)
    print("Old :",age)
    print("Her Favs : ")
    for food in foods:
        print(f"-",food)
name = 'Farii'
age = 24
foodie(name,age,'Cashewnuts', 'Pasta', 'SimCurry','myLipie')

def foodie(name, age, *foods, **places ):
    print("Hers : ",name)
    print("Old :",age)
    print("Her Favs : ")
    for food in foods:
        print(f"❤️",food)

    for key,value in places.items():
        print()
name = 'Farii'
age = 24
kw = {"fun": "R/a" ,"Chill" :"Baridhara"}
foodie(name,age,'Cashewnuts', 'Pasta', 'SimCurry','myLipie',kw )

def us(*vibes, **places):
    print('Some vibes : ')
    for vibe in vibes:
        print(vibe)
    for key,value in places.items():
        print(f"{key} is {value}")
pla = {'R/a' : 'Good', 'Niku' : 'Modarate'}
us('Chill','Anxious','party','love',**pla)

