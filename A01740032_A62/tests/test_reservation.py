# test_reservation.py
import unittest
from unittest.mock import patch
from io import StringIO
from A01740032_A62.classes.hotel import Hotel
from A01740032_A62.classes.customer import Customer
from A01740032_A62.classes.reservation import Reservation

class TestReservation(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada prueba"""
        self.customer = Customer("C001", "Juan Pérez", "juan.perez@example.com")
        self.hotel = Hotel(1, "Hotel Prueba", "Ciudad Prueba", 100)
        self.reservation = Reservation("R001", self.customer, self.hotel, "2023-01-01", "2023-01-10")

    def test_creacion_reservation(self):
        """Test para verificar la correcta creación de un objeto Reservation"""
        self.assertEqual(self.reservation.reservation_id, "R001")
        self.assertEqual(self.reservation.customer, self.customer)
        self.assertEqual(self.reservation.hotel, self.hotel)
        self.assertEqual(self.reservation.start_date, "2023-01-01")
        self.assertEqual(self.reservation.end_date, "2023-01-10")
        self.assertEqual(self.reservation.status, "activa")

    def test_modificar_estado_reservacion(self):
        """Test para verificar la actualización del estado de la reservación"""
        nuevo_estado = "cancelada"
        self.reservation.set_status(nuevo_estado)
        self.assertEqual(self.reservation.get_status(), nuevo_estado)

    def test_mostrar_informacion(self):
        """Test para verificar que mostrar_informacion imprime la salida correcta."""
        expected_output = (
            f"ID de la Reservación: R001\n"
            f"ID del Cliente: C001\n"
            f"ID del Hotel: 1\n"
            f"Fecha de Inicio: 2023-01-01\n"
            f"Fecha de Fin: 2023-01-10\n"
            f"Estado: activa\n"
        )
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.reservation.mostrar_informacion()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
