class Student():  # 定义一个空的类
    pass


mingyue = Student()  # 定义一个对象


class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):  # 系统默认一个self参数
        print("I 在做作业")
        return None


yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()