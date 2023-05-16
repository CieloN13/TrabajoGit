
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
class Tringulo(FigurGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

def calcular_area_triangulo( base, altura):
     areaTriangulo = (base * altura) / 2
     return areaTriangulo

def calcular_perimetro_tiangulo(lado1,lado2, lado3):
        perimetroTriangulo= lado1 + lado2 + lado3
        return perimetroTriangulo

def calcula_tipo_tringulo(lado1,lado2, lado3):
    if  lado1 == lado2 and lado2 ==lado3:
        print("El tringulo es equilatero")
    elif lado1 == lado2 and lado2 != lado3:
        print("El tringulo es isoseles")
    elif lado1 !=lado2 and lado2 != lado3:
        print("El tringulo es escaleno")
    else:
        exit()
class Rectangulo(FigurGeometrica):
    def __init__(self,lado_largo, lado_corto):
        self.lado_largo=lado_largo
        self.lado_corto=lado_corto
def calcular_area_rectangulo(lado_largo, lado_corto):
    areaRectangulo= lado_largo*lado_corto  
    return areaRectangulo 
#en este espacio se esta creando la opcion 1 que corresponde al triangulo,
#Se realiza el llamado de las funciones que se crearon anteriormente 
i=0            
while i ==0:
    print("calcular el area de que objeto geometrico")
    print("1. Triangulo ")
    print("2. cuadrado")
    print("3. circulo")
    print("4. rectangulo")
    opcion = int(input())
    if opcion==1:
        print("Elija lo que desea calcular del triangulo")
        print("1.Area")
        print("2.Perimetro")
        print("3.Tipo de triangulo segun sus lados ")
        opciont = int(input())
        if opciont==1:
            base=float(input("Ingrese el valor de la base: "))
            altura=float(input("Ingrese el valor de la altura "))
            print (calcular_area_triangulo(base, altura))
        elif opciont==2:
            lado1=float(input("Ingrese el valor del lado 1: "))
            lado2=float(input("Ingrese el valor del lado 2: "))
            lado3=float(input("Ingrese el valor del lado 3: "))
            
            print (calcular_perimetro_tiangulo(lado1,lado2, lado3))
            
        elif opciont==3:
            lado1=float(input("Ingrese el valor del lado 1: "))
            lado2=float(input("Ingrese el valor del lado 2: "))
            lado3=float(input("Ingrese el valor del lado 3: "))

            print(calcula_tipo_tringulo( lado1,lado2, lado3))
    elif opcion==4:
        print("Elija lo que desea calcular del Rectangulo")
        print("1.Area")
        print("2.Perimetro")
        print("3.Diagonal")
        opcionr = int(input())
        lado_largo=float(input("Ingrese el valor del lado mas grande: "))
        lado_corto=float(input("Ingrese el valor del lado mas corto: "))
        if opcionr==1:
            print(calcular_area_rectangulo(lado_largo,lado_corto))