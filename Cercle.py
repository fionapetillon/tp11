class Cercle :

    def __init__(self,r):
        self.__r=r

    def getR(self):
        return self.__r

    def __add__(self, deux):
        return Cercle(self.__r+deux.__r)

    def __lt__(self, deux):
        return self.__r < deux.__r

    def __gt__(self, deux):
        return self.__r > deux.__r

if __name__ == '__main__' :
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(str(c3.getR()))
    print(c4)
    print(c5)




