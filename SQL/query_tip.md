# 쿼리 최적화 팁

## 1. select시에는 꼭 필요한 컬럼만 불러온다.
- 많은 컬럼 값을 불러올수록 DB는 더 많은 로드를 부담하게 되기 때문
- 불필요한 컬럼이 있다면 과감히 제외하자

<br>

## 2. 조건 부여 시, 가급적이면 기존 DB값에 별도의 연산을 걸지 않는 것이 좋다.
- full table scan을 하면서 모든 cell값을 탐색하고, 수식을 걸고, 조건 충족 여부를 판단해야하는 쿼리 지양
- 기존에 갖고 있는 인덱스를 그대로 활용할 수 있도록 하자

<br>

## 3. like 사용 시 와일드카드 문자열(%)을 string 앞부분에는 배치하지 않는 것이 좋다.
- 2번과 같은 원리
- like "...%"는 기존 인덱스를 활용할 수 있지만, like "%..."는 풀테이블 스캔

<br>

## 4. select distinct, union distinct와 같이 중복 값을 제거하는 연산은 최대한 사용하지 않아야한다.
- 중복 값을 제거하는 연산은 많은 시간이 걸림
- distinct 연산 대체 방법
	- exists
	- ex) select m.id, title from movie m where exists (select 'X' from rating r where m.id = r.movie_id)

<br>

## 5. 같은 내용의 조건이라면 group by 연산 시에는 가급적 having보다는 where절을 사용하는 것이 좋음
- 쿼리 실행 순서에서, where절이 having절보다 먼저 실행되므로,
- where절로 미리 데이터 크기를 작게 만들면 group by에서 다뤄야 하는 데이터 크기가 작아지기 때문에 더 효율적인 연산 가능

<br>

## 6. 3개 이상의 테이블을 inner join 할 땐, 크기가 가장 큰 테이블을 from절에 배치하고, inner join절에는 남은 테이블을 작은 순서대로 배치하는 것이 좋음
- inner join 과정에서 최소한의 combination을 탐색하도록 순서를 배열하자는 얘기 (근데 항상 통용되진 않음)

<br>

## 7. 자주 사용하는 데이터의 형식에 대해서는 미리 전처리된 테이블을 따로 보관/관리 하는 것이 좋음
- 예를 들어, 사용자에 의해 발생한 log데이터 중 필요한 이벤트만 모아서 따로 적재하거나 핵심 서비스 지표를 주기적으로 계산해서 따로 모아두기 등

<br>

## 8. 기타
- order by는 연산 중간에 사용하지 않기
- limit 활용하기

<br>

### 출처
- [쿼리최적화:빠른 쿼리를 위한 7가지 체크리스트](https://medium.com/watcha/%EC%BF%BC%EB%A6%AC-%EC%B5%9C%EC%A0%81%ED%99%94-%EC%B2%AB%EA%B1%B8%EC%9D%8C-%EB%B3%B4%EB%8B%A4-%EB%B9%A0%EB%A5%B8-%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-7%EA%B0%80%EC%A7%80-%EC%B2%B4%ED%81%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-bafec9d2c073)
