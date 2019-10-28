import os
#返回一个储存所选文件夹下所有属于filter内的文件类型的文件的文件名列表
def all_path(dirname,filter):
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            ext = os.path.splitext(apath)[1]
            if ext in filter:
                result.append(apath)
    return result
#在此处修改路径
path="C:\\Users\\H1402\\Desktop\\test\\"
#合并所有.c文件
i=all_path(path,[".c"])
#生成空文件out.c
with open("out.c",'w') as out:
    out.write("")
#合并文件
for file in i:
    iname=os.path.splitext(os.path.basename(file))[0]
    ext=os.path.splitext(os.path.basename(file))[1]
    #输出符合条件的文件名
    print(file)
    with open(file,'r') as f, open("out.c",'a') as out:
        out.writelines("\\\\"+iname+ext+"\n")
        c=f.read(1)
        while(c!=''):
            out.write(c)
            c=f.read(1)
#合并所有.h文件
i=all_path(path,[".h"])
#生成空文件out.h
with open("out.h",'w') as out:
    out.write("")
#合并文件
for file in i:
    iname=os.path.splitext(os.path.basename(file))[0]
    ext=os.path.splitext(os.path.basename(file))[1]
    #输出符合条件的文件名
    print(file)
    with open(file,'r') as f, open("out.h",'a') as out:
        out.writelines("\\\\"+iname+ext+"\n")
        c=f.read(1)
        while(c!=''):
            out.write(c)
            c=f.read(1)
