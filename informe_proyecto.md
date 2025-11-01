# Sistema de Control Fuzzy para Cálculo de Propinas
## Proyecto de Lógica Matemática - Universidad del Valle de Guatemala

---

## 1. Introducción

Este proyecto implementa un sistema de control fuzzy utilizando la librería scikit-fuzzy de Python para resolver el problema de determinar la propina apropiada en un restaurante basándose en la calidad del servicio y la comida.

### 1.1 Justificación de la Elección

Se eligió la **Opción 2** (implementación práctica con scikit-fuzzy) por las siguientes razones:

- **Facilidad de implementación**: scikit-fuzzy proporciona herramientas predefinidas
- **Resultados tangibles**: Genera visualizaciones y datos concretos
- **Aplicación práctica**: El problema es fácil de entender y tiene relevancia real
- **Documentación abundante**: Existe amplia información y ejemplos disponibles

---

## 2. Descripción del Problema

### 2.1 Planteamiento

El sistema determina el porcentaje de propina apropiado (10%-25%) basándose en:

- **Calidad del servicio** (escala 0-10)
- **Calidad de la comida** (escala 0-10)

### 2.2 Justificación del Problema

Este problema es ideal para lógica fuzzy porque:

1. **Subjetividad**: La evaluación de "calidad" es inherentemente subjetiva
2. **Incertidumbre**: No hay límites precisos entre "bueno" y "excelente"
3. **Múltiples variables**: Combina diferentes aspectos de la experiencia
4. **Aplicación práctica**: Situación común en la vida real

---

## 3. Metodología

### 3.1 Variables del Sistema

#### Variables de Entrada:
- **calidad_servicio**: Universo [0, 10]
- **calidad_comida**: Universo [0, 10]

#### Variable de Salida:
- **propina**: Universo [0, 25] (porcentaje)

### 3.2 Funciones de Membresía

Se utilizaron funciones triangulares para todas las variables:

#### Para Calidad del Servicio y Comida:
- **Pobre**: trimf([0, 0, 5])
- **Promedio**: trimf([0, 5, 10])
- **Excelente**: trimf([5, 10, 10])

#### Para Propina:
- **Baja**: trimf([0, 0, 13])
- **Media**: trimf([0, 13, 25])
- **Alta**: trimf([13, 25, 25])

### 3.3 Base de Reglas

El sistema implementa 9 reglas fuzzy:

1. **Servicio Pobre ∧ Comida Pobre → Propina Baja**
2. **Servicio Pobre ∧ Comida Promedio → Propina Baja**
3. **Servicio Pobre ∧ Comida Excelente → Propina Media**
4. **Servicio Promedio ∧ Comida Pobre → Propina Baja**
5. **Servicio Promedio ∧ Comida Promedio → Propina Media**
6. **Servicio Promedio ∧ Comida Excelente → Propina Media**
7. **Servicio Excelente ∧ Comida Pobre → Propina Media**
8. **Servicio Excelente ∧ Comida Promedio → Propina Media**
9. **Servicio Excelente ∧ Comida Excelente → Propina Alta**

---

## 4. Implementación Técnica

### 4.1 Herramientas Utilizadas

- **Python 3.13**
- **scikit-fuzzy 0.5.0**: Librería principal para lógica fuzzy
- **NumPy 2.3.4**: Operaciones numéricas
- **Matplotlib 3.10.7**: Visualizaciones
- **SciPy 1.16.3**: Funciones científicas

### 4.2 Arquitectura del Sistema

```python
class SistemaPropinasSimple:
    def __init__(self):
        self.setup_variables()
        self.setup_membership_functions()
        self.setup_rules()
        self.setup_control_system()
```

### 4.3 Método de Defuzzificación

Se utiliza el método del **centroide** (por defecto en scikit-fuzzy) para convertir la salida fuzzy en un valor numérico preciso.

---

## 5. Resultados y Análisis

### 5.1 Casos de Estudio

| Servicio | Comida | Propina | Interpretación |
|----------|--------|---------|----------------|
| 1/10     | 1/10   | 8.2%    | Experiencia muy negativa |
| 6.5/10   | 6.0/10 | 12.9%   | Servicio promedio |
| 10/10    | 10/10  | 21.0%   | Experiencia excepcional |
| 2/10     | 8/10   | 11.6%   | Comida excelente, servicio pobre |
| 9/10     | 4/10   | 12.4%   | Servicio excelente, comida pobre |

### 5.2 Análisis de Comportamiento

1. **Coherencia**: El sistema produce resultados lógicos y consistentes
2. **Sensibilidad**: Responde apropiadamente a cambios en las entradas
3. **Robustez**: Maneja casos extremos de manera razonable
4. **Gradualidad**: Las transiciones entre categorías son suaves

### 5.3 Visualizaciones Generadas

- **funciones_membresia.png**: Muestra las funciones de membresía triangulares
- **superficie_control.png**: Superficie 3D del comportamiento del sistema

---

## 6. Reflexiones Individuales

### 6.1 Aprendizajes Técnicos

- **Comprensión de la lógica fuzzy**: El proyecto permitió entender cómo la lógica fuzzy maneja la incertidumbre y la imprecisión de manera más natural que la lógica clásica.

- **Implementación práctica**: Aprender a usar scikit-fuzzy demostró cómo las herramientas modernas facilitan la implementación de conceptos teóricos complejos.

- **Diseño de sistemas**: La importancia de definir correctamente las variables, funciones de membresía y reglas para obtener resultados coherentes.

### 6.2 Aplicaciones de la Lógica Fuzzy

Durante el desarrollo, se identificaron múltiples aplicaciones potenciales:

- **Sistemas de recomendación**: Para sugerir productos o servicios
- **Control automático**: En sistemas de climatización, control de velocidad
- **Diagnóstico médico**: Para evaluar síntomas con incertidumbre
- **Finanzas**: Evaluación de riesgo crediticio

### 6.3 Desafíos Encontrados

1. **Configuración del entorno**: Problemas iniciales con dependencias de Python
2. **Definición de reglas**: Balancear la simplicidad con la precisión
3. **Interpretación de resultados**: Asegurar que los valores de salida sean intuitivos

---

## 7. Reflexión Grupal

### 7.1 Ventajas de la Lógica Fuzzy

- **Manejo de incertidumbre**: Permite trabajar con conceptos imprecisos de manera natural
- **Flexibilidad**: Se adapta bien a problemas del mundo real donde las categorías no son absolutas
- **Interpretabilidad**: Las reglas son comprensibles para humanos
- **Robustez**: Funciona bien incluso con datos imperfectos

### 7.2 Limitaciones Observadas

- **Subjetividad en el diseño**: La definición de funciones de membresía puede ser arbitraria
- **Complejidad computacional**: Puede ser más lenta que métodos tradicionales
- **Dificultad de optimización**: Ajustar parámetros requiere experiencia

### 7.3 Comparación con Lógica Clásica

| Aspecto | Lógica Clásica | Lógica Fuzzy |
|---------|----------------|--------------|
| Valores de verdad | {0, 1} | [0, 1] |
| Manejo de incertidumbre | Limitado | Excelente |
| Interpretabilidad | Alta | Alta |
| Complejidad | Baja | Media |
| Aplicabilidad real | Limitada | Amplia |

---

## 8. Conclusiones

### 8.1 Logros del Proyecto

1. **Implementación exitosa**: Se desarrolló un sistema fuzzy funcional y completo
2. **Resultados coherentes**: El sistema produce salidas lógicas y útiles
3. **Visualizaciones efectivas**: Se generaron gráficos que facilitan la comprensión
4. **Documentación completa**: Se creó documentación técnica y reflexiva

### 8.2 Aprendizajes Clave

- La lógica fuzzy es especialmente útil para problemas con incertidumbre inherente
- Las herramientas modernas como scikit-fuzzy facilitan significativamente la implementación
- El diseño cuidadoso de reglas y funciones de membresía es crucial para el éxito
- La visualización es fundamental para entender y validar el comportamiento del sistema

### 8.3 Aplicaciones Futuras

Este proyecto sienta las bases para explorar aplicaciones más complejas de la lógica fuzzy en:

- Sistemas de control industrial
- Inteligencia artificial y machine learning
- Sistemas de soporte a la decisión
- Procesamiento de lenguaje natural

---

## 9. Referencias y Recursos

### 9.1 Librerías Utilizadas

- **scikit-fuzzy**: https://pythonhosted.org/scikit-fuzzy/
- **NumPy**: https://numpy.org/
- **Matplotlib**: https://matplotlib.org/
- **SciPy**: https://scipy.org/

### 9.2 Documentación Técnica

- Zadeh, L.A. (1965). "Fuzzy sets". Information and Control, 8(3), 338-353.
- Mamdani, E.H. (1974). "Application of fuzzy algorithms for control of simple dynamic plant"

### 9.3 Archivos del Proyecto

- `sistema_propinas_simple.py`: Implementación principal
- `requirements.txt`: Dependencias del proyecto
- `funciones_membresia.png`: Visualización de funciones de membresía

---

**Fecha de elaboración**: Noviembre 2025  
**Curso**: Lógica Matemática  
**Universidad del Valle de Guatemala**