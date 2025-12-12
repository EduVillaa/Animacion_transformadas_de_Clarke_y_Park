# Animacion_transformadas_de_Clarke_y_Park

![mi_animacion](https://github.com/user-attachments/assets/f773093f-b70c-4c4b-9b7e-cca223a769bd)

# README — Transformadas de Clarke y Park y Animación en Python

## 1. Introducción

En el análisis y control de máquinas eléctricas de corriente alterna, es habitual trabajar con magnitudes trifásicas (corrientes, tensiones o flujos magnéticos). Sin embargo, estas señales son variables en el tiempo y están acopladas entre sí, lo cual complica el análisis y el diseño de controladores.

Para simplificar este estudio se emplean dos transformadas fundamentales:

- **Transformada de Clarke (a → αβ)**
- **Transformada de Park (αβ → dq)**

Estas transformaciones permiten convertir un sistema trifásico en un conjunto de variables más fáciles de manejar, ya sea en un marco de referencia estacionario (αβ) o en un marco giratorio vinculado al rotor o al campo magnético (dq).

---

## 2. Transformada de Clarke

La **transformada de Clarke** convierte tres señales trifásicas equilibradas \( a, b, c \) en dos señales ortogonales \( \alpha, \beta \) situadas en un marco de referencia **estacionario**.  
Su objetivo es **representar un sistema trifásico en un plano bidimensional** sin pérdida de información.

### ¿Por qué es útil?

- Permite visualizar la magnitud y orientación del vector espacial.
- Facilita el análisis del comportamiento instantáneo de la máquina.
- Es un paso previo para aplicar la transformada de Park.

### Interpretación

Un sistema trifásico sinusoidal equilibrado se convierte en un **vector giratorio** en el plano αβ.

---

## 3. Transformada de Park

La **transformada de Park** toma las componentes αβ y las convierte en componentes **d** y **q**, que pertenecen a un marco de referencia **giratorio** con una velocidad angular \( \theta \).

### ¿Por qué es útil?

- En el marco dq, las variables del sistema trifásico pasan a ser **constantes** (si el régimen es estacionario).
- Esto simplifica enormemente el control de máquinas AC, especialmente el **control vectorial**.
- Permite desacoplar la corriente relacionada con el **par (q)** y la corriente relacionada con el **flujo (d)**.

## Explicación del código
El código adjunto:

1. **Genera un sistema trifásico sinusoidal equilibrado** en las fases a, b y c.  
2. **Aplica la transformada de Clarke** para obtener las componentes α y β.  
3. **Aplica la transformada de Park** usando un ángulo de referencia θ(t), típicamente \(\theta = \omega t\).  
4. **Crea una animación** que muestra:
   - Cómo el vector trifásico se proyecta en el plano αβ.
   - Cómo esas componentes se transforman en dq mediante un eje giratorio.
5. **Actualiza la animación en tiempo real**, permitiendo observar la relación geométrica entre las transformaciones.

### Qué se ve en la animación

- Las señales trifásicas se convierten en un punto que gira en el plano αβ.
- El marco dq rota a velocidad constante.
- La componente d corresponde a la proyección del vector sobre el eje giratorio.
- La componente q es la proyección perpendicular.
- Si el sistema es sinusoidal y el marco dq gira a la misma velocidad, d y q parecen **constantes**.

---

## 4. Requisitos para ejecutar el código

### Librerías necesarias

```bash
pip install matplotlib numpy

