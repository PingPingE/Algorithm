#텍스트파일에서 가장 많이 나온 word와 그 횟수 출력하기
fname = input("Enter file name(include .txt): ")
fhandle = open(fname)
m = {}
for i in fhandle:
    #i = i.strip() #양쪽 공백 제거
    words = i.split()
    for j in words:
        m[j] = m.get(j,0)+1

maxW = ''#가장 많이 나온 word
maxC = -1 #해당 word의 count
for word, count in m.items():
    if count > maxC : #maxC보다 현재 value값이 더 크면
    #갱신
        maxW = word
        maxC = count
print(maxW, maxC)
