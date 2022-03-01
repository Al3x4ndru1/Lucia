import random
from backend.enums import comunication
from backend.enums import FLowers
from backend.Chemicas import Chemichals
from backend.Chemicas import comunicationChem

def flowes():
    var = FLowers
    watercost = 1.0
    var=comunication("Rose")
    plants=random.randint(0, 167)
    varchem = Chemichals
    varchem = comunicationChem(var.value[2])
    print(varchem.value[0])
    print(" Name:",var.value[0],'\n',"Price:",var.value[1]," euros",'\n',"Chemichal:", var.value[2],'\n', "Themperature:",var.value[3],"Celsiu",'\n',"Luminosity", var.value[4], "Watts", '\n', "Waterperplant", var.value[5], "liters")
    range=plants/2
    sold=random.randint(0, plants)
    week=random.randint(14,16)
    cost=((watercost*var.value[5]*(plants/10))+ varchem.value[1]*(plants/8))*week
    Profit=var.value[1] * sold
    Damage=var.value[1] *(plants-sold)
    print("Plants:",plants,'\n',"Sold:",sold,'\n',"Profit:", Profit-cost, "euros",'\n',"Damage:",Damage,"euros",'\n',"Weeks",week, '\n',"Cost:",cost)