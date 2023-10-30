num = str(input("請輸入學號:"))
name = str(input("請輸入姓名:"))
c = float(input("請輸入國文成績:"))
m = float(input("請輸入數學成績:"))
p = float(input("請輸入電腦成績:"))
t = round(float(c+m+p),2)
T = round(float(t/3),2)

student = {}
student = dict()
student['sid'] = num
student['sname'] = name
student['fchina'] = c
student['fmath'] = m
student['finfo'] = p

print("-"*80)
print("{}({})+同學你好".format(student['sid'],student['sname']))
print("以下是您各科成績與分數評定")
print()
print("國文：{}/數學：{}/電腦：{}/總分：{}/平均：{}".format(student['fchina'],student['fmath'] ,student['finfo'],t,T))
print("-"*80)
if T>=60:
    print("成績判定：合格")
else:
    print("成績判定：不合格")
print()
