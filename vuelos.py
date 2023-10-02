class Reserva:
    def __init__(self, nombre_pasajero, numero_vuelo, fecha):
        self.nombre_pasajero = nombre_pasajero
        self.numero_vuelo = numero_vuelo
        self.fecha = fecha

    def mostrar_detalle(self):
        raise NotImplementedError("Este método debe ser implementado en las clases derivadas.")


class ReservaEconomica(Reserva):
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, asiento):
        super().__init__(nombre_pasajero, numero_vuelo, fecha)
        self.asiento = asiento

    def mostrar_detalle(self):
        print(f"Reserva Económica - Nombre del pasajero: {self.nombre_pasajero}, Número de vuelo: {self.numero_vuelo}, Fecha: {self.fecha}, Asiento: {self.asiento}")


class ReservaBusiness(Reserva):
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, sala_espera):
        super().__init__(nombre_pasajero, numero_vuelo, fecha)
        self.sala_espera = sala_espera

    def mostrar_detalle(self):
        print(f"Reserva Business - Nombre del pasajero: {self.nombre_pasajero}, Número de vuelo: {self.numero_vuelo}, Fecha: {self.fecha}, Sala de espera: {self.sala_espera}")


class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, servicio):
        super().__init__(nombre_pasajero, numero_vuelo, fecha)
        self.servicio = servicio

    def mostrar_detalle(self):
        print(f"Reserva Primera Clase - Nombre del pasajero: {self.nombre_pasajero}, Número de vuelo: {self.numero_vuelo}, Fecha: {self.fecha}, Servicio: {self.servicio}")



reserva_economica = ReservaEconomica("John Doe", "FL123", "2023-10-05", "22A")
reserva_business = ReservaBusiness("Jane Smith", "FL456", "2023-10-10", "Sala VIP")
reserva_primera_clase = ReservaPrimeraClase("Alice Johnson", "FL789", "2023-10-15", "Mayordomo personal")

reserva_economica.mostrar_detalle()
reserva_business.mostrar_detalle()
reserva_primera_clase.mostrar_detalle()
