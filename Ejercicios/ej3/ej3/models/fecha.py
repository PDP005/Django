from datetime import datetime
class Fecha():
    hoy= datetime.now()
    def __init__(self,fecha=hoy):
        self.__fecha=fecha
