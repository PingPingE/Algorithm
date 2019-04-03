#이메일 계정에 따른 조회수 데이터베이스
import sqlite3
conn = sqlite3.connect('test1.sqlite')#데이터 베이스에 접근할 수 있는지 확인
cur = conn.cursor()#핸들(명령을 보내고 답을 받음) 생성

cur.execute("DROP TABLE IF EXISTS Counts") #테이블 삭제하고 시작
cur.execute("CREATE TABLE Counts(email TEXT, count INTEGER)")

fname = input("파일 이름:")
m = {}
if(len(fname)< 1): fname = 'mbox-short.txt'
fh = open(fname)
for i in fh:
    if not i.startswith('From:'): continue
    p = i.split()
    email = p[1]
    m[email] = m.get(email,0)+1 #key값이 email인 value+1(만약 없으면 key = email, value=0인 딕셔너리 생성 후 +1)
    #execute 메소드를 이용하여 sql문장을 DB서버에 보낸다
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,)) #?를 사용하므로써 SQL주입을 막을 수 있음
    row = cur.fetchone() #한줄 읽기

    if row is None:#없으면 추가
        cur.execute("INSERT INTO Counts(email,count) VALUES(?,1)", (email,))

    else:#있으면 조회수 1 증가
        cur.execute("UPDATE Counts SET count = count+1 WHERE email =?", (email,))
    conn.commit() #데이터 확정 갱신

sqlstr= "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10" #가장 위의 10개만
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])


cur.close() #DB연결을 닫기
maxE = ''
maxC = -1
for E,C in m.items():
    if C > maxC:
        maxC = C
        maxE = E
print("가장 조회수가 많은 이메일:", maxE ,"조회수:", maxC)
