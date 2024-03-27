import sqlite3
from users_adminitration import *

class User():
    
    # faltan definir atributos de este objeto y sus métodos 
    def __init__(self, name: str, password: str) -> None:
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute(f'SELECT name FROM users WHERE name = "{name}";')
        if len(cur.fetchall()) == 0:
            raise UserNotFount
        else:
            cur.execute(f'SELECT password FROM users WHERE name = "{name}";')
            consulta: list[tuple[str]] = cur.fetchall()

            if consulta[0][0] != password:
                raise WrongPassword
            else:
                cur.execute(f'SELECT tag FROM user_tags WHERE user = "{name}";')
                self.tags: list[str] = list()
                for i in cur.fetchall():
                    for j in i:
                        self.tags.append(j)
                
                self.name: str = name
                self.password: str = password

    def show_tags(self):
        return self.tags

    def add_tag(self, labelname: str):
        if labelname in self.tags:
            raise TagLogged
        else:
            self.tags.append(labelname)
            add_tag(self.name, labelname)