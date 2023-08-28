#import Stats
import random
from .Chances import *
from .Stats import *

class Artifact:
    def __init__(self, mainStat, subStats):
        self.__Main = mainStat
        self.__Stats = subStats
        self.__Lvl = 0;
        self.__Chances = rollChances[0]

    def upgrade(self):
        if (len(self.__Stats) == 3):
            pass
        elif (len(self.__Stats) == 4):
            aleatorio = random.randint(1,100)
            statIndex = 0
            found = False
            suma = 0
            i = 0 

            while i in range(0,len(self.__Chances)) and not found:
                #print(f"El valor de la suma es: {suma} el valor del aleatorio es: {aleatorio}, self_chaces: ")
                if(suma < aleatorio <= (suma + self.__Chances[i])):
                    statIndex = i;
                    found = True
                else:
                    suma += self.__Chances[i]
                
                i+=1
            
            print(list(self.__Stats[statIndex].keys())[0])

            statToUpgrade = list(self.__Stats[statIndex].keys())[0]
            quantity = genshinStats[statToUpgrade][random.randint(0,3)]
            
            self.__Stats[statIndex][statToUpgrade] += quantity
            self.__Lvl += 4
            self.__Chances = rollChances[self.__Lvl]
            #print(f"El indice a mejorar es: {statIndex}")
            
    def getStats(self):
        return self.__Stats
    
    def printInfo(self):
        print(f"El stat principal es")