import sys


class Sepeda:
    isSepedaRun = False
    @staticmethod
    def run():
        if(Sepeda.isCarRun):
            print('SEPEDA IN RUNING')
        else:
            print('SEPEDA IN NOT RUN')

class FoldingBike(Sepeda):
    def __init__(self):
        super(FoldingBike).__init__()
    @staticmethod
    def gowes():
        try :
            FoldingBike.runAll()
        except:
            print('Berangkat \n ', sys.exc_info)

FoldingBike.gowes()
