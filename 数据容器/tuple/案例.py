

if __name__ == '__main__':
    students = [
        ("S001", "王林", 85, 92, 78),
        ("S002", "李慕婉", 92, 88, 95),
        ("S003", "十三", 78, 85, 82),
        ("S004", "曾牛", 88, 79, 91),
        ("S005", "周轶", 95, 96, 89),
        ("S006", "王卓", 76, 82, 77),
        ("S007", "红蝶", 89, 91, 94),
        ("S008", "徐立国", 75, 69, 82),
        ("S009", "许木", 86, 89, 98),
        ("S010", "遁天", 66, 59, 72)
    ]
    name_list=[]
    pjf_list=[]
    chinese_list=[]
    math_list=[]
    flag=-1
    english_list=[]
    for i in students:
        i_id,i_name,i_chinese,i_math,i_english=i
        totle=i_chinese+i_math+i_english
        pjf=(i_chinese+i_math+i_english)/3
        print(f"{i_name}的总分为{totle},平均分为{pjf}")
        chinese_list.append(i_chinese)
        math_list.append(i_math)
        english_list.append(i_english)
        pjf_list.append(pjf)
        name_list.append(i_name)
        chinese_list.sort()
        math_list.sort()
        english_list.sort()
    print(f"语文最低分{chinese_list[0]},最高分{chinese_list[9]}")
    print(f"数学最低分{math_list[0]},最高分{math_list[9]}")
    print(f"英语最低分{english_list[0]},最高分{english_list[9]}")
    for i in pjf_list:
        flag += 1
        if i>90:
            print(f"平均分大于90的同学：{name_list[flag]}")
