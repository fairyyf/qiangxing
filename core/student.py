from interface import common_interface,student_interface
from lib import common

student_info={
    "name":None
}

def student_register():
    """
    注册
    :return:
    """
    while True:
        name = input("请输入名字:").strip()
        password = input("请输入密码").strip()
        conf_password = input("请确认密码:").strip()
        if password == conf_password:
            flg,msg = student_interface.student_register_interface(name,password)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次密码不一致")


def student_login():
    """
    登入
    :return:
    """
    while True:
        name = input("请输入名字").strip()
        password = input("请输入密码").strip()
        flg,msg=common_interface.login_interface(name,password,"student")
        if flg:
            print(msg)
            student_info["name"]=name
            break
        else:
            print(msg)


@common.logn_auth("student")
def choose_school():
    """
    选择学校
    :return:
    """
    school_list=common_interface.check_all_school()
    print(school_list)
    if not school_list:
        print("请联系管理员创建学校")
        return 
    for i,school in enumerate(school_list):
        print("%s:%s" %(i,school))
    choice = input("请选择学校").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice < len(school_list):
            flg,msg=student_interface.choose_school_interface(student_info["name"],school_list[choice])
            if flg:
                print(msg)
            else:
                print(msg)
        else:
            print("选择请在范围内")
    else:
        print("请用数字选择学校")

@common.logn_auth("student")
def choose_course():
    """
    选择课程
    :return:
    """
    flg,course_list = student_interface.get_can_choose_course_interface(student_info["name"])
    if flg:
        for i,course in enumerate(course_list):
            print("%s:%s" %(i,course))
        choice = input("请选择课程:").strip()
        if choice.isdigit():
            choice=int(choice)
            if choice<len(course_list):
                flg,msg=student_interface.choose_course_interface(student_info["name"],course_list[choice])
                if flg:
                    print(msg)
                else:
                    print(msg)
            else:
                print("请选择范围内的数字")
        else:
            print("请用数字选课程")
    else:
        print(course_list)

@common.logn_auth("student")
def check_score():
    course_list=student_interface.look_course(student_info["name"])
    print(course_list)

func_dic = {
    '1': student_register,
    '2': student_login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score
}


def student_view():
    while True:
        print('''
        1 注册
        2 登陆
        3 选择学校
        4 选择课程
        5 查看成绩
        ''')
        choice = input('请选择功能:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice]()