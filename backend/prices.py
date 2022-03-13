from enum import Enum


class Prices(Enum):
    # name, price (euro), chemichal, temperature(Celcius), luminosity(Watts), waterperplant(liters)
    Electicity = ["Electicity", 5.00, 1]
    Gas = ["Gas", 9, 1]


def comunicationprices(names):
    for item in Prices:
        if item.name == names:

            return item
