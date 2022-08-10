def solution(id_list, report, k):
    answer = []
    report_set = set(report)

    report_contents = []
    report_contents_2 =[]
    sorted_report = []
    report_count = []
    user_report_id = []


    for i in report_set:
        temp = i.split()
        report_contents.append(temp)   
        report_contents_2.append(temp[1])


    sorted_report = sorted(report_contents)
    temp_user =sorted_report[0][0]

    for i in id_list:
        report_count.append(report_contents_2.count(i))

    print(sorted_report)
    
    temp_user_report_id = []

    for i in sorted_report:
        if temp_user == i[0]:
            temp_user_report_id.append(i[1])
            print(i[1])
        else:
            temp_user == i[0]
            print("else : ", i)
            user_report_id.append(temp_user_report_id)
            print("report id : " , user_report_id)
            temp_user_report_id = []
            print(temp_user_report_id)
            temp_user_report_id.append(i[1])
            print(temp_user_report_id)

    print (user_report_id)
    print (report_count)

    #solting and Create user_report_id List  
    

        
    for j in user_report_id:

        count = 0
        for m in j:            
            if report_count[id_list.index(m)]>= k:                
                count += 1
        answer.append(count)
        
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

print(solution(id_list, report, 2))
