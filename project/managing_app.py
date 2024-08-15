from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle, CargoVan, PassengerCar] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for u in self.users:
            if u.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        else:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        else:
            if vehicle_type == 'PassengerCar':
                vehicle = PassengerCar(brand, model, license_plate_number)
                self.vehicles.append(vehicle)
                return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

            elif vehicle_type == 'CargoVan':
                vehicle = CargoVan(brand, model, license_plate_number)
                self.vehicles.append(vehicle)
                return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

            else:
                return f"Vehicle type {vehicle_type} is inaccessible."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif r.start_point == start_point and r.end_point == end_point and r.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
        else:
            route = Route(start_point, end_point, length, len(self.routes) + 1)
            self.routes.append(route)
            for y in self.routes:
                if y.start_point == start_point and y.end_point == end_point and y.length > length:
                    y.is_locked = True

            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        elif vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        elif route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        else:
            vehicle.drive(route.length)

            if is_accident_happened:
                vehicle.is_damaged = True
                user.decrease_rating()

                return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery:" \
                       f" {vehicle.battery_level}% Status: Damaged"
            else:
                user.increase_rating()

                return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery:" \
                       f" {vehicle.battery_level}% Status: OK"

    # def repair_vehicles(self, count: int):
    #     broken_vehicles = []
    #     for v in self.vehicles:
    #         if v.is_damaged:
    #             broken_vehicles.append(v)
    #     sorted_broken_vehicles = sorted(broken_vehicles, key=lambda x: -x.brand)
    #
    # def users_report(self):
        result = ''
        for u in sorted(self.users, key=lambda x: -x.rating):
            result += f"{u.__str__()}\n"

        return result


app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.users_report())

