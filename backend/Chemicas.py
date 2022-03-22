from enum import Enum

class Chemichals(Enum):
                    #name       price quantity
    CHEMICHAL1 = ["Chemichal1", 2.00, 800.00]
    CHEMICHAL2 = ["Chemichal2", 7.00, 250.00]
    CHEMICHAL3 = ["Chemichal3", 9.00, 250.00]


def comunicationChem (names):

    for item in Chemichals:
        if item.name==names:
            return item