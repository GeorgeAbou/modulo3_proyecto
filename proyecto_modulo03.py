


import  random 

import matplotlib.pyplot as plt

"""
Programa que simula una maquina de Galton,con 3000canicas y 12 niveles 
"""
numero_canicas = 3000
niveles_obstaculos = 12

def maquina(canica, nivel) :#funcion que simula el orden de distribucion de las canicas 
   
   
	carril = [0] * (( nivel* 2) + 1)#se crea una variable para enumerar los carries tomando como opcion de niveles  por cada lado

	for canica in range(0, canica): #ciclo for principal para interactuar con cada canica
		total=0
		for nivel in range(1, nivel+1):	#ciclo for para cada nivel de obstaculo se empieza desde 1
         
			alearorio = random.randint(0, 1)#se genera un numero aleatorio que simulara la direccion que tomara la canica 
			if(alearorio >= 0.5):#sentido aleatorio hacia la derecha
				total += 1
			else:
				total -= 1	#sentido aleatorio hacia la izquierda
		carril[total + nivel] += 1 #aumenta el paso con cada nivel

	for i in range(0, nivel + 1):#ciclo for para generar el carril
		carril[i] = carril[i*2]	

	return carril[0:nivel]# regresa el orden final de las canicas
           
          
      
  

def mostrar_grafico(hist):
    '''
    funcion para graficar la Maquina Galton
    se coloca titulo,etiquetas del eje x , y
    se intica el tamaño de las celdas y color
    
    '''
    plt.bar(range(len(hist)), hist, width=1, color='green')
    plt.title('Simulación  Máquina de Galton')
    plt.ylabel('Numero de canicas')
    plt.xlabel('orden de canicas')
    plt.show()

 

galton=maquina(numero_canicas,niveles_obstaculos)           
            
print(galton) 
mostrar_grafico(galton)      
            
print("Ha finalizado el programa")            
            
            
            
            
            
            
            
            
            
            
            
            
    
