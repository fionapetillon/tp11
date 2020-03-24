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

    def __mul__(self,complex):
        return Complex(self.__r*complex.__r, self.__im*complex.__im)

    def __truediv__(self, complex):
        return Complex((self.__r/complex.__r),(self.__im/ complex.__im))

    def __abs__(self,complex):
        return Complex(abs(self.__r), abs(self.__im))

    def __eq__(self,complex):
        return Complex((self.__r == complex.__r) and (self.__im == complex.__im))

    def __ne__(self,complex):
        return Complex((self.__r != complex.__r)or (self.__im != complex.__im))

    def __str__(self):
        return (str(self.__r)+ str(self.__im)+ "+i")

if __name__ == '__main__':
    c1 = Complex(1,2)
    c2 = Complex(2,3)
    print( c1 + c2)
    print( c1 - c2)
    print(c1*c2)
    print(c1/c2)


