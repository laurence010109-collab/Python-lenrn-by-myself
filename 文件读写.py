with open("E:/Code/Python-lenrn-by-myself/test.txt","r+",encoding="utf-8") as f:
    f.write("asdfghjkl\n")
    f.write("zxcvbnmmm\n")
    f.write("qwertyuii\n")

    f.seek(0)
    a=f.read()
    print(a)