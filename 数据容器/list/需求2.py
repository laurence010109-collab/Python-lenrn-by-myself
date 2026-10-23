if __name__ == '__main__':
    list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30]
    my_list=[]
    for i in list4:
        if(i%3==0 or i%5==0):
            my_list.append(i**2)
    print(my_list)