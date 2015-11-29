
ALL_UNITS = {
    "Archer": {
        "Description": "",
        "Cost": {
            "Food": 20,
            "Wood": 20
        },
        "Attack": 10,
        "Defense": 10,
        "MaxHealth": 50
    }
}

class Unit:
    def __init__(self, unit_name):
        self.unit_data = ALL_UNITS[unit_name]
        self.current_health = self.unit_data["MaxHealth"]

    @staticmethod
    def get_all_units():
        return ALL_UNITS

    def get_current_health(self):
        return self.current_health

    def get_attack(self):
        return self.unit_data["Attack"]

    def get_defense(self):
        return self.unit_data["Defense"]

    def get_max_health(self):
        return self.unit_data["MaxHealth"]
