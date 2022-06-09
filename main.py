
class nodo():
    def __init__(self,dato):
        self.item1 = dato
        self.siguiente = None
        self.anterior = None

class funciones():

    def __init__(self):
        self.cabeza = None
    def ingresar_elemento(self,x):
        if self.cabeza is None:
            nuevo_elemento = nodo(x)
            self.cabeza = nuevo_elemento
            self.cabeza.siguiente = self.cabeza
            self.cabeza.anterior = self.cabeza
            return
        else:
            nod = self.cabeza
            while nod.siguiente is not None:
                if nod.siguiente is self.cabeza:
                    #print('encontrado')
                    break
                nod = nod.siguiente
            nuevo_elemento = nodo(x)
            nod.siguiente = nuevo_elemento
            nuevo_elemento.anterior = nod
            nuevo_elemento.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_elemento

    def mostrar(self):
        if self.cabeza is None:
            print('no hay elementos en la cola')
            return
        else:
            nod = self.cabeza
            print('>>> Lista Completo')
            while nod is not None:
                print(nod.item1)
                if nod.siguiente is self.cabeza:
                    break
                nod = nod.siguiente
            try:
                numero = int(input('Ingresar un numero de la lista: '))



                nod1 = self.cabeza
                while nod1 is not None:
                    if nod1.item1 == numero:
                        print('nodo anterior: ',nod1.anterior.item1,', nodo actual: ',nod1.item1,', nodo siguiente: ',nod1.siguiente.item1)
                        break
                    if nod1.siguiente is self.cabeza:
                        print('El numero no pertenece a la lista')
                        break
                    nod1 = nod1.siguiente
            except:
                print('El dato ingresado no es un numero')

    def ingresar_opc(self):
        print('Ingresar la opcion')
        trycatch = True
        num = 0
        while (trycatch):
            try:
                num = int(input())
                trycatch = False
            except ValueError:
                print('Ingresar un numero entero')
        return num

    def menuPrincipal(self):
        while True:
            print('--MENU PRINCIPAL--')
            print('------------------')
            print('1. Ingresar numero')
            print('2. Mostrar')
            print('3. Salir')

            opc = self.ingresar_opc()
            if opc == 1:
                try:
                    num = int(input('Ingresar un numero entero: '))
                    self.ingresar_elemento(num)
                except:
                    print('El dato ingresado no es un numero')
            elif opc == 2:

                self.mostrar()
            elif opc == 3:
                break
            else:
                print('La opcion no existe')

if __name__ == '__main__':
    nuevo = funciones()
    nuevo.menuPrincipal()
    #nuevo.ingresar_elemento(1)
    #nuevo.ingresar_elemento(2)
    #nuevo.ingresar_elemento(3)
    #nuevo.ingresar_elemento(4)
    #nuevo.ingresar_elemento(5)

    #nuevo.mostrar()