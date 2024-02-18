# test_customer.py
import io
import unittest
from unittest.mock import patch
from A01740032_A62.classes.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada prueba."""
        self.customer = Customer("C001", "Juan Pérez", "juan.perez@example.com")

    def test_creacion_customer(self):
        """Test para verificar la correcta creación de un objeto Customer."""
        self.assertEqual(self.customer.customer_id, "C001")
        self.assertEqual(self.customer.name, "Juan Pérez")
        self.assertEqual(self.customer.contact, "juan.perez@example.com")

    def test_modificar_contacto(self):
        """Test para verificar la actualización del contacto del cliente."""
        nuevo_contacto = "juan.perez_modificado@example.com"
        self.customer.set_contact(nuevo_contacto)
        self.assertEqual(self.customer.get_contact(), nuevo_contacto)

    def test_modificar_nombre(self):
        """Test para verificar la actualización del nombre del cliente."""
        nuevo_nombre = "Carlos Fuentes"
        self.customer.set_name(nuevo_nombre)
        self.assertEqual(self.customer.get_name(), nuevo_nombre)

    def test_mostrar_informacion(self):
        """Test para verificar que mostrar_informacion imprime la salida correcta."""
        expected_output = f"ID del Cliente: C001\nNombre: Juan Pérez\nContacto: juan.perez@example.com\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.customer.mostrar_informacion()
            self.assertEqual(fake_out.getvalue(), expected_output)

# Si ejecutas este script directamente, corre los tests
if __name__ == '__main__':
    unittest.main()
