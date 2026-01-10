from pathlib import Path

class PartsList():
    
    def __init__(self, parts):
        self.parts = []

    def __str__(self):
        pass

class Part():
    
    def __init__(self, part_number='', part_type='', manufacturer=''):
        self.part_number = ''
        self.part_type = ''
        self.manufacturer = ''

    def get_part_number(self):
        checking_part_number = True
        verify_part_number = ''
        self.part_number = input('Enter Part Number: ')
        while checking_part_number == True:
            verify_part_number = input(f'Is this the correct part number? {self.part_number} (Y/N): ')
            if verify_part_number.upper() == 'Y':
                print(f'You have enetered the part number {self.part_number}')
                break
            else:
                self.part_number = input('Enter Part Number: ')
                continue

    def get_part_type(self):
        checking_part_type = True
        verify_part_type = ''
        self.part_type = input('Enter Part Type: ')
        self.part_type = self.part_type.split(' ')
        print(self.part_type)
        self.part_type = '_'.join(self.part_type)
        while checking_part_type == True:
            verify_part_type = input(f'Is this the correct part type? {self.part_type} (Y/N): ')
            if verify_part_type.upper() == 'Y':
                print(f'You have enetered the part type {self.part_type}')
                break
            else:
                self.part_type = input('Enter Part Type: ')
                continue

            

def main():

    parts_file = open('current_parts_list.txt', 'r')
    current_parts_list = parts_file.read()
    current_parts_list = current_parts_list.split()
    print(current_parts_list)
    
    new_part = Part()
    new_part.get_part_number()
    print(new_part.part_number)
    new_part.get_part_type()
    print(new_part.part_type)
    



    #new_path = "C:\\Users\\aaron\\OneDrive\\Documents\\VScode\\Python\\python_programs\\sandbox_testing" + "\\" + part_type + "\\" + part_number

    #print(new_path)

    #Path(new_path).mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    main()