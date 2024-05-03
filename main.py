class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    # Функция для вывода средней оценки за домашние задания конкретных студентов
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n" + \
            f" Средняя оценка за домашние задания: {self.average_grade()}\n" + \
            f" Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" + \
            f" Завершенные курсы: {''.join(self.finished_courses)}"

    def average_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 2)

    # Сравнение средних оценок лекторов за курсы
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Функции для подсчета и вывода средней оценки за лекции конкретных лекторов
    def average_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n" + \
            f" Средняя оценка за лекции: {self.average_grade()}"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return False


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибкa'


# Студенты, которые учатся на курсах
Alisa = Student('Alisa', 'Bond', 'female')
Alisa.courses_in_progress += ['Python', 'Git']
Alisa.finished_courses += ['Введение в программирование']

Jack = Student('Jack', 'Vorobey', 'male')
Jack.courses_in_progress += ['Python']
Jack.courses_in_progress += ['Git']
Jack.finished_courses += ['Введение в программирование']

best_student = Student('Ruby', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

# Имена ревьюеров и курсы
Jams = Reviewer('Jams', 'Bond')
Jams.courses_attached += ['Python']

Melisa = Reviewer('Melisa', 'Kolin')
Melisa.courses_attached += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

# Ревьюеры выставляют оценки студентам
cool_reviewer.rate_hw(Alisa, 'Python', 9.9)
cool_reviewer.rate_hw(Jack, 'Python', 9.8)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(Alisa, 'Git', 9.8)
cool_reviewer.rate_hw(Jack, 'Git', 9.8)
cool_reviewer.rate_hw(best_student, 'Git', 9.8)

# Имена лекторов и их курсы
Mikle = Lecturer('Mikle', 'Nikson')
Mikle.courses_attached += ['Python']

Samanta = Lecturer('Samanta', 'Vinch')
Samanta.courses_attached += ['Git']

cool_lecturer = Lecturer('Bob', 'Silver')
cool_lecturer.courses_attached += ['Python', 'Git']

# Студенты выставляют оценки лекторам
Alisa.rate_lecturer(Mikle, 'Python', 9.9)
Alisa.rate_lecturer(Samanta, 'Git', 9.9)

Jack.rate_lecturer(Mikle, 'Python', 9.9)
Jack.rate_lecturer(Samanta, 'Git', 9.9)

best_student.rate_lecturer(cool_lecturer, 'Python', 9.8)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)


# Создаем функции для подсчета средней оценки по всем студентам за конкретный курс
def average_grade_students(students, course):
    sum_grades = 0
    count_students = 0

    for student in students:
        if course in student.grades:
            sum_grades += sum(student.grades[course])
            count_students += len(student.grades[course])
    if count_students == 0:
        return 0
    else:
        return f"Средняя оценка по домашнему заданию по всем студентам по курсу {course}: {round(sum_grades / count_students, 2)}"


# Создаем функции для подсчета средней оценки по всем лекторам за конкретный курс
def average_grade_lecturers(lecturers, course):
    sum_grades = 0
    count_lecturers = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            count_lecturers += len(lecturer.grades[course])
    if count_lecturers == 0:
        return "Ошибка"
    else:
        return f"Средняя оценка всех лекторов по курсу {course}: {round(sum_grades / count_lecturers, 2)}"


# Сравнение средних оценок студентов по курсам
def __eq__(self, other):
    if isinstance(other, Student):
        return self.average_grade() == other.average_grade()
    return False


print(Alisa == Jack)
print(Jack == best_student)
print(best_student == Alisa)

# Сравнение средних оценок лекторов по курсам
print(Mikle == Samanta)
print(Samanta == cool_lecturer)
print(Mikle == cool_lecturer)

print(best_student.grades)
print()
print(cool_lecturer.grades)
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(Jack)
print()
print(average_grade_students([Alisa, Jack, best_student], 'Python'))
print()
print(average_grade_lecturers([Mikle, Samanta], 'Python'))
print()
print(average_grade_students([Alisa, Jack, best_student], 'Git'))
print()
print(average_grade_lecturers([Mikle, Samanta], 'Git'))
