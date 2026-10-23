if __name__ == '__main__':
    day=(input("请输入星期几："))
    match day:
        case "1":
            print("今天是星期一")
        case "2":
            print("今天是星期二")
        case "3":
            print("今天是星期三")
        case "4":
            print("今天是星期四")
        case "5":
            print("今天是星期五")
        case "6":
            print("今天是星期6")
        case _:
            print("错误")