class Complex :

    def __init__(self,relle,imaginaire):
        self.__r=relle
        self.__im=imaginaire

    def getR(self):
        return self.__r

    def getIm(self):
        return self.__im

    def __add__(self,complex):
        return Complex(self.__r + complex.__r, self.__im + complex.__im)

    def __sub__(self,complex):
        return Complex(self.__r - complex.__r, self.__im - complex.__im)

    def __truediv__(self, complex):
        return Complex(self.__r / complex.__r, self.__im / complex.__im)

    def __abs__(self,complex):
        return Complex((self.__r**2)+ complex.__r, self.__im - complex.__im)
