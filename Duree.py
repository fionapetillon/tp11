class Duree:

    def __init__(self,heure,minute,seconde):
        self.__h=heure
        self.__min=minute
        self.__s=seconde

    def getH(self):
        return self.__h

    def getMIN(self):
        return self.__min

    def getS(self):
        return self.__s

    def __str__(self):
        return (str(self.__h)+"h"+str(self.__min)+"min"+str(self.__s)+"s")

    def __add__(self, other):
        s = self.__s + other.__s
        min = self.__min + other.__min + (s//60)
        h= self.__h + other.__h  + (min//60)
        return Duree(h,min%60,s%60)

if __name__ == '__main__':
    d1=Duree(12,22,52)
    d2=Duree(1,20,20)
    print(d1)
    print(d2)
    print(d1+d2)
