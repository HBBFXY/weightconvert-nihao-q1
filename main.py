#WeightConvert.py
WeightStr=input("请输入带有符号的重量值:")
if WeightStr[-2]in("pb"):
    C=(eval(WeightStr[0:-2])/2.2046)
    print("转换后的重量是{:.3f}kg".format(C))
elif WeightStr.endswith("kg"):
    F=(eval(WeightStr[0:-2])*2.2046)
    print("转换后的重量为{:.3f}pb".format(F))
else:
    print("输入格式错误")
