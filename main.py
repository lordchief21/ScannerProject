from scanner import *
from login import *

def main():
    login = Login()
    login.create_user()
    if login.login_user():
        fujitsu = Scanner()
        fujitsu.confg_scanner()
        fujitsu.start_scanning()
    else: print("Usuario invalido")



if __name__ == "__main__":
    main()