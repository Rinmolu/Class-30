class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price
computer1 = computer()
computer1.sell()
computer1.__maxprice = 1000
computer1.sell()
computer1.setmaxprice(2000)
computer1.sell()
