class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return (f"姓名：{self.name} | 语文：{self.chinese} |"
                f" 数学：{self.math} | 英语：{self.english} | 总分: {self.chinese + self.math + self.english}")

    def update_score(self, chinese = None, math = None, english = None):
        if chinese is not None and 0 <= chinese <= 100:
            self.chinese = chinese
        if math is not None and 0 <= math <= 100:
            self.math = math
        if english is not None and 0 <= english <= 100:
            self.english = english

class EduManagement:
    system_version = "1.0.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input("请输入学生姓名：")
        if name != [student.name for student in self.student_list]:
            chinese = int(input("请输入学生语文成绩："))
            math = int(input("请输入学生数学成绩："))
            english = int(input("请输入学生英语成绩："))
            if 0 < chinese < 100 and 0 < math < 100 and 0 < english < 100:
                student = Student(name, chinese, math, english)
                self.student_list.append(student)
            else:
                print("成绩范围为1-100分")
        else:
            print("该学生已录入")

    def modify_student(self):
        name = input("请输入要修改学生的姓名：")
        mod_student = None
        for student in self.student_list:
            if student.name == name:
                mod_student = student
                print(mod_student.__str__())
                subject = input("请输入要修改的学科：")
                if subject == "语文":
                    chinese = int(input("请输入学生语文成绩："))
                    mod_student.update_score(chinese)
                if subject == "数学":
                    math = int(input("请输入学生数学成绩："))
                    mod_student.update_score(math)
                if subject == "英语":
                    english = int(input("请输入学生英语成绩："))
                    mod_student.update_score(english)
                if subject == "subject":
                    chinese = int(input("请输入学生语语成绩："))
                    math = int(input("请输入学生数学成绩："))
                    english = int(input("请输入学生英语成绩："))
                    mod_student.update_score(chinese, math, english)

    def clear_student(self):
        name = input("请输入要修改学生的姓名：")
        cle_student = None
        for student in self.student_list:
            if student.name == name:
                cle_student = student
                cle_student.update_score(0, 0, 0)

    def show_all_students(self):
        for student in self.student_list:
            print(student)

# 测试
if __name__ == '__main__':
    edu = EduManagement()
    # 交互菜单
    while True:
        print(f"\n===== {edu.system_name} v{edu.system_version} =====")
        print("1. 添加学生")
        print("2. 修改学生成绩")
        print("3. 删除学生所有成绩")
        print("4. 查看所有学生")
        print("5. 退出系统")

        choice = input("请输入操作序号：").strip()
        match choice:
            case "1":
                edu.add_student()
            case "2":
                edu.modify_student()
            case "3":
                edu.clear_student()
            case "4":
                edu.show_all_students()
            case "5":
                print("感谢使用，系统已退出！")
                break
            case _:
                print("错误：输入序号无效，请重新选择！")
