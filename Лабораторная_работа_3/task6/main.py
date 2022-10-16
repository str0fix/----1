list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max=min(list_numbers)
count=0
index=0
while ( True ):
    if (list_numbers[count-1]>max):
        index=count-1
        max=list_numbers[count-1]
    if (count == (len(list_numbers)-1) ):
        break
    count+=1

list_numbers[index], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[index]
# TODO Оформить решение

print(list_numbers)
