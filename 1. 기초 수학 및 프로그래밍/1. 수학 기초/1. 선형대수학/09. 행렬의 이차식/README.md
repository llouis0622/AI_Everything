# 1. 이차식(quadratic form) 정의

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
    

# 2. 양정치 행렬(positive definite)

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
    

# 3. 벡터의 미분

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