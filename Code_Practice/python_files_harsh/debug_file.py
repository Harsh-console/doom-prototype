lis = [2,3,4,1,5,0]
#insetion sort
def insertion_sort(lis):
    for i in range(1, len(lis)):
        temp_num = lis[i]
        for j in range(1, i+2):
            k = i-j
            if lis[k] > temp_num:
                lis[k+1] = lis[k]
            else:
                break
        lis[k+1] = temp_num
    return lis
print(insertion_sort(lis))