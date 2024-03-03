me={
"name":"李学健",
"age":21,
"QQ":"1796448871"
}
print(me.get("name"))
print(me.get("QQ"))
print(me["QQ"])
# 新加了一个键值对
me["birthday"]="2002.11.21"
print(me)
