# Archivo: servicios/gestion_vehiculos.py
"""
Módulo de servicios que gestiona las operaciones con vehículos.
"""

from modelos.vehiculo import Vehiculo
from modelos.automovil import Automovil

class GestionVehiculos:
    def __init__(self):
        """Constructor de la clase de servicios"""
        self.vehiculos = []
    
    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la lista de gestión.
        
        Args:
            vehiculo (Vehiculo): Instancia de Vehiculo o Automovil
        
        Returns:
            str: Confirmación de la operación
        """
        self.vehiculos.append(vehiculo)
        return f"Vehículo {vehiculo.marca} agregado correctamente"
    
    def mostrar_todos_vehiculos(self):
        """
        Muestra información de todos los vehículos registrados.
        Demuestra polimorfismo al llamar al método mostrar_informacion()
        que tiene diferentes implementaciones.
        
        Returns:
            list: Lista con información de todos los vehículos
        """
        info_vehiculos = []
        for vehiculo in self.vehiculos:
            info_vehiculos.append(vehiculo.mostrar_informacion())
        return info_vehiculos
    
    def arrancar_todos(self):
        """
        Intenta arrancar todos los vehículos.
        Ejemplo de polimorfismo: mismo método, diferentes resultados.
        
        Returns:
            list: Lista con mensajes de arranque de cada vehículo
        """
        mensajes = []
        for vehiculo in self.vehiculos:
            mensajes.append(vehiculo.arrancar())
        return mensajes
    
    def contar_automoviles(self):
        """
        Cuenta cuántos automóviles hay en la lista.
        
        Returns:
            int: Número de automóviles
        """
        count = 0
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, Automovil):
                count += 1
        return count