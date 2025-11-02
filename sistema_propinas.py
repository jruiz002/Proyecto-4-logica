"""
Sistema de Control Fuzzy para Cálculo de Propinas - Versión Simplificada
Proyecto de Lógica Matemática - Universidad del Valle de Guatemala
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class SistemaPropinasSimple:
    def __init__(self):
        """Inicializa el sistema de control fuzzy para propinas"""
        self.setup_variables()
        self.setup_membership_functions()
        self.setup_rules()
        self.setup_control_system()
    
    def setup_variables(self):
        """Define las variables de entrada y salida del sistema"""
        # Variables de entrada
        self.calidad_servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_servicio')
        self.calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
        
        # Variable de salida
        self.propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')
    
    def setup_membership_functions(self):
        """Define las funciones de membresía para cada variable"""
        
        # Funciones de membresía para calidad del servicio
        self.calidad_servicio['pobre'] = fuzz.trimf(self.calidad_servicio.universe, [0, 0, 5])
        self.calidad_servicio['promedio'] = fuzz.trimf(self.calidad_servicio.universe, [0, 5, 10])
        self.calidad_servicio['excelente'] = fuzz.trimf(self.calidad_servicio.universe, [5, 10, 10])
        
        # Funciones de membresía para calidad de la comida
        self.calidad_comida['pobre'] = fuzz.trimf(self.calidad_comida.universe, [0, 0, 5])
        self.calidad_comida['promedio'] = fuzz.trimf(self.calidad_comida.universe, [0, 5, 10])
        self.calidad_comida['excelente'] = fuzz.trimf(self.calidad_comida.universe, [5, 10, 10])
        
        # Funciones de membresía para la propina
        self.propina['baja'] = fuzz.trimf(self.propina.universe, [0, 0, 13])
        self.propina['media'] = fuzz.trimf(self.propina.universe, [0, 13, 25])
        self.propina['alta'] = fuzz.trimf(self.propina.universe, [13, 25, 25])
    
    def setup_rules(self):
        """Define las reglas del sistema fuzzy"""
        self.reglas = [
            # Si servicio es pobre y comida es pobre -> propina baja
            ctrl.Rule(self.calidad_servicio['pobre'] & self.calidad_comida['pobre'], 
                     self.propina['baja']),
            
            # Si servicio es pobre y comida es promedio -> propina baja
            ctrl.Rule(self.calidad_servicio['pobre'] & self.calidad_comida['promedio'], 
                     self.propina['baja']),
            
            # Si servicio es pobre y comida es excelente -> propina media
            ctrl.Rule(self.calidad_servicio['pobre'] & self.calidad_comida['excelente'], 
                     self.propina['media']),
            
            # Si servicio es promedio y comida es pobre -> propina baja
            ctrl.Rule(self.calidad_servicio['promedio'] & self.calidad_comida['pobre'], 
                     self.propina['baja']),
            
            # Si servicio es promedio y comida es promedio -> propina media
            ctrl.Rule(self.calidad_servicio['promedio'] & self.calidad_comida['promedio'], 
                     self.propina['media']),
            
            # Si servicio es promedio y comida es excelente -> propina media
            ctrl.Rule(self.calidad_servicio['promedio'] & self.calidad_comida['excelente'], 
                     self.propina['media']),
            
            # Si servicio es excelente y comida es pobre -> propina media
            ctrl.Rule(self.calidad_servicio['excelente'] & self.calidad_comida['pobre'], 
                     self.propina['media']),
            
            # Si servicio es excelente y comida es promedio -> propina media
            ctrl.Rule(self.calidad_servicio['excelente'] & self.calidad_comida['promedio'], 
                     self.propina['media']),
            
            # Si servicio es excelente y comida es excelente -> propina alta
            ctrl.Rule(self.calidad_servicio['excelente'] & self.calidad_comida['excelente'], 
                     self.propina['alta'])
        ]
    
    def setup_control_system(self):
        """Configura el sistema de control"""
        self.sistema_control = ctrl.ControlSystem(self.reglas)
        self.simulacion = ctrl.ControlSystemSimulation(self.sistema_control)
    
    def calcular_propina(self, servicio, comida):
        """
        Calcula la propina basándose en las entradas
        
        Args:
            servicio (float): Calidad del servicio (0-10)
            comida (float): Calidad de la comida (0-10)
            
        Returns:
            float: Porcentaje de propina recomendado
        """
        self.simulacion.input['calidad_servicio'] = servicio
        self.simulacion.input['calidad_comida'] = comida
        
        # Ejecutar la simulación
        self.simulacion.compute()
        
        return self.simulacion.output['propina']
    
    def visualizar_funciones_membresia(self):
        """Genera gráficos de las funciones de membresía y los guarda en archivos"""
        fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(10, 12))

        # Gráfico para calidad del servicio
        self.calidad_servicio.view(ax=ax0)
        ax0.set_title('Funciones de Membresía - Calidad del Servicio')
        ax0.grid(True)

        # Gráfico para calidad de la comida
        self.calidad_comida.view(ax=ax1)
        ax1.set_title('Funciones de Membresía - Calidad de la Comida')
        ax1.grid(True)

        # Gráfico para propina
        self.propina.view(ax=ax2)
        ax2.set_title('Funciones de Membresía - Propina (%)')
        ax2.grid(True)

        plt.tight_layout()
        plt.savefig('images/funciones_membresia.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Gráfico guardado: images/funciones_membresia.png")
    
    def generar_tabla_resultados(self):
        """Genera una tabla de resultados para diferentes combinaciones"""
        print("\n=== TABLA DE RESULTADOS ===")
        print("Servicio | Comida | Propina | Interpretación")
        print("-" * 50)
        
        resultados = []
        for servicio in range(0, 11, 2):
            for comida in range(0, 11, 2):
                propina = self.calcular_propina(servicio, comida)
                
                # Interpretar el resultado
                if propina < 10:
                    interpretacion = "Muy Baja"
                elif propina < 15:
                    interpretacion = "Baja"
                elif propina < 20:
                    interpretacion = "Media"
                else:
                    interpretacion = "Alta"
                
                print(f"   {servicio:2d}    |   {comida:2d}   | {propina:5.1f}% | {interpretacion}")
                resultados.append((servicio, comida, propina, interpretacion))
        
        return resultados
    
    def generar_superficie_control(self):
        """Genera una superficie de control 3D y la guarda en un archivo"""
        # Crear rangos para las variables de entrada
        servicio_range = np.arange(0, 11, 1)
        comida_range = np.arange(0, 11, 1)

        # Crear matrices para almacenar los resultados
        propinas = np.zeros((len(servicio_range), len(comida_range)))

        # Calcular propina para cada combinación
        for i, servicio in enumerate(servicio_range):
            for j, comida in enumerate(comida_range):
                propinas[i, j] = self.calcular_propina(servicio, comida)

        # Crear el gráfico de superficie
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        X, Y = np.meshgrid(comida_range, servicio_range)
        surf = ax.plot_surface(X, Y, propinas, cmap='viridis', alpha=0.8)

        ax.set_xlabel('Calidad de la Comida')
        ax.set_ylabel('Calidad del Servicio')
        ax.set_zlabel('Propina (%)')
        ax.set_title('Superficie de Control - Sistema de Propinas Fuzzy')

        fig.colorbar(surf)
        plt.savefig('images/superficie_control.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Gráfico guardado: images/superficie_control.png")
        return propinas

def main():
    """Función principal para demostrar el sistema"""
    print("=== Sistema de Control Fuzzy para Propinas ===")
    print("Universidad del Valle de Guatemala")
    print("Proyecto de Lógica Matemática\n")
    
    # Crear instancia del sistema
    sistema = SistemaPropinasSimple()
    
    # Visualizar funciones de membresía
    print("Generando gráficos de funciones de membresía...")
    sistema.visualizar_funciones_membresia()
    
    # Generar tabla de resultados
    resultados = sistema.generar_tabla_resultados()
    
    # Generar superficie de control
    print("Generando superficie de control...")
    sistema.generar_superficie_control()
    
    # Ejemplos específicos
    print("\n=== CASOS DE ESTUDIO ESPECÍFICOS ===")
    
    casos_estudio = [
        (6.5, 6.0, "Restaurante promedio - servicio y comida regulares"),
        (10, 10, "Restaurante excelente - servicio y comida excepcionales"),
        (2, 8, "Servicio deficiente pero comida excelente"),
        (9, 4, "Servicio excelente pero comida deficiente"),
        (1, 1, "Experiencia completamente negativa"),
        (7.5, 8.5, "Buen restaurante - servicio bueno, comida muy buena"),
        (3.5, 5.5, "Experiencia por debajo del promedio")
    ]
    
    for servicio, comida, descripcion in casos_estudio:
        propina = sistema.calcular_propina(servicio, comida)
        print(f"\n{descripcion}:")
        print(f"  • Calidad del servicio: {servicio}/10")
        print(f"  • Calidad de la comida: {comida}/10")
        print(f"  • Propina recomendada: {propina:.1f}%")
        
        # Análisis del resultado
        if propina < 12:
            analisis = "Propina mínima debido a la experiencia insatisfactoria"
        elif propina < 16:
            analisis = "Propina moderada, hay aspectos que mejorar"
        elif propina < 20:
            analisis = "Propina estándar para un servicio aceptable"
        else:
            analisis = "Propina generosa por un servicio excepcional"
        
        print(f"  • Análisis: {analisis}")
    
    print(f"\n=== RESUMEN DEL SISTEMA ===")
    print("• Variables de entrada: Calidad del servicio (0-10) y Calidad de la comida (0-10)")
    print("• Variable de salida: Porcentaje de propina (0-25%)")
    print("• Funciones de membresía: Triangulares (pobre, promedio, excelente)")
    print("• Reglas fuzzy: 9 reglas que combinan las variables de entrada")
    print("• Método de defuzzificación: Centroide")
    print("\n¡Sistema ejecutado exitosamente!")

if __name__ == "__main__":
    main()