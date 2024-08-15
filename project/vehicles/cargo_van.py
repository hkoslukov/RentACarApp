from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super(CargoVan, self).__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        mileage_passed = self.MAX_MILEAGE - mileage
        first_calculation = self.MAX_MILEAGE / mileage_passed
        self.battery_level = 100 - int(100 / first_calculation + 5)
