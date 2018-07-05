from db import db_handler
class BaseClass:
    def save(self):
        """存储文件"""
        db_handler.save(self)
    @classmethod
    def get_obj_by_name(cls,name):
        """读取文件夹"""
        return db_handler.select(name,cls.__name__.lower())

class Admin(BaseClass):
    """管理员类登记"""
    def __init__(self,name,password):
        self.name=name
        self.password=password

        self.save()
    def create_school(self,school_name,addr):
        School(school_name,addr)

    def create_course(self,name):
        Course(name)
    def create_tercher(self,name,password):
        Teacher(name,password)

class Teacher(BaseClass):
    """老师类登记"""
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.course_list=[]
        self.save()
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()
    def modify_score(self,student,course_name,scores):
        student.scores[course_name]=scores
        student.save()

class Student(BaseClass):
    """学生类登记"""
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school =None
        self.course_list=[]
        self.scores={}
        self.save()
    def get_school(self):
        return self.school

    def choose_school(self,name):
        self.school=name
        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.scores[course_name] = 0
        self.save()
        
        
class School(BaseClass):
    def __init__(self,name,addr):
        self.name =name
        self.addr = addr
        self.course_list=[]
        self.save()
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()
class Course(BaseClass):
    def __init__(self,name):
        self.name =name
        self.studen_list=[]
        self.save()
    def student_list(self,name):
        self.studen_list.append(name)
        self.save()