def selection_sort(arr,i):
    '''selection sort array by recursive'''
    if i == 0:
        return arr
    '''marking max at right'''
    cur_max = arr[i]
    temp_ind = 0
    for ind in range(0,i):
        if arr[ind]>cur_max:
            cur_max = arr[ind]
            temp_ind = ind
    '''swap cur_max to arr[i]'''
    if cur_max != arr[i]:
        temp = arr[i]
        arr[i] = cur_max
        arr[temp_ind] = temp
    return selection_sort(arr,i-1)


arr = [2,5,6,8,9,1,4,3,7,100,1500,12,18,1]
sorted_arr = selection_sort(arr,len(arr)-1)
print(sorted_arr)
