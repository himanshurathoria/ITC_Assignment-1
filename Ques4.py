marks= []
for i in range (0, 5):
    print("\nEnter marks")
    ele = int(input())
    marks.append(ele)
marks.sort()
print("The marks in ascending order are as follows", marks)
