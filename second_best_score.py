if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #print(arr)

    
    next_max=max_num=-100
    for i in range(0,len(arr)):
        if arr[i] > max_num:
            next_max = max_num
            max_num = arr[i]
        elif arr[i] > next_max and arr[i] != max_num:
            next_max = arr[i]
            
    print(next_max)
