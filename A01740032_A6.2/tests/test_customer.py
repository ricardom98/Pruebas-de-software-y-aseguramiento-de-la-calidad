# test_customer.py
import unittest
from classes.customer import Customer  # Asegúrate de ajustar este importe según tu estructura de proyecto

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada prueba"""
        self.customer = Customer("C001", "Juan Pérez", "juan.perez@example.com")

    def test_creacion_customer(self):
        """Test para verificar la correcta creación de un objeto Customer"""
        self.assertEqual(self.customer.customer_id, "C001")
        self.assertEqual(self.customer.name, "Juan Pérez")
        self.assertEqual(self.customer.contact, "juan.perez@example.com")

    def test_modificar_contacto(self):
        """Test para verificar la actualización del contacto del cliente"""
        nuevo_contacto = "juan.perez_modificado@example.com"
        self.customer.set_contact(nuevo_contacto)
        self.assertEqual(self.customer.get_contact(), nuevo_contacto)

# Si ejecutas este script directamente, corre los tests
if __name__ == '__main__':
    unittest.main()
