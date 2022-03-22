from enum import Enum


class FLowers(Enum):
    # name, price (euro), chemichal, temperature(Celcius), luminosity(Watts), waterperplant(liters)
    Hyacinth = ["Hyacinth", 5.00, "CHEMICHAL2", 12.00, 45.00, 1.0]
    Rose = ["Rose", 20.00, "CHEMICHAL1", 18.00, 50.00, 1.23]
    Tulip = ["Tulip", 4.00, "CHEMICAHL3", 10.00, 44.00, 2.00]


def comunication (names):

    for item in FLowers:
        if item.name==names:
            return item



