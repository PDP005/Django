class asignatura:
    def __init__(self, nombre, profesor, horas):
        self.__nombre = nombre
        self.__profesor = profesor
        self.__horas = horas
        
    @property
    def nombre(self):
        return self.__nombre

    @property
    def profesor(self):
        return self.__profesor

    @property
    def desc(self):
        return self.__horas