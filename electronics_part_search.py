from pathlib import Path

class PartsList():
    
    def __init__(self, parts):
        self.parts = []

    def __str__(self):
        pass

class Part():
    
    def __init__(self, part_number = '', part_type = '', description = '', manufacturer = ''):
        self.part_number = ''
        self.part_type = ''
        self.description = ''
        self.manufacturer = ''

    def get_part_number(self):
        checking_part_number = True
        verify_part_number = ''
        while checking_part_number == True:
            self.part_number = input('Enter Part Number: ')
            verify_part_number = input(f'Is this the correct part number? {self.part_number} (Y/N): ')
            if verify_part_number.upper() == 'Y':
                print(f'You have enetered the part number {self.part_number}\n')
                break
            else:
                continue

    def get_part_description(self):
        checking_part_description = True
        verify_part_description = ''
        while checking_part_description == True:
            self.description = input('Enter Part Description: ')
            verify_part_description = input(f'Is this the correct part type? {self.description} (Y/N): ')
            if verify_part_description.upper() == 'Y':
                print(f'You have enetered the part description {self.description}\n')
                break
            else:
                continue

    def get_part_type(self):
        checking_part_type = True
        verify_part_type = ''
        while checking_part_type == True:
            self.part_type = input('Enter Part Type: ')
            self.part_type = self.part_type.split(' ')
            self.part_type = '_'.join(self.part_type)
            verify_part_type = input(f'Is this the correct part type? {self.part_type} (Y/N): ')
            if verify_part_type.upper() == 'Y':
                print(f'You have enetered the part type {self.part_type}\n')
                break
            else:
                continue

    def get_manufacturer(self):
        checking_manufacturer = True
        verify_manufacturer = ''
        while checking_manufacturer == True:
            self.manufacturer = input('Enter Part Manufacturer: ')
            self.manufacturer = self.manufacturer.split(' ')
            self.manufacturer = '_'.join(self.manufacturer)
            verify_manufacturer = input(f'Is this the correct part manufacturer? {self.manufacturer} (Y/N): ')
            if verify_manufacturer.upper() == 'Y':
                print(f'You have entered the part manufacturer {self.manufacturer}\n')
                break
            else:
                continue

    def get_new_part(self):
        self.get_part_number()
        self.get_part_description()
        self.get_part_type()
        self.get_manufacturer()

    def __str__(self):

        return (f'Part Number: {self.part_number}\n'
                f'Description: {self.description}\n'
                f'Part Type: {self.part_type}\n'
                f'Manufacturer: {self.manufacturer}\n'
        )

def main():

    parts_file = open('current_parts_list.txt', 'r')
    current_parts_list = parts_file.read()
    current_parts_list = current_parts_list.split()
    print(current_parts_list)
    
    new_part = Part()
    new_part.get_new_part()
    print(new_part)

    if new_part.part_number in current_parts_list:
        print('This part is already logged\n')
    else:
        print('The new part is entered')



    #new_path = "C:\\Users\\aaron\\OneDrive\\Documents\\VScode\\Python\\python_programs\\sandbox_testing" + "\\" + part_type + "\\" + part_number

    #print(new_path)

    #Path(new_path).mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    main()