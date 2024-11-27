class Student:
    def __init__(self, student_id, name, age, email, phone_number):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.grades = []
    
    def add_grade(self, course_name, grade):
        self.grades.append({'course': course_name, 'grade': grade})
    
    def calculate_average_grade(self):
        total = 0
        for grade_entry in self.grades:
            total += grade_entry['grade']
        if len(self.grades) > 0:
            average = total / len(self.grades)
            return average
        else:
            return 0

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, student_id, name, age, email, phone_number):
        if name == "" or age <= 0 or email == "" or phone_number == "":
            print("Ошибка: некорректные данные студента.")
        else:
            student = Student(student_id, name, age, email, phone_number)
            self.students.append(student)
            print(f"Студент {name} добавлен.")
    
    def remove_student(self, student_id):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Студент с ID {student_id} удалён.")
                found = True
        if not found:
            print(f"Ошибка: студент с ID {student_id} не найден.")
    
    def add_grade_to_student(self, student_id, course_name, grade):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                if course_name != "" and grade >= 0:
                    student.add_grade(course_name, grade)
                    print(f"Оценка {grade} по курсу {course_name} добавлена студенту {student.name}.")
                else:
                    print("Ошибка: некорректные данные оценки.")
                found = True
        if not found:
            print(f"Ошибка: студент с ID {student_id} не найден.")
    
    def print_student_info(self, student_id):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                print(f"ID: {student.student_id}")
                print(f"Имя: {student.name}")
                print(f"Возраст: {student.age}")
                print(f"Email: {student.email}")
                print(f"Телефон: {student.phone_number}")
                print("Оценки:")
                for grade_entry in student.grades:
                    print(f" - {grade_entry['course']}: {grade_entry['grade']}")
                average = student.calculate_average_grade()
                print(f"Средний балл: {average}")
                found = True
        if not found:
            print(f"Ошибка: студент с ID {student_id} не найден.")
    
    def send_email_to_student(self, student_id, subject, message):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                # Логика отправки email (упрощённо)
                print(f"Отправка email студенту {student.email}:")
                print(f"Тема: {subject}")
                print(f"Сообщение: {message}")
                found = True
        if not found:
            print(f"Ошибка: студент с ID {student_id} не найден.")

def main():
    manager = StudentManager()
    
    # Добавление студентов
    manager.add_student(1, "Иван Иванов", 20, "ivanov@example.com", "+79001234567")
    manager.add_student(2, "Пётр Петров", 22, "petrov@example.com", "+79007654321")
    
    # Добавление оценок
    manager.add_grade_to_student(1, "Математика", 85)
    manager.add_grade_to_student(1, "Физика", 90)
    manager.add_grade_to_student(2, "Математика", 75)
    
    # Вывод информации о студентах
    manager.print_student_info(1)
    manager.print_student_info(2)
    
    # Отправка email студенту
    manager.send_email_to_student(1, "Напоминание", "Не забудьте сдать лабораторную работу.")
    
    # Удаление студента
    manager.remove_student(2)
    manager.print_student_info(2)

if __name__ == "__main__":
    main()
