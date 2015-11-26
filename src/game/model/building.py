
ALL_BUILDINGS = {
    "Food Mill": {
        "Description": "Provides food bonuses.",
        "Effects": {
            "Bonus": {
                "Tile": {
                    "Food": 1.0
                },
                "Map": {
                    "Food": 0.1
                }
            }
        },
        "Cost": {
            "Wood": 100
        }
    },
    "Coin Press": {
        "Description": "Provides gold bonuses.",
        "Effects": {
            "Bonus": {
                "Tile": {
                    "Gold": 1.0
                },
                "Map": {
                    "Gold": 0.1
                }
            }
        },
        "Cost": {
            "Wood": 100
        }
    },
    "Armory": {
        "Description": "Allows advanced military units to be built.",
        "Effects": {
            "Unlocks": {
                "Units": ["Knight"]
            }
        },
        "Cost": {
            "Wood": 100
        }
    }
}

class Building:
    def __init__(self, building_name):
        self.building_data = ALL_BUILDINGS[building_name]

    @staticmethod
    def get_all_buildings():
        return ALL_BUILDINGS

    def get_building_map_bonuses(self):
        try:
            return self.building_data["Effects"]["Bonus"]["Map"]
        except KeyError:
            return None

    def get_building_tile_bonuses(self):
        try:
            return self.building_data["Effects"]["Bonus"]["Tile"]
        except KeyError:
            return None
