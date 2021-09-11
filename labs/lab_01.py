#!/usr/bin/env python
# coding: utf-8

# # MAT281 - Laboratorio N°01

# <a id='p1'></a>
# 
# ## Problema 01
# 
# ### a) Calcular el número $\pi$
# 
# En los siglos XVII y XVIII, James Gregory y Gottfried Leibniz descubrieron una serie infinita que sirve para calcular $\pi$:
# 
# $$\displaystyle \pi = 4 \sum_{k=1}^{\infty}\dfrac{(-1)^{k+1}}{2k-1} = 4(1-\dfrac{1}{3}+\dfrac{1}{5}-\dfrac{1}{7} + ...) $$
# 
# Desarolle un programa para estimar el valor de $\pi$ ocupando el método de Leibniz, donde la entrada del programa debe ser un número entero $n$ que indique cuántos términos de la suma se utilizará.
# 
# 
# * **Ejemplo**: *calcular_pi(3)* = 3.466666666666667, *calcular_pi(1000)* = 3.140592653839794
# 

# ### Definir Función
# 

# In[251]:


import math

def calcular_pi(n):
    
    """
    calcular_pi(n: int) -> float
    calcular_pi(n)
    
    Aproximacion del valor de pi mediante el método de Leibniz
    
    Parameters
    ----------
    n : int
        Numero de terminos.
    
    Returns
    -------
    output : float
        Valor aproximado de pi.
        
    Examples
    --------
    >>> calcular_pi(3)
    3.466666666666667
    
    >>> calcular_pi(1000) 
    3.140592653839794
    """
    
    suma=0
    for i in range(1,n+1):
        suma=suma+((-1)**(i+1))/(2*i-1)
    return 4*suma
   
    
   


# In[246]:


print('siendo que pi es:', math.pi)
for i in range(10):
    print('la aproximacion', i, 'es', calcular_pi(i))


# In[247]:


error1=[]
numero_pi=[]
aprox_pi=[]
n1=[]
for i in range(20):
    if math.pi>calcular_pi(i):
        error1.append(math.pi-calcular_pi(i))
    else:
        error1.append(calcular_pi(i)-math.pi)
    numero_pi.append(math.pi)
    aprox_pi.append(calcular_pi(i))
    n1.append(i)


# In[248]:


plt.plot(n1,error1)
plt.title('Error de la aproximación')
plt.xlabel('Valor de n')
plt.ylabel('Error ')
plt.show()


# In[250]:


plt.plot(n1,aprox_pi)
plt.plot(n1,numero_pi)
plt.legend(labels=['Aproximacion', 'Número pi'])
plt.title('Convergencia del método')
plt.xlabel('Valor de n')
plt.ylabel('Aproximación ')
plt.show()


# In[252]:


# Acceso a la documentación
help(calcular_pi)


# ### Verificar ejemplos

# In[231]:


# ejemplo 01
assert calcular_pi(3) == 3.466666666666667, "ejemplo 01 incorrecto"


# In[232]:


# ejemplo 02
assert calcular_pi(1000) == 3.140592653839794, "ejemplo 02 incorrecto"


# **Observación**:
# 
# * Note que si corre la línea de comando `calcular_pi(3.0)` le mandará un error ... ¿ por qué ?
# * En los laboratorio, no se pide ser tan meticuloso con la documentacion.
# * Lo primero es definir el código, correr los ejemplos  y  luego documentar correctamente.

# ### b) Calcular el número $e$
# 
# Euler realizó varios aportes en relación a $e$, pero no fue hasta 1748 cuando publicó su **Introductio in analysin infinitorum** que dio un tratamiento definitivo a las ideas sobre $e$. Allí mostró que:
# 
# 
# En los siglos XVII y XVIII, James Gregory y Gottfried Leibniz descubrieron una serie infinita que sirve para calcular π:
# 
# $$\displaystyle e = \sum_{k=0}^{\infty}\dfrac{1}{k!} = 1+\dfrac{1}{2!}+\dfrac{1}{3!}+\dfrac{1}{4!} + ... $$
# 
# Desarolle un programa para estimar el valor de $e$ ocupando el método de Euler, donde la entrada del programa debe ser un número entero $n$ que indique cuántos términos de la suma se utilizará.
# 
# 
# * **Ejemplo**: *calcular_e(3)* =2.5, *calcular_e(1000)* = 2.7182818284590455

# ### Definir función

# Primero definimos la función factorial que nos facilitará la definición de la función pedida

# In[36]:


def factorial(n):
    if n==0:
        return 1
    factorial=n
    i=1
    for i in range(1,n):
        factorial=factorial*i
        i=i+1
    return factorial


# por ejemplo calculemos los primeros 10 factoriales

# In[228]:


for i in range(10):
    print('el factorial de', i, 'es', factorial(i))


# grafiquemos como se vería esto

# In[76]:


import matplotlib.pyplot as plt
import numpy as np


# In[77]:


numero=[]
factoriales=[]
for i in range(1,8):
    numero.append(i)
    factoriales.append(factorial(i))


# In[78]:


plt.plot(numero, factoriales)
plt.title('Primeros factoriales', size = 15)
plt.show()


# así, la función pedida es

# In[145]:


def calcular_e(n):
    """
    calcular_e(n: int) -> float
    calcular_e(n)
    
    Aproximacion del valor de 4 mediante el método de Leibniz
    
    Parameters
    ----------
    n : int
        Numero de terminos.
    
    Returns
    -------
    output : float
        Valor aproximado de pi.
        
    Examples
    --------
    >>> calcular_e(3)
    2.5
    
    >>> calcular_e(1000)
    2.7182818284590455
    """
    suma=0
    for i in range(n):
        suma=suma+1/factorial(i)
    return suma


# por ejemplo las primeras 10 aproximaciones son

# In[112]:


print('siendo que e es:', math.exp(1))
for i in range(10):
    print('La aproximación', i, 'es', calcular_e(i))


# pero veamos que por defecto, algunos valores son aproximados a cero, por lo que no se dará el error en el ejemplo 02

# In[187]:


def calcular_e2(n):
    suma=0
    for i in range(n+1):
        suma=suma+1/factorial(i)
        if i==1000:
            print('el sumando mil es', 1/factorial(i))
    return suma


# In[188]:


calcular_e(1000)


# In[189]:


calcular_e2(1000)


# In[169]:


calcular_e(1000)-calcular_e2(1000)


# lo que claramente no es correcto

# In[141]:


error=[]
numero_e=[]
aprox=[]
n=[]
for i in range(20):
    if math.exp(1)>calcular_e(i):
        error.append(math.exp(1)-calcular_e(i))
    else:
        error.append(calcular_e(i)-math.exp(1))
    numero_e.append(math.exp(1))
    aprox.append(calcular_e(i))
    n.append(i)


# In[142]:


plt.plot(n,error)
plt.title('Error de la aproximación')
plt.xlabel('Valor de n')
plt.ylabel('Error ')
plt.show()


# In[144]:


plt.plot(n,aprox)
plt.plot(n,numero_e)
plt.legend(labels=['Aproximacion', 'Número de euler'])
plt.title('Convergencia del método')
plt.xlabel('Valor de n')
plt.ylabel('Aproximación ')
plt.show()


# ### Verificar ejemplos

# In[128]:


# ejemplo 01
assert calcular_e(3) == 2.5, "ejemplo 01 incorrecto"


# In[131]:


# ejemplo 02
assert calcular_e(1000) ==  2.7182818284590455, "ejemplo 02 incorrecto"


# In[130]:


calcular_e(1000)


# <a id='p2'></a>
# 
# ## Problema 02
# 
# 
# Sea $\sigma(n)$ definido como la suma de los divisores propios de $n$ (números menores que n que se dividen en $n$).
# 
# Los [números amigos](https://en.wikipedia.org/wiki/Amicable_numbers) son  enteros positivos $n_1$ y $n_2$ tales que la suma de los divisores propios de uno es igual al otro número y viceversa, es decir, $\sigma(n_1)=\sigma(n_2)$ y $\sigma(n_2)=\sigma(n_1)$.
# 
# 
# Por ejemplo, los números 220 y 284 son números amigos.
# * los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110; por lo tanto $\sigma(220) = 284$. 
# * los divisores propios de 284 son 1, 2, 4, 71 y 142; entonces $\sigma(284) = 220$.
# 
# 
# Implemente una función llamada `amigos` cuyo input sean dos números naturales $n_1$ y $n_2$, cuyo output sea verifique si los números son amigos o no.
# 
# * **Ejemplo**: *amigos(220,284)* = True, *amigos(6,5)* = False
# 

# ### Definir Función

# In[256]:


def amigos(x,y):
    
    """
    amigos(x: int ,y:int) -> Boleano
    amigos(x,y)
    
    
    
    Parameters
    ----------
    x : int
        Un numero entero.
    y : int
        Un numero entero.
    
    Returns
    -------
    output : Buleano
        Verdadero si son amigos, Falso si no lo son
        
    Examples
    --------
    >>> amigos(220,284)
    True
    
    >>> amigos(6,5)
    False
    """
    
    
    suma1=0
    suma2=0
    for i in range(1,x):
        if x/i==int(x/i):
            suma1=suma1+i
    for i in range(1,y):
        if y/i==int(y/i):
            suma2=suma2+i
    if suma1==y and suma2==x:
        return True
    return False


# ### Verificar ejemplos

# In[257]:


amigos(220,284)


# In[201]:


amigos(6,5)


# <a id='p3'></a>
# 
# ## Problema 03
# 
# La [conjetura de Collatz](https://en.wikipedia.org/wiki/Collatz_conjecture), conocida también como conjetura $3n+1$ o conjetura de Ulam (entre otros nombres), fue enunciada por el matemático Lothar Collatz en 1937, y a la fecha no se ha resuelto.
# 
# Sea la siguiente operación, aplicable a cualquier número entero positivo:
# * Si el número es par, se divide entre 2.
# * Si el número es impar, se multiplica por 3 y se suma 1.
# 
# La conjetura dice que siempre alcanzaremos el 1 (y por tanto el ciclo 4, 2, 1) para cualquier número con el que comencemos. 
# 
# Implemente una función llamada `collatz` cuyo input sea un número natural positivo $N$ y como output devulva la secuencia de números hasta llegar a 1.
# 
# * **Ejemplo**: *collatz(9)* = [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# ### Definir Función

# In[258]:


def collatz(n):
    """
    collatz(n: int) -> list
    collatz(n)
    
    Lista de la sucesion definida anteriormente por el método de collatz
    
    Parameters
    ----------
    n : int
        Numero de terminos.
    
    Returns
    -------
    output : list
        Lista de la sucesion definida  por el método de collatz
        
    Examples
    --------
    >>> collatz(9)
    [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    
  
    """
    salida=[]
    i=n
    salida.append(int(i))
    while(i!=1):
        if i/2==int(i/2):
            i=i/2
            salida.append(int(i))
        else:
            i=3*i+1
            salida.append(int(i))
    return salida


# In[259]:


collatz(9)


# ### Verificar ejemplos

# In[260]:


# ejemplo 01
assert collatz(9) == [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "ejemplo 01 incorrecto"


# <a id='p4'></a>
# 
# ## Problema 04
# 
# La [conjetura de Goldbach](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) es uno de los problemas abiertos más antiguos en matemáticas. Concretamente, G.H. Hardy, en 1921, en su famoso discurso pronunciado en la Sociedad Matemática de Copenhague, comentó que probablemente la conjetura de Goldbach no es solo uno de los problemas no resueltos más difíciles de la teoría de números, sino de todas las matemáticas. Su enunciado es el siguiente:
# 
# $$\textrm{Todo número par mayor que 2 puede escribirse como suma de dos números primos - Christian Goldbach (1742)}$$
# 
# Implemente una función llamada `goldbach` cuyo input sea un número natural positivo $N$ y como output devuelva la suma de dos primos ($N1$ y $N2$) tal que: $N1+N2=N$. 
# 
#  * **Ejemplo**: goldbash(4) = (2,2), goldbash(6) = (3,3) , goldbash(8) = (3,5)

# ### Definir función

# In[225]:



def goldbash(n):
    lista=[]
    lista_primos=[]
    for i in range(n):
        for k in range(1,i):
            if i/k==int(1/k):
                lista.append(k)
        if lista==[1]:
            lista_primos.append(i)
    for i in lista_primos:
        for j in lista_primos:
            if i+j==n:
                return (i,j)
    


# In[261]:


goldbash(4)


# ### Verificar ejemplos

# In[238]:


# ejemplo 01
assert  goldbash(4) == (2,2), "ejemplo 01 incorrecto"


# In[239]:


# ejemplo 02
assert goldbash(6) == (3,3), "ejemplo 02 incorrecto"


# In[240]:


# ejemplo 03
assert goldbash(8) == (3,5), "ejemplo 03 incorrecto"


# In[ ]:




