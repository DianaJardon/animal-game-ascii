from doctest import ELLIPSIS_MARKER
from mimetypes import init
import animal

#Menu
#while
#Decisiones
#Dibujos
#Clase


menu = {
    '1': '1.Loro',
    '2': '2.Serpiente',
    '0': '0.Exit',
}

class Animal():
    loro=0
    serpiente=0
    
    animales_lista = {
        1:animal.loro,
        2:animal.serpiente
    }
    def __init__(self, loro, serpiente):
        self.loro = loro
        self.serpiente = serpiente

    def mostrar_animal(self,op):
        print(self.animales_lista[op])

#Ejecucion principal
if __name__ == '__main__':
    for opcion in menu:
        print(menu.get(opcion))


    op = int(input('Elige qué animal quieres ver: '))
    
    while True:
        if op == 0:
            # El usuario quiere dejar de jugar
            print("Bay")

            break
        elif op == 1:
            #Imprimir animal
            print(animal.loro)
            
        elif op == 2:
            print(animal.serpiente)
            
        else:
            #Opcion invalida
            print('Opción inválida, intentelo nuevamente')
            for opcion in menu:
                print(menu.get(opcion))
        op = int(input('Elige qué animal quieres ver: '))
