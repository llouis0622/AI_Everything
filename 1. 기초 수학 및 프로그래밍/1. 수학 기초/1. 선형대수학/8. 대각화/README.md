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