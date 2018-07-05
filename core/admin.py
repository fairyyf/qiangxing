from interface import student_interface,teacher_interface,admin_interface,common_interface
from lib import common

admin_info={
    "name":None
}

def admin_register():
    """管理员注册"""
    while True:
        name = input("请输入账号:").strip()
        password =input("请输入密码:").strip()
        conf_password = input("请确认密码:").strip()
        if password == conf_password:
            flg,msg=admin_interface.admin_register_interface(name, password)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次密码不一致")

def admin_login():
    """登入"""
    while True:
        name = input("请输入账号:").strip()
        password =input("请输入密码:").strip()
        flg,msg=common_interface.login_interface(name,password,"admin")
        if flg:
            admin_info["name"]=name
            print(msg)
            break
        else:
            print(msg)
    
@common.logn_auth(user_type="admin")
def create_school():
    """构建学校"""
    school_name=input("请输入学校名字：").strip()
    address=input("请输入地址").strip()
    flg,msg=admin_interface.create_school_interface(admin_info["name"],school_name,address)
    if flg:
        print(msg)
    else:
        print(msg)
    
    
@common.logn_auth(user_type="admin")
def create_teacher():
    """构建老师"""
    teacher_name=input("请输入老师名字：").strip()
    flg,msg=admin_interface.create_teacher_interface(admin_info["name"],teacher_name)
    if flg:
        print(msg)
    else:
        print(msg)
@common.logn_auth(user_type="admin")
def create_course():
    """
    创建课程
    :return: 
    """
    school_list=common_interface.check_all_school()
    if school_list:
        for i,school in enumerate(school_list):
            print("%s:%s" %(i,school))
        choice = input("选择学校").strip()
        if choice.isdigit():
            choice=int(choice)
            if choice < len(school_list):

                course_name=input("请输入课程名字：").strip()
                flg,msg=admin_interface.create_course_interface(admin_info["name"],course_name,school_list[choice])
                if flg:
                    print(msg)
                else:
                    print(msg)
            else:
                print("请选择正确的")
        else:
            print("输入数字")
    else:
        print("学校不存在")

func_dic={
    "1":admin_register,
    "2":admin_login,
    "3":create_school,
    "4":create_teacher,
    "5":create_course
}

def admin_view():
    while True:
        print("""
        1  注册
        2  登入
        3  创建学校
        4  创建老师
        5  创建课程
        """)
        choice =input("请输入选择：").strip()
        if choice == "q":break
        elif not choice in func_dic:continue
        func_dic[choice]()
        