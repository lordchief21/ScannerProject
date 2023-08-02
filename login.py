
class Login:
    def __init__(self):
        self.user = {}
    
    def create_user(self):
        username = input("Introduzca su numero de empleador: ")
        password = input("Escanee su QR: ")
        self.user[username] = password
    
    def login_user(self) -> bool:
        username = input("Introduzca su numero de empleador: ")
        password = input("Escanee su QR: ")
        if self.user.get(username) == password:
            return True
        else:
            return False