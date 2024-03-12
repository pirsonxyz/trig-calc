import math
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
import os
import time
from mpmath import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rich.progress import track
import sys
from fractions import Fraction

def calculate_distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def visualize_trigonometric(func_type='sin', amplitude=1.0, frequency=1.0):
    def generate_data(func, phase_angle, num_points=1000):
        x = np.linspace(0, 2*np.pi, num_points)
        y = amplitude * func(frequency * x + phase_angle)
        return x, y

    
    def update(frame):
        phase_angle = frame * np.pi / 180  
        x, y = generate_data(selected_func, phase_angle)
        line.set_data(x, y)
        return line,

    
    func_map = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan}
    if func_type not in func_map:
        raise ValueError("Nombre de funcion invalida. escoge 'sin', 'cos', or 'tan'.")

    selected_func = func_map[func_type]

    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-3, 3) 


    x, y = generate_data(selected_func, 0)
    line, = ax.plot(x, y)

    
    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=True)

    plt.show()
    
def plot_triangle(x_coords, y_coords):
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    plt.plot(x_coords, y_coords, 'b-')  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangulo ABC')
    plt.grid(True)
    plt.gca().spines['left'].set_position('zero')
    plt.gca().spines['bottom'].set_position('zero')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.axis('equal')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.xticks(range(int(min(x_coords))-1, int(max(x_coords))+2))
    plt.yticks(range(int(min(y_coords))-1, int(max(y_coords))+2))
    
    plt.show()

    
def plot_sqrt(x_coords, y_coords):
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    plt.plot(x_coords, y_coords, 'b-')  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Paralelogramo ABCD')
    plt.grid(True)
    plt.gca().spines['left'].set_position('zero')
    plt.gca().spines['bottom'].set_position('zero')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.axis('equal')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.xticks(range(int(min(x_coords))-1, int(max(x_coords))+2))
    plt.yticks(range(int(min(y_coords))-1, int(max(y_coords))+2))
    
    plt.show()

def sleep_and_clear():

    exit = input('Quieres reiniciar? (s/n): ')
    if exit == 's': 
        for i in track((range(1)), description="Reiniciando..."):
            time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('[red]Adios!')
        time.sleep(0.5)
        sys.exit()
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = 0
    while name != KeyboardInterrupt:
        
        print(Panel('[red]Bienvenido a la calculadora trigonometrica!', title='Calculadora', subtitle='Creada por Pirson!'))
        print('\n')
        table = Table(title='Opciones')

        table.add_column('Numero', justify='right', style='cyan', no_wrap=True)
        table.add_column('Descripcion', style='magenta')
        
        table.add_row('1', 'Calcular el seno, tangente, cos y sus contrarios.',)
        table.add_row('2', 'Convertir de radianes.',)
        table.add_row('3', 'Aplicar funciones trigonometricas a triangulos definidos.')
        table.add_row('4', 'Graficar un triangulo en base a sus coordenadas y calcular la distancia entre puntos.')
        table.add_row('5', 'Visualizar funciones trigonometricas en base a una amplitud o frecuencia.')
        table.add_row('6', 'Resolver ecuaciones cuadraticas.')
        table.add_row('7', 'Calcular distancia en un paralelogramo con coordenadas(x,y).')
        table.add_row('Ctrl + c', 'Salir.',)

        console = Console()
        console.print(table)
        name = int(Prompt.ask("Elige tu opcion"))
        
        match name:
            case 1:
                x = int(input('Introduce tu numero: '))
                c = int(Prompt.ask('1 para tan, 2 para cos, 3 para sin, 4 para sec, 5 para cot, 6 para ctan, 7 para cosec'))
                
                x = math.radians(x)
                
                match c:
                    case 1:
                        print(f'Resultado: {math.tan(x)}')
                    case 2:
                        print(f'Resultado: {math.cos(x)}')
                    case 3:
                        print(f'Resultado: {math.sin(x)}')
                    case 4:
                        print(f'Resultado: {sec(x)}')
                    case 5:
                          print(f'Resultado: {cot(x)}')
                    case 6:
                        print(f'Resultado: {1/tan(x)}') 
                    case 7:
                        print(f'Resultado: {csc(x)}')
                    case _:
                        print('[red] Opcion invalida!')
                        continue     
            case 2:
                print('1 para seno a angulo, 2 para cos a angulo, 3 para tan a angulo: \n')
                c = int(input('Elije: '))
                x = float(input('Escribe el numero: '))
                if c == 1:
                    print(f'Resultado de {x} radianes es {math.degrees(math.asin(x))} grados')
                elif c == 2:
                     print(f'Resultado de {x} radianes es {math.degrees(math.acos(x))} grados')
                elif c == 3:
                     print(f'Resultado de {x} radianes es {math.degrees(math.atan(x))} grados')
            case 3:
                ca = int(input('Introduce el cateto adyacente: '))
                co = int(input('Introduce el cateto contrario: '))
                h = int(input('Introduce la hipotenusa: '))
                choice = int(input('sin, cos o tan?(1/2/3): '))
                
                if choice == 1:
                    x = co/h
                    print(f'Resultado: {x}')
                elif choice == 2:
                    x = ca / h
                    print(f'Resultado: {x}')
                elif choice == 3:
                    x = co / ca
                    print(f'Resultado: {x}')
            case 4:
                print('Introduce las coordenas para los vertices del triangulo:')
                vertices = ['A', 'B', 'C']
                x_coords = []
                y_coords = []

                for vertex in vertices:
                    x = float(input(f'Entra la coordenada x para {vertex}: '))
                    y = float(input(f'Entra la coordenada y para {vertex}: '))
                    x_coords.append(x)
                    y_coords.append(y)

                distance_AB = calculate_distance(x_coords[0], y_coords[0], x_coords[1], y_coords[1])
                distance_AC = calculate_distance(x_coords[0], y_coords[0], x_coords[2], y_coords[2])
                distance_BC = calculate_distance(x_coords[1], y_coords[1], x_coords[2], y_coords[2])

                print(f'Distancia entre A y B: {distance_AB}')
                print(f'Distancia entre A y C: {distance_AC}')
                print(f'Distancia entre B y C: {distance_BC}')

                plot_triangle(x_coords, y_coords)
            case 5:
                amp = float(input('Introduce la amplitud: '))
                freq = float(input('Introduce la frecuencia: '))
                func = str(input('Que funcion quieres ver? (sin/cos/tan)?: '))
                
                visualize_trigonometric(func, amp, freq)
            case 6:
                print('Calculadora de ecuaciones cuadraticas!')
                a = int(input('Introduce a: '))
                b = int(input('Introduce b: '))
                c = int(input('Introduce c: '))
                
                d = b**2-4*a*c # discriminant

                if d < 0:
                    print ('Esta ecuacion no tiene solucion!')
                elif d == 0:
                    x = (-b+math.sqrt(b**2-4*a*c))/2*a
                    print (f'Esta ecuacion tiene una solucion. x = {x}')
                else:
                    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
                    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
                    print (f'Esta ecuacion tienes dos soluciones. x1 = {x1}, x2 = {x2}')
                    pp = int(input('Quieres ver las soluciones como fracciones? (1/0): '))

                    if pp == 1:
                        print(f'x1 = {Fraction(x1).limit_denominator()}')
                        print(f'x2 = {Fraction(x2).limit_denominator()}')
            case 7:
                print('Introduce las coordenas para los vertices del cuadrado:')
                vertices = ['A', 'B', 'C', 'D']
                x_coords = []
                y_coords = []

                for vertex in vertices:
                    x = float(input(f'Entra la coordenada x para {vertex}: '))
                    y = float(input(f'Entra la coordenada y para {vertex}: '))
                    x_coords.append(x)
                    y_coords.append(y)

                distance_AB = calculate_distance(x_coords[0], y_coords[0], x_coords[1], y_coords[1])
                distance_DC = calculate_distance(x_coords[3], y_coords[3], x_coords[2], y_coords[2])
                distance_BC = calculate_distance(x_coords[1], y_coords[1], x_coords[2], y_coords[2])
                distance_AD = calculate_distance(x_coords[0], y_coords[0], x_coords[3], y_coords[3])

                print(f'Distancia entre A y B: {distance_AB}')
                print(f'Distancia entre D y C: {distance_DC}')
                print(f'Distancia entre B y C: {distance_BC}')
                print(f'Distancia entre A y D: {distance_AD}')

                plot_sqrt(x_coords, y_coords)
            case _:
                print('Opcion no valida!')
                sleep_and_clear()
                continue
        sleep_and_clear()
                               
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[red]Adios!')
