#
# Ejercicio 4
# 

# Contexto: Aplicacion de un crowd haciendo uso de herencia basica entre las clases basicas "student" y "university"
# codigo de ejercicio 4 realizado en ingles a modo de practica en este idioma y tambien por motivos de entendimiento

# se realiza el uso de varios archivos como mera curiosidad de como trabajarlos, en este caso se usa el archivo "student.py" y "university.py"

# tambien se planea un programa basico crowd que permite ingresar datos de estudiantes y estudantes universitarios


# CROWD incompleto cabe recalcar

import student as st
import university as uni


def students_grades(grades):

    line = ""
    while line != "exit":
        print(f"""
        Write your grades one by one after intro.
        When you are done, type "exit".

        Grades: {grades} 
        """)
        line = input("Grade: ")
        if line != "exit":
            grades.append(line)
        else:
            break
    return grades


def main():
    menu_message = """
    WELCOME TO THE STUDENT CRAZY SYSTEM

    1. Add a student
    2. Add a university student
    3. Exit
    """

    print(menu_message)
    option = input("Enter your option: ")
    while option != "3":
        name = input("Enter your name: ")
        id = input("Enter your id: ")
        grades = students_grades([])

        if option == "1":
            students = st.Student(name, id, grades)
            print(students.__str__())
        elif option == "2":
            university_name = input("Enter your university name: ")
            university_level = int(input("Enter your university level: "))

            university = uni.University(name, id, grades, university_level, university_name)
            print(university.__str__())
        elif option == "3":
            print('Bye!')
            break
        else:
            print("Invalid option")
        print(menu_message)
        option = input("Enter your option: ")
    print("Bye!")


main()
