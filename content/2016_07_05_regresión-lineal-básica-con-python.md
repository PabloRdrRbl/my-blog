Title: Regresión lineal básica con Python
Date: 2016-7-5 12:34
Modified: 2016-7-5 12:34
Category:
Tags: Python, Scipy, Estadística
Slug: regresion-lineal-basica-con-python
Authors: Pablo Rodríguez Robles
Status: draft


Esta es una entrada cortita que siempre he querido hacer. En cualquier práctica de laboratorio puede que tengamos que hacer algo tan sencillo como una regresión lineal. Esto es algo muy fácil de hacer en Python, veamos cómo.

Supongamos que hemos estado tomando medidas de cierto fenómeno físico (imaginemos que estamos midiendo un caudal, en el que medimos volumen y tiempo) en el laboratorio con el fin de saber si se cumple una relación lineal supuesta.

$$ Q = \frac{V}{t} $$

Una vez tenemos nuestros datos, que en este caso hemos apuntado en un archivo CSV (*comma-separated values*, [ver más aquí](https://es.wikipedia.org/wiki/CSV)), solamente tenemos que procesarlos con Python.

Los datos pueden tener esta pinta dentro del archivo `datos.csv`:

```text
1,2,5,7,10,15 # tiempo (s)
2,6,7,9,14,19 # volumen (m^3)
```

El siguiente script es todo lo que necesitamos:

```python
# Calculates the linear regression model for the data

# Import libraries
import numpy as np
from scipy import stats

# Load experimental data
data = np.loadtxt('data.csc', delimiter=',', dtype=float)
x = data[0]
y = data[y]

# Model
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
```
