try:
    age=int (input("age:"))
    print(2/0)
    print(age)
except ValueError:
    print("Invalid printing")
    print("输错东西了")
except ZeroDivisionError:
    print("你确定你零岁?")
