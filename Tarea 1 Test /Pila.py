class pila:
    def __init__(self):
        self.elemento = []

    def push(self, dato):
            self.elemento.append(dato)
  
    def pop(self):
                if(len(self.elemento) ==0):
                       return "Pila Vacia"
                else:
                       return self.elemento.pop(0)

mipila = pila()
mipila.push("primer valor")
mipila.push("segundo valor")
mipila.push("tercer valor")

print(mipila.pop())
print(mipila.pop())
print(mipila.pop())
