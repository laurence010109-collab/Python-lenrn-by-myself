s=input("请输入字符串：")
# left=0
# right=len(s)-1
# flag=True
# while left<right:
#     if s[left]!=s[right]:
#         print("不属于回文字")
#         flag=False
#         break
#     left+=1
#     right-=1
# if flag:
#     print("属于回文字")

if s==s[::-1]:
    print("属于回文字")
else:
    print("不属于回文字")
