# test_reservation.py
import unittest
from classes.reservation import Reservation  # Asegúrate de ajustar este importe según tu estructura de proyecto

class TestReservation(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada prueba"""
        self.reservation = Reservation("R001", "C001", "H001", "2023-01-01", "2023-01-10")

    def test_creacion_reservation(self):
        """Test para verificar la correcta creación de un objeto Reservation"""
        self.assertEqual(self.reservation.reservation_id, "R001")
        self.assertEqual(self.reservation.customer_id, "C001")
        self.assertEqual(self.reservation.hotel_id, "H001")
        self.assertEqual(self.reservation.start_date, "2023-01-01")
        self.assertEqual(self.reservation.end_date, "2023-01-10")
        self.assertEqual(self.reservation.status, "activa")

    def test_modificar_estado_reservacion(self):
        """Test para verificar la actualización del estado de la reservación"""
        nuevo_estado = "cancelada"
        self.reservation.set_status(nuevo_estado)
        self.assertEqual(self.reservation.get_status(), nuevo_estado)

# Si ejecutas este script directamente, corre los tests
if __name__ == '__main__':
    unittest.main()
