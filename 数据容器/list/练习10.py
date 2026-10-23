if __name__ == '__main__':
    list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
    list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
    list3 = ['W', 'A', 'S', 'D']
    my_list=list1+list2+list3
    new_list=[]
    print(my_list)
    my_list.sort()
    print(my_list)
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

