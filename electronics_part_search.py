from pathlib import Path

def main():

    part_number = input('Enter Part Number: ')
    part_type = input('Enter Part Type: ')
    part_manufacturer = input('Enter Manufacturer')



    new_path = "C:\\Users\\aaron\\OneDrive\\Documents\\VScode\\Python\\python_programs\\sandbox_testing" + "\\" + part_type + "\\" + part_number

    print(new_path)

    Path(new_path).mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    main()