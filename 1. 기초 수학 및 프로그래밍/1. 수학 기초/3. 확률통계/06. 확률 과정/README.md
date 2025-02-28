# 1. 확률 과정

## 1. 확률 과정(stochastic process) 정의

- 시간과 관련된 확률 변수의 집합
- 확률 과정을 구성하는 확률 변수 → 모두 시간 혹은 시점과 관련되어 있음

## 2. 마팅게일(martingale)

- 공평한 게임 특성을 가진 확률 과정
    
    $$
    E(|X_t|) < \infty
    $$
    
    $$
    E(X_{t + 1}|X_0, X_1, \cdots, X_t) = X_t
    $$
    
    $$
    E(X_0) = E(X_t)
    $$
    

# 2. 마르코프 체인

## 1. 마르코프 체인(Markov chain) 정의

- 미래 시점에서의 결과는 오직 현재 시점에만 의존하며 과거 시점에는 의존하지 않는 것
- Markov property
    
    $$
    P(X_{n + 1} = j|X_0 = i_0, X_1 = i_1, \cdots, X_{n - 1} = i_{n - 1}, X_n = i) \\ = P(X_{n + 1} = j|X_n = i)
    $$
    
- one-step 전이 확률
    
    $$
    P_{ij}^{n, n + 1} = P(X_{n + 1} = j|X_n = i)
    $$
    
- 정상성(stationary) : 시점에 어떤 시점을 넣더라도 등식은 성립함

## 2. one-step 전이 확률 행렬

- 1시점 이후의 결과 : 다음 시행에서의 결과
- 마르코프 행렬(Markov matrix), 전이 확률 행렬(transition probability matrix)
    
    $$
    P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} & \cdots \\ P_{10} & P_{11} & P_{12} & P_{13} & \cdots \\ P_{20} & P_{21} & P_{22} & P_{23} & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \\ P_{i0} & P_{i1} & P_{i2} & P_{i3} & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix}
    $$
    
- 전이 확률은 0보다 크거나 같음
    
    $$
    P_{ij} \geq 0 \ for \ i, j = 0, 1, 2, \cdots
    $$
    
- 특정 시점을 기준으로 바로 다음 시점에 발생할 수 있는 모든 값에 대한 확률을 더한 값은 1
    
    $$
    \sum^\infty_{j=0}P_{ij} = 1 \ for \ i = 0, 1, 2, \cdots
    $$
    

## 3. n-step 전이 확률 행렬

- m 시점의 상태가 i라고 주어졌을 때 n 시점 이후의 상태가 j가 될 확률
    
    $$
    P^{(n)} = [P_{ij}^{(n)}]
    $$
    
    $$
    P_{ij}^{(n)} = P(X_{m + n} = j|X_m = i)
    $$
    
    $$
    P_{ij}^{(n)} = \sum^\infty_{k=0}P_{ik}P_{kj}^{(n - 1)}, \quad where P_{ij}^{(0)} = \begin{cases} 1, \quad if \ i = j \\ 0, \quad if \ i \neq j\end{cases}
    $$
    
    $$
    P^{(n)} = P \times P \times \cdots \times P = P^n
    $$
    

# 3. First Step Analysis

## 1. 3 x 3 행렬의 First Step Analysis

- 첫 번째 전이 이후 발생하는 확률 분석 → 전확률 공식과 Markov property를 이용해 변수들의 특성 파악
    
    $$
    P = \begin{bmatrix} P_{00} & P_{01} & P_{02} \\ P_{10} & P_{11} & P_{12} \\ P_{20} & P_{21} & P_{22} \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ \alpha & \beta & \gamma \\ 0 & 0 & 1 \end{bmatrix}
    $$
    
- absorption : 시간이 지나도 상태가 변하지 않는 것
    
    $$
    T = \min\{n \geq 0; X_n = 0 \ or \ X_n = 2\}
    $$
    
    - 상태 0 또는 상태 2에 absorption될 때, 둘 중 상태 0에 absorption되었을 확률
        
        $$
        u_1 = P(X_T = 0|X_0 = 1) \\ u_1 = \alpha + \beta u_1 \Leftrightarrow u_1 = \frac{\alpha}{1 - \beta} = \frac{\alpha}{\alpha + \gamma}
        $$
        
    - 상태 0 또는 상태 2에 absorption될 때, 둘 중 상태 2에 absorption되었을 확률
        
        $$
        u_2 = P(X_T = 2|X_0 = 1) \\ u_2 = \beta u_2 + \gamma \Leftrightarrow u_2 = \frac{\gamma}{1 - \beta} = \frac{\gamma}{\alpha + \gamma}
        $$
        
    
    $$
    u_1 + u_2 = \frac{\alpha}{\alpha + \gamma} + \frac{\gamma}{\alpha + \gamma} = 1
    $$
    
    - absorption되는 데 걸리는 시간
        
        $$
        v = E[T|X_0 = 1] \\ v = 1 + \beta v \Leftrightarrow v = \frac{1}{1 - \beta}
        $$
        
        $$
        P(T > k|X_0 = 1) = \beta^k, \quad k = 0, 1, \cdots
        $$
        

## 2. 4 x 4 행렬의 First Step Analysis

- 상태 0, 상태 3 → absorption
- 상태 1, 상태 2 → transient
    
    $$
    P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} \\ P_{10} & P_{11} & P_{12} & P_{13} \\ P_{20} & P_{21} & P_{22} & p_{23} \\ P_{30} & P_{31} & P_{32} & p_{33} \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ P_{10} & P_{11} & P_{12} & P_{13} \\ P_{20} & P_{21} & P_{22} & p_{23} \\ 0 & 0 & 0 & 1 \end{bmatrix}
    $$
    
    $$
    T = \min\{n \geq 0; X_n = 0 \ or \ X_n = 3\}
    $$
    
    $$
    u_i = P(X_T = 0|X_0 = i), \quad for \ i = 1, 2 \\ v_i = E(T|X_) = i), \quad for \ i = 1, 2
    $$
    
- $u_1$ 구하기
    
    $$
    u_1 = P(X_T = 0|X_0 = 1) \\ u_1 = P_{10} + P_{11}u_1 + P_{12}u_2
    $$
    
- $u_2$ 구하기
    
    $$
    u_2 = P(X_T = 0|X_0 = 2) \\ u_2 = P_{20} + P_{21}u_1 + P_{22}u_2
    $$
    

$$
v_1 = E(T|X_0 = 1) \\ v_2 = E(T|X_0 = 2)
$$

- 상태 1로 시작했을 때, absorption되는 데 걸리는 시간의 기댓값
    
    $$
    v_1 = E(T|X_0 = 1) \\ v_1 = 1 + P_{11}v_1 + P_{12}v_2
    $$
    
- 상태 2로 시작했을 때, absorption되는 데 걸리는 시간의 기댓값
    
    $$
    v_2 = E(T|X_0 = 2) \\ v_2 = 1 + P_{21}v_1 + P_{22}v_2
    $$
    

## 3. n x n 행렬의 First Step Analysis

- 마르코프 체인이 가질 수 있는 상태 : 0 ~ N까지의 N + 1가지
- 0 ~ r - 1까지의 상태 → transient
- r ~ N까지의 상태 → absorption
    
    $$
    P = \begin{bmatrix} Q(r \times r) & R(r \times (N - r + 1)) \\ 0((N - r + 1) \times r) & I((N - r + 1) \times (N - r + 1)) \end{bmatrix}
    $$
    
- 초기 상태에서 특정 상태로 absorption될 확률
    
    $$
    U_{ik} = u_i = P(absorption \ in \ k|X_0 = i), \quad r \leq k \leq N
    $$
    
    $$
    u_i = P_{ik} + \sum^{r - 1}_{j = 0}P_{ij}u_j
    $$
    
- absorption될 때까지 걸리는 시간
    
    $$
    T = \min\{n \geq 0; X_n \geq r\}
    $$
    
    $$
    I(i) = \begin{cases} 1, \quad if \ i = m \\ 0, \quad if \ i \neq m \end{cases} \quad 0 \leq m < r
    $$
    
- T 시점 동안 상태에 도달한 횟수
    
    $$
    w_i = E\left[ \sum^{T - 1}_{n=0}I(X_n)|X_0 = i \right]
    $$
    
    $$
    w_i = I(i) + \sum^{r - 1}_{j=0}P_{ij}w_j \quad for \ i = 0, 1, \cdots, r - 1
    $$
    
    $$
    v_i = E(T|X_0 = i) = 1 + \sum^{r - 1}_{j=0}P_{ij}v_i
    $$
    

# 4. 랜덤 워크

## 1. 랜덤 워크(random walk) 정의

- 임의의 상태 $i$에서 시작했을 때 다음 스텝에서 상태 $i$에 그대로 머물거나 혹은 이웃에 존재하는 상태 $i - 1$ 혹은 $i + 1$로 이동하는 마르코프 체인
- 0, $N$ → absorption
- 1 ~ $N - 1$ → transient

## 2. 랜덤 워크의 전이 확률 행렬

$$
P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} & \cdots & P_{0N - 1} & P_{0N} \\ P_{10} & P_{11} & P_{12} & P_{13} & \cdots & P_{1N - 1} & P_{1N} \\ P_{20} & P_{21} & P_{22} & P_{23} & \cdots & P_{2N - 1} & P_{2N} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ P_{N - 1 0} & P_{N - 11} & P_{N - 12} & P_{N - 13} & \cdots & P_{N - 1N - 1} & P_{N - 1N} \\ P_{N0} & P_{N1} & P_{N2} & P_{N3} & \cdots & P_{NN - 1} & P_{NN} \end{bmatrix} \\ = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 & 0 \\ q_1 & r_1 & p_1 & 0 & \cdots & 0 & 0 \\ 0 & q_2 & r_2 & p_2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & r_{N - 1} & p_{N - 1} \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}
$$

$$
P(X_{n + 1} = i + 1|X_n = i) = p_i \\ P(X_{n + 1} = i - 1|X_n = i) = q_i \\ P(X_{n + 1} = i|X_n = i) = r_i
$$

## 3. 랜덤 워크에서 파산 확률

$$
u_i = P(X_n \text{이 상태 N이 되기 전에 상태 0이 될 확률}|X_0 = i) \\ = \begin{cases} \frac{N - i}{N}, \quad when \ p = q = 1/2 \\ \frac{(q/p)^i - (q/p)^N}{1 - (q/p)^N}, \quad when \ p \neq q \end{cases}
$$

$$
u_i = pu_i + qu_i
$$

- $i = 0$
    
    $$
    u_1 = pu_2 + qu_0 \\ x_2 = \frac{q}{p}x_1
    $$
    
- $i = 2$
    
    $$
    u_2 = pu_3 + qu_1 \\ x_3 = (\frac{q}{p})^2x_1
    $$
    
- $i = 3$
    
    $$
    u_3 = pu_4 + qu_2 \\ x_4 = (\frac{q}{p})^3x_1
    $$
    
- $i = k - 1$
    
    $$
    u_{k - 1} = pu_k + qu_{k - 2} \\ x_k = (\frac{q}{p})^{k - 1}x_1
    $$
    
- $i = N - 1$
    
    $$
    u_{N - 1} = pu_N + qu_{N - 2} \\ x_N= (\frac{q}{p})^{N - 1}x_1
    $$
    

$$
u_k = \begin{cases} 1 - (\frac{k}{N} ) = \frac{(N - k)}{N}, \quad if \ p = q = \frac{1}{2} \\ 1 - \frac{1 - (\frac{q}{p})^k}{1 - (\frac{q}{p}^N)} = \frac{(\frac{q}{p})^k - (\frac{q}{p})^N}{1 - (\frac{q}{p})^N}, \quad if \ p \neq q \end{cases}
$$

## 4. 파산할 때까지 걸리는 평균 시간

$$
P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} & \cdots & P_{0N - 1} & P_{0N} \\ P_{10} & P_{11} & P_{12} & P_{13} & \cdots & P_{1N - 1} & P_{1N} \\ P_{20} & P_{21} & P_{22} & P_{23} & \cdots & P_{2N - 1} & P_{2N} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ P_{N - 1 0} & P_{N - 11} & P_{N - 12} & P_{N - 13} & \cdots & P_{N - 1N - 1} & P_{N - 1N} \\ P_{N0} & P_{N1} & P_{N2} & P_{N3} & \cdots & P_{NN - 1} & P_{NN} \end{bmatrix} \\ = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 & 0 \\ q_1 & r_1 & p_1 & 0 & \cdots & 0 & 0 \\ 0 & q_2 & r_2 & p_2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & r_{N - 1} & p_{N - 1} \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}
$$

$$
v_i = E(T|X_0 = i) = 1 + \sum^{r - 1}_{j=0}P_{ij}v_i
$$

$$
x_i = u_i - u_{i - 1} \quad for \ i=1, 2, \cdots, N
$$

- $i = 1$
    
    $$
    v_1 = 1 + \frac{1}{2}v_2 + \frac{1}{2}v_0 \\ -1 = \frac{1}{2}x_2 + \frac{1}{2}x_1
    $$
    
- $i = 2$
    
    $$
    v_2 = 1 + \frac{1}{2}v_3 + \frac{1}{2}v_1 \\ -1 = \frac{1}{2}x_3 + \frac{1}{2}x_2
    $$
    
- $i = 3$
    
    $$
    v_3 = 1 + \frac{1}{2}v_4 + \frac{1}{2}v_2 \\ -1 = \frac{1}{2}x_4 + \frac{1}{2}x_3
    $$
    
- $i = N - 1$
    
    $$
    v_{N - 1} = 1 + \frac{1}{2}v_N + \frac{1}{2}v_{N - 2} \\ -1 = \frac{1}{2}x_N + \frac{1}{2}x_{N - 1}
    $$
    

$$
v_k = k(N - k), \quad k = 0, 1, \cdots, N
$$

## 5. 일반화 랜덤 워크의 파산 확률

$$
P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} & \cdots & P_{0N - 1} & P_{0N} \\ P_{10} & P_{11} & P_{12} & P_{13} & \cdots & P_{1N - 1} & P_{1N} \\ P_{20} & P_{21} & P_{22} & P_{23} & \cdots & P_{2N - 1} & P_{2N} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ P_{N - 1 0} & P_{N - 11} & P_{N - 12} & P_{N - 13} & \cdots & P_{N - 1N - 1} & P_{N - 1N} \\ P_{N0} & P_{N1} & P_{N2} & P_{N3} & \cdots & P_{NN - 1} & P_{NN} \end{bmatrix} \\ = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 & 0 \\ q_1 & r_1 & p_1 & 0 & \cdots & 0 & 0 \\ 0 & q_2 & r_2 & p_2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & r_{N - 1} & p_{N - 1} \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}
$$

$$
T = \min\{n \geq 0; X_n = 0 \ or \ X_n = N \}
$$

$$
u_i = q_iu_{i - 1} + r_iu_i + p_iu_{i + 1}, \quad for \ i=, 2, \cdots, N - 1 \\ u_0 = 1, \quad u_N = 0 \\ q_i + r_i + p_i = 1 \\ x_i = u_i - u_{i - 1}, \quad for \ i=1, 2, \cdots, N
$$

- $i = 1$
    
    $$
    u_1 = q_1u_0 + r_1u_1 + p_1u_2 \\ x_2 = \frac{q_1}{p_1}x_1
    $$
    
- $i = 2$
    
    $$
    u_2 = q_2u_1 + r_2u_2 + p_2u_3 \\ x_3 = \frac{q_1q_2}{p_1p_2}x_1
    $$
    
- $i = k - 1$
    
    $$
    x_{k} = \frac{q_1q_2\cdots q_{N - 1}}{p_1p_2\cdots p_{N - 1}}x_1
    $$
    
- $i = N - 1$
    
    $$
    x_N = \frac{q_1q_2\cdots q_{N - 1}}{p_1p_2\cdots p_{N - 1}}x_1
    $$
    

$$
u_k = \frac{\rho_k + \rho_{k + 1} + \cdots + \rho_{k - 1}}{1 + \rho_1 + \rho_2 + \cdots + \rho_{N - 1}} \quad k = 1, 2, \cdots, N - 1
$$

## 6. 일반화 랜덤 워크의 파산까지 걸리는 시간

$$
P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} & \cdots & P_{0N - 1} & P_{0N} \\ P_{10} & P_{11} & P_{12} & P_{13} & \cdots & P_{1N - 1} & P_{1N} \\ P_{20} & P_{21} & P_{22} & P_{23} & \cdots & P_{2N - 1} & P_{2N} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ P_{N - 1 0} & P_{N - 11} & P_{N - 12} & P_{N - 13} & \cdots & P_{N - 1N - 1} & P_{N - 1N} \\ P_{N0} & P_{N1} & P_{N2} & P_{N3} & \cdots & P_{NN - 1} & P_{NN} \end{bmatrix} \\ = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 & 0 \\ q_1 & r_1 & p_1 & 0 & \cdots & 0 & 0 \\ 0 & q_2 & r_2 & p_2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & r_{N - 1} & p_{N - 1} \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}
$$

- $i = 1$
    
    $$
    v_1 = 1 + q_1v_0 + r_1v_1 + p_1v_2 \\ x_2 = \frac{q_1}{p_1}x_1 - \frac{1}{p_1}
    $$
    
- $i = 2$
    
    $$
    v_2 = 1 + q_2v_1 + r_2v_2 + p_2v_3 \\ x_3 = \frac{q_1q_2}{p_1p_2}x_1 - \frac{q_2}{p_1p_2} - \frac{1}{p_2}
    $$
    
- $i = 3$
    
    $$
    x_4 = \frac{q_1q_2q_3}{p_1p_2p_3}x_1 - \frac{q_2q_3}{p_1p_2p_3} - \frac{q_3}{p_2p_3} - \frac{1}{p_3}
    $$
    
- $i = k - 1$
    
    $$
    x_k = \rho_{k - 1}x_1 - \Phi_{k - 1}
    $$
    
- $i = N - 1$
    
    $$
    x_N = \rho_{N - 1}x_1 - \Phi_{N - 1}
    $$
    

$$
v_k = (1 + \rho_1 + \rho_2 + \cdots + \rho_{k - 1})(\frac{\Phi_1 + \Phi_2 + \cdots + \Phi_{N - 1}}{1 + \rho_1 + \rho_2 + \cdots + \rho_{N - 1}}) - (\Phi_1 + \Phi_2 + \cdots + \Phi_{k - 1}) \\ for \ k = 1, 2, \cdots, N - 1
$$

# 5. 포아송 과정

## 1. 포아송 과정(poisson process) 정의

- 포아송 분포와 관련있는 확률 과정
    
    $$
    X(t_1) - X(t_0), \quad X(t_2) - X(t_1), \quad \cdots, \quad X(t_n) - X(t_{n - 1})
    $$
    
    $$
    P(X(s + t) - X(s) = k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}, \quad k = 0, 1, 2, \cdots
    $$
    
    $$
    X(0) = 0
    $$
    
- 포아송 과정
    
    $$
    X(t) = n((0, t])
    $$
    
- 체류 시간(sojourn time) : 현재 이벤트가 발생한 시간에서 직전 이벤트가 발생할 때까지 걸린 시간을 뺀 것
- 대기 시간(waiting time) : n번째 이벤트가 발생할 때까지 걸리는 시간

# 6. 브라운 운동

## 1. 브라운 운동(Brownian motion) 정의

- 연속형 시간, 연속형 상태 공간에서의 확률 과정 중 하나
- $B(0) = 0$이고 $B(t)$는 $t$에 대해 연속
- 브라운 운동의 increment의 분포의 평균은 항상 0, 분산은 시간 차에 의존함
    
    $$
    B(s + t) - B(s) \sim N(0, \sigma^2t)
    $$
    
- 만약 임의의 구간이 서로 겹치지 않으면 구간 차는 서로 독립임
    
    $$
    [t_i, t_j) \rarr B(t_j) - B(t_i)
    $$
    
    $$
    Cov[B(s), B(t)] = \sigma^2 \min\{s, t\}
    $$
    

## 2. Geometric Brownian Motion(GBM)

$$
X(t) = xe^{drift+diffusion}t = xe^{(\mu - \frac{1}{2}\sigma^2)t+\sigma B(t)}
$$