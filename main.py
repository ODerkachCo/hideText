from stegano import lsb
import os
from colorama import init, Fore, Back, Style
from pyfiglet import Figlet

ERROR = Fore.RED
RST = Style.RESET_ALL
MSG = Fore.YELLOW
APRV = Fore.GREEN

def add_text_to_picture(p_path, text, n_path):
    try:
        secret = lsb.hide(p_path, text)
        if n_path == '':
            secret.save(p_path)
        else:
            secret.save(n_path)
        return '\n[+] Text added to the picture\n'
    except Exception as ex:
        return f'\n{ERROR}[-] {ex}\n{RST}'

def get_hidden_text(p_path):
    try:
        return lsb.reveal(p_path)
    except Exception as ex:
        return f'\n{ERROR}[-] {ex}\n{RST}'

def show_result(text):
    arr = text.split(', ')
    print('\nHidden text is:')
    for i in arr:
        print(i)
    print('\n')

def password(f_path):
    isPassword = False
    result = ''
    while not isPassword:
        password = input("Enter your password.\n>")
        if password != "pass":
            result = f'{ERROR}[-] Error: access denied, wrong password.{RST}'
        else:
            result = f'\n{APRV}[+] Access granted!{RST}'
            isPassword = True
    return result

def help():
    dash = '-'   
    return f'\n{dash*33}{MSG}\nadd{RST} - add text to the picture\n{MSG}read{RST} - read text in the picture\n{MSG}exit{RST} - close program\n{dash*33}\n'

def main():
    init()
    preview = Figlet(font='slant')
    print(preview.renderText('HIDE TEXT'))
    while True:
        u_input = input(f'Type {MSG}help{RST} to see allowed commands\n> ').lower()
        if u_input == "add":
            picture = input("Enter path to picture.\n> ")
            txt = input("Enter your text.\n> ")
            n_path = input("Enter new path.\n> ")
            print(add_text_to_picture(picture, txt, n_path))
        if u_input == "read":
            picture = input("Enter path to picture.\n> ")
            print(password(picture))              
            show_result(get_hidden_text(picture))

        if u_input == "exit":
            quit(f'{ERROR}Program ended!{RST}')
        if u_input == "help":
            print(help())

if __name__ == "__main__":
    main()