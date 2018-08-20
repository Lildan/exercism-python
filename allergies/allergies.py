ALLERGIES = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
    }

class Allergies(object):
    allergy_code = 0
     
    def __init__(self, score):
        self.allergy_code = score

    def is_allergic_to(self, item):
        for key in ALLERGIES:
            if ALLERGIES[key] == item:
                if key & self.allergy_code == key:
                    return True
                return False
        return False

    @property
    def lst(self):
        ret = []

        for key in ALLERGIES:
            if  key & self.allergy_code == key:
                ret.append(ALLERGIES[key])
        
        return ret
