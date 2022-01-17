# 트리거와 프로시저
## 정의
- 트리거: <strong>특정 이벤트 발생</strong> 시마다 <strong>자동 수행</strong>되는 절차형 SQL
	- 무결성 유지, 로그 메시지 출력 등의 목적으로 사용됨

- 프로시저: <strong>특정 기능을 수행하는 일종의 트랜잭션 언어</strong>이며 <strong>호출</strong>을 통해 미리 저장해 놓은 작업 수행
	- 보통 시스템의 일일 마감 작업, 일괄 작업 등에 주로 사용됨

<br>

## 작성
- 트리거: 테이블에 작성
	- <strong>only SQL문</strong>만 작성 가능
		- 근데 DCL은 안됨 / DCL이 포함된 프로시저나 함수 호출도 안됨

- 프로시저: 미리 수행할 명령을 입력해놓음
	- <strong>SQL문, if문, while문 등의 제어 명령이나 반복 명령을 기술</strong>할 수 있기에 일종의 프로그램도 만들 수 있음 

<br>

## 실행
- 트리거: 지정된 이벤트 발생 시 자동 실행
	- 삽입,갱신, 삭제 등 이벤트 발생 시 트리거가 설정되어 있으면 트리거의 SQL문이 자동으로 실행
	- 반환 값 없음

- 프로시저: 필요할 때 호출하여 실행
	- 반환 가능

<br>

## 매개 변수
- 트리거: 매개 변수 전달 불가능
- 프로시저: 매개 변수 전달 가능

<br>

## commit & rollback
- 트리거: commit, rollback 실행 불가
- 프로시저: commit, rollback 실행 가능

<br>



- 참조
	- https://ko.gadget-info.com/difference-between-trigger
	- https://keumjae.tistory.com/131
	- https://m.blog.naver.com/dlguswls9998/221780280565