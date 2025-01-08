# 1. 스칼라(scalar)

## 1. 스칼라 정의

- 크기만으로 나타낼 수 있는 물리량
- 길이(length), 부피(volume), 거리(distance) 등
- 데이터 셋을 구성하는 하나의 구성 원소, 하나의 숫자
- 기하학적으로 축 위의 점 하나로 표현 가능

## 2. 스칼라의 기본 연산

- 스칼라 덧셈
    
    $x = 2, y = 3 → z = x + y = 2 + 3 = 5$
    
- 스칼라 뺄셈
    
    $x = 4, y = 1 → z = x - y = 4 - 1 = 3$
    
- 스칼라 곱셈
    
    $x = 5, y = 3 → z = x \times y = 5 \times 3 = 15$
    
- 스칼라 나눗셈
    
    $x = 5, y = 2 → z = x \div y = 5 \div 2 = 5/2 = 2.5$
    

# 2. 벡터(vector)

## 1. 벡터 정의

- 스칼라의 집합
- 행렬을 구성하는 기본 단위
- 크기와 방향을 모두 나타내는 개념
- 기하학적으로 벡터를 구성하는 각 숫자 → 공간상의 좌표에 해당
- 화살표 길이 : 벡터 크기
- 화살표 방향 : 벡터 방향
- 행 벡터 : 벡터를 구성하는 원소가 되는 스칼라를 행 방향으로 나열한 벡터
- 열 벡터 : 벡터를 구성하는 원소가 되는 스칼라를 열 방향으로 나열한 벡터
- 크기와 방향이 같음 = 동일한 벡터
- 영 벡터 : 길이가 0인 벡터
- 마이너스 부호 : 벡터의 길이는 그대로, 방향이 정반대

## 2. 벡터의 덧셈과 뺄셈

- 벡터 덧셈
    - 더하고자 하는 두 벡터의 크기가 동일할 때만 연산 가능
    - 교환 법칙 성립
    
    $$
    a = \begin{pmatrix}1\\2\\3 \end{pmatrix}, \quad b = \begin{pmatrix}4\\5\\6 \end{pmatrix} \\ \begin{aligned} a + b &= \begin{pmatrix}1\\2\\3 \end{pmatrix} + \begin{pmatrix}4\\5\\6 \end{pmatrix} \\ &= \begin{pmatrix}1 + 4\\2 + 5\\3 + 6 \end{pmatrix} \\ &= \begin{pmatrix}5\\7\\9 \end{pmatrix} \end{aligned}
    $$
    
- 벡터 뺄셈
    - 빼고자 하는 두 벡터의 크기가 동일할 때만 연산 가능
    - 빼고자 하는 벡터의 방향을 바꿔 더하는 것
    
    $$
    a = \begin{pmatrix}7\\3\\9 \end{pmatrix}, \quad b = \begin{pmatrix}2\\5\\7 \end{pmatrix} \\ \begin{aligned} a - b &= \begin{pmatrix}7\\3\\9 \end{pmatrix} + \begin{pmatrix}2\\5\\7 \end{pmatrix} \\ &= \begin{pmatrix}7 - 2\\3 - 5\\9 - 7 \end{pmatrix} \\ &= \begin{pmatrix}5\\-2\\2 \end{pmatrix} \end{aligned}
    $$
    

## 3. 벡터의 스칼라 곱

- 벡터의 길이와 방향 변경 가능
- 곱하는 값이 1보다 큼 → 해당 벡터보다 길이가 커짐
- 곱하는 값이 1보다 작음 → 해당 벡터보다 길이가 작아짐
- 곱하는 값이 음수임 → 해당 벡터의 크기 변경 및 방향도 바뀜

## 4. 벡터 기본 연산의 성질

- $u + v = v + u$
- $(u + v) + w = u + (v + w)$
- $u + 0 = 0 + u = u$
- $u + (-u) = 0$
- $a(bu) = (ab)u$
- $a(u + v) = au + av$
- $(a + b)u = au + bu$

# 3. 벡터 내적(inner product)

## 1. 내적 정의

- 벡터를 마치 수처럼 곱하는 개념
- 방향이 일치하는 만큼 곱함
- 한 벡터를 다른 벡터로 정사영시켜 그 벡터의 크기를 곱함

## 2. 벡터 내적

- 벡터의 내적 결과값 = 스칼라
    
    $$
    a \cdot b = |a| \ |b| \cos \theta
    $$