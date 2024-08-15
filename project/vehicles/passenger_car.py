from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super(PassengerCar, self).__init__(brand, model, license_plate_number, PassengerCar.MAX_MILEAGE)

    def drive(self, mileage: float):
        mileage_passed = self.MAX_MILEAGE - mileage
        first_calculation = self.MAX_MILEAGE / mileage_passed
        self.battery_level = 100 - int(100 / first_calculation)
