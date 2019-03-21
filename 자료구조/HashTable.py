def same_name(li):#동명이인 조사
    result = set() #동명이인 저장
    dict_n = {}
    
    for i in  li: #각 이름마다 몇 명인지 조사
        if i in dict_n: #딕셔너리 키 값에 있으면 +1
            dict_n[i] += 1
        else:
            dict_n[i]  =1 #없으면 추가

    for i,j in dict_n.items(): #value를 조사해서 1보다 크면 동명이인 존재
        if j >1:
            result.add(i)
    return result
n = ["Suzi", "suzi", "Kate", "Kate","Bin", "Bini","So","So"]
print(same_name(n))



def find_fr(fr, who):#who의 모든 친구 조사(친구의 친구도 모두) 
    fr_set = set() #연관된 모든 친구를 저장할 set
    qu = []#앞으로 조사할 친구
    qu.append(who)
    fr_set.add(who)
    while qu:#조사할 친구가 있으면
        i = qu.pop(0) #꺼내고
        print(i)#출력
        
        for j in fr[i]: #그리고 그 친구의 친구를 조사
            if j not in fr_set: #set에 없으면
                fr_set.add(j) #set에 추가하고
                qu.append(j) #앞으로 조사할 친구에 추가
                
    
fr_info = {
    "Summer" : ["John", "Mike","Jerry"],
    "John" : ["Bob", "Summer"],
    "Mike" : ["Bob","Jin","Summer"],
    "Jerry" : ["Kate", "Relly","Summer","Cook"],
    "Bob":["John", "Mike"],
    "Jin":[ "Mike","Cook"],
    "Cook":["Jin","Jerry"],
    "Relly":["Jerry"],
    "Kate":["Jerry"]
    }
find_fr(fr_info, "Kate")
