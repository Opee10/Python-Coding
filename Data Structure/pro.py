import json

class LabPC:
    def __init__(self, pc_number, os, status):
        self.pc_number = pc_number
        self.os = os
        self.status = status

    def __str__(self):
        return f"PC Number: {self.pc_number}, OS: {self.os}, Status: {self.status}"

class Lab:
    def __init__(self):
        self.pcs = []

    def add_pc(self, pc_number, os, status):
        pc = LabPC(pc_number, os, status)
        self.pcs.append(pc)

    def update_pc(self, pc_number, os=None, status=None):
        for pc in self.pcs:
            if pc.pc_number == pc_number:
                if os:
                    pc.os = os
                if status:
                    pc.status = status
                return True
        return False

    def remove_pc(self, pc_number):
        for pc in self.pcs:
            if pc.pc_number == pc_number:
                self.pcs.remove(pc)
                return True
        return False

    def display_all_pcs(self):
        for pc in self.pcs:
            print(pc)

    def display_pc(self, pc_number):
        for pc in self.pcs:
            if pc.pc_number == pc_number:
                print(pc)
                return True
        return False

    def search_pc(self, pc_number):
        for pc in self.pcs:
            if pc.pc_number == pc_number:
                print(pc)
                return True
        return False

    def check_pc_number(self, pc_number):
        for pc in self.pcs:
            if pc.pc_number == pc_number:
                return True
        return False

    def save_to_file(self, file_path):
        with open(file_path, "w") as file:
            json.dump([pc.__dict__ for pc in self.pcs], file)

    def load_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        self.pcs = [LabPC(**pc) for pc in data]

def main():
    lab = Lab()

    while True:
        print("1. Add PC")
        print("2. Update PC")
        print("3. Remove PC")
        print("4. Display all PCs")
        print("5. Display PC")
        print("6. Search PC")
        print("7. Save to file")
        print("8. Load from file")
        print("9. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pc_number = input("Enter PC number: ")
            os = input("Enter operating system: ")
            status = input("Enter status: ")
            if lab.check_pc_number(pc_number):
                print("PC number already exists.")
                action = input("Do you want to update or remove the existing PC? (update/remove/no): ")
                if action == "update":
                    lab.update_pc(pc_number, os=os, status=status)
                elif action == "remove":
                    lab.remove_pc(pc_number)
            else:
                lab.add_pc(pc_number, os, status)

        elif choice == "2":
            pc_number = input("Enter PC number: ")
            os = input("Enter operating system (leave blank if not updating): ")
            status = input("Enter status (leave blank if not updating): ")
            if not lab.update_pc(pc_number, os=os, status=status):
                print("PC number not found.")
11