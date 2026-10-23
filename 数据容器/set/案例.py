if __name__ == '__main__':
    football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
    basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
    french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
    art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
    first_set=french_set.intersection(art_set)
    print(f"同时学习法语和艺术：{first_set}")
    seconf_set=football_set.difference(basketball_set)
    print(f"学足球但是不学篮球：{seconf_set}")
    thread_set=football_set & basketball_set & french_set & art_set
    print(thread_set)
    all_student=football_set | basketball_set | french_set | art_set
    for student in all_student:
        count=0
        if student in football_set:
            count+=1
        if student in basketball_set:
            count+=1
        if student in art_set:
            count+=1
        if student in french_set:
            count+=1
        print(f"{student}选修了{count}门课程")