import datetime
import random
from backend.enums import comunication
from backend.enums import FLowers
from backend.Chemicas import Chemichals
from backend.Chemicas import comunicationChem
from backend.prices import comunicationprices
from backend.prices import Prices
from backend.senzori.water.water import intoduce
from backend.printing import credings
from backend.senzori.luminosity.luminosity1 import checklum
from backend.senzori.temperature.temperature import checktemp

import csv
import eel


def flowes():
        var = FLowers
        watercost = 1.0
        var = comunication("Rose")
        plants = random.randint(0, 167)
        intoduce(plants,var.value[5])
        varchem = Chemichals
        varchem = comunicationChem(var.value[2])
        checklum(var.value[4])
        checktemp(var.value[3])
        eel.Numbarplants(plants)
        eel.Typeplants("Blue")
        # the next print statement will show each var.value meaning, can be uncommented print(" Name:", var.value[0],
        # '\n', "Price:", var.value[1], " euros", '\n', "Chemichal:", var.value[2], '\n', "Themperature:",
        # var.value[3], "Celsiu", '\n', "Luminosity", var.value[4], "Watts", '\n', "Waterperplant",var.value[5],
        # "liters")


        sold = random.randint(0, plants)
        week = random.randint(14, 16)
        cost = ((watercost * var.value[5] * (plants / 10)) + varchem.value[1] * (plants / 8)) * week
        Profit = var.value[1] * sold
        Damage = var.value[1] * (plants - sold)

        Current_Date = datetime.datetime.now()  # datetime.datetime.today().strftime('%d-%b-%Y')
        # in the right part is the corect code but I chosed to add the time as well to be able to create more csv in
        # a shord period of time


        with open(("./backend/Csv_files/Production_" + str(Current_Date) + '.csv'), 'w') as new_file:
            csv.writer = csv.writer(new_file, delimiter=' ')

            csv.writer.writerow(['Name:', var.value[0]])
            csv.writer.writerow(['Price:', var.value[1], 'euros'])
            csv.writer.writerow(['Chemichal:', var.value[2]])
            csv.writer.writerow(['Themperature:', var.value[3], 'Celsiu'])
            csv.writer.writerow(['Luminosity', var.value[4], 'Watts'])
            csv.writer.writerow(['Waterperplant', var.value[5], 'liters'])
            csv.writer.writerow(['Plants:', plants])
            csv.writer.writerow(['Sold:', sold])
            csv.writer.writerow(['Profit:', Profit - cost, 'euros'])
            csv.writer.writerow(['Damage:', Damage, 'euros'])
            csv.writer.writerow(['Weeks', week])
            csv.writer.writerow(['Cost:', cost, 'euros'])
            new_file.close()

        credings() # read the csv files