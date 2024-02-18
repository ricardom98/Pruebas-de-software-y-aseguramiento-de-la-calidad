class Reservation:
    def __init__(self, reservation_id, customer_id, hotel_id, start_date, end_date, status="activa"):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def get_reservation_id(self):
        return self.reservation_id

    def get_customer_id(self):
        return self.customer_id

    def get_hotel_id(self):
        return self.hotel_id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def mostrar_informacion(self):
        print(f"ID de la Reservación: {self.reservation_id}")
        print(f"ID del Cliente: {self.customer_id}")
        print(f"ID del Hotel: {self.hotel_id}")
        print(f"Fecha de Inicio: {self.start_date}")
        print(f"Fecha de Fin: {self.end_date}")
        print(f"Estado: {self.status}")
