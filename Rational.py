class Rational :

    def __init__(self,numerateur,denominateur):
        self.__num=numerateur
        self.__denom=denominateur

    def getNUM(self):
        return self.__num

    def getDENOM(self):
        return self.__denom

    def __add__(self,other):
        if self.__denom==other.__denom:
            return Rational(self.__num + other.__num,other.__denom)
        else:
            r=other.getDENOM()
            other.__denom=self.getDENOM()%other.getDENOM()
            self.__denom=r
            return Rational(self.__num + other.__num,other.getDENOM())




    def __sub__(self,other):
        if self.__denom==other.__denom:
            return Rational(self.__num - other.__num,other.__denom)
        else:
            r=other.__denom
            other.__denom=self.__num%other.__denom
            self.__denom=r
            return Rational(self.__num - other.__num,other.getDENOM())


    def __mul__(self,other):
        return Rational(self.__num*other.__num, self.__denom*other.__denom)

    def __truediv__(self, other):
        return Rational((self.__num*other.__denom),(self.__denom* other.__num))



if __name__ == '__main__':
    f1=Rational(1,2)
    f2=Rational(3,4)
    f3=f1+f2
    f4=f1-f2
    f5=f1*f2
    print(f3.getNUM(),"/",f3.getDENOM())
    print(f4.getNUM(),"/",f4.getDENOM())
    print(f5.getNUM(),"/",f5.getDENOM())
