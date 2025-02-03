# 1. 행렬(matrix)

## 1. 행렬 정의

- 사각형 형태로 숫자를 나열하는 것
- 행과 열로 구성
- 행 벡터의 집합, 열 벡터의 집합
- 행렬 원소 : 행렬을 구성하는 각 스칼라 값

## 2. 행렬의 덧셈과 뺄셈

- 행렬 간 덧셈, 뺄셈 가능
- 각 행렬의 동일 위치에 대응하는 원소끼리 덧셈, 뺼셈 수행
    
    $$
    A = \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 6 & 1 \end{pmatrix}, \quad B = \begin{pmatrix}1 & 4 \\ 4 & -1 \\ 2 & 5 \end{pmatrix} \\ A + B = \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 6 & 1 \end{pmatrix} + \begin{pmatrix}1 & 4 \\ 4 & -1 \\ 2 & 5 \end{pmatrix} = \begin{pmatrix}2 + 1 & 7 + 4 \\ 3 + 4 & 4 + (-1) \\ 6 + 2 & 1 + 5 \end{pmatrix} = \begin{pmatrix}3 & 11 \\ 7 & 3 \\ 8 & 6 \end{pmatrix} \\ A - B = \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 6 & 1 \end{pmatrix} - \begin{pmatrix}1 & 4 \\ 4 & -1 \\ 2 & 5 \end{pmatrix} = \begin{pmatrix}2 - 1 & 7 - 4 \\ 3 - 4 & 4 - (-1) \\ 6 - 2 & 1 - 5 \end{pmatrix} = \begin{pmatrix}1 & 3 \\ -1 & 5 \\ 4 & -4 \end{pmatrix}
    $$
    

## 3. 행렬의 스칼라 곱

- 스칼라 * 행렬
- 행렬에 포함도니 모든 원소에 스칼라를 곱함
- 행렬의 길이 변화
    
    $$
    A = \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 6 & 1 \end{pmatrix} \\ 2A = 2 \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 6 & 1 \end{pmatrix} = \begin{pmatrix}2 \times 2 & 7 \times 2 \\ 3 \times 2 & 4 \times 2 \\ 6 \times 2 & 1 \times 2 \end{pmatrix} = \begin{pmatrix}4 & 14 \\ 6 & 8 \\ 12 & 2 \end{pmatrix}
    $$
    

## 4. 행렬의 원소 곱

- 크기가 동일한 두 행렬에서 동일한 위치의 원소들끼리 서로 곱하는 것
    
    $$
    A = \begin{pmatrix}1 & 5 \\ 6 & 4 \\ 2 & 7 \end{pmatrix}, \quad B = \begin{pmatrix}5 & -1 \\ 1 & 2 \\ 4 & 1 \end{pmatrix} \\ A \odot B = \begin{pmatrix}1 & 5 \\ 6 & 4 \\ 2 & 7 \end{pmatrix} \odot \begin{pmatrix}5 & -1 \\ 1 & 2 \\ 4 & 1 \end{pmatrix} = \begin{pmatrix}1 \times 5 & 5 \times -1 \\ 6 \times 1 & 4 \times 2 \\ 2 \times 4 & 7 \times 1 \end{pmatrix} = \begin{pmatrix}5 & -5 \\ 6 & 8 \\ 8 & 7 \end{pmatrix}
    $$
    

## 5. 행렬 곱

- 행렬끼리 서로 곱하는 것
- 곱하는 행렬의 열 크기와 곱해지는 행렬의 행 크기가 일치해야 계산 가능
- 교환 법칙이 성립하지 않음
    
    $$
    \begin{aligned} AB &= \begin{pmatrix}2 & 7 \\ 3 & 4 \\ 5 & 2 \end{pmatrix} \begin{pmatrix}3 & -3 & 5 \\ -1 & 2 & 1 \end{pmatrix} \\ &= \begin{pmatrix}2 \times 3 + 7 \times (-1) & 2 \times (-3) + 7 \times 2 & 2 \times 5 + 7 \times (-1) \\ 3 \times 3 + 4 \times (-1) & 3 \times (-3) + 4 \times 2 & 3 \times 5 + 4 \times (-1) \\ 5 \times 3 + 2 \times (-1) & 5 \times (-3) + 2 \times 2 & 5 \times 5 + 2 \times (-1) \end{pmatrix} \\ &= \begin{pmatrix}-1 & 8 & 3 \\ 5 & -1 & 11 \\ 13 & -11 & 23 \end{pmatrix} \end{aligned}
    $$
    

## 6. 행렬의 대각합(trace)

- 정사각 행렬일 때 주 대각 원소를 모두 더한 값
- 주 대각 원소 : 행렬의 행 번호와 열 번호가 동일한 원소
    
    $$
    A = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \\ \text{tr}(A) = a_{11} + a_{12} + a_{13}
    $$
    

## 7. 행렬 연산 성질

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

# 2. 전치 행렬(transposed matrix)

## 1. 전치 행렬 정의

- 기존 행렬의 행과 열을 바꾼 행렬
- 전치 행렬로 변환 시 행렬의 크기 변경
    
    $$
    U = \begin{pmatrix}u_{11} & u_{12} \\ u_{21} & u_{22} \\ u_{31} & u_{32}\end{pmatrix} \rarr U^T = \begin{pmatrix}u_{11} & u_{21} & u_{31} \\ u_{12} & u_{22} & u_{32}  \end{pmatrix}
    $$
    

## 2. 전치 행렬 성질

- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(A - B)^T = A^T - B^T$
- $(aA)^T = aA^T$
- $(AB)^T = B^TA^T$

# 3. 대칭 행렬(symmetric matrix)

## 1. 대칭 행렬 정의

- 기존 행렬과 전치 행렬이 동일한 정사각 행렬
- 행 번호와 열 번호를 바꾸어도 값이 동일한 행렬
    
    $$
    A = \begin{pmatrix}a & b & c \\ b & d & e \\ c & e & f \end{pmatrix}, \quad A^T = \begin{pmatrix}a & b & c \\ b & d & e \\ c & e & f \end{pmatrix} \\ A_{ij} = A_{ji}, \quad A = A^T
    $$
    

## 2. 대칭 행렬 성질

- 대칭 행렬 간 덧셈이나 뺄셈의 결과는 대칭 행렬
- 대칭 행렬 간 곱셈이나 나눗셈의 결과가 반드시 대칭 행렬은 아님
- 대칭 행렬의 거듭 제곱 결과는 대칭 행렬
- 대칭 행렬에 자신의 전치 행렬을 곱한 결과는 대칭 행렬
    
    $$
    A = \begin{pmatrix}5 & 2 \\ 2 & 1 \end{pmatrix}, \quad B = \begin{pmatrix}3 & 1 \\ 1 & 4 \end{pmatrix} \\ A + B = \begin{pmatrix}5 & 2 \\ 2 & 1 \end{pmatrix} + \begin{pmatrix}3 & 1 \\ 1 & 4 \end{pmatrix} = \begin{pmatrix}5 + 3 & 2 + 1 \\ 2 + 1 & 1 + 4 \end{pmatrix} = \begin{pmatrix}8 & 3 \\ 3 & 5 \end{pmatrix} \\ A - B = \begin{pmatrix}5 & 2 \\ 2 & 1 \end{pmatrix} - \begin{pmatrix}3 & 1 \\ 1 & 4 \end{pmatrix} = \begin{pmatrix}5 - 3 & 2 - 1 \\ 2 - 1 & 1 - 4 \end{pmatrix} = \begin{pmatrix}2 & 1 \\ 1 & -3 \end{pmatrix}
    $$
    
    $$
    A = \begin{pmatrix}5 & 2 \\ 2 & 1 \end{pmatrix}, \quad B = \begin{pmatrix}3 & 1 \\ 1 & 4 \end{pmatrix} \\ AB = \begin{pmatrix}5 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix}3 & 1 \\ 1 & 4 \end{pmatrix} = \begin{pmatrix}5 \times 3 + 2 \times 1 & 5 \times 1 + 2 \times 4 \\ 2 \times 3 + 1 \times 1 & 2 \times 1 + 1 \times 4 \end{pmatrix} = \begin{pmatrix}17 & 13 \\ 7 & 6 \end{pmatrix} \\ BA = \begin{pmatrix}3 & 1 \\ 1 & 4 \end{pmatrix} \begin{pmatrix}5 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix}3 \times 5 + 1 \times 2 & 2 \times 2 + 1 \times 1 \\ 1 \times 5 + 4 \times 2 & 1 \times 2 + 4 \times 1 \end{pmatrix} = \begin{pmatrix}17 & 7 \\ 13 & 6 \end{pmatrix}
    $$
    
    $$
    A = \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} \\ A^2 = \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix}3 \times 3 + 2 \times 2 & 3 \times 2 + 2 \times 1 \\ 2 \times 3 + 1 \times 2 & 2 \times 2 + 1 \times 1 \end{pmatrix} = \begin{pmatrix}13 & 8 \\ 8 & 5 \end{pmatrix} \\ A^3 = \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix}13 & 8 \\ 8 & 5 \end{pmatrix} \begin{pmatrix}3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix}55 & 34 \\ 34 & 21 \end{pmatrix}
    $$
    
    $$
    A = \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix}, \quad A^T = \begin{pmatrix}1 & 3 \\ 2 & 4 \end{pmatrix} \\ A^TA = \begin{pmatrix}1 & 3 \\ 2 & 4 \end{pmatrix} \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix}1 \times 1 + 3 \times 3 & 1 \times 2 + 3 \times 4 \\ 2 \times 1 + 4 \times 3 & 2 \times 2 + 4 \times 4 \end{pmatrix} = \begin{pmatrix}10 & 14 \\ 14 & 20 \end{pmatrix} \\ AA^T = \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix}1 & 3 \\ 2 & 4 \end{pmatrix} = \begin{pmatrix}1 \times 1 + 2 \times 2 & 1 \times 3 + 2 \times 4 \\ 3 \times 1 + 4 \times 2 & 3 \times 3 + 4 \times 4 \end{pmatrix} = \begin{pmatrix}5 & 11 \\ 11 & 25 \end{pmatrix}
    $$
    

# 4. 대각 행렬(diagonal matrix)

## 1. 대각 행렬 정의

- 행렬의 주 대각 원소가 아닌 원소가 0인 정사각 행렬
- 대각 행렬의 역행렬 : 주 대각 원소의 역수
- 대각 행렬의 거듭 제곱 : 대각 원소의 거듭 제곱
    
    $$
    D = \begin{pmatrix}d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & d_n \end{pmatrix} \\ D^{-1} = \begin{pmatrix}1/d_1 & 0 & \cdots & 0 \\ 0 & 1/d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & 1/d_n \end{pmatrix} \\ D^k = \begin{pmatrix}d_1^k & 0 & \cdots & 0 \\ 0 & d_2^k & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & d_n^k \end{pmatrix}
    $$
    

## 2. 대각 행렬 성질

- 일반 행렬 * 대각 행렬 : 일반 행렬의 열 값 대각 행렬 원소 배
- 대각 행렬 * 일반 행렬 : 일반 행렬의 행 값 대각 행렬 원소 배
    
    $$
    A = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad D = \begin{pmatrix}d_{11} & 0 & 0 \\ 0 & d_{22} & 0 \\ 0 & 0 & d_{33} \end{pmatrix} \\ \begin{aligned} AD &= \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \begin{pmatrix}d_{11} & 0 & 0 \\ 0 & d_{22} & 0 \\ 0 & 0 & d_{33} \end{pmatrix} = \begin{pmatrix}a_{11} \times d_{11} & a_{12} \times d_{22} & a_{13} \times d_{33} \\ a_{21} \times d_{11} & a_{22} \times d_{22} & a_{23} \times d_{33} \\ a_{31} \times d_{11} & a_{32} \times d_{22} & a_{33} \times d_{33} \end{pmatrix} \end{aligned} \\ \begin{aligned} DA &= \begin{pmatrix}d_{11} & 0 & 0 \\ 0 & d_{22} & 0 \\ 0 & 0 & d_{33} \end{pmatrix} \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = \begin{pmatrix}a_{11} \times d_{11} & a_{12} \times d_{11} & a_{13} \times d_{11} \\ a_{21} \times d_{22} & a_{22} \times d_{22} & a_{23} \times d_{22} \\ a_{31} \times d_{33} & a_{32} \times d_{33} & a_{33} \times d_{33} \end{pmatrix} \end{aligned}
    $$
    

# 5. 단위 행렬(identity matrix)

## 1. 단위 행렬 정의

- 주 대각 원소가 1이고 나머지 원소는 모두 0인 대각 행렬
- 항등 행렬
    
    $$
    I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}
    $$
    

## 2. 단위 행렬 성질

- 행렬 * 단위 행렬 = 행렬
    
    $$
    A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}, \quad I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\ AI = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \\ IA = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}  = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \\ AI = IA = A
    $$
    

# 6. 영 행렬(zero matrix)

## 1. 영 행렬 정의

- 행렬 구성 원소가 모두 0인 행렬
    
    $$
    0 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
    $$
    

## 2. 영 행렬 성질

- 임의의 행렬 + 영 행렬 = 기존 행렬
- 임의의 행렬 - 영 행렬 = 기존 행렬
- 임의의 행렬 * 영 행렬 = 영 행렬
    
    $$
    A + 0 = A, \quad A - 0 = A \\ 0 - A = -A, \quad A - A = 0 \\ A0 = 0, \quad 0A = 0
    $$
    

# 7. 삼각 행렬(triangular matrix)

## 1. 삼각 행렬 정의

- 행렬의 구성 원소가 삼각형 형태를 띄는 행렬
- 상 삼각 행렬(upper) : 주 대각 원소 아래쪽에 있는 모든 원소가 0인 정사각 행렬
- 하 삼각 행렬(lower) : 주 대각 원소 위쪽에 있는 모든 원소가 0인 정사각 행렬
    
    $$
    A_u = \begin{pmatrix}a_{11} & a_{12} & a_{13} \\ 0 & a_{22} & a_{23} \\ 0 & 0 & a_{33} \end{pmatrix}, \quad A_l = \begin{pmatrix}a_{11} & 0 & 0 \\ a_{21} & a_{22} & 0 \\ a_{31} & a_{32} & a_{33} \end{pmatrix}
    $$
    

## 2. 삼각 행렬 성질

- 삼각 행렬 간 덧셈, 뺄셈, 곱셈 결과 = 삼각 행렬
- 상 삼각 행렬의 전치 행렬 = 하 삼각 행렬
- 하 삼각 행렬의 전치 행렬 = 상 삼각 행렬
    
    $$
    A = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix}, \quad B = \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} \\ A + B = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix} + \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix}8 & 10 & 12 \\ 0 & 14 & 16 \\ 0 & 0 & 18 \end{pmatrix} \\ A - B = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix} - \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix}6 & 6 & 6 \\ 0 & 6 & 6 \\ 0 & 0 & 6 \end{pmatrix} \\ AB = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix} \begin{pmatrix}1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix}7 & 46 & 115 \\ 0 & 40 & 116 \\ 0 & 0 & 72 \end{pmatrix}
    $$
    
    $$
    A^T = \begin{pmatrix}7 & 8 & 9 \\ 0 & 10 & 11 \\ 0 & 0 & 12 \end{pmatrix}^T = \begin{pmatrix}7 & 0 & 0 \\ 8 & 10 & 0 \\ 9 & 11 & 12 \end{pmatrix} \\ C^T = \begin{pmatrix}1 & 0 & 0 \\ 2 & 3 & 0 \\ 4 & 5 & 6 \end{pmatrix}^T = \begin{pmatrix}1 & 2 & 4 \\ 0 & 3 & 5 \\ 0 & 0 & 6 \end{pmatrix}
    $$
    

# 8. 토플리츠 행렬(Toeplitz matrix)

## 1. 토플리츠 행렬 정의

- 왼쪽에서 오른쪽으로 내려가는 각 대각선의 원소들이 동일한 행렬
- 시계열 분석 시 사용
- 시계열 데이터를 행렬 형태로 변환 시 토플리츠 행렬 사용
    
    $$
    T = \begin{pmatrix}t_0 & t_{-1} & t_{-2} & \cdots & \cdots & t_{-(n-1)} \\ t_1 & t_0 & t_{-1} & \ddots & \ddots & \vdots \\ t_2 & t_1 & t_0 & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & t_{-1} & t_{-2} \\ \vdots & \ddots & \ddots & t_1 & t_0 & t_{-1} \\ t_{n-1} & t_{n-2} & \cdots & t_2 & t_1 & t_0 \end{pmatrix} \\ T_{i, j} = T_{i+1, j+1} = t_{i-j}
    $$
    

# 9. 이중 대각 행렬(bidiagonal matrix)

## 1. 이중 대각 행렬 정의

- 대각 원소뿐만 아니라 대각 원소의 바로 위쪽 혹은 아래쪽 원소가 0이 아닌 행렬
- upper bidiagonal matrix : 대각 원소 위쪽에 위치한 원소가 0이 아닌 이중 대각 행렬
- lower bidiagonal matrix : 대각 원소 아래쪽에 위치한 원소가 0이 아닌 이중 대각 행렬

# 10. 하우스홀더 행렬(householder matrix)

## 1. 하우스홀더 행렬 정의

- 어떤 행렬을 다른 형태로 변환할 때 사용하는 행렬 중 하나
- 정사각 행렬이며 모든 열이 정규 직교인 행렬
    
    $$
    v = \begin{pmatrix}v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} \\ H = I - 2 \frac{vv^T}{v^Tv}
    $$