# 1. 텐서(tensor) 정의

- 고차원 행렬
- n차원 텐서 → n차 텐서(nth-order tensor)

## 2. 텐서 구성 원소

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

# 2. 텐서 기본 연산

## 1. 텐서 노름

- 텐서의 모든 구성 원소의 제곱합에 루트를 씌운 것
    
    $$
    ||X|| = \sqrt{\sum^I_{i=1}\sum^J_{j=1}\sum^K_{k=1}x^2_{ijk}}
    $$
    
    $$
    ||X|| = \sqrt{\sum^{I_1}_{i_1=1}\sum^{I_2}_{i_2=1}\cdots\sum^{I_N}_{i_N=1}x^2_{i_1i_2\cdots i_N}}
    $$
    

## 2. 텐서 내적

- 서로 다른 텐서의 동일한 위치의 구성 원소끼리 곱한 후 모두 더하는 것
    
    $$
    \lang X, Y \rang = \sum^I_{i=1}\sum^J_{j=1}\sum^K_{k=1}x_{ijk}y_{ijk}
    $$
    
    $$
    \lang X, Y \rang = \sum^{I_1}_{i_1=1}\sum^{I_2}_{i_2=1}\cdots\sum^{I_N}_{i_N=1}x_{i_1i_2\cdots i_N}y_{i_1i_2\cdots i_N}
    $$
    

## 3. Rank One 텐서

- 텐서를 N개의 벡터의 외적으로 표현할 수 있는 것
    
    $$
    X = a^{(1)}_{i_1} \otimes a^{(2)}_{i_2} \otimes \cdots \otimes a^{(N)}_{i_N}
    $$
    
    $$
    a = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_I \end{pmatrix}, \quad b = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_J \end{pmatrix}, \quad c = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_K \end{pmatrix} \\ X = a \otimes b \otimes c \\ x_{ijk} = a_ib_jc_k
    $$
    

## 4. 텐서 대칭성

- cubical : 텐서의 모든 mode의 크기가 동일한 것, 초대칭(supersymmetric)
    
    $$
    x_{ijk} = x_{ikj} = x_{jik} = x_{jki} = x_{kij} = x_{kji}, \quad \text{for all} \ i, j, k = 1, 2, \cdots , I
    $$
    
- 2개 이상의 mode에 대해 부분적으로 대칭성 만족 가능
    
    $$
    X_k = X^T_k, \quad \text{for all} \ k = 1, 2, \cdots , K
    $$
    

## 5. 대각 텐서(diagonal tensor)

- 텐서 전체의 대각 원소가 모두 1인 텐서
    
    $$
    X \in \mathbb{R}^{I_1 \times I_2 \times \cdots \times I_N}, \ i_1 = i_2 = \cdots = i_N \rarr x_{i_1i_2\cdots i_N} \neq 0
    $$
    

## 6. 텐서 행렬화(matricization)

- 텐서를 행렬로 변환하는 것, N차 텐서를 행렬로 변환하는 과정
- unfolding, flattening
- mode-n matricization
    
    $$
    j = 1 + \sum^N_{{k=1}, {k\neq n}}(i_k - 1)J_k \quad \text{with} \ J_k = \prod^{k-1}_{{m=1}, {m\neq n}} I_m
    $$
    

## 7. 텐서 곱

- 텐서와 행렬, 텐서와 벡터를 mode-n 형태로 곱하는 것
- n-mode product
    
    $$
    (X \times U)_{i_1 \cdots i_{n-1}ji_{n+1} \cdots i_N} = \sum^{I_n}_{i_n=1}x_{i_1i_2\cdots i_N}u_{ji_N}
    $$
    
    $$
    y = X \times_n U \Leftrightarrow Y_{(n)} = UX_{(n)}
    $$