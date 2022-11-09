def merge_sort(arr):
    if len(arr)>1:
        '''split array'''
        l_arr = arr[:len(arr)//2]
        r_arr = arr[len(arr)//2:]

        '''recursive'''
        merge_sort(l_arr)
        merge_sort(r_arr)

        i=0 #left index
        j=0 #right index
        k=0 #array index
        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i+=1
            else:
                arr[k] = r_arr[j]
                j+=1
            k+=1
        '''check if we didnt put everything'''
        if j<len(r_arr) or i<len(l_arr):
            while j<len(r_arr):
                arr[k] = r_arr[j]
                k+=1
                j+=1
            while i<len(l_arr):
                arr[k] = l_arr[i]
                k+=1
                i+=1
    return arr

arr = [1,2,3,4,5,6,7,8,100,15,30,45]
sorted_arr = merge_sort(arr)
print(sorted_arr)
