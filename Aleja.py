
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
class circulo(FigurGeometrica):
    def __init__(self, radio):
        self.radio=radio
       
def calcular_area_circulo(radio):
    areaCirculo= 3.14159 * radio**2
    return areaCirculo

def calcular_diametro_circulo(radio):
    diametroCirculo =radio + radio
    return diametroCirculo

def calcular_circunferencia_circulo(radio):
    circunferenciaCirculo = 2* 3.14159 * radio**2
    return circunferenciaCirculo
class Rectangulo(FigurGeometrica):
    def __init__(self,lado_largo, lado_corto):
        self.lado_largo=lado_largo
        self.lado_corto=lado_corto
def calcular_perimetro_rectangulo(lado_largo, lado_corto):
    """El perímetro del rectángulo es igual a la suma de las longitudes de sus cuatro lados."""
    perimetroRectangulo= ((lado_largo+lado_largo)+(lado_corto+lado_corto)) 
    return perimetroRectangulo
#en este espacio se esta creando la opcion 3 que corresponde al circulo,
#Se realiza el llamado de las funciones que se crearon anteriormente 
i=0            
while i ==0:
    print("calcular el area de que objeto geometrico")
    print("1. Triangulo ")
    print("2. cuadrado")
    print("3. circulo")
    print("4. rectangulo")
    opcion = int(input())
    elif opcion==3:
        print("Elija lo que desea calcular del circulo")
        print("1.Area")
        print("2.Perimetro")
        print("3.Circunferencia")
        opcioncir = int(input())
        radio=float(input("Ingrese el valor del radio: "))
        if opcioncir==1:
            print(calcular_area_circulo(radio))
        elif opcioncir==2:
            print(calcular_diametro_circulo(radio))
        elif opcioncir==3:
            print(calcular_circunferencia_circulo(radio))
        else:
            print("invalido")
    elif opcion==4:
        print("Elija lo que desea calcular del Rectangulo")
        print("1.Area")
        print("2.Perimetro")
        print("3.Diagonal")
        opcionr = int(input())
        lado_largo=float(input("Ingrese el valor del lado mas grande: "))
        lado_corto=float(input("Ingrese el valor del lado mas corto: "))
        elif opcionr==2:
            print(calcular_perimetro_rectangulo(lado_largo,lado_corto))