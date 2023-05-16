
"""
Realice un algoritmo en donde se muestre un menú de 4 opciones, en donde se permita seleccionar una opción. En la opción 1 se va a calcular el área, 
perímetro y el tipo de triangulo de un triángulo, en la opción 2 calcular el área, perímetro y Diagonal de un cuadrado,
en la tercera opción calcular el área, Diámetro y circunferencia de un circulo y en la cuarta opción calcular el área, perímetro y Diagonal de rectángulo. 
•	Triangulo: Área, perímetro y el tipo de triangulo
•	Cuadrado: Área, perímetro y Diagonal 
•	Circulo: Área, Diámetro y circunferencia
•	Rectángulo: Área(Nicole), perímetro(Aleja) y Diagonal (Luis).

"""
class FigurGeometrica:
    def __init__(self):
        pass
class Rectangulo(FigurGeometrica):
    def __init__(self,lado_largo, lado_corto):
        self.lado_largo=lado_largo
        self.lado_corto=lado_corto
i=0            
while i ==0:
    print("calcular el area de que objeto geometrico")
    print("1. Triangulo ")
    print("2. cuadrado")
    print("3. circulo")
    print("4. rectangulo")
    opcion = int(input())
    elif opcion==4:
        print("Elija lo que desea calcular del Rectangulo")
        print("1.Area")
        print("2.Perimetro")
        print("3.Diagonal")
        opcionr = int(input())
        lado_largo=float(input("Ingrese el valor del lado mas grande: "))
        lado_corto=float(input("Ingrese el valor del lado mas corto: "))