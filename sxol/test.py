import ctypes
import time
from tabulate import tabulate
from colorama import Fore, Back, Style
import cmd
import requests
import os


class MyApp(cmd.Cmd):
    
    os.system("cls")
    prompt = f'\t\t\t\t\t {Fore.RED}>{Fore.RESET} '

    def __init__(self):
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleTitleW("Al3x Script Library")
        super().__init__()
        super().__init__()
        self.do_menu()
    

    def default(self, line):
        print(f"\n\t\t\t\t   {Fore.RED}ERROR {Fore.RESET}- {Fore.RED}[{Fore.YELLOW}{line}{Fore.RED}]{Fore.YELLOW} είναι μη έγκυρη εντολή{Fore.RESET}.\n")
        time.sleep(1)
        os.system("cls")
        self.do_menu()

    def emptyline(self):
        print(f"\n\t\t\t\t         {Fore.RED}ERROR {Fore.RESET}- {Fore.YELLOW}Μη έγκυρη εντολή{Fore.RESET}.\n")
        time.sleep(1)
        os.system("cls")
        self.do_menu()


    def do_menu(self):  
        table = f"""
        \t\t\t\t╭───────────────────────╮
        \t\t\t\t│  {Fore.RED}Al3x Script Library{Fore.RESET}  │
        \t\t\t\t├───────────────────────┤
        \t\t\t\t│ {Fore.RED}1{Fore.RESET}. {Fore.YELLOW}Python Scripts{Fore.RESET}     │
        \t\t\t\t│ {Fore.RED}2{Fore.RESET}. {Fore.YELLOW}Javascript Scripts{Fore.RESET} │
        \t\t\t\t│ {Fore.RED}3{Fore.RESET}. {Fore.YELLOW}Exit{Fore.RESET}               │
        \t\t\t\t╰───────────────────────╯
        """
        print(table)
        # table = [[f"{Fore.RED}1{Fore.RESET}. {Fore.YELLOW}Python Scripts{Fore.RESET}"], [f"{Fore.RED}2{Fore.RESET}. {Fore.YELLOW}Javascript Scripts{Fore.RESET}"], [f"{Fore.RED}3{Fore.RESET}. {Fore.YELLOW}Exit{Fore.RESET}"]]
        # print(tabulate(table, headers=[f"{Fore.RED}Al3x Script Library{Fore.RESET}"], tablefmt='rounded_outline'))


    def loading(self):
        os.system("cls")
        message = "Loading"
        while True:
            for i in range(4):
                print(message + "." * i)
                time.sleep(1)
                os.system("cls")
            break

    def do_2(self, this):
        self.list_github_files_js()

    def list_github_files_js(self):
        self.loading()
        os.system("cls")
        url = "https://api.github.com/repos/AkisGeorg/Javascript-Scripts/contents"
        headers = {'Accept': 'application/vnd.github+json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            files = response.json()
            table = []
            for i, file in enumerate(files):
                table.append([f"{Fore.YELLOW}{i+1}{Fore.RESET}", f"{Fore.BLUE}{file['name']}{Fore.RESET}", f"{Fore.GREEN}{file['size']}{Fore.RESET}"])
            print(tabulate(table, headers=[f"{Fore.RED}#{Fore.RESET}", f"{Fore.RED}Όνομα{Fore.RESET}", f"{Fore.RED}Μέγεθος (bytes){Fore.RESET}"], tablefmt='rounded_outline', numalign="center"))
            print(f"Επιλέξτε τον αριθμό του αρχείου που θέλετε να κατεβάσετε. (Γράψτε 'back' για να γυρίσετε πίσω.):")
            file_number = input("> ")
            if file_number == "back":
                time.sleep(0.500)
                os.system("cls")
                self.do_menu()
            elif int(file_number) <= len(files):
                selected_file = files[int(file_number) - 1]
                download_url = selected_file["download_url"]
                response = requests.get(download_url)
                open(selected_file["name"], 'wb').write(response.content)
                print(f"{selected_file['name']} κατέβηκε με επιτυχία!")
                time.sleep(2)
                os.system("cls")
                self.do_menu()
            else:
                print("Λάθος αριθμός αρχείου!")
                os.system("cls")
                self.do_menu()
        else:
            print(f'Error: {response.status_code}')

    def do_1(self, this):
        self.list_github_files_py()

    def list_github_files_py(self):
        self.loading()
        os.system("cls")
        url = "https://api.github.com/repos/AkisGeorg/Python-Scripts/contents"
        headers = {'Accept': 'application/vnd.github+json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            files = response.json()
            table = []
            for i, file in enumerate(files):
                table.append([f"{Fore.YELLOW}{i+1}{Fore.RESET}", f"{Fore.BLUE}{file['name']}{Fore.RESET}", f"{Fore.GREEN}{file['size']}{Fore.RESET}"])
            print(tabulate(table, headers=[f"{Fore.RED}#{Fore.RESET}", f"{Fore.RED}Όνομα{Fore.RESET}", f"{Fore.RED}Μέγεθος (bytes){Fore.RESET}"], tablefmt='rounded_outline', numalign="center"))
            print(f"Επιλέξτε τον αριθμό του αρχείου που θέλετε να κατεβάσετε. (Γράψτε 'back' για να γυρίσετε πίσω.):")
            file_number = input("> ")
            if file_number == "back":
                time.sleep(0.500)
                os.system("cls")
                self.do_menu()
            elif int(file_number) <= len(files):
                selected_file = files[int(file_number) - 1]
                download_url = selected_file["download_url"]
                response = requests.get(download_url)
                open(selected_file["name"], 'wb').write(response.content)
                print(f"{selected_file['name']} κατέβηκε με επιτυχία!")
                time.sleep(2)
                os.system("cls")
                self.do_menu()
            else:
                print("Λάθος αριθμός αρχείου!")
                os.system("cls")
                self.do_menu()
        else:
            print(f'Error: {response.status_code}')


    def do_3(self, line):
        os.system("cls")
        exit()

if __name__ == '__main__':
    MyApp().cmdloop()
