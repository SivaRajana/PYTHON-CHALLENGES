if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, float(score)])
    # print (records)
    
    lower_1 = records[0][1]
    lower_2 = None
    # print (type(lower_1))
    for name, score in records:
        # print (score, lower_1, lower_2)
        if (score < lower_1):
            lower_2 = lower_1
            lower_1 = score
        elif (lower_2 == None) or (score < lower_2):
            if(score != lower_1):
                lower_2 = score
    # print (lower_2)
    result_names = []
    for name, score in records:
        if (score == lower_2):
            result_names.append(name)
    
    result_names.sort()
    for i in result_names:
        print (i)
