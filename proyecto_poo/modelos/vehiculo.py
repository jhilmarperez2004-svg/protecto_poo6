# Archivo: modelos/vehiculo.py
"""

"""

class Vehiculo:
    def __init__(self, marca, modelo, año):
        """
        Constructor de la clase base Vehiculo.
        
        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo
            año (int): Año de fabricación
        """
        # Atributos privados (encapsulación)
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    
    # Getters y Setters para acceder a los atributos privados
    @property
    def marca(self):
        """Getter para la marca del vehículo"""
        return self.__marca
    
    @marca.setter
    def marca(self, nueva_marca):
        """Setter para la marca del vehículo"""
        self.__marca = nueva_marca
    
    @property
    def modelo(self):
        """Getter para el modelo del vehículo"""
        return self.__modelo
    
    @modelo.setter
    def modelo(self, nuevo_modelo):
        """Setter para el modelo del vehículo"""
        self.__modelo = nuevo_modelo
    
    @property
    def año(self):
        """Getter para el año del vehículo"""
        return self.__año
    
    @año.setter
    def año(self, nuevo_año):
        """Setter para el año del vehículo"""
        if nuevo_año > 1885:  # Primer automóvil patentado
            self.__año = nuevo_año
        else:
            print("Año no válido para un vehículo")
    
    def mostrar_informacion(self):
        """
        Método que muestra información básica del vehículo.
        Este método será sobrescrito (polimorfismo).
        """
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}"
    
    def arrancar(self):
        """
        Método común para todos los vehículos.
        Demuestra polimorfismo al tener diferentes implementaciones.
        """
        return "El vehículo está arrancando..."