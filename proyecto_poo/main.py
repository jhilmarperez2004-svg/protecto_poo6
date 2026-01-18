# Archivo: main.py
"""
Archivo principal que demuestra el funcionamiento del programa.
Crea instancias de las clases y muestra los conceptos de POO.
"""

from modelos.vehiculo import Vehiculo
from modelos.automovil import Automovil
from servicios.gestion_vehiculos import GestionVehiculos

def main():
    """
    Función principal que demuestra todos los conceptos de POO:
    - Herencia
    - Encapsulación
    - Polimorfismo
    - Creación de instancias
    """
    
    print("=" * 50)
    print("DEMOSTRACIÓN DE CONCEPTOS DE PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=" * 50)
    
    # 1. DEMOSTRACIÓN DE ENCAPSULACIÓN
    print("\n1. ENCAPSULACIÓN:")
    print("-" * 30)
    
    # Crear instancia de Vehiculo (clase base)
    vehiculo_base = Vehiculo("Genérica", "Transporte", 2020)
    
    # Acceder a atributos privados mediante getters (encapsulación)
    print(f"Marca obtenida mediante getter: {vehiculo_base.marca}")
    print(f"Modelo obtenido mediante getter: {vehiculo_base.modelo}")
    
    # Modificar atributos mediante setters
    vehiculo_base.marca = "Marca Actualizada"
    vehiculo_base.modelo = "Modelo Actualizado"
    print(f"Después de setters: {vehiculo_base.marca} {vehiculo_base.modelo}")
    
    # 2. DEMOSTRACIÓN DE HERENCIA
    print("\n2. HERENCIA:")
    print("-" * 30)
    
    # Crear instancia de Automovil (clase derivada)
    mi_auto = Automovil("Toyota", "Corolla", 2023, "Híbrido", 4)
    otro_auto = Automovil("Tesla", "Model 3", 2024, "Eléctrico", 4)
    
    print(f"Automóvil creado: {mi_auto.marca} {mi_auto.modelo}")
    print(f"Hereda atributos de Vehiculo: Año = {mi_auto.año}")
    
    # 3. DEMOSTRACIÓN DE POLIMORFISMO
    print("\n3. POLIMORFISMO:")
    print("-" * 30)
    
    # Crear diferentes tipos de vehículos
    vehiculo_generico = Vehiculo("Marca Genérica", "Modelo Básico", 2021)
    
    # Lista que contiene diferentes tipos de objetos (polimorfismo)
    lista_vehiculos = [vehiculo_generico, mi_auto, otro_auto]
    
    print("Mismo método mostrar_informacion(), diferentes implementaciones:")
    for vehiculo in lista_vehiculos:
        print(f"  - {vehiculo.mostrar_informacion()}")
    
    print("\nMismo método arrancar(), diferentes comportamientos:")
    for vehiculo in lista_vehiculos:
        print(f"  - {vehiculo.arrancar()}")
    
    # 4. USO DE LA CAPA DE SERVICIOS
    print("\n4. GESTIÓN CON LA CAPA DE SERVICIOS:")
    print("-" * 30)
    
    gestor = GestionVehiculos()
    
    # Agregar vehículos al gestor
    gestor.agregar_vehiculo(vehiculo_generico)
    gestor.agregar_vehiculo(mi_auto)
    gestor.agregar_vehiculo(otro_auto)
    
    # Mostrar todos los vehículos
    print("Todos los vehículos registrados:")
    for info in gestor.mostrar_todos_vehiculos():
        print(f"  - {info}")
    
    # Arrancar todos los vehículos (polimorfismo)
    print("\nArrancando todos los vehículos:")
    for mensaje in gestor.arrancar_todos():
        print(f"  - {mensaje}")
    
    # Contar automóviles específicos
    print(f"\nTotal de automóviles en el sistema: {gestor.contar_automoviles()}")
    
    # 5. MÉTODOS ESPECÍFICOS DE LA CLASE DERIVADA
    print("\n5. MÉTODOS ESPECÍFICOS DE AUTOMOVIL:")
    print("-" * 30)
    
    print(f"Método específico de Automovil: {mi_auto.abrir_puertas(2)}")
    print(f"Intento de abrir más puertas de las que tiene: {mi_auto.abrir_puertas(5)}")
    
    print("\n" + "=" * 50)
    print("DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 50)

# Punto de entrada del programa
if __name__ == "__main__":
    main()