def solution(id_list, report, k):
    answer = []
    report_set = set(report)

    report_contents = []
    report_count = []
    user_report_id = []


    for i in report_set:
        report_contents.append(i.split())        
    for i in id_list:
        temp_count = 0
        temp_id = []
        for j in report_contents:
            if j[1] == i:
                temp_count += 1
            if j[0] == i:
                temp_id.append(j[1])
        user_report_id.append(temp_id)
        report_count.append(temp_count)   

        
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
