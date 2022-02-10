import logging
import datetime as dt
from battery import Battery


class Simulation:
    pass

class Charger:

    def __init__(self, 
        input_ac_power_rating: float, 
        input_dc_power_rating: float, efficiency: float, power_factor: float, rated_voltage: float, rated_amperage: float):
        self.input_dc_power_rating = input_dc_power_rating
        self.efficiency = efficiency

    def charge(self):
        
        return self.input_dc_power_rating * self.efficiency

class Route:
    pass



class ElectricBus:

    def __init__(self):
        self.battery = Battery(400, 1, '1')

    def drive(self, speed: float, time: float, core_systems_power: float, ancillary_systems_power: float, heating_systems_power: float, cooling_systems_power: float):
        self.battery.discharge(-1.0, 10.0, dt.datetime.now())
