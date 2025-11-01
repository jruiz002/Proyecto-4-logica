# Sistema de Control Fuzzy para Cálculo de Propinas

Proyecto de Lógica Matemática - Universidad del Valle de Guatemala

## 📋 Descripción

Este proyecto implementa un sistema de control fuzzy que determina la propina apropiada en un restaurante basándose en la calidad del servicio y la comida, utilizando la librería scikit-fuzzy de Python.

## 🚀 Instalación y Ejecución

### Paso 1: Activar el entorno virtual

```bash
source venv_fuzzy/bin/activate
```

### Paso 2: Ejecutar el sistema

```bash
python sistema_propinas_simple.py
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
├── informe_proyecto.md          # Documento de análisis completo
├── generar_pdf.py               # Script para generar PDF
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

## 📖 Documentación

El archivo `informe_proyecto.md` contiene:
- Metodología completa
- Análisis de resultados
- Reflexiones individuales y grupales
- Conclusiones y aprendizajes

## 🎯 Objetivos Cumplidos

✅ Implementación exitosa de lógica fuzzy  
✅ Sistema funcional con resultados coherentes  
✅ Visualizaciones generadas automáticamente  
✅ Documentación completa con reflexiones  
✅ Casos de estudio diversos y análisis detallado  

## 👥 Autor

Proyecto desarrollado para el curso de Lógica Matemática  
Universidad del Valle de Guatemala  
Noviembre 2025