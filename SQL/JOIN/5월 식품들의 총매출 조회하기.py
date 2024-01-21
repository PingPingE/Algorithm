'''
문제)
다음은 식품의 정보를 담은 FOOD_PRODUCT 테이블과 식품의 주문 정보를 담은 FOOD_ORDER 테이블입니다.
FOOD_PRODUCT 테이블은 다음과 같으며 PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE는 식품 ID, 식품 이름, 식품코드, 식품분류, 식품 가격을 의미합니다
FOOD_ORDER 테이블은 다음과 같으며
ORDER_ID, PRODUCT_ID, AMOUNT, PRODUCE_DATE, IN_DATE, OUT_DATE, FACTORY_ID, WAREHOUSE_ID는 각각 주문 ID, 제품 ID, 주문량, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID를 의미합니다.

FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요.
이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.

'''



-- 조건: 생산일자(order.produce_date) = '2022-05-*'
-- 1. food_order에서 조건을 충족하는 row filtering
-- 2. product_id를 key로 sum amount
-- 3. food_product와 join

select product.product_id, product.product_name, product.price*sales_count as total_sales
from food_product as product
join
(
    select product_id, sum(amount) as sales_count from food_order
    where produce_date like "2022-05-%" group by product_id
) as p_order
on product.product_id = p_order.product_id
order by total_sales desc, product_id asc
;
