def maze(m,start,end): #li에서 start부터 end까지 가는 경로 찾기(미로찾기)
    qu = [] #가볼 곳
    done = set() #간 곳
    qu.append(start)
    done.add(start)
    while qu: #가볼 곳이 있으면
        p = qu.pop(0)#하나 꺼내고
        v= p[-1] #꺼낸 문자열에서 가장 마지막 부분을 가볼 것임
        if v==end: #만약 문자열의 가장 마지막(v)이 도착지라면
            return p #끝
        
        for i in m[v]:#v와 연결돼있는 경로 탐색
            if i not in done: #이미 가본 곳이 아니라면
                done.add(i)
                qu.append(p+i)
                
    return "no"#못빠져나갔을 떼
    
                        

m = {'a':['e'], 'b':['c','f'], 'c':['b','d'],'d':['c'],'e':['a','i'], 'f':['b','g','j'],
     'g':['f','h'],'h':['g','l'],'i':['e','m'],'j':['f','k','n'],'k':['j','o'], 'l':['h','p'],
     'm':['i','n'],'n':['m','j'],'o':['k'],'p':['l']}
print(maze(m,'a','p'))
                                            
