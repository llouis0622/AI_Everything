# 1. 스칼라와 벡터

## 1. 스칼라(scalar)

### 스칼라

- 크기만으로 나타낼 수 있는 물리량
- 길이(length), 부피(volume), 거리(distance) 등
- 데이터 셋을 구성하는 하나의 구성 원소, 하나의 숫자
- 기하학적으로 축 위의 점 하나로 표현 가능

### 스칼라의 기본 연산

- 스칼라 덧셈
    
    $x = 2, y = 3 → z = x + y = 2 + 3 = 5$
    
- 스칼라 뺄셈
    
    $x = 4, y = 1 → z = x - y = 4 - 1 = 3$
    
- 스칼라 곱셈
    
    $x = 5, y = 3 → z = x \times y = 5 \times 3 = 15$
    
- 스칼라 나눗셈
    
    $x = 5, y = 2 → z = x \div y = 5 \div 2 = 5/2 = 2.5$
    

## 2. 벡터(vector)

### 벡터

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

### 벡터의 덧셈과 뺄셈

- 벡터 덧셈
    - 더하고자 하는 두 벡터의 크기가 동일할 때만 연산 가능
    - 교환 법칙 성립
- 벡터 뺄셈
    - 빼고자 하는 두 벡터의 크기가 동일할 때만 연산 가능
    - 빼고자 하는 벡터의 방향을 바꿔 더하는 것

### 벡터의 스칼라 곱

- 벡터의 길이와 방향 변경 가능
- 곱하는 값이 1보다 큼 → 해당 벡터보다 길이가 커짐
- 곱하는 값이 1보다 작음 → 해당 벡터보다 길이가 작아짐
- 곱하는 값이 음수임 → 해당 벡터의 크기 변경 및 방향도 바뀜

### 벡터 기본 연산의 성질

- $u + v = v + u$
- $(u + v) + w = u + (v + w)$
- $u + 0 = 0 + u = u$
- $u + (-u) = 0$
- $a(bu) = (ab)u$
- $a(u + v) = au + av$
- $(a + b)u = au + bu$

## 3. 벡터 내적(inner product)

### 내적

- 벡터를 마치 수처럼 곱하는 개념
- 방향이 일치하는 만큼 곱함
- 한 벡터를 다른 벡터로 정사영시켜 그 벡터의 크기를 곱함
- 벡터의 내적 결과값 = 스칼라
    
    $$
    a \cdot b = |a| \ |b| \cos \theta
    $$
    

## 4. 외적과 크로네커 곱

### 외적

- 외적(outer product), 텐서 곱(tensor product)
- 벡터 외적 결과 → 행렬
    
    $$
    u = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \\ v_4 \end{pmatrix} \\ u \otimes v = uv^T = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \begin{pmatrix} v_1 & v_2 & v_3 & v_4 \end{pmatrix} = \begin{pmatrix} u_1v_1 & u_1v_2 & \cdots & u_1v_m \\ u_2v_1 & u_2v_2 & \cdots & u_2v_m \\ \vdots & \vdots & \ddots & \vdots \\ u_nv_1 & u_nv_2 & \cdots & u_nv_m \end{pmatrix}
    $$
    

### 크로네커 곱(Kronecker product)

- 외적의 특별한 경우
- 행렬 $n \times p$, 행렬 $m \times d$ → 크로네커 곱 행렬 $nm \times pd$
    
    $$
    A = \begin{pmatrix} a_{11} & a_{12}  & \cdots & a_{1p} \\ a_{21} & a_{22}  & \cdots & a_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2}  & \cdots & a_{np} \end{pmatrix}, \quad B = \begin{pmatrix} b_{11} & b_{12}  & \cdots & b_{1d} \\ b_{21} & b_{22}  & \cdots & b_{2d} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m1} & b_{m2}  & \cdots & b_{md} \end{pmatrix} \\ A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B  & \cdots & a_{1p}B \\ a_{21}B & a_{22}B  & \cdots & a_{2p}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1}B & a_{n2}B  & \cdots & a_{np}B \end{pmatrix} \\ = \begin{pmatrix}a_{11}b_{11} & a_{11}b_{12} & \cdots & a_{11}b_{1d} & \cdots & \cdots & a_{1p}b_{11} & a_{1p}b_{12} & \cdots & a_{1p}b_{1d} \\ a_{11}b_{21} & a_{11}b_{22} & \cdots & a_{11}b_{2d} & \cdots & \cdots & a_{1p}b_{21} & a_{1p}b_{22} & \cdots & a_{1p}b_{1d} \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ a_{11}b_{m1} & a_{11}b_{m2} & \cdots & a_{11}b_{md} & \cdots & \cdots & a_{1p}b_{m1} & a_{1p}b_{m2} & \cdots & a_{1p}b_{md}  \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ a_{n1}b_{11} & a_{n1}b_{12} & \cdots & a_{n1}b_{1d} & \cdots & \cdots & a_{np}b_{11} & a_{np}b_{12} & \cdots & a_{np}b_{1d} \\ a_{n1}b_{21} & a_{n1}b_{22} & \cdots & a_{n1}b_{2d} & \cdots & \cdots & a_{np}b_{21} & a_{np}b_{22} & \cdots & a_{np}b_{2d} \\ \vdots & \vdots & \ddots & \vdots & \cdots & \cdots & \vdots & \vdots & \ddots & \vdots \\ a_{n1}b_{m1} & a_{n1}b_{m2} & \cdots & a_{n1}b_{m1} & \cdots & \cdots & a_{np}b_{m1} & a_{np}b_{m1} & \cdots & a_{np}b_{md} \end{pmatrix}
    $$
    

## 5. 벡터 곱

### 벡터 곱

- 벡터 곱(vector product), 크로스 곱(cross product)
- 3차원 공간의 벡터들 간에 적용할 수 있는 연산
- 단위 벡터를 사용해 벡터와 벡터의 곱 표현 가능
    
    $$
    i = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad j = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad k = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \\ u = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} \\ \begin{aligned} u \times v &= \begin{vmatrix} i & j & k \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} \\ &= \begin{vmatrix} u_2 & u_3 \\ v_2 & v_3\end{vmatrix}i - \begin{vmatrix} u_1 & u_3 \\ v_1 & v_3\end{vmatrix}j + \begin{vmatrix} u_1 & u_2 \\ v_1 & v_2\end{vmatrix}k  \\ &= (u_2v_3 - u_3v_2)i - (u_1v_3 - u_3v_1)j + (u_1v_2 - u_2v_1)k \end{aligned}
    $$
    

### 벡터 곱의 기하학적 의미

- 벡터 곱 → 두 벡터에 전부 수직인 벡터
- 두 벡터가 평행 → 벡터 곱 크기 0
    
    $$
    ||u \times v|| = ||u|| \ ||v|| \ |\sin \theta|
    $$
    

## 6. 삼중 곱

### 스칼라 삼중 곱

- 두 벡터에 벡터 곱을 한 이후 남은 벡터와 내적하는 것
- 세 백터를 행 벡터 또는 열 벡터로 갖는 행렬식
    
    $$
    u = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}, \quad w = \begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} \\ u \cdot (v \times w) \\ u \cdot (v \times w) = \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}
    $$
    

### 벡터 삼중 곱

- 벡터 간 연산을 모두 벡터 곱으로 수행
    
    $$
    u \times (v \times w)
    $$
    

# 2. 행렬(matrix)

## 1. 행렬

### 행렬 정의

- 사각형 형태로 숫자를 나열하는 것
- 행과 열로 구성
- 행 벡터의 집합, 열 벡터의 집합
- 행렬 원소 : 행렬을 구성하는 각 스칼라 값

### 행렬의 덧셈과 뺄셈

- 행렬 간 덧셈, 뺄셈 가능
- 각 행렬의 동일 위치에 대응하는 원소끼리 덧셈, 뺼셈 수행

### 행렬의 스칼라 곱

- 스칼라 * 행렬
- 행렬에 포함도니 모든 원소에 스칼라를 곱함
- 행렬의 길이 변화

### 행렬의 원소 곱

- 크기가 동일한 두 행렬에서 동일한 위치의 원소들끼리 서로 곱하는 것

### 행렬 곱

- 행렬끼리 서로 곱하는 것
- 곱하는 행렬의 열 크기와 곱해지는 행렬의 행 크기가 일치해야 계산 가능
- 교환 법칙이 성립하지 않음
    
    $$
    \begin{aligned} AB &= \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 5 & 2 \end{pmatrix} \begin{pmatrix}3 & -3 & 5 \\ -1 & 2 & 1 \end{pmatrix} \\ &= \begin{pmatrix}2 \times 3 + 7 \times (-1) & 2 \times (-3) + 7 \times 2 & 2 \times 5 + 7 \times (-1) \\ 3 \times 3 + 4 \times (-1) & 3 \times (-3) + 4 \times 2 & 3 \times 5 + 4 \times (-1) \\ 5 \times 3 + 2 \times (-1) & 5 \times (-3) + 2 \times 2 & 5 \times 5 + 2 \times (-1) \end{pmatrix} \\ &= \begin{pmatrix}-1 & 8 & 3 \\ 5 & -1 & 11 \\ 13 & -11 & 23 \end{pmatrix} \end{aligned}
    $$
    

### 행렬의 대각합(trace)

- 정사각 행렬일 때 주 대각 원소를 모두 더한 값
- 주 대각 원소 : 행렬의 행 번호와 열 번호가 동일한 원소
    
    $$
    A = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \\ \text{tr}(A) = a_{11} + a_{12} + a_{13}
    $$
    

### 행렬 연산 성질

- $A + B = B + A$
- $A + (B + C) = (A + B) + C$
- $A(BC) = (AB)C$
- $A(B + C) = AB + AC$
- $(B + C)A = BA + CA$
- $A(B - C) = AB - AC$
- $(B - C)A = BA - CA$
- $a(B + C) = aB + aC$
- $a(B - C) = aB - aC$
- $(a + b)C = aC + bC$
- $(a - b)C = aC - bC$
- $a(bC) = abC$
- $a(BC) = (aB)C = B(aC)$

## 2. 전치 행렬(transposed matrix)

### 전치 행렬 정의

- 기존 행렬의 행과 열을 바꾼 행렬
- 전치 행렬로 변환 시 행렬의 크기 변경

### 전치 행렬 성질

- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(A - B)^T = A^T - B^T$
- $(aA)^T = aA^T$
- $(AB)^T = B^TA^T$

## 3. 대칭 행렬(symmetric matrix)

### 대칭 행렬 정의

- 기존 행렬과 전치 행렬이 동일한 정사각 행렬
- 행 번호와 열 번호를 바꾸어도 값이 동일한 행렬
    
    $$
    A = \begin{pmatrix}a & b & c \\ b & d & e \\ c & e & f \end{pmatrix}, \quad A^T = \begin{pmatrix}a & b & c \\ b & d & e \\ c & e & f \end{pmatrix} \\ A_{ij} = A_{ji}, \quad A = A^T
    $$
    

### 대칭 행렬 성질

- 대칭 행렬 간 덧셈이나 뺄셈의 결과는 대칭 행렬
- 대칭 행렬 간 곱셈이나 나눗셈의 결과가 반드시 대칭 행렬은 아님
- 대칭 행렬의 거듭 제곱 결과는 대칭 행렬
- 대칭 행렬에 자신의 전치 행렬을 곱한 결과는 대칭 행렬

## 4. 대각 행렬(diagonal matrix)

### 대각 행렬 정의

- 행렬의 주 대각 원소가 아닌 원소가 0인 정사각 행렬
- 대각 행렬의 역행렬 : 주 대각 원소의 역수
- 대각 행렬의 거듭 제곱 : 대각 원소의 거듭 제곱
    
    $$
    D = \begin{pmatrix}d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & d_n \end{pmatrix} \\ D^{-1} = \begin{pmatrix}1/d_1 & 0 & \cdots & 0 \\ 0 & 1/d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & 1/d_n \end{pmatrix} \\ D^k = \begin{pmatrix}d_1^k & 0 & \cdots & 0 \\ 0 & d_2^k & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & d_n^k \end{pmatrix}
    $$
    

### 대각 행렬 성질

- 일반 행렬 * 대각 행렬 : 일반 행렬의 열 값 대각 행렬 원소 배
- 대각 행렬 * 일반 행렬 : 일반 행렬의 행 값 대각 행렬 원소 배
    
    $$
    A = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad D = \begin{pmatrix}d_{11} & 0 & 0 \\ 0 & d_{22} & 0 \\ 0 & 0 & d_{33} \end{pmatrix} \\ \begin{aligned} AD &= \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \begin{pmatrix}d_{11} & 0 & 0 \\ 0 & d_{22} & 0 \\ 0 & 0 & d_{33} \end{pmatrix} = \begin{pmatrix}a_{11} \times d_{11} & a_{12} \times d_{22} & a_{13} \times d_{33} \\ a_{21} \times d_{11} & a_{22} \times d_{22} & a_{23} \times d_{33} \\ a_{31} \times d_{11} & a_{32} \times d_{22} & a_{33} \times d_{33} \end{pmatrix} \end{aligned} \\ \begin{aligned} DA &= \begin{pmatrix}d_{11} & 0 & 0 \\ 0 & d_{22} & 0 \\ 0 & 0 & d_{33} \end{pmatrix} \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = \begin{pmatrix}a_{11} \times d_{11} & a_{12} \times d_{11} & a_{13} \times d_{11} \\ a_{21} \times d_{22} & a_{22} \times d_{22} & a_{23} \times d_{22} \\ a_{31} \times d_{33} & a_{32} \times d_{33} & a_{33} \times d_{33} \end{pmatrix} \end{aligned}
    $$
    

## 5. 단위 행렬(identity matrix)

### 단위 행렬 정의

- 주 대각 원소가 1이고 나머지 원소는 모두 0인 대각 행렬
- 항등 행렬
    
    $$
    I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}
    $$
    

### 단위 행렬 성질

- 행렬 * 단위 행렬 = 행렬
    
    $$
    A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}, \quad I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\ AI = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \\ IA = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}  = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \\ AI = IA = A
    $$
    

## 6. 영 행렬(zero matrix)

### 영 행렬 정의

- 행렬 구성 원소가 모두 0인 행렬
    
    $$
    0 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
    $$
    

### 영 행렬 성질

- 임의의 행렬 + 영 행렬 = 기존 행렬
- 임의의 행렬 - 영 행렬 = 기존 행렬
- 임의의 행렬 * 영 행렬 = 영 행렬
    
    $$
    A + 0 = A, \quad A - 0 = A \\ 0 - A = -A, \quad A - A = 0 \\ A0 = 0, \quad 0A = 0
    $$
    

## 7. 삼각 행렬(triangular matrix)

### 삼각 행렬 정의

- 행렬의 구성 원소가 삼각형 형태를 띄는 행렬
- 상 삼각 행렬(upper) : 주 대각 원소 아래쪽에 있는 모든 원소가 0인 정사각 행렬
- 하 삼각 행렬(lower) : 주 대각 원소 위쪽에 있는 모든 원소가 0인 정사각 행렬
    
    $$
    A_u = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ 0 & a_{22} & a_{23} \\ 0 & 0 & a_{33} \end{pmatrix}, \quad A_l = \begin{pmatrix}a_{11} & 0 & 0 \\ a_{21} & a_{22} & 0 \\ a_{31} & a_{32} & a_{33} \end{pmatrix}
    $$
    

### 삼각 행렬 성질

- 삼각 행렬 간 덧셈, 뺄셈, 곱셈 결과 = 삼각 행렬
- 상 삼각 행렬의 전치 행렬 = 하 삼각 행렬
- 하 삼각 행렬의 전치 행렬 = 상 삼각 행렬
    
    $$
    A = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix}, \quad B = \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} \\ A + B = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix} + \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix}8 & 10 & 12 \\ 0 & 14 & 16 \\ 0 & 0 & 18 \end{pmatrix} \\ A - B = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix} - \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix}6 & 6 & 6 \\ 0 & 6 & 6 \\ 0 & 0 & 6 \end{pmatrix} \\ AB = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix} \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix}7 & 46 & 115 \\ 0 & 40 & 116 \\ 0 & 0 & 72 \end{pmatrix}
    $$
    
    $$
    A^T = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix}^T = \begin{pmatrix}7 & 0 & 0 \\ 8 & 10 & 0 \\ 9 & 11 & 12 \end{pmatrix} \\ C^T = \begin{pmatrix}1 & 0 & 0 \\ 2 & 3 & 0 \\ 4 & 5 & 6 \end{pmatrix}^T = \begin{pmatrix}1 & 2 & 4 \\ 0 & 3 & 5 \\ 0 & 0 & 6 \end{pmatrix}
    $$
    

## 8. 토플리츠 행렬(Toeplitz matrix)

- 왼쪽에서 오른쪽으로 내려가는 각 대각선의 원소들이 동일한 행렬
- 시계열 분석 시 사용
- 시계열 데이터를 행렬 형태로 변환 시 토플리츠 행렬 사용
    
    $$
    T = \begin{pmatrix}t_0 & t_{-1} & t_{-2} & \cdots & \cdots & t_{-(n-1)} \\ t_1 & t_0 & t_{-1} & \ddots & \ddots & \vdots \\ t_2 & t_1 & t_0 & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & t_{-1} & t_{-2} \\ \vdots & \ddots & \ddots & t_1 & t_0 & t_{-1} \\ t_{n-1} & t_{n-2} & \cdots & t_2 & t_1 & t_0 \end{pmatrix} \\ T_{i, j} = T_{i+1, j+1} = t_{i-j}
    $$
    

## 9. 이중 대각 행렬(bidiagonal matrix)

- 대각 원소뿐만 아니라 대각 원소의 바로 위쪽 혹은 아래쪽 원소가 0이 아닌 행렬
- upper bidiagonal matrix : 대각 원소 위쪽에 위치한 원소가 0이 아닌 이중 대각 행렬
- lower bidiagonal matrix : 대각 원소 아래쪽에 위치한 원소가 0이 아닌 이중 대각 행렬

## 10. 하우스홀더 행렬(householder matrix)

- 어떤 행렬을 다른 형태로 변환할 때 사용하는 행렬 중 하나
- 정사각 행렬이며 모든 열이 정규 직교인 행렬
    
    $$
    v = \begin{pmatrix}v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} \\ H = I - 2 \frac{vv^T}{v^Tv}
    $$
    

# 3. 선형 시스템

## 1. 선형 방정식(linear equation)

### 선형 방정식 정의

- 방정식 : 변수가 포함된 식에서 해당 변수가 특정 값만 가질 때만 성립하는 등식
- 선형 방정식 : 변수가 모두 일차항으로 이루어진 방정식
    
    $$
    a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
    $$
    

### 선형 방정식 예

- 그래프의 각 축 : 선형 방정식의 변수
    
    $$
    2x + 4y = 8 \\ -6y + 3z = 12 \\ 2x + 3y + 4z = 5
    $$
    

### 선형 방정식이 아닌 경우

- 변수가 삼각 함수, 지수 함수인 경우
- 변수끼리의 곱이나 제곱근인 경우
    
    $$
    y = \cos x \\ 1 = 2^x + y \\ x + \sqrt{y} = 2 \\ x + y + 2z + yz = 3
    $$
    

## 2. 선형 시스템(linear system)

### 선형 시스템 정의

- 선형 방정식의 집합
- 연립 1차 방정식
- 선형 시스템을 만족시키는 해 : 선형 방정식의 집합이 그래프 상에서 만나는 지점
- 선형 시스템에서 발생 가능한 상화
    - 오직 하나의 해 : 두 직선이 오직 한 점에서만 만나는 경우
    - 무한개의 해 : 두 직선이 일치하는 경우
    - 해가 존재하지 않음 : 두 직선이 평행하는 경우
- 첨가 행렬(argumented matrix) : 선형 시스템의 상수 부분만 모아서 행렬 형태로 나타낸 것
    
    $$
    a_{11}x_1 + a_{12}x_2 + \cdots + a_{1p}x_p = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2p}x_p = b_2 \\ \vdots \\ a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{np}x_p = b_n
    $$
    
    $$
    \begin{pmatrix}a_{11} & a_{12} & \cdots & a_{1p} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2p} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{np} & b_n \end{pmatrix} \\ \begin{pmatrix}a_{11} & a_{12} & \cdots & a_{1p} \\ a_{21} & a_{22} & \cdots & a_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{np} \end{pmatrix} \begin{pmatrix}b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}
    $$
    

### 기본 행 연산(elementary row operation)

- 한 행에 0이 아닌 상수를 모두 곱함
- 두 행을 교환함
- 한 행의 배수를 다른 행에 더함

### 가우스 조르단 소거법(Gauss Jordan elimination)

- 가우스 행렬(Gauss matrix) : 각 행의 가장 첫 원소는 1이고 1 아래의 위치하는 원소는 모두 0인 행렬
- 행렬 구성 원소가 사다리꼴 형태로 남은 것
    
    $$
    \begin{pmatrix}1 & 2 & -1 & 2 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0\end{pmatrix}
    $$
    
- 기약 가우스 행렬(reduced Gauss matrix) : 가장 첫 원소가 1인 열에 대해 1을 제외한 나머지 행 원소가 모두 0인 형태
    
    $$
    \begin{pmatrix}1 & 0 & -1 & 2 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0\end{pmatrix}
    $$
    
- 가우스 조르단 소거법 : 기약 가우스 행렬 형태를 이용해 방정식의 해를 구하는 방법
    - 선형 시스템의 첨가 행렬 구하기
    - 기본 행 연산 결과를 첨가 행렬에 적용
    - 첨가 행렬이 기약 가우스 행렬 형태가 되면 종료
    - 첨가 행렬을 선형 시스템으로 표현

### 가우스 소거법(Gaussian elimination)

- 선형 시스템의 첨가 행렬을 가우스 행렬로 변환한 후 해를 구하는 방법
    - 선형 시스템의 첨가 행렬 구하기
    - 첨가 행렬을 가우스 행렬로 변환
    - 첨가 행렬을 선형 시스템으로 표현

## 3. 동차 선형 시스템(homogeneous linear system)

- 선형 시스템의 우변이 모두 0인 선형 시스템
- 해가 존재하지 않는 경우가 없음 → 적어도 하나의 해가 존재함
- 선형 시스템의 선형 방정식은 상수항이 0 → 오직 하나의 해 or 무한개의 해
    
    $$
    a_{11}x_1 + a_{12}x_2 + \cdots + a_{1p}x_p = 0 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2p}x_p = 0 \\ \vdots \\ a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{np}x_p = 0
    $$
    

# 4. 행렬 심화

## 1. 행렬식(determinant)

- 행렬의 특성을 하나의 숫자로 표현하는 방법 중 하나
- 정사각 행렬을 스칼라로 변환하는 함수
- 역행렬 구하기 가능
- 해당 행렬의 특성 파악 가능
- 행렬식의 절대값 : 해당 행렬이 단위 공간을 얼마나 늘렸는지 줄였는지 파악 가능

## 2. 행렬식 계산

### 2 **× 2 행렬 행렬식**

- 주 대각 행렬 원소를 곱한 값에 나머지 두 원소를 곱한 값을 뺌
- 행렬식 : 두 개의 벡터로 만들 수 있는 평행사변형의 넓이
    
    $$
    \det(A) = |A| = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}
    $$
    

### 3 **× 3 행렬 행렬식**

- 2차원 행렬의 행렬식 연장선
    
    $$
    |A| = \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11} \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12} \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13} \begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
    $$
    
- 소행렬식(minor of entry) : 행렬의 특정 행과 특정 열을 제외하고 구성된 부분 행렬의 행렬식
- 여인수(cofactor of entry) : 소행렬의 행렬식에 소행렬의 위치에 따라 적절한 부호를 붙여 얻어진 값
    
    $$
    A = \begin{pmatrix} 3 & 2 & 0 \\ -1 & -3 & 6 \\ 2 & 3 & -5 \end{pmatrix} \\ M_{11} = \begin{vmatrix} 3 & 2 & 0 \\ -1 & -3 & 6 \\ 2 & 3 & -5 \end{vmatrix} = \begin{vmatrix} 3 & 6 \\ 3 & -5 \end{vmatrix} = -3 \\ C_{11} = (-1)^{1+1}M_{11} = -3
    $$
    
- 여인수 전개(cofactor expansion) : 특정 행을 정하고 해당 행에 대한 원소와 여인수를 곱한 값을 모두 합함
    
    $$
    \det(A) = a_{11}C_{11} + a_{12}C_{12} + \cdots + a_{1n}C_{1n}
    $$
    

## 3. 행렬식의 성질

### 삼각 행렬 행렬식

- 주 대각 원소의 곱
    
    $$
    A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ 0 & a_{22} & a_{23} \\ 0 & 0 & a_{33} \end{pmatrix} \\ \det(A) = a_{11}a_{22}a_{33}
    $$
    

### 대각 행렬 행렬식

- 주 대각 원소의 곱
    
    $$
    A = \begin{pmatrix} a_{11} & 0 & 0 \\ 0 & a_{22} & 0 \\ 0 & 0 & a_{33} \end{pmatrix} \\ \det(A) = a_{11}a_{22}a_{33}
    $$
    
- 단위 행렬 행렬식 = 1
    
    $$
    I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\ \det(A) = 1
    $$
    

### 전치 행렬 행렬식

- 기본 행렬 행렬식 = 전치 행렬 행렬식
    
    $$
    \det(A) = \det(A^T)
    $$
    

### 특정 행과 열의 원소가 모두 0일 때 행렬식

- 행렬에 0으로 구성된 행 또는 열 존재 시 행렬식은 0
- 모든 원소가 0인 행 또는 열을 기준으로 여인수 구하면 0
    
    $$
    A = \begin{pmatrix} 1 & 5 & 0 \\ 6 & 2 & 0 \\ 4 & 3 & 0 \end{pmatrix} \\ \det(A) = 0
    $$
    

### 행렬의 기본 행 연산과 행렬식

- 한 행에 0이 아닌 상수를 모두 곱함
- 두 행을 교환
- 한 행의 배수를 다른 행에 더함
    
    $$
    k \det(A) = \det(B) \\ k \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = \begin{vmatrix} ka_{11} & ka_{12} & ka_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}
    $$
    
    $$
    \det(kA) = k^n\det(A) \\ \begin{vmatrix} ka_{11} & ka_{12} & ka_{13} \\ ka_{21} & ka_{22} & ka_{23} \\ ka_{31} & ka_{32} & ka_{33} \end{vmatrix} = k^3\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}
    $$
    
    $$
    -\det(A) = \det(B) \\ -\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = \begin{vmatrix} a_{21} & a_{22} & a_{23} \\ a_{11} & a_{12} & a_{13} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}
    $$
    
    $$
    \det(A) = \det(B) \\ \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} + ka_{11} & a_{32} + ka_{12} & a_{33} + ka_{13} \end{vmatrix}
    $$
    

### 비례하는 행과 열에 대한 행렬식

- 서로 비례하는 두 행 또는 두 열이 존재할 때 행렬식은 0
    
    $$
    A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 0 \\ 3 & 6 & 1 \end{pmatrix} \\ \det(A) = 0, \quad \det(B) = 0
    $$
    

### 행렬 곱과 행렬식

- 각각의 행렬의 행렬식을 곱한 값과 동일
    
    $$
    \det(AB) = \det(A) \det(B)
    $$
    

## 4. 역행렬(inverse matrix)

- 한 행렬에 다른 행렬을 곱한 결과가 단위 행렬이 되는 행렬
- 가역 행렬 : 어떤 행렬의 역행렬이 존재하는 경우
- 특이 행렬 : 행렬의 역행렬이 존재하지 않는 경우
    
    $$
    AA^{-1} = A^{-1}A = I
    $$
    

## 5. 역행렬 계산

### 2 **× 2 행렬 역행렬 구하기**

- 행렬의 행렬식이 0이 아님
    
    $$
    A = \begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \\ A^{-1} = \frac{1}{a_{11}a_{22} - a_{12}a_{21}} \begin{pmatrix}a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix}
    $$
    
    $$
    (AB)^{-1} = B^{-1}A^{-1}
    $$
    

### n **× n 행렬 역행렬 구하기**

- 여인수 행렬 : 행렬의 여인수로 구성된 행렬
    
    $$
    A = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22}  & a_{23} \\ a_{31} & a_{32} & a_{33}\end{pmatrix} \\ C = \begin{pmatrix}c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22}  & c_{23} \\ c_{31} & c_{32} & c_{33}\end{pmatrix} \\ A^{-1} = \frac{1}{\det(A)}\text{adj}(A)
    $$
    

## 6. 정사각 행렬의 거듭 제곱

- 정사각 행렬의 0승 → 단위 행렬
- 정사각 행렬의 n승 → 정사각 행렬을 n번 곱한 결과
    
    $$
    A^0 = I \\ A^n = AA \cdots A \\ A^nA^m = A^{n+m} \\ (A^n)^m = A^{nm}
    $$
    

## 7. 역행렬의 성질

### 역행렬 거듭 제곱

- 행렬의 역행렬을 n번 거듭 제곱 → 행렬의 역행렬을 n번 곱한 값
    
    $$
    A^{-n} = (A^{-1})^n = A^{-1}A^{-1} \cdots A^{-1}
    $$
    

### 역행렬과 전치 행렬

- 행렬이 가역 행렬일 때 행렬의 전치 행렬도 가역 행렬
    
    $$
    (A^{-1})^T = (A^T)^{-1}
    $$
    

### 거듭 제곱 행렬의 역행렬

- 행렬이 가역 행렬일 때 행렬의 거듭 제곱 행렬도 가역 행렬

### 역행렬과 행렬식

$$
\det(A^{-1}) = \frac{1}{\det(A)}
$$

## 8. 직교 행렬(orthogonal matrix)

- 어떤 행렬의 행 벡터와 열 벡터가 유클리드 공간의 정규 직교 기저를 이루는 행렬
- 사이 각도 90도 → 두 벡터 내적값이 0
- 정규 직교 행렬 : 행렬을 구성하는 각 행 벡터 혹은 열 벡터의 길이가 1이며 서로 수직인 벡터로 이루어진 행렬
- 자기 자신과 자신의 전치 행렬 행렬곱 → 단위 행렬
    
    $$
    AA^T = A^TA = I
    $$
    
- 직교 행렬의 전치 행렬 → 직교 행렬
- 직교 행렬의 역행렬 → 직교 행렬
- 직교 행렬끼리의 곱 → 직교 행렬
- 직교 행렬의 행렬식 → 1 or -1

## 9. 닮음

### 닮음 정의

- $B = P^{-1}AP$를 만족하는 가역 행렬이 존재할 때, 정사각 행렬 $A$, $B$는 서로 닮음
- 위 조건을 만족하는 직교 행렬 존재 → 직교 닮음

### 닮음의 성질

- 서로 닮은 행렬의 행렬식은 동일
    
    $$
    \det(A) = \det(B)
    $$
    
- 행렬 $A$가 가역 행렬 → $P^{-1}AP$도 가역 행렬
- 행렬 $A$, $P^{-1}AP$의 랭크와 널리티 동일
- 행렬 $A$, $P^{-1}AP$의 대각합 동일
    
    $$
    rank(A) = rank(P^{-1}AP) \\ nullity(A) = nullity(P^{-1}AP)
    $$
    
- 행렬 $A$, $P^{-1}AP$의 고윳값 동일
    
    $$
    tr(A) = tr(P^{-1}AP)
    $$
    

# 5. 기저와 차원

## 1. 벡터 공간(vector space)

### 벡터 공간

- 벡터의 덧셈과 스칼라 곱이 정의된 공간
- 선형 공간
- 내적 공간(inner product space) : 벡터 공간의 확장된 개념, 길이 및 각도가 정의되어 있는 공간
- 벡터 공간 공리
    - 공간에 속하는 벡터에 대해 두 벡터의 합인 벡터도 공간에 속함
    - 임의의 스칼라가 존재하고 벡터가 공간에 속할 때 스칼라와 벡터의 곱도 공간에 속함
    - $u + v = v + u$
    - $u + (v + w) = (u + v) + w$
    - $u + 0 = 0 + u$
    - $u + (-u) = (-u) + u = 0$
    - $a(u + v) = au + av$
    - $(a + b)u = au + bu$
    - $a(bu) = (ab)u$
    - $1u = u$
- 1차원 : 직선 공간
- 2차원 : 평면 공간
- 3차원 : 공간
- 유닛 벡터(unit vector) : 어떤 공간의 좌표 축의 기본 벡터

### 부분 공간(subspace)

- 벡터 공간의 일부분
- 스팬(span) : 벡터 공간의 부분 공간을 생성하는 것

## 2. 선형 변환(linear transformation)

- 두 벡터 공간 사이 함수
- 벡터 확대, 축소, 회전, 반사 등

## 3. 선형 독립(linear independent)

- 선형 조합(linear combination) : 한 벡터를 다른 벡터와 스칼라로 조합할 수 있는 것
    
    $$
    w = a_1u_1 + a_2u_2 + \cdots + a_nu_n
    $$
    
- 선형 독립 : 한 집합이 벡터 공간 내 벡터들의 집합일 때 한 집합에 속하는 벡터를 한 집합에 속하는 다른 벡터들의 선형 조합으로 표현할 수 없음
- 선형 종속(linear dependent) : 특정 벡터를 다른 벡터의 선형 조합으로 표현 가능

## 4. 기저(basis)

### 기저

- 벡터 공간을 생성하는 선형 독립인 벡터들
- 기저의 조합으로 공간을 생성할 수 있음
- 기저가 되기 위한 조건
    - n차원 공간을 구성하기 위해서는 n개의 기저 벡터가 필요함
    - 벡터 집합이 n차원 공간의 기저이면 차원 공간 내 존재하는 모든 벡터는 선형 독립

### 기저와 벡터 공간

- 벡터 공간의 성질
    - n개가 넘는 벡터가 만드는 집합은 선형 종속
    - n개 미만의 벡터가 만드는 집합은 벡터 공간 생성 불가
    - 벡터 공간의 모든 기저 벡터 개수는 동일

## 5. 차원(dimension)

- 해당 공간을 구성하는 기저 벡터 개수
- n차원 공간을 나타내기 위해서는 기저 n개 필요

## 6. 행 공간, 열 공간, 영 공간

### 행 공간, 열 공간, 영 공간 정의

- 행 공간(row spaces) : 행 벡터로 span할 수 있는 공간
- 열 공간(column spaces) : 열 벡터로 span할 수 있는 공간
- 영 공간(row spaces) : 행렬이 주어질 때 행렬과 벡터의 곱이 0을 만족하는 모든 벡터의 집합

### 행 공간, 열 공간, 영 공간 성질

- 기본 행 연산 → 행렬의 영 공간을 변화시키지 않음
- 기본 행 연산 → 행렬의 행 공간을 변화시키지 않음
- 행렬의 행 공간과 열 공간 차원은 동일

## 7. 랭크(rank)와 널리티(nullity)

### 랭크와 널리티 정의

- 랭크 : 행 공간과 열 공간의 공통 차원
- 풀 랭크 행렬 : 행렬의 랭크가 해당 행렬이 가질 수 있는 랭크 중 최대치인 경우
- 널리티 : 행렬의 영 공간의 차원

### 랭크와 널리티 성질

- 행렬이 임의의 행렬이면 $\text{rank}(A) = \text{rank}(A^T)$
- 행렬이 n개의 열을 가진 행렬이면 $\text{rank}(A) + \text{nullity}(A) = n$

# 6. 내적

## 1. 내적(inner product)

### 내적 공간(inner product space)

- 벡터 공간에서 다음 공리를 만족하는 벡터 공간
    - $\langle u, v \rangle = \langle v, u \rangle$
    - $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$
    - $\langle au, v \rangle = a \langle u, v \rangle$
    - $\langle u, v \rangle \geq 0$

### 내적 정의

- 벡터와 벡터의 연산 결과값 → 스칼라
- 각 벡터의 동일한 위치에 있는 원소를 서로 곱한 후 더함
    
    $$
    \lang u, v \rang  = u \cdot v = u_1v_1 + u_2v_2 + \cdots + u_nv_n \\ u = \begin{pmatrix}u_1 \\ u_2 \\ u_3\end{pmatrix}, \quad v = \begin{pmatrix}v_1 \\ v_2 \\ v_3\end{pmatrix} \\ \lang u, v \rang = u^Tv = \begin{pmatrix}u_1 & u_2 & u_3\end{pmatrix} \begin{pmatrix}v_1 \\ v_2 \\ v_3\end{pmatrix} = u_1v_1 + u_2v_2 + u_3v_3
    $$
    

### 내적 성질

- 벡터의 길이(norm)을 구하거나 벡터 사이 관계 파악 가능
- 두 벡터 사이의 각도 추정 가능
    - 내적 > 0 → 두 벡터 사이 각도 < 90
    - 내적 < 0 → 두 벡터 사이 각도 > 90
    - 내적 = 0 → 두 벡터 사이 각도 = 90
- 벡터의 길이 파악 가능 → 벡터의 노름(norm)
    - 자기 자신의 내적 값의 제곱근 계산
    
    $$
    u = (u_1, u_2, \cdots, u_n) \\ ||u|| = \sqrt{u_1^2 + u_2^2 + \cdots + u_n^2}
    $$
    
- 벡터의 길이와 x축과의 각도를 알고 있을 때
    - 벡터 좌표 → 길이와 두 벡터 사이의 각도로 표현 가능
    - x좌표 → 코사인, y좌표 → 사인
    
    $$
    u = (u_1, u_2) \rarr u = (||u|| \cos \theta, ||v|| \sin \theta) \\ u \cdot v = ||u|| \ ||v|| \cos \theta \\ \cos \theta = \frac{u \cdot v}{||u|| \ ||v||}
    $$
    

### 정사영(projection)

- 한 벡터 공간에 속한 벡터를 부분 공간으로 수직으로 투영하는 것
- 좌표계의 종류와 상관없이 내적 값을 항상 구할 수 있음
- 한 벡터에 대한 축을 지정하고 정사영 → 2가지 종류의 정사영이 나옴
    
    $$
    ||proj_vu|| = ||u|| \ |\cos \theta|
    $$
    
    $$
    \begin{aligned} \lang u, v\rang &= ||u|| \ ||v|| \cos \theta \\ &= (||v||) \times (||u|| \cos \theta) \\ &= (length \ of  \ vector \ v) \times (length \ of \ vector \ proj_v u)\end{aligned}
    $$
    

## 2. 직교 공간과 정규 직교 공간

### 직교 공간(orthogonal space)

- 직교(orthogonal) : 두 직선 또는 두 평면이 직각을 이루며 만나는 것
- 정규 직교(orthonormal) : 각 벡터의 길이가 1이면서 직교하는 것

### 정규 직교 공간(orthonormal space)

- 정규 직교 벡터(orthonormal vector) : 직교 공간에 존재하는 직교 벡터의 길이가 모두 1
- 정규 직교 공간(orthonormal space) : 정규 직교 벡터가 만드는 공간
- 정규화(normalization) : 직교 벡터를 정규 직교 벡터로 바꾸는 것, 해당 벡터의 길이로 나눔
    
    $$
    v = \frac{1}{||u||}u \\ ||v|| = ||\frac{1}{||u||}u|| = 1
    $$
    

### 정규 직교 벡터를 활용한 좌표 표현

- 벡터 공간의 정규 직교 기저가 존재할 때 벡터 공간에 포함되는 임의의 벡터
    
    $$
    a = \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_n \rangle v_n
    $$
    
- 임의의 벡터 → 정규 기저 벡터의 조합
    
    $$
    a = c_1v_1 + c_2v_2 + \cdots + c_nv_n
    $$
    
    $$
    \begin{aligned} a &= \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_n \rangle v_n \\ &= c_1v_1 + c_2v_2 + \cdots + c_nv_n \end{aligned}
    $$
    
- 벡터와 기저 벡터 내적
    
    $$
    \begin{aligned} \langle a, v_i \rangle &= \langle c_1v_1 \rangle + \langle c_2v_2 \rangle + \cdots + \langle c_nv_n, v_i \rangle \\ &= \langle c_1v_1, v_i \rangle + \langle c_2v_2, v_i \rangle + \cdots + \langle c_nv_n, v_i \rangle \\ &= \langle c_iv_i, v_i \rangle \\ &= c_iv_i^Tv_i \\ &= c_i \end{aligned}
    $$
    
    $$
    \begin{aligned} a &= c_1v_1 + c_2v_2 + \cdots + c_nv_n \\ &= \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_n \rangle v_n \end{aligned}
    $$
    

### 직교 벡터를 활용한 좌표 표현

- 벡터 공간 내 직교 기저 표현
    
    $$
    a = \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_n \rang}{||u_n||^2}u_n
    $$
    
- 직교 기저일 때 좌표 표현
    
    $$
    a = \left \{ \frac{\lang a, u_1 \rang}{||u_1||^2}u_1, \frac{\lang a, u_2 \rang}{||u_2||^2}u_2, \cdots, \frac{\lang a, u_n \rang}{||u_n||^2}u_n \right \}
    $$
    
- 직교 기저 → 정규 직교 기저 벡터
    
    $$
    u_1, u_2, \cdots, u_n \rarr \left \{ \frac{u_1}{||u_1||}, \frac{u_2}{||u_2||}, \cdots, \frac{u_n}{||u_n||} \right \}
    $$
    
- 정규 직교 벡터를 기준으로 변환
    
    $$
    \begin{aligned} a &= \lang a, \frac{u_1}{||u_1||} \rang \frac{u_1}{||u_1||} + \lang a, \frac{u_2}{||u_2||} \rang \frac{u_2}{||u_2||} + \cdots + \lang a, \frac{u_n}{||u_n||} \rang \frac{u_n}{||u_n||} \\ &= \lang a, u_1 \rang \frac{u_1}{||u_1||^2} + \lang a, u_2 \rang \frac{u_2}{||u_2||^2} + \cdots + \lang a, u_n \rang \frac{u_n}{||u_n||^2} \\ &= \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_n \rang}{||u_n||^2}u_n \end{aligned}
    $$
    
    $$
    a = \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_n \rang}{||u_n||^2}u_n
    $$
    

## 3. 그램 슈미트 과정

### 정사영 정리(projection theorem)

- 벡터 공간의 부분 공간이 존재할 때 벡터 공간에 속하는 임의의 벡터는 다음과 같음
    
    $$
    a = w_1 + w_2
    $$
    
    - $w_1$ : 부분 공간에 속하는 벡터
    - $w_2$ : 부분 공간의 직교 공간에 속하는 벡터
    
    $$
    \begin{aligned} a &= w_1 + w_2 \\ &\Leftrightarrow w_2 = a - w_1 \\ &\Leftrightarrow a = Proj_wa + Proj_{w^{\bot}} a \\ &\Leftrightarrow Proj_{w^{\bot}} a = a - Proj_wa \\ &\Leftrightarrow a = Proj_wa + (a - Proj_wa) \end{aligned}
    $$
    

### 직교 정사영

- 직교 + 정사영 개념
    
    $$
    Proj_wa = \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_r \rang}{||u_r||^2}u_r
    $$
    
- 직교 벡터를 활용한 좌표 표현 방법
    
    $$
    \left \{ \frac{\lang a, u_1 \rang}{||u_1||^2}, \frac{\lang a, u_2 \rang}{||u_2||^2}, \cdots, \frac{\lang a, u_r \rang}{||u_r||^2} \right \}
    $$
    
- 전체 벡터 공간의 임의의 벡터 → 정사영시킨 벡터
    
    $$
    Proj_wa = \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_r \rangle v_r
    $$
    

### 그램 슈미트 과정(Gram-Schmidt Process)

- 기저 벡터를 직교 기저 벡터로 변환하는 과정
- 새로운 직교 기저 벡터 정의
    
    $$
    u_1 = s_1
    $$
    
- 직교 기저 벡터 → 직교인 벡터 생성
    
    $$
    u_2 = s_2 - \frac{\lang s_2, u_1 \rang}{||u_1||^2}u_1
    $$
    
- 생성할 기저 벡터가 앞에서 생성한 벡터들과 직교함
    
    $$
    u_3 = s_3 - \frac{\lang s_3, u_1 \rang}{||u_1||^2}u_1 - \frac{\lang s_3, u_2 \rang}{||u_2||^2}u_2
    $$
    
- 나머지 직교 기저 벡터
    
    $$
    u_n = s_n - \frac{\lang s_n, u_1 \rang}{||u_1||^2}u_1 - \frac{\lang s_3, u_2 \rang}{||u_2||^2}u_2 - \cdots - \frac{\lang s_n, u_{n-1} \rang}{||u_{n-1}||^2}u_{n-1}
    $$
    

## 4. QR 분해

### 기본적인 QR 분해 방법

- 행렬이 풀 랭크 → 열 벡터는 모두 선형 독립
    
    $$
    A = QR
    $$
    
    - $Q$ : $n \times p$ 행렬, 정규 직교 벡터
    - $R$ : 가역 상 삼각 행렬
- 열 벡터의 표현식
    
    $$
    a_1 = \langle a_1, v_1 \rangle v_1 + \langle a_1, v_2 \rangle v_2 + \cdots + \langle a_1, v_n \rangle v_n \\ a_2 = \langle a_2, v_1 \rangle v_1 + \langle a_2, v_2 \rangle v_2 + \cdots + \langle a_2, v_n \rangle v_n \\ \vdots \\ a_n = \langle a_n, v_1 \rangle v_1 + \langle a_n, v_2 \rangle v_2 + \cdots + \langle a_n, v_n \rangle v_n
    $$
    
    $$
    \begin{pmatrix}a_1 & a_2 & \cdots & a_n \end{pmatrix} \begin{pmatrix}v_1 & v_2 & \cdots & v_n \end{pmatrix} = \begin{pmatrix} \lang a_1, v_1 \rang & \lang a_2, v_1 \rang & \cdots & \lang a_n, v_1 \rang \\ \lang a_1, v_2 \rang & \lang a_2, v_2 \rang & \cdots & \lang a_n, v_2 \rang \\ \vdots & \vdots & \ddots & \vdots \\ \lang a_1, v_n \rang & \lang a_2, v_n \rang & \cdots & \lang a_n, v_n \rang \end{pmatrix}
    $$
    
- QR 분해
    
    $$
    A = QR \\ Q = \begin{pmatrix}v_1 & v_2 & \cdots & v_n \end{pmatrix} \\ R = \begin{pmatrix} \lang a_1, v_1 \rang & \lang a_2, v_1 \rang & \cdots & \lang a_n, v_1 \rang \\ 0 & \lang a_2, v_2 \rang & \cdots & \lang a_n, v_2 \rang \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lang a_n, v_n \rang \end{pmatrix}
    $$
    

### 그램 슈미트 과정을 이용한 QR 분해

- 직교 기저 벡터 구하기
- 기존 직교 기저 벡터가 아닌 다른 직교 기저 벡터 구하기
- 다음 차례의 직교 기저 벡터 구하기
- 앞서 구한 직교 벡터 → 정규 직교 벡터로 변환
- Q 행렬 구하기 → R 행렬 구하기

### 하우스홀더 방법을 이용한 QR 분해

- 행렬의 1열을 기준으로 벡터 노름 구하기
- 위에서 구한 벡터로 하우스홀더 행렬 구하기
- 하우스홀더 행렬과 기본 행렬 곱하기
- 앞서 구한 행렬의 1열, 1행을 없애고 새로운 행렬 생성하기
- 위 단계를 반복하면서 하우스홀더 행렬들을 구하고 이를 바탕으로 QR 행렬 구하기

# 7. 고윳값과 고유 벡터

## 1. 고윳값과 고유 벡터 개념

- 특성 : 벡터의 방향은 변하지 않고 크기만 변하는 특성
- 고유 벡터(eigenvector) : 벡터에 선형 변환했을 때, 방향은 변하지 않고 크기만 변하는 벡터
- 고윳값(eigenvalue) : 선형 변환 이후 변한 크기
- 고윳값 부호 → 고유 벡터 방향 파악
- 고윳값 크기 → 고유 벡터 길이 파악
    
    $$
    Ax = \lambda x
    $$
    

## 2. 고윳값과 고유 벡터 계산

### 2 × 2 행렬의 고윳값과 고유 벡터 구하기

- 동차 선형 시스템
    
    $$
    \begin{aligned} &Ax = \lambda x \\ &\Leftrightarrow Ax - \lambda x = 0 \\ &\Leftrightarrow (A - \lambda I)x = 0 \end{aligned}
    $$
    
- 특성 방정식(characteristic equation)
    
    $$
    \det(A - \lambda I) = 0
    $$
    

### 3 × 3 행렬의 고윳값과 고유 벡터 구하기

- 2 × 2 행렬의 고윳값과 고유 벡터를 구하는 과정과 동일

### QR 분해를 이용한 방법

- QR 분해 → 직교 행렬과 상 삼각 행렬로 분해
- 분해할 행렬 준비
- 반복 수행할 행렬 초기 행렬 생성
- 초기 행렬에 대해 QR 분해 수행
- 앞에서 구한 Q, R 행렬로 다음 차례 행렬 구하기
- 위 과정을 반복해 QR 분해 수행
    
    $$
    A_0(Q_0Q_1\cdots Q_{k-1}Q_k) = A_{k+1}Q_0Q_1\cdots Q_{k-1}Q_k)
    $$
    

## 3. 고윳값과 고유 벡터 성질

- 행렬의 고윳값과 고유 벡터
    
    $$
    A^nx = \lambda^n x
    $$
    
- 정사각 행렬이 가역 행렬이기 위한 조건 → 행렬의 고윳값이 0이 아님
- 고유 벡터는 유일하지 않음

# 8. 행렬 분해

## 1. 대각화(diagonalization)

- 행렬 → 대각 행렬
- 대각화 가능 : 정사각 행렬 $A$에 대해 $P^{-1}AP$가 대각 행렬이 되는 가역 행렬이 존재
- 대각화 가능 여부 → 해당 행렬의 고윳값의 개수로 판단

## 2. 직교 대각화(orthogonal diagonalization)

- 정사각 행렬이 대각 행렬일 때
    
    $$
    D = P^{-1}AP = P^TAP
    $$
    
- 행렬의 고유 벡터는 $n$개의 정규 직교 벡터 만족
- 행렬이 직교 대각화 가능하기 위해 반드시 대칭 행렬이어야 함
- 공분산 행렬
    
    $$
    \begin{pmatrix} \sigma_{11} & \sigma_{12} & \cdots & \sigma_{1p} \\ \sigma_{21} & \sigma_{22} & \cdots & \sigma_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{p1} & \sigma_{p2} & \cdots & \sigma_{pp}\end{pmatrix}
    $$
    

## 3. 고윳값 분해(eigenvalue decomposition)

- 직교 대각화의 한 종류
- 행렬을 고유 벡터, 고윳값의 곱으로 분해
    
    $$
    \begin{pmatrix} \sigma_{11} & \sigma_{12} & \sigma_{13} \\ \sigma_{21} & \sigma_{22} & \sigma_{23} \\ \sigma_{31} & \sigma_{32} & \sigma_{3} \end{pmatrix} = \begin{pmatrix} u_1 & u_2 & u_3 \end{pmatrix} \begin{pmatrix} \lambda_1 & 0 & 0 \\  0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{pmatrix} \begin{pmatrix} u_1^T \\ u_2^T \\ u_3^T \end{pmatrix} \\ A = PDP^T
    $$
    

## 4. 특이값 분해(Singular Value Decomposition)

- 행렬 분해 기법 중 하나
- 정사각 행렬을 대상으로 하는 고윳값 분해를 $m \times n$ 행렬로 일반화시킨 것
- 차원 축소를 위한 도구
- 데이터와 부분 공간으로부터의 수직 거리 최소화 → 부분 공간 구하기
- 특이값 : 행렬의 고윳값에 루트를 씌운 값
    
    $$
    A = U\Sigma V^T
    $$
    
- 행렬 $U$ 열벡터 → $AA^T$의 고유 벡터로 구성
- 행렬 $V$ 열벡터 → $A^TA$의 고유 벡터로 구성
    
    $$
    \begin{aligned} AA^T &= (U\Sigma V^T)(U\Sigma V^T)^T \\ &= U\Sigma V^T V\Sigma^T U^T \\ &= U\Sigma \Sigma^T U^T \end{aligned}
    $$
    
    $$
    \begin{aligned} A^TA &= (U\Sigma V^T)^T(U\Sigma V^T) \\ &= V\Sigma^T U^T U\Sigma V^T \\ &= V\Sigma^T \Sigma V^T \end{aligned}
    $$
    
    $$
    A_{n \times p} = U_{n \times n} \Sigma_{n \times p} V_{p \times p}^T
    $$
    
    $$
    A = U\Sigma V^T \\ AV = U\Sigma
    $$
    

## 5. 기본 행렬

- 기본 행렬(elementary matrix) : 단위 행렬에서 기본 행 연산을 수행한 행렬
- 기본 행렬 역행렬
    - 행렬 원소의 주 대각 원소만 0이 아닌 대각 행렬 → 주 대각 원소의 역수 대입
    - 기본 행렬이 대각 행렬이 아닌 경우 → 주 대각 원소가 아닌 0이 아닌 값에 음수 붙이기

## 6. LU 분해(LU factorization)

### LU 분해 정의

- 정사각 행렬을 하 삼각 행렬과 상 삼각 행렬로 분해하는 것
    
    $$
    A = LU \\ \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = \begin{pmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{pmatrix} \begin{pmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{pmatrix}
    $$
    

### LU 분해 방법

- 하 삼각 행렬 + 상 삼각 행렬로 분해
    
    $$
    A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}
    $$
    
    $$
    A = LU \\ \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = \begin{pmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{pmatrix} \begin{pmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{pmatrix}
    $$
    
    - 상 삼각 행렬 : 가우스 행렬 형태
    - 하 삼각 행렬 : 가우스 행렬로 변환하는 과정에서 구하기 가능
- 행렬 → 가우스 행렬 변환 : 기본 행 연산 수행
    
    $$
    E_nE_{n-1}\cdots E_2E_1A = U
    $$
    
    $$
    A = E_1^{-1}E_2^{-1}\cdots E_{n-1}^{-1}E_n^{-1}U
    $$
    
    $$
    E_1^{-1}E_2^{-1}\cdots E_{n-1}^{-1}E_n^{-1} = L
    $$
    

### LU 분해 쉽게 하기

- 가우스 행렬의 형태로 바꿀 때 곱하는 수 기억
- 행렬의 주 대각 원소를 1로 바꾸기 위해 곱하는 수의 역수 → 행렬 L의 주 대각 원소
- 행렬의 주 대각 원소 아래에 위치한 원소를 0으로 만들기 위해 필요한 배수의 음수 → 행렬 L의 위치에 둠

### LU 분해와 선형 시스템의 해

- $A = LU$ → $Ax = b$를 $LUx = b$로 바꿔씀
    
    $$
    Ax = b \Leftrightarrow LUx = b
    $$
    
- $Ux$ 부분을 $y$로 정의
    
    $$
    Ux = y
    $$
    
- $Ux = y$ → $LUx = b$를 $Ly = b$로 바꿔씀
    
    $$
    Ly = b
    $$
    
- $Ux = y$에 앞서 구한 $y$값을 넣고 $x$에 대해 품
    
    $$
    Ux = y
    $$
    

# 9. 행렬의 이차식

## 1. 이차식(quadratic form) 정의

- 다항식을 벡터 형태로 나타낼 때 사용하는 유용한 방법
    
    $$
    w_1x_1 + w_2x_2 + \cdots + w_px_p
    $$
    
    $$
    \begin{pmatrix} w_1 & w_2 & \cdots & w_p \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_p \end{pmatrix} = w^Tx
    $$
    
- cross product term : 인덱스가 서로 다른 $(x_i, x_j)$ 경우의 곱
- cross product term 일반화 → $w_kx_ix_j$
- 행렬 $W$ : 대칭 행렬
- $W$의 대각 원소 → 최고차항이 2인 제곱 항
- 대각 원소가 아닌 원소 → cross product term의 절반 값
- $x^TWx$ 형태로 표현한 식을 $W$에 대한 이차식
    
    $$
    \begin{aligned} x^TWx &= \begin{pmatrix} x_1 & x_2 & \cdots & x_d \end{pmatrix} \begin{pmatrix} w_1 & 0 & \cdots & 0 \\ 0 & w_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & 0 \\ 0 & 0 & \cdots & w_d \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_d \end{pmatrix} \\ &= w_1x_1^2 + w_2x_2^2 + \cdots + w_dx_d^2 \end{aligned}
    $$
    

## 2. 양정치 행렬(positive definite)

- 양정치 행렬 : 행렬이 대칭 행렬이면서 고윳값이 모두 0보다 큼
    
    $$
    x^TWx > 0, \ \text{for all} \ x \neq 0
    $$
    
- 준양정치 행렬 : 행렬이 대칭 행렬이면서 고윳값이 모두 0보다 크거나 같음
    
    $$
    x^TWx \geq 0, \ \text{for all} \ x \neq 0
    $$
    
- 음정치 행렬 : 대칭 행렬의 고윳값이 모두 0보다 작음
    
    $$
    x^TWx < 0, \ \text{for all} \ x \neq 0
    $$
    
- 준음정치 행렬 : 대칭 행렬의 고윳값이 모두 0보다 작거나 같음
    
    $$
    x^TWx \leq 0, \ \text{for all} \ x \neq 0
    $$
    

## 3. 벡터의 미분

- 변수 $y$를 가중치 벡터 $x$로 미분
    
    $$
    \frac{\partial y}{\partial x} = \begin{pmatrix} \frac{\partial y}{\partial x_1} \\ \frac{\partial y}{\partial x_2} \\ \vdots \\ \frac{\partial y}{\partial x_p} \end{pmatrix}
    $$
    
- 특정 변수를 벡터 $x$에 대해 미분
    
    $$
    x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_p \end{pmatrix}, \quad w = \begin{pmatrix} w_1 \\ w_2 \\ \vdots \\ w_p \end{pmatrix}
    $$
    
    $$
    y = w^Tx \\ y = x^Tw
    $$
    
    $$
    \frac{\partial y}{\partial x} = \frac{\partial (w^Tx)}{\partial x} = \frac{\partial (x^Tw)}{\partial x} = w
    $$
    
    $$
    \frac{\partial y}{\partial x_i} = \frac{\partial (w_1x_1 + w_2x_2 + \cdots + w_px_p)}{\partial x_i} = w_i
    $$
    
    $$
    \frac{\partial y}{\partial x} = \begin{pmatrix} w_1 \\ w_2 \\ \vdots \\ w_p \end{pmatrix} = w
    $$
    
- 대칭 행렬 $A$에 대해 이차식 표현인 $x^TAx$ 미분
    
    $$
    \frac{\partial (x^TAx)}{\partial x} = 2Ax
    $$
    
- 대칭 행렬 $X^TX$에 적용
    
    $$
    \frac{\partial (w^TX^TXw)}{\partial w} = 2X^TXw
    $$
    

# 10. 텐서

## 1. 텐서(tensor) 정의

- 고차원 행렬
- n차원 텐서 → n차 텐서(nth-order tensor)
- 벡터 : 1차원 직선 형태
    
    $$
    x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}
    $$
    
- 행렬 : 2차원 평면 구조
    
    $$
    x = \begin{pmatrix} x_{11} & x_{12} & \cdots & x_{1p} \\ x_{21} & x_{22} & \cdots & x_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ x_{n1} & x_{n2} & \cdots & x_{np} \end{pmatrix}
    $$
    
- 텐서 : 3차원 공간 형태 구조
    
    $$
    x = \begin{pmatrix} x_{111} & x_{121} & \cdots & x_{1J1} \\ x_{211} & x_{221} & \cdots & x_{2J1} \\ \vdots & \vdots & \ddots & \vdots \\ x_{I11} & x_{I21} & \cdots & x_{IJ1} \end{pmatrix}, \begin{pmatrix} x_{112} & x_{122} & \cdots & x_{1J2} \\ x_{212} & x_{222} & \cdots & x_{2J2} \\ \vdots & \vdots & \ddots & \vdots \\ x_{I12} & x_{I22} & \cdots & x_{IJ2} \end{pmatrix}, \cdots, \begin{pmatrix} x_{11K} & x_{12K} & \cdots & x_{1JK} \\ x_{21K} & x_{22K} & \cdots & x_{2JK} \\ \vdots & \vdots & \ddots & \vdots \\ x_{I1K} & x_{I2K} & \cdots & x_{IJK} \end{pmatrix}
    $$
    
    - fiber : 하나의 인덱스를 고정한 텐서의 구성 원소
    - Mode 1(column) fibers, Mode 2(row) fibers, Mode 3(tube) fibers
    - slice : 텐서의 2차원 파트, 인덱스 두 개를 고정시키는 것
    - Horizontal slices, Lateral slices, Frontal slices

## 2. 텐서 기본 연산

### 텐서 노름

- 텐서의 모든 구성 원소의 제곱합에 루트를 씌운 것
    
    $$
    ||X|| = \sqrt{\sum^I_{i=1}\sum^J_{j=1}\sum^K_{k=1}x^2_{ijk}}
    $$
    
    $$
    ||X|| = \sqrt{\sum^{I_1}_{i_1=1}\sum^{I_2}_{i_2=1}\cdots\sum^{I_N}_{i_N=1}x^2_{i_1i_2\cdots i_N}}
    $$
    

### 텐서 내적

- 서로 다른 텐서의 동일한 위치의 구성 원소끼리 곱한 후 모두 더하는 것
    
    $$
    \lang X, Y \rang = \sum^I_{i=1}\sum^J_{j=1}\sum^K_{k=1}x_{ijk}y_{ijk}
    $$
    
    $$
    \lang X, Y \rang = \sum^{I_1}_{i_1=1}\sum^{I_2}_{i_2=1}\cdots\sum^{I_N}_{i_N=1}x_{i_1i_2\cdots i_N}y_{i_1i_2\cdots i_N}
    $$
    

### Rank One 텐서

- 텐서를 N개의 벡터의 외적으로 표현할 수 있는 것
    
    $$
    X = a^{(1)}_{i_1} \otimes a^{(2)}_{i_2} \otimes \cdots \otimes a^{(N)}_{i_N}
    $$
    
    $$
    a = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_I \end{pmatrix}, \quad b = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_J \end{pmatrix}, \quad c = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_K \end{pmatrix} \\ X = a \otimes b \otimes c \\ x_{ijk} = a_ib_jc_k
    $$
    

### 텐서 대칭성

- cubical : 텐서의 모든 mode의 크기가 동일한 것, 초대칭(supersymmetric)
    
    $$
    x_{ijk} = x_{ikj} = x_{jik} = x_{jki} = x_{kij} = x_{kji}, \quad \text{for all} \ i, j, k = 1, 2, \cdots , I
    $$
    
- 2개 이상의 mode에 대해 부분적으로 대칭성 만족 가능
    
    $$
    X_k = X^T_k, \quad \text{for all} \ k = 1, 2, \cdots , K
    $$
    

### 대각 텐서(diagonal tensor)

- 텐서 전체의 대각 원소가 모두 1인 텐서
    
    $$
    X \in \mathbb{R}^{I_1 \times I_2 \times \cdots \times I_N}, \ i_1 = i_2 = \cdots = i_N \rarr x_{i_1i_2\cdots i_N} \neq 0
    $$
    

### 텐서 행렬화(matricization)

- 텐서를 행렬로 변환하는 것, N차 텐서를 행렬로 변환하는 과정
- unfolding, flattening
- mode-n matricization
    
    $$
    j = 1 + \sum^N_{{k=1}, {k\neq n}}(i_k - 1)J_k \quad \text{with} \ J_k = \prod^{k-1}_{{m=1}, {m\neq n}} I_m
    $$
    

### 텐서 곱

- 텐서와 행렬, 텐서와 벡터를 mode-n 형태로 곱하는 것
- n-mode product
    
    $$
    (X \times U)_{i_1 \cdots i_{n-1}ji_{n+1} \cdots i_N} = \sum^{I_n}_{i_n=1}x_{i_1i_2\cdots i_N}u_{ji_N}
    $$
    
    $$
    y = X \times_n U \Leftrightarrow Y_{(n)} = UX_{(n)}
    $$