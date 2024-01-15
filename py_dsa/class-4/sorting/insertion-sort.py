
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]

        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

my_arr=[12,5,7,3,8,0,1]
insertion_sort(my_arr)
print(my_arr)

# my_list = [12, 11, 13, 5, 6]
# my_list.sort()
# print(my_list)