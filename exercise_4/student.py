
# Abstraccion basica de estudiante con datos basicos (Nombre, identificador y grados)

class Student:

    def __init__(self, name, id, grades):
        self.__name = name
        self.__id = id
        self.__grades = grades

    ### Getters ###
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_grades(self):
        return self.__grades

    def __str__(self):
        return f"""
    Your name is {self.__name}
    Your id is {self.__id}
    Your grades are {self.__grades}
    """
