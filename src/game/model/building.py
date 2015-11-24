
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
        }
    },
    "Coin Press": {},
    "Armory": {
        "Description": "Allows advanced military units to be built.",
        "Effects": {
            "Unlocks": {
                "Units": ["Knight"]
            }
        }
    }
}

class Building:
    def __init__(self):
        pass
