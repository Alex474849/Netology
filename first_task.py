
class Student:
    """
    All students which can give marks Lecturers
    """

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = 0

    def grade_s(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades_f_s:
                lecturer.grades_f_s[course] += [grade]
            else:
                lecturer.grades_f_s[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценказа ДЗ: {self.avg} \nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {self.finished_courses}'

        return text


    def average_value(self, name, course_g):
        avg = sum(self.grades[name]) / len(self.grades[name])
        self.avg += avg

    def __lt__(self, other):
        if isinstance(other, Student):
            return
        return self.avg < other.avg

class Mentor:
    """"
    ALL mentors
    """

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Revewier(Mentor):
    '''
    Reviewier checking homeworks and give marks
    '''

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text

class Lecturer(Mentor):
    '''
    Doing lessons and student can give him mark
    '''

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_f_s = {}
        self.avg1 = 0

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg1}'
        return text

    def average_value(self, name, course_g):
        avg = sum(self.grades_f_s[name]) / len(self.grades_f_s[name])
        self.avg1 += avg

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return
        return self.avg1 < other.avg1


le = Lecturer('Lisa', 'Swan')
le.courses_attached += ['C++']
st = Student('Roy', 'Jhons', 'male')
st.courses_in_progress += ['Python']
st.finished_courses += ['C++']
st1 = Student('Ericka', 'Smith', 'Female')
st1.courses_in_progress += ['C++']
st1.finished_courses += ['Python']
re = Revewier('Alek', 'Bolduin')
re.courses_attached += ['Python']
re.rate_hw(st, 'Python', 9)
re.rate_hw(st, 'Python', 7)
re.rate_hw(st, 'Python', 4)
re1 = Revewier('Denzel', 'Wshington')
re.courses_attached += ['C++']
re.rate_hw(st1, 'C++', 7)
re.rate_hw(st1, 'C++', 8)
re.rate_hw(st1, 'C++', 9)
st1.average_value(f'C++', [7, 8, 9])
st.average_value('Python', [9, 7, 4])
le = Lecturer('Lisa', 'Swan')
le.courses_attached += ['C++']
st.grade_s(le, 'C++', 4)
st.grade_s(le, 'C++', 8)
st.grade_s(le, 'C++', 2)
st.grade_s(le, 'C++', 3)
le.average_value('C++', [4, 8, 2, 3])
le2 = Lecturer('Brad', 'Pitt')
le2.courses_attached += ['Python']
st1.grade_s(le2, 'Python', 7)
st1.grade_s(le2, 'Python', 10)
st1.grade_s(le2, 'Python', 10)
le2.average_value('Python', [7, 10, 10])
# print(f'Выводим среднее оценки студентов и лекторов \nСтудент: {st.grades} \nЛекторы: {le.grades_f_s}')
# print(st.avg < st1.avg) # Сравниваем средние оценки студентов
# print(le.avg1 < le2.avg1) # Сравниваем средние оценки лекторов


'''
Согласно 3 заданию выводим всех лекторов, ревьюеров, студентов
'''
print(st1)
print()
print(st)
print()
print(le)
print()
print(le2)
print()
print(re)



