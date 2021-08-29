

class Persona:
    Nome = "sconosciuto"
    AltezzaCm = 0


class Tubi:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class tubi_classe:
    def __init__(self):                              
        self.x = 300
        self.y = 100 #.randint(-75,150)


# Giampiero
persona_1 = Persona()
persona_1.Nome = "Giampiero"
persona_2 = Persona()
persona_2.Nome = "Mazinga z"
#print("inizio")
#print(persona_1)
#print(persona_1.Nome)
#print(persona_2)
#print(persona_2.Nome)

#t = tubi_classe()
#print(f"x: {t.x}")


tubi_1 = Tubi(50, 150)
#tubi_1.x = 10
#tubi_1.y = 20
#tubi_1.z = 30

print(f"x: {tubi_1.x}")
print(f"y: {tubi_1.y}")

tubi_1.x = 100000 
print(f"x: {tubi_1.x}")


print("fine")