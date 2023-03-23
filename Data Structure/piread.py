'''filename ='chat.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
filename = 'chat.txt'''
filename = 'chat.txt'


'''with open(filename, 'w') as file_obj:
    file_obj.write("I am Opee\n")
    file_obj.write("I am 22")
    file_obj.write("I am python pro")'''
'''with open(filename, 'a') as file_obj:
    file_obj.write("Append moood on")
    file_obj.write("Append moood offfffffffffffffffffff")'''
with open(filename, 'r') as file_obj:
    file_obj.read(filename)