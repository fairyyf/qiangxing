from conf import setting
import os
import pickle
def save(obj):
    """存储文件"""
    path_dir = os.path.join(setting.Base_DB,obj.__class__.__name__.lower())
    #拼接文档名为类的名字
    if not os.path.exists(path_dir):#判断文档是否存在
        os.mkdir(path_dir)#在没有的情况下创建文档
    path_obj=os.path.join(path_dir,obj.name)#拼接文件写入名字
    with open(path_obj,"wb") as f:
        pickle.dump(obj,f)
        f.flush()
def select(name,dir_type):
    path_dir=os.path.join(setting.Base_DB,dir_type)
    #是读取哪一类的文档
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)#在没有的情况下创建文档
    path_obj=os.path.join(path_dir,name)#拼接文档下的文件名
    if os.path.exists(path_obj):#判断文件是否存在
        with open(path_obj,"rb") as f:
            return pickle.load(f)
    else:
        return None
