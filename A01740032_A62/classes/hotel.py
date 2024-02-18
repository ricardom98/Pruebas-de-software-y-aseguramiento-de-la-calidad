'''Hotel Class'''

from classes.customer import Customer

class Hotel:
    def __init__(self, id, nombre, ubicacion, num_habitaciones):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_habitaciones = num_habitaciones
        self.habitaciones_disponibles = num_habitaciones  # Inicialmente, todas las habitaciones están disponibles.

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_num_habitaciones(self):
        return self.num_habitaciones

    def set_num_habitaciones(self, num_habitaciones):
        self.num_habitaciones = num_habitaciones

    def get_habitaciones_disponibles(self):
        return self.habitaciones_disponibles

    def set_habitaciones_disponibles(self, habitaciones_disponibles):
        self.habitaciones_disponibles = habitaciones_disponibles

    def actualizar_habitaciones_disponibles(self, cantidad):
        """Actualiza el número de habitaciones disponibles.
           Aumenta con números positivos, disminuye con negativos."""
        self.habitaciones_disponibles += cantidad

    def mostrar_informacion(self):
        print(f"Hotel ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Número total de habitaciones: {self.num_habitaciones}")
        print(f"Habitaciones disponibles: {self.habitaciones_disponibles}")

    def reservar_cuarto(self, customer: Customer):
        '''
        Reserves a room
        '''
        # pylint: disable=import-outside-toplevel
        from classes.reservation import Reservation
        reservation = Reservation(hotel=self, customer=customer)
        self.reservations.append(reservation)
        return reservation