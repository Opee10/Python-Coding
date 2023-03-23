import json
json.load()
def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

def add_pc(data):
    while True:
        pc_number = input('Enter PC number: ')
        if pc_number in data:
            print('Error: PC number already exists.')
            choice = input('Do you want to modify or remove the existing PC? (M/R/N): ')
            if choice.lower() == 'm':
                update_pc(data, pc_number)
                return
            elif choice.lower() == 'r':
                remove_pc(data, pc_number)
                return
            elif choice.lower() == 'n':
                return
            else:
                print('Invalid choice.')
        else:
            break
    os = input('Enter OS: ')
    status = input('Enter status: ')
    data[pc_number] = {'os': os, 'status': status}
    print(f'PC {pc_number} added.')

def update_pc(data, pc_number):
    if pc_number not in data:
        print(f'Error: PC {pc_number} does not exist.')
        return
    os = input('Enter OS (press enter to keep current value): ')
    status = input('Enter status (press enter to keep current value): ')
    if os:
        data[pc_number]['os'] = os
    if status:
        data[pc_number]['status'] = status
    print(f'PC {pc_number} updated.')

def remove_pc(data, pc_number):
    if pc_number not in data:
        print(f'Error: PC {pc_number} does not exist.')
        return
    del data[pc_number]
    print(f'PC {pc_number} removed.')

def display_all_pc(data):
    if not data:
        print('No PCs found.')
        return
    for pc_number, pc_data in data.items():
        print(f'PC {pc_number}: OS={pc_data["os"]}, Status={pc_data["status"]}')

def display_pc(data, pc_number):
    if pc_number not in data:
        print(f'Error: PC {pc_number} does not exist.')
        return
    pc_data = data[pc_number]
    print(f'PC {pc_number}: OS={pc_data["os"]}, Status={pc_data["status"]}')

def search_pc(data):
    pc_number = input('Enter PC number to search: ')
    if pc_number in data:
        display_pc(data, pc_number)
    else:
        print(f'PC {pc_number} not found.')
        choice = input('Do you want to add it? (Y/N): ')
        if choice.lower() == 'y':
            add_pc(data)

def store_pc(data):
    choice = input('Do you want to store the PC data in a file? (Y/N): ')
    if choice.lower() == 'y':
        filename = input('Enter filename (press enter to use default "data.json"): ') or 'data.json'
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f'PC data stored in file {filename}.')

def menu():
    data = load_data()
    while True:
        print('\nPC Lab Management\n------------------')
        print('1. Add PC')
        print('2. Update PC')
        print('3. Remove PC')
        print('4. Display all PCs')
        print('5')

ld = load_data()
sd = save_data('')
ap = add_pc(load_data())
up = update_pc('pc2','one')
rp = remove_pc('pc3','two')
dp = display_pc('pc4','three')
dap = display_all_pc(display_pc())
sp = search_pc('pc6')
stp = store_pc('pc7')
mn = menu()



