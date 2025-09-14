#WeightConvert.py
WeightStr=input()
if WeightStr[-2:]in("kg"):
    C=(eval(WeightStr[:-2])*2.2046)
    print("对应的英制重量为{:.3f}磅".format(C))
elif WeightStr[-2:]in("ld"):
    F=(eval(WeightStr[:-2])/2.2046)
    print("对应的公制重量为{:.3f}公斤".format(F))
else:
    print("输入格式错误")
