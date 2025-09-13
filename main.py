#WeightConvert.py
WeightStr=input()
if WeightStr[-2]in("kg"):
    C=(eval(WeightStr[0:-2])*2.2046)
    print("转换后的重量是{:.3f}磅".format(C))
elif WeightStr[-2]in("kg"):
    F=(eval(WeightStr[0:-2])/2.2046)
    print("转换后的重量为{:.3f}公斤".format(F))
else:
    print("输入格式错误")
