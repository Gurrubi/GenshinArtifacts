from classes.Artifact import *
from classes.Stats import *

def checkValue(name, value):
    result = False;
    value = float(value)
    for values in genshinStats[name]:
        if(values == value and not result):
            result = True;

    return result

if __name__ == "__main__":
    #print(list(genshinStats.keys())[0])
    #*genshinStats[0]

    print("Introduzca Artefacto:\n")
    todaInfo = input()

    todaInfo = todaInfo.replace(' ','')
    mainStat = todaInfo.split("|")[0].split("+")[0]
    subStats = []

    for stat in todaInfo.split("|")[1].split(","):
        if(checkValue(stat.split("+")[0], stat.split("+")[1])):
            subStats.append({stat.split("+")[0]: float(stat.split("+")[1])})

    #print(f"La main stat: {mainStat}, las substats: {subStats}")

    artefacto = Artifact(mainStat, subStats)

    activo = True

    while(activo):
        print(f"Artefacto MainStat {mainStat} | {artefacto.getStats()}")
        interacion = input()
        artefacto.upgrade()