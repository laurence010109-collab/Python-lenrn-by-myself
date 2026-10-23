def get_grade(score):
    if score>=90:
        print('A')
    if score>=75 and score<90:
        print('B')
    if score >= 60 and score < 75:
        print('C')


if __name__ == '__main__':
    get_grade(60)