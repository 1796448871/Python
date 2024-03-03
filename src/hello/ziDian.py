phone=input("phone: ")
map={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    # 按win+;就可以调出emjor表情页面
    "!":"😊"
}
for ch in phone:
    print(map.get(ch))