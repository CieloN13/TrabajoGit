
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
class Cuadrado(FigurGeometrica):
    def __init__(self,lado):
        self.lado=lado

def calcular_area_cuadrado(lado):
    areaCuadrado= lado*lado  
    return areaCuadrado   
def calcular_perimetro_cuadrador(lado):
    perimetroCuadrado= lado*4 
    return perimetroCuadrado

def caular_diagonal_cuadrado(lado):
    from math import sqrt
    diagonalCuadrado= lado**2
    return diagonalCuadrado
class Rectangulo(FigurGeometrica):
    def __init__(self,lado_largo, lado_corto):
        self.lado_largo=lado_largo
        self.lado_corto=lado_corto
def calcular_diagonal_rectangulo(lado_largo, lado_corto):
    """Calcular diagonal se eleva el ancho y la longitud al cuadrado y luego suma estos números"""
    from math import sqrt
    diagonalrectangulo= ((lado_largo*2)+(lado_corto*2))
    return diagonalrectangulo

i=0    
while i ==0:
    print("calcular el area de que objeto geometrico")
    print("1. Triangulo ")
    print("2. cuadrado")
    print("3. circulo")
    print("4. rectangulo")
    opcion = int(input())
    elif opcion==2:
        print("Elija lo que desea calcular del cuadrado")
        print("1.Area")
        print("2.Perimetro")
        print("3.Diagonal")
        opcionc = int(input())
        lado=float(input("Ingrese el valor de un lado "))
        if opcionc==1:
            print(calcular_area_cuadrado(lado))
        elif opcionc==2:
            print(calcular_perimetro_cuadrador(lado))
        elif opcionc==3:
            print(caular_diagonal_cuadrado(lado))
    elif opcion==4:
        print("Elija lo que desea calcular del Rectangulo")
        print("1.Area")
        print("2.Perimetro")
        print("3.Diagonal")
        opcionr = int(input())
        lado_largo=float(input("Ingrese el valor del lado mas grande: "))
        lado_corto=float(input("Ingrese el valor del lado mas corto: "))
        elif opcionr==3:
            print(calcular_diagonal_rectangulo(lado_largo,lado_corto))
        else:
            print("invalido")