ALLERGIES = {
"eggs": 1,
"peanuts": 2,
"shellfish": 4,
"strawberries": 8,
"tomatoes": 16,
"chocolate": 32,
"pollen": 64,
"cats": 128
}

class Allergies(object):
    allergy_code = 0
     
    def __init__(self, score):
        self.allergy_code = score

    def is_allergic_to(self, item):
        if item in ALLERGIES:        
            if ALLERGIES[item] & self.allergy_code == ALLERGIES[item]:
                return True
        return False

    @property
    def lst(self):
        ret = []

        for key in ALLERGIES:
            if  ALLERGIES[key] & self.allergy_code == ALLERGIES[key]:
                ret.append(key)
        
        return ret
