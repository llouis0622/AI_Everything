# 1. 대각화(diagonalization)

- 행렬 → 대각 행렬
- 대각화 가능 : 정사각 행렬 $A$에 대해 $P^{-1}AP$가 대각 행렬이 되는 가역 행렬이 존재
- 대각화 가능 여부 → 해당 행렬의 고윳값의 개수로 판단

# 2. 직교 대각화(orthogonal diagonalization)

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
    

# 3. 고윳값 분해(eigenvalue decomposition)

- 직교 대각화의 한 종류
- 행렬을 고유 벡터, 고윳값의 곱으로 분해
    
    $$
    \begin{pmatrix} \sigma_{11} & \sigma_{12} & \sigma_{13} \\ \sigma_{21} & \sigma_{22} & \sigma_{23} \\ \sigma_{31} & \sigma_{32} & \sigma_{3} \end{pmatrix} = \begin{pmatrix} u_1 & u_2 & u_3 \end{pmatrix} \begin{pmatrix} \lambda_1 & 0 & 0 \\  0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{pmatrix} \begin{pmatrix} u_1^T \\ u_2^T \\ u_3^T \end{pmatrix} \\ A = PDP^T
    $$
    

# 4. 특이값 분해(Singular Value Decomposition)

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
    

# 5. 기본 행렬

- 기본 행렬(elementary matrix) : 단위 행렬에서 기본 행 연산을 수행한 행렬
- 기본 행렬 역행렬
    - 행렬 원소의 주 대각 원소만 0이 아닌 대각 행렬 → 주 대각 원소의 역수 대입
    - 기본 행렬이 대각 행렬이 아닌 경우 → 주 대각 원소가 아닌 0이 아닌 값에 음수 붙이기

# 6. LU 분해(LU factorization)

## 1. LU 분해 정의

- 정사각 행렬을 하 삼각 행렬과 상 삼각 행렬로 분해하는 것
    
    $$
    A = LU \\ \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = \begin{pmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{pmatrix} \begin{pmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{pmatrix}
    $$
    

## 2. LU 분해 방법

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
    

## 3. LU 분해 쉽게 하기

- 가우스 행렬의 형태로 바꿀 때 곱하는 수 기억
- 행렬의 주 대각 원소를 1로 바꾸기 위해 곱하는 수의 역수 → 행렬 L의 주 대각 원소
- 행렬의 주 대각 원소 아래에 위치한 원소를 0으로 만들기 위해 필요한 배수의 음수 → 행렬 L의 위치에 둠

## 4. LU 분해와 선형 시스템의 해

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