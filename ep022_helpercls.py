# 记录学生成绩
class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


# 使用这个类很简单
book = SimpleGradeBook()
book.add_student('牛顿')
book.report_grade('牛顿', 90)
print(book.average_grade('牛顿'))
"""
90.0
"""


# 分科目记录成绩，需要把成绩记录定义成字典
class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


# _grades 的键是学生名字，值是分科目的成绩字典 by_subject
# by_subject 字典的键是科目名字 subject，值是成绩列表
# 虽然嵌套了一层字典，使用起来还是比较方便
book = BySubjectGradebook()
book.add_student('爱因斯坦')
book.report_grade('爱因斯坦', '数学', 75)
book.report_grade('爱因斯坦', '数学', 65)
book.report_grade('爱因斯坦', '体育', 90)
book.report_grade('爱因斯坦', '体育', 95)
print(book.average_grade('爱因斯坦'))
"""
81.25
"""

import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))


# 编写科目类，该类包含一系列考试成绩
class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


# 编写学生类，包括学生学习的所有课程
class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        # if name not in self._subjects:
        #     self._subjects[name] = Subject()
        # return self._subjects[name]
        # 我是这么写的，一句搞定
        return self._subjects.setdefault(name, Subject())

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


# 最后编写包含所有学生考试成绩的容器类
class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        # if name not in self._students:
        #     self._students[name] = Student()
        # return self._students[name]
        # 我是这么写的，一句搞定
        return self._students.setdefault(name, Student())


book = Gradebook()
albert = book.student('爱因斯坦')
math = albert.subject('数学')
math.report_grade(80, 0.1)
math.report_grade(90, 0.1)
print(albert.average_grade())
"""
85.0
"""
