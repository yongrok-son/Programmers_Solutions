def solution(id_list, report, k):
    answer = [0 for i in id_list]
    report_set = set(report)
    report_contents = []
    report_contents_2 =[]
    sorted_report = []
    report_count = []

    for i in report_set:
        temp = i.split()
        report_contents.append(temp)   
        report_contents_2.append(temp[1])


    sorted_report = sorted(report_contents)
    temp_user =sorted_report[0][0]

    for i in id_list:
        report_count.append(report_contents_2.count(i))

    
    temp_user_report_id = []
    for i in sorted_report:
        if temp_user == i[0]:
            temp_user_report_id.append(i[1])
        else:            
            for j in temp_user_report_id: 
                if report_count[id_list.index(j)]>= k:               
                    answer[id_list.index(temp_user)] += 1

            temp_user = i[0]
            temp_user_report_id = [] 
            temp_user_report_id.append(i[1])
    
    for j in temp_user_report_id: 
        if report_count[id_list.index(j)]>= k:               
            answer[id_list.index(temp_user)] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

print(solution(id_list, report, 2))
