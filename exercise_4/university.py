# Datos de un estudiante universitario, este heredado del estudiante común

import student

class University(student.Student):
    def __init__(self, name, id, grades, level, name_university):
        super().__init__(name, id, grades)
        self.__level = level
        self.__name_university = name_university


    def get_level(self):
        return self.__level

    def get_name_university(self):
        return self.__name_university

    def __str__(self):
        return f"""
        Your name is {super().get_name()}
        Your id is {super().get_id()}
        Your grades are {super().get_grades()}
        Your level is {self.__level}
        Your university is {self.__name_university}
        """