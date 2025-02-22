# 1. 이산형 균일 분포

## 1. 이산형 균일 분포 정의

- 균일 분포(uniform distribution) : 이산형 확률 분포의 한 종류, 확률 변수가 특정 값을 가질 확률이 모두 동일한 분포
- 이산형 균일 분포(discrete uniform distribution)
    
    $$
    X \sim U(1, N) \\ P(X = x) = \frac{1}{N}, \quad x = 1, 2, \cdots, N
    $$
    

## 2. 이산형 균일 분포의 기댓값

$$
E(X) = \frac{N + 1}{2}
$$

## 3. 이산형 균일 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \frac{(N + 1)(2N + 1)}{6}
$$

$$
Var(X) = \frac{(N + 1)(N - 1)}{12}
$$

## 4. 이산형 균일 분포 일반화 형태

$$
X \sim U(a, b)
$$

$$
P(X = x) = \frac{1}{b - a + 1}, \quad x = a, a + 1, a + 2, \cdots, b
$$

$$
E(X) = \frac{a + b}{2}
$$

$$
Var(X) = \frac{(N + 1)(N - 1)}{12}
$$

# 2. 베르누이 분포

## 1. 베르누이 분포(Bernoulli distribution) 정의

- 한 번 시행했을 때의 성공할 확률 or 실패할 확률을 나타내는 것
- 베르누이 시행
    
    $$
    X \sim Berenoulli(p) \\ P(X = x) = p^x(1-p)^{1-x}, \quad x = 0, 1
    $$
    
    $$
    E(X) = p
    $$
    
    $$
    Var(X) = p(1 - p)
    $$
    

## 2. 베르누이 분포의 기댓값

$$
E(X) = p
$$

## 3. 베르누이 분포의 분산

$$
Var(X) = p(1 - p)
$$

# 3. 이항 분포

## 1. 이항 분포(binomial distribution) 정의

- 이항 정리(binomial theorem)
    
    $$
    (p + q)^n = \sum^n_{x=0}\binom{n}{x}p^xq^{n-x}
    $$
    
    $$
    2^n = (1 + 1)^n = \sum^n_{x=0}\binom{n}{x}1^x1^{n - x} = \sum^n_{x = 0}\binom{n}{x}
    $$
    
- 이항 분포 : 독립적인 베르누이 시행을 n번 했을 때의 성공 횟수
    
    $$
    Y_1, Y_2, \cdots, Y_n \sim Bernoulli(p) \\ X = \sum^n_{i=1}Y_i
    $$
    
    $$
    X \sim Binomial(n, p) \\ P(X = x) = \binom{n}{x}p^x(1 - p)^{n - x}, \quad x = 0, 1, \cdots, n
    $$
    
    $$
    \binom{n}{x} = \frac{n!}{x!(n - x)!}
    $$
    
    $$
    E(X) = np
    $$
    
    $$
    Var(X) = np(1 - p)
    $$
    

## 2. 이항 분포의 적률 생성 함수

$$
M_X(t) = [pe^t + (1 - p)]^n
$$

## 3. 이항 분포의 기댓값

$$
E(X) = np
$$

## 4. 이항 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = n(n - 1)p^2 + np
$$

$$
Var(X) = np(1 - p)
$$

# 4. 포아송 분포

## 1. 포아송 분포(Poisson distribution) 정의

- 확률 변수가 단위 시간 동안 발생하는 이벤트의 횟수인 것
    
    $$
    X \sim Poisson(\lambda) \\ P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}, \quad x = 0, 1, 2, \cdots \\ e^\lambda = \sum^\infty_{x=0}\frac{\lambda^x}{x}
    $$
    
    $$
    E(X) = \lambda
    $$
    
    $$
    Var(X) = \lambda
    $$
    

## 2. 포아송 분포의 적률 생성 함수

$$
M_X(t) = e^{\lambda(e^{t} - 1)}
$$

## 3. 포아송 분포의 기댓값

$$
E(X) = \lambda
$$

## 4. 포아송 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \lambda^2 + \lambda
$$

$$
Var(X) = \lambda
$$

## 5. 이항 분포의 포아송 근사

$$
P(X = x) = \binom{n}{x}p^x(1 - p)^{n - x}, \quad x = 0, 1, \cdots, n \\ X \sim Binomial(n, p)
$$

$$
P(X = x) \approx \frac{e^{-np}(np)^x}{x!}, \quad x = 0, 1, 2, \cdots \\ X \sim Poisson(\lambda = np)
$$

$$
X \sim Binomial(n, p = \frac{\lambda}{n})
$$

$$
Y \sim Poisson(\lambda)
$$

$$
\lim_{n \rarr \infty}Binomial(n, p = \frac{\lambda}{n}) = \frac{e^{-\lambda}\lambda^x}{x!} = Poisson(\lambda)
$$

$$
\lim_{n \rarr \infty}Binomial(n, p = \frac{\lambda}{n}) = Poisson(\lambda)
$$

# 5. 기하 분포

## 1. 기하 분포(geometric distribution) 정의

- 베르누이 시행을 계속 시행할 때, 처음 성공할 때까지의 시행 횟수 or 처음 성공할 때까지의 실패 횟수
- 확률 변수를 시행 횟수라고 보는 경우
    
    $$
    X = \text{처음 성공할 때까지의 시행 횟수} \\ X \sim Geometric(p) \\ P(X = x) = p(1 - p)^{x - 1}, \quad x = 1, 2, \cdots
    $$
    
    $$
    E(X) = \frac{1}{p}
    $$
    
    $$
    Var(X) = \frac{1 - p}{p^2}
    $$
    
- 확률 변수를 성공할 때까지의 실패 횟수로 보는 경우
    
    $$
    Y = \text{처음 성공할 때까지의 실패 횟수} \\ Y \sim Geometric(p) \\ X = Y + 1 \quad Y = X - 1 \\ P(Y = y) v= p(1 - p)^y, \quad y = 0, 1, \cdots
    $$
    
    $$
    E(X) = \frac{1 - p}{p}
    $$
    
    $$
    Var(X) = \frac{1 - p}{p^2}
    $$
    

## 2. 기하 분포의 누적 분포 함수

$$
P(X \leq x) = 1 - (1 - p)^x \\ P(X > x) = (1 - p)^x
$$

## 3. 기하 분포의 적률 생성 함수

$$
M_X(t) = \frac{pe^t}{1 - (1 - p)e^t}
$$

## 4. 기하 분포의 무기억성(memoryless property)

- 만약 확률 변수가 기하 분포를 따름 → 확률 변수는 무기억성을 가짐
    
    $$
    X \sim Geometric(p) \\ P(X > y + z|X > y) = P(X > z), \quad for \ all \ y, z > 0 \\ P(X > y + z) = P(X > y) P(X > z), \quad for \ all \ y, z > 0
    $$
    
- 만약 확률 변수가 이산형 확률 변수이고 무기억성을 가짐 → 확룰 변수는 기하 분포를 따름

## 5. 기하 분포의 기댓값

$$
E(X) = \frac{1}{p}
$$

## 6. 기하 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \frac{2 -p}{p^2}
$$

$$
Var(X) = \frac{1 - p}{p^2}
$$

# 6. 음이항 분포

## 1. 음이항 분포(negative binomial distribution) 정의

- 베르누이 시행을 반복할 때, r번째 성공할 때까지의 시행 횟수/실패 횟수
- 확률 변수를 성공할 때까지의 시행 횟수로 보는 경우
    
    $$
    Z_1, Z_2, \cdots, Z_n \sim Bernoulli(p) \\ X = \inf\left\{n: \sum^n_{i=1}Z_i = r\right\} \\ X \sim NegativeBinomial(r, p)
    $$
    
    $$
    X = \text{r번 성공할 때까지의 시행 횟수} \\ X \sim NegativeBinomial(r, p) \\ P(X = x) = \binom{x - 1}{r - 1}p^r(1 - p)^{x - r}, \quad x = r, r + 1, \cdots
    $$
    
    $$
    E(X) = \frac{r}{p}
    $$
    
    $$
    Var(X) = \frac{r(1 - p)}{p^2}
    $$
    
- 확률 변수를 성공할 때까지의 실패 횟수로 보는 경우
    
    $$
    Y = \text{r번 성공할 때까지의 실패 횟수} \\ X = Y + r \quad Y = X - r \\ P(Y = y) = \binom{r + y - 1}{y}p^r(1 - p)^y, \quad y = 0, 1, \cdots
    $$
    
    $$
    E(Y) = \frac{r(1 - p)}{p}
    $$
    
    $$
    Var(Y) = \frac{r(1 - p)}{p^2}
    $$
    

## 2. 음이항 분포와 기하 분포의 관계

$$
X_r = X_1 + (X_2 - X_1) + (X_3 - X_2) + \cdots + (X_r - X_{r - 1})
$$

$$
X_1 \sim Geometric(p) \\ X_2 - X_1 \sim Geometric(p) \\ X_3 - X_2 \sim Geometric(p) \\ \vdots \\ X_r - X_{r - 1} \sim Geometric(p)
$$

## 3. 음이항 분포의 기댓값

$$
E(Y) = \frac{r(1-p)}{p}
$$

## 4. 음이항 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(Y^2) = E[Y(Y - 1)] + E(Y)
$$

$$
Var(Y) = \frac{r(1 - p)}{p^2}
$$