from battery import Battery

class ElectricBus:

    def __init__(self, 
                 battery_capacity: float = 400,
                 id: str = "",
                 energy_performance: float = 3.0):
        self.battery = Battery(id, battery_capacity)
        self.energy_perfomance = energy_performance

    def drive(self, speed: float, time: float, distance: float, core_systems_power: float, ancillary_systems_power: float, heating_systems_power: float, cooling_systems_power: float):
        self.battery.discharge(-1.0, 10.0, dt.datetime.now())