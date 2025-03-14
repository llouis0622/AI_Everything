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
    

# 4. 외적과 크로네커 곱

## 1. 벡터 외적

- 외적(outer product), 텐서 곱(tensor product)
- 벡터 외적 결과 → 행렬
    
    $$
    u = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \\ v_4 \end{pmatrix} \\ u \otimes v = uv^T = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \begin{pmatrix} v_1 & v_2 & v_3 & v_4 \end{pmatrix} = \begin{pmatrix} u_1v_1 & u_1v_2 & \cdots & u_1v_m \\ u_2v_1 & u_2v_2 & \cdots & u_2v_m \\ \vdots & \vdots & \ddots & \vdots \\ u_nv_1 & u_nv_2 & \cdots & u_nv_m \end{pmatrix}
    $$
    

## 2. 크로네커 곱(Kronecker product)

- 외적의 특별한 경우
- 행렬 $n \times p$, 행렬 $m \times d$ → 크로네커 곱 행렬 $nm \times pd$
    
    $$
    A = \begin{pmatrix} a_{11} & a_{12}  & \cdots & a_{1p} \\ a_{21} & a_{22}  & \cdots & a_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2}  & \cdots & a_{np} \end{pmatrix}, \quad B = \begin{pmatrix} b_{11} & b_{12}  & \cdots & b_{1d} \\ b_{21} & b_{22}  & \cdots & b_{2d} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m1} & b_{m2}  & \cdots & b_{md} \end{pmatrix} \\ A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B  & \cdots & a_{1p}B \\ a_{21}B & a_{22}B  & \cdots & a_{2p}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1}B & a_{n2}B  & \cdots & a_{np}B \end{pmatrix} \\ = \begin{pmatrix}a_{11}b_{11} & a_{11}b_{12} & \cdots & a_{11}b_{1d} & \cdots & \cdots & a_{1p}b_{11} & a_{1p}b_{12} & \cdots & a_{1p}b_{1d} \\ a_{11}b_{21} & a_{11}b_{22} & \cdots & a_{11}b_{2d} & \cdots & \cdots & a_{1p}b_{21} & a_{1p}b_{22} & \cdots & a_{1p}b_{1d} \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ a_{11}b_{m1} & a_{11}b_{m2} & \cdots & a_{11}b_{md} & \cdots & \cdots & a_{1p}b_{m1} & a_{1p}b_{m2} & \cdots & a_{1p}b_{md}  \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ a_{n1}b_{11} & a_{n1}b_{12} & \cdots & a_{n1}b_{1d} & \cdots & \cdots & a_{np}b_{11} & a_{np}b_{12} & \cdots & a_{np}b_{1d} \\ a_{n1}b_{21} & a_{n1}b_{22} & \cdots & a_{n1}b_{2d} & \cdots & \cdots & a_{np}b_{21} & a_{np}b_{22} & \cdots & a_{np}b_{2d} \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ a_{n1}b_{m1} & a_{n1}b_{m2} & \cdots & a_{n1}b_{m1} & \cdots & \cdots & a_{np}b_{m1} & a_{np}b_{m1} & \cdots & a_{np}b_{md} \end{pmatrix}
    $$
    

# 5. 벡터 곱

## 1. 벡터 곱 정의

- 벡터 곱(vector product), 크로스 곱(cross product)
- 3차원 공간의 벡터들 간에 적용할 수 있는 연산
- 단위 벡터를 사용해 벡터와 벡터의 곱 표현 가능
    
    $$
    i = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad j = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad k = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \\ u = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} \\ \begin{aligned} u \times v &= \begin{vmatrix} i & j & k \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} \\ &= \begin{vmatrix} u_2 & u_3 \\ v_2 & v_3\end{vmatrix}i - \begin{vmatrix} u_1 & u_3 \\ v_1 & v_3\end{vmatrix}j + \begin{vmatrix} u_1 & u_2 \\ v_1 & v_2\end{vmatrix}k  \\ &= (u_2v_3 - u_3v_2)i - (u_1v_3 - u_3v_1)j + (u_1v_2 - u_2v_1)k \end{aligned}
    $$
    

## 2. 벡터 곱의 기하학적 의미

- 벡터 곱 → 두 벡터에 전부 수직인 벡터
- 두 벡터가 평행 → 벡터 곱 크기 0
    
    $$
    ||u \times v|| = ||u|| \ ||v|| \ |\sin \theta|
    $$
    

# 6. 삼중 곱

## 1. 스칼라 삼중 곱

- 두 벡터에 벡터 곱을 한 이후 남은 벡터와 내적하는 것
- 세 백터를 행 벡터 또는 열 벡터로 갖는 행렬식
    
    $$
    u = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}, \quad w = \begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} \\ u \cdot (v \times w) \\ u \cdot (v \times w) = \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}
    $$
    

## 2. 벡터 삼중 곱

- 벡터 간 연산을 모두 벡터 곱으로 수행
    
    $$
    u \times (v \times w)
    $$