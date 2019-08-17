if __name__ == '__main__':
    myList = []
    minimum=second_min=100
    min_index=second_min_index=0
    for i in range(int(input())):
        name = input()
        score = float(input())
        
        if score < minimum:
            second_min=minimum
            second_index=min_index
            minimum=score
            min_index= i
        elif minimum < score and score < second_min:
            second_min=score
            second_index=i


        myList.append([name, score])
    #print(myList)
    #print("min", minimum, min_index)
    #print("second min", second_min, second_index)
    
    i=second_index
    names=[]
    for i in range(second_index, len(myList),1):
        #print(myList[i][0], myList[i][1])
        if myList[i][1] != second_min:
            break
        names.append(myList[i][0])
    names.sort()
    for i in range(0, len(names),1):
        print(names[i])
    
