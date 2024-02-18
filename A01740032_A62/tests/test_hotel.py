# test_hotel.py
import unittest
from classes.hotel import Hotel  # Ajusta este importe según tu estructura de proyecto

class TestHotel(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada prueba"""
        self.hotel = Hotel(1, "Hotel Prueba", "Ubicación Prueba", 100)

    def test_creacion_hotel(self):
        """Test para verificar la correcta creación de un objeto Hotel"""
        self.assertEqual(self.hotel.id, 1)
        self.assertEqual(self.hotel.nombre, "Hotel Prueba")
        self.assertEqual(self.hotel.ubicacion, "Ubicación Prueba")
        self.assertEqual(self.hotel.num_habitaciones, 100)
        self.assertEqual(self.hotel.habitaciones_disponibles, 100)

    def test_actualizar_habitaciones_disponibles(self):
        """Test para verificar la actualización de habitaciones disponibles"""
        self.hotel.actualizar_habitaciones_disponibles(-10)
        self.assertEqual(self.hotel.habitaciones_disponibles, 90)
        
        # Verificar que también se puede aumentar el número de habitaciones disponibles
        self.hotel.actualizar_habitaciones_disponibles(5)
        self.assertEqual(self.hotel.habitaciones_disponibles, 95)

# Si ejecutas este script directamente, corre los tests
if __name__ == '__main__':
    unittest.main()
