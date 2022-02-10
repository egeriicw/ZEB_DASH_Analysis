class Battery:
    
    def __init__(self, 
                 id: str,
                 capacity: float = 400.0,
                 soc: float = 1.0,
                 charging_power_limit: float = 1.0,
                 discharging_power_limit: float = -1.0,
                 charging_efficiency: float = 0.95,
                 discharging_efficiency: float = 0.95):
        self.id = id
        self.capacity = capacity
        self.charging_power_limit = charging_power_limit
        self.discharging_power_limit = discharging_power_limit
        self.charging_efficiency = charging_efficiency
        self.discharging_efficiency= discharging_efficiency
        self.soc = soc
        self.current_charge = soc * capacity
        self.soc_upper_limit = 0.9
        self.soc_lower_limit = 0.1
        self.charging = False
        self.soc_logger = {}

    
    def charge(self, power_input: float, min_convert_to_hour: float, timestamp: str):
        if self.soc <= self.soc_upper_limit:
            self.soc = ((self.soc * self.capacity) + (power_input * min_convert_to_hour)) / self.capacity
        pass

    def discharge(self, power_output: float, min_convert_to_hour: float, timestamp: dt):
        if self.soc >= self.soc_lower_limit:
            self.soc = ((self.soc * self.capacity) - (power_output * min_convert_to_hour)) / self.capacity
