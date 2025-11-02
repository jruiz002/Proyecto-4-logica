# Sistema de Control Fuzzy para Cálculo de Propinas

Proyecto de Lógica Matemática - Universidad del Valle de Guatemala

## 📋 Descripción

Este proyecto implementa un sistema de control fuzzy que determina la propina apropiada en un restaurante basándose en la calidad del servicio y la comida, utilizando la librería scikit-fuzzy de Python.

## 🚀 Instalación y Ejecución

### Paso 1: Activar el entorno virtual

```bash
source venv_fuzzy/bin/activate
```

#### Windows (PowerShell / Símbolo del sistema)

Si está en Windows, puede crear y activar un entorno virtual e instalar las dependencias con los siguientes comandos.

PowerShell (recomendado):

```powershell
py -3.11 -m venv .venv
# Permite la ejecución del script de activación solo en la sesión actual
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

Símbolo del sistema (cmd.exe):

```cmd
py -3.11 -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### Paso 2: Ejecutar el sistema

```bash
python sistema_propinas.py
```

### Paso 3: Ver los resultados

El sistema generará:
- Tabla de resultados con diferentes combinaciones
- Casos de estudio específicos
- Gráfico de funciones de membresía (`funciones_membresia.png`)

## 📁 Estructura del Proyecto

```
Proyecto 4/
├── sistema_propinas_simple.py    # Implementación principal
├── sistema_propinas_fuzzy.py     # Versión completa con gráficos 3D
├── requirements.txt              # Dependencias
├── README.md                    # Este archivo
├── funciones_membresia.png      # Visualización generada
├── superficie_control.png       # Superficie 3D (si se genera)
└── venv_fuzzy/                  # Entorno virtual
```

## 🔧 Dependencias

- Python 3.13+
- scikit-fuzzy 0.5.0
- NumPy 2.3.4
- Matplotlib 3.10.7
- SciPy 1.16.3

## 📊 Características del Sistema

### Variables de Entrada
- **Calidad del servicio**: Escala 0-10
- **Calidad de la comida**: Escala 0-10

### Variable de Salida
- **Propina**: Porcentaje 0-25%

### Funciones de Membresía
- **Triangulares** para todas las variables
- **Categorías**: Pobre, Promedio, Excelente

### Base de Reglas
- **9 reglas fuzzy** que combinan las variables de entrada
- **Método de defuzzificación**: Centroide

## 📈 Resultados Ejemplo

| Servicio | Comida | Propina | Interpretación |
|----------|--------|---------|----------------|
| 10/10    | 10/10  | 21.0%   | Experiencia excepcional |
| 6.5/10   | 6.0/10 | 12.9%   | Servicio promedio |
| 1/10     | 1/10   | 8.2%    | Experiencia muy negativa |

## 📊 Interpretación de las Funciones de Membresía

La gráfica generada (`funciones_membresia.png`) muestra las **funciones de membresía triangulares** para la variable de salida "propina":

### Análisis de la Gráfica:
- **🔵 Línea azul (baja)**: Propina baja (0-13%)
  - Máximo grado de pertenencia en 0%
  - Decrece linealmente hasta 13%

- **🟠 Línea naranja (media)**: Propina media (0-25%)
  - Máximo grado de pertenencia en 13%
  - Forma triangular simétrica centrada en 13%

- **🟢 Línea verde (alta)**: Propina alta (13-25%)
  - Máximo grado de pertenencia en 25%
  - Crece linealmente desde 13%

### Características Clave:
✅ **Solapamiento inteligente**: Las funciones se superponen en las zonas de transición  
✅ **Transiciones suaves**: No hay cambios abruptos entre categorías  
✅ **Manejo de incertidumbre**: Un valor puede pertenecer parcialmente a múltiples categorías  
✅ **Interpretabilidad**: Las formas triangulares son fáciles de entender
