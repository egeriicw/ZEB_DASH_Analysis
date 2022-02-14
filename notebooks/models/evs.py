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




