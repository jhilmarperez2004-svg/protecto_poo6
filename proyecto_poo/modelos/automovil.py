# Archivo: modelos/automovil.py
"""
Módulo que contiene la clase derivada Automovil.
Implementa herencia de Vehiculo y sobrescribe métodos (polimorfismo).
"""

from modelos.vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_combustible, num_puertas):
        """
        Constructor de la clase derivada Automovil.
        
        Args:
            marca (str): Marca del automóvil
            modelo (str): Modelo del automóvil
            año (int): Año de fabricación
            tipo_combustible (str): Tipo de combustible (gasolina, diesel, eléctrico)
            num_puertas (int): Número de puertas
        """
        # Llamada al constructor de la clase base (herencia)
        super().__init__(marca, modelo, año)
        
        # Atributos específicos de Automovil
        self.tipo_combustible = tipo_combustible
        self.num_puertas = num_puertas
    
    # Polimorfismo: Sobrescritura del método de la clase base
    def mostrar_informacion(self):
        """
        Método sobrescrito que muestra información específica del automóvil.
        Ejemplo de polimorfismo: Mismo nombre, diferente implementación.
        """
        info_base = super().mostrar_informacion()
        return f"{info_base}, Combustible: {self.tipo_combustible}, Puertas: {self.num_puertas}"
    
    # Polimorfismo: Sobrescritura de otro método
    def arrancar(self):
        """
        Método sobrescrito con comportamiento específico para automóviles.
        """
        return f"El automóvil {self.marca} {self.modelo} enciende el motor de {self.tipo_combustible}"
    
    # Método específico de Automovil
    def abrir_puertas(self, num_puertas_abrir):
        """
        Método específico de la clase Automovil.
        
        Args:
            num_puertas_abrir (int): Número de puertas a abrir
        
        Returns:
            str: Mensaje indicando cuántas puertas se abrieron
        """
        if num_puertas_abrir <= self.num_puertas:
            return f"Abriendo {num_puertas_abrir} puerta(s) del automóvil"
        else:
            return f"El automóvil solo tiene {self.num_puertas} puertas"