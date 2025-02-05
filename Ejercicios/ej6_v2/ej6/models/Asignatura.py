class asignatura:
    def __init__(self, nombre, foto, horas):
        self.__nombre = nombre
        self.__foto = foto
        self.__horas = horas
        
    @property
    def nombre(self):
        return self.__nombre

    @property
    def foto(self):
        return self.__foto

    @property
    def desc(self):
        return self.__horas