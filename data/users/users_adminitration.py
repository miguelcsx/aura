import sqlite3
from class_user import User

con = sqlite3.connect("users.db")
cur = con.cursor()

# esta función es MUY NECESARIA, errores del módulo
def close_con_users() -> None:
    """Función para cerrar el conector de este módulo"""
    con.close()
    return

class UsersExceptions(Exception):
    text = None

# Exceptions
class UserNotFount(UsersExceptions):
    text = "The user is not found in the database"

    def __str__(self):
        return f"UserNotFount: {self.text}"

class UserLogged(UsersExceptions):
    text = "The user has already been registered in the database"

    def __str__(self) -> str:
        return f"UserLogged {self.text}"

class UserNotLogged(UsersExceptions):
    text = 'The user has not been registered'

    def __str__(self) -> str:
        return f"UserNotLogged {self.text}"

class WrongPassword(UsersExceptions):
    text = "Wrong Password"

    def __str__(self) -> str:
        return self.text

# functions
def add_user(name: str, password: str) -> None:
    """Agregar usuarios a la base de datos"""

    cur.execute(f'SELECT name FROM users WHERE name = "{name}";')
    
    if len(cur.fetchall()) != 0:
        raise UserLogged
    else:
        cur.execute(f'INSERT INTO users (name, password) VALUES ("{name}", "{password}");')
        con.commit()

    return None


def delet_user(name: str, password: str) -> None:
    """Eliminar usuarios de la base de datos"""

    cur.execute(f'SELECT name FROM users WHERE name = "{name}";')

    if(len(cur.fetchall())) == 0:
        raise UserNotFount
    else:
        cur.execute(f'SELECT password FROM users WHERE name = "{name}"')
        confirm: list[tuple[str]] = cur.fetchall()

        if confirm[0][0] != password:
            raise WrongPassword
        else:
            cur.execute(f'DELETE FROM users WHERE name = "{name}"')
            con.commit()
    return

def show_users() -> list[tuple[str]]:
    """Retorna una lista con los nombres de los usuarios"""

    cur.execute("SELECT name FROM users;")
    resultado = cur.fetchall()
    
    return resultado

def select_user(name: str, password: str) -> User:
    """Esta función dependerán de los parámetros del
    constructor para User"""

    cur.execute(f'SELECT name FROM users WHERE name = "{name}";')
    
    if len(cur.fetchall()) == 0:
        raise UserNotFount
    else:
        cur.execute(f'SELECT password FROM users WHERE name = "{name}";')
        confirm: list[tuple[str]] = cur.fetchall()
        
        if confirm[0][0] != password:
            raise WrongPassword
        else:
            resultado = User(name, password)
            return resultado