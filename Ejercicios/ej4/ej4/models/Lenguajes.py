class Lenguajes:
    def __init__(self, nombre, año, desc):
        self.__nombre = nombre
        self.__año = año
        self.__desc = desc

    @property
    def nombre(self):
        return self.__nombre

    @property
    def año(self):
        return self.__año

    @property
    def desc(self):
        return self.__desc
