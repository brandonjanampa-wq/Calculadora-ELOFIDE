from math import sin, cos, tan, pi,sqrt

print("Hola soy un programa que puede calcular el area"
      " de un rwctangulo ")
base = int(input(" escribe la base del rectangulo "))
altura = int(input(" escribe la altura del rectangulo"))
area = base * altura
print("el area es ;",area)

print(".................................................")

print("Hola voy a calcular el promedio de 5 notas")
nota1 = float(input(" escribe la nota del 1"))
nota2 = float(input(" escribe la nota del 2"))
nota3 = float(input(" escribe la nota del 3"))
nota4 = float(input(" escribe la nota del 4"))
nota5 = float(input(" escribe la nota del 5"))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5)/5
print("el promedio es ",promedio)

print(".................................................")
num=int(input(" escribe un numero de 3 cifras"))
u=num%10
d=(num%100)//10
c=num//100
newnum=u*100+d*10+c
print(newnum)
a=sqrt(9)

print(".................................................")

colores=int(input(" cantidad de colores :"))

caja_24=colores//24
colores-=caja_24*24
caja_12=colores//12
colores-=caja_12*12
caja_6=colores//6
colores-=caja_6*6
sobrantes=colores

print("Colores :",colores)
print(caja_24," cajas de 24 colores")
print(caja_12," cajas de 12 colores")
print(caja_6," cajas de 6 colores")
print(sobrantes," cajas restantes ")

print("...........................................................")

seg=int(input(" escribe un numero de segundos :"))

D=seg//86400
seg=seg%86400
H=seg//3600
seg=seg%3600
M=seg//60
S=seg%60

print(D," :",H,":",M,":",S)

print(".................................................")
print("Hola voy a calcular el rea de cualquier poligono regular ")
n=float(input(" escribe un numero de lados de la fgura :"))
s=float(input(" escriba la longitud de los lados : "))
area=(n*(s**2))/4*(tan(pi/n))
print("el area es ",area)

print(".................................................")

edad=int(input(" escribe tu edad :"))
print("es mayor de edad"*(edad>=18)+"Es menor de edad"*(edad<=18))

print(".................................................")

consumo=int(input(" escribe cuanto es tu consumo en Wt :"))

precio=float(0.4522*(consumo<=100)+0.7*(consumo>100))

total=(consumo*precio)*(consumo<=100)+(100*0.4522+((consumo-100)*precio)*(consumo>100))

print("el total es ",total)

print(".................................................")

num=int(input(" escribe un numero :"))

resultado=("Es par "*(num%2==0)+"Es impar|"*(num%2!=0))

print(resultado)
