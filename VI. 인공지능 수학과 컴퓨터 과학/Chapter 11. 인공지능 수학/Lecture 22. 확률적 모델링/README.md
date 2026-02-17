# 1. 기초 개념

## 1. 경우의 수

### 팩토리얼(factorial)

- 1부터 N까지의 모든 자연수의 곱
- $!$

### 조합(combination)

- 서로 다른 N개의 원소를 가지는 어떤 집합에서 순서에 상관없이 x개의 원소를 선택할 수 있는 가짓수
    
    $$
    \binom{n}{x} = \frac{n!}{x!(n-x)!}
    $$
    

## 2. 함수

### 함수(function) 정의

- 어떤 집합의 각 원소를 다른 집합의 유일한 원소에 대응시키는 것
- 대응 : 서로 다른 집합의 원소끼리 짝지어주는 것
    
    $$
    f : X \rarr Y
    $$
    
    $$
    y = f(x)
    $$
    

### 단조 함수(monotone function)

- 단조 증가 함수와 단조 감소 함수를 포함하는 함수
- 단조 증가 함수 : 주어진 구간에서 감소하는 구간이 없는 함수, $x_1 \leq  x_2 \rarr f(x_1) \leq f(x_2)$
- 단조 감소 함수 : 주어진 구간에서 증가하는 구간이 없는 함수, $x_1 \leq  x_2 \rarr f(x_1) \geq f(x_2)$

## 3. 수열

### 수열(sequence) 정의

- 차례대로 나열된 수의 열
    
    $$
    a_1, a_2, a_3, \cdots, a_n
    $$
    

### 등차수열(arithmetic sequence)

- 첫째 항부터 차례대로 특정 수를 더해서 만든 수열
- 공차(common difference) : 더하는 특정 수
    
    $$
    a_n = a_1 + (n - 1)d
    $$
    

### 등비수열(geometric sequence)

- 첫째 항부터 차례대로 일정한 수를 곱해 만든 수열
- 공비(common ratio) : 곱하는 일정한 수
    
    $$
    a_n = ar^{n-1}
    $$
    
    $$
    S_n = \frac{a_1(1-r^n)}{1 - r}
    $$
    

### 무한급수(infinite series)

- 무한 수열의 각 항을 모두 더한 식
    
    $$
    \lim_{n \rarr \infty}\sum^n_{i=1}a_i = \sum^\infty_{i=1}a_i = a_1 + a_2 + a_3 + \cdots + a_n + \cdots
    $$
    
    $$
    \lim_{n \rarr \infty}\sum^n_{i=1}a_i = S
    $$
    
- 무한 등비 급수(infinite geometric series) : 무한급수 중 첫째 항이 $a$이고 공비가 $r$인 무한 등비수열의 무한급수
    
    $$
    \sum^\infty_{i=1}ar^{i-1} = a + ar + ar^2 + \cdots + ar^{n-1} + \cdots
    $$
    
    $$
    \sum^\infty_{x=1}ar^{x-1} = \frac{a}{1-r}, \quad |r| < 1
    $$
    

# 2. 확률

## 1. 확률의 기초

### 확률을 배우는 이유

- 무작위로 일어나는 사건들을 이해하고 해석하기 위함
- 사건이 발생할 수 있는 확률을 기반으로 어떤 일을 계획하거나 결정 가능

### 확률(probability) 정의

- 표본 공간(sample space) : 발생 가능한 모든 결과의 집합, $\Omega$
- 사건(event) : 표본 공간의 부분 집합, 표본 공간을 구성하는 집합의 일부분
- 확률 : 어떤 사건이 발생할 가능성을 0과 1 사이의 숫자로 수치화시킨 것
    
    $$
    P(A) = \frac{\text{사건 A의 결과 개수}}{\text{발생 가능한 모든 경우의 개수}}
    $$
    
- 모든 확률이 0과 1 사이에 존재함 → 확률은 0보다 작은 값이 나올 수 없음
- 발생 가능한 모든 사건의 확률의 합은 1
- 동시에 발생할 수 없는 사건들에 대해 각 사건의 합의 확률은 개별 확률이 일어난 확률의 합과 같음

### 확률의 종류

- 이론적 확률(theoretical probability)
    - 이론에 기반한 확률
    - 아직 발생하지 않은 미래에 초점을 맞추는 방법
- 경험적 확률(empirical probability)
    - 과거의 경험에 기반한 확률
    - 과거에 얻은 데이터를 기반으로 함

### 독립(independent)

- 각각의 두 사건이 발생할 확률을 곱한 결과가 두 사건이 동시에 발생할 확률과 동일
    
    $$
    P(A \cap B) = P(A)P(B)
    $$
    

### 배반(disjoint)

- 두 사건이 동시에 발생할 확률이 0인 것
    
    $$
    P(A \cap B) = 0
    $$
    
    $$
    P(A \cup B) = P(A) + P(B)
    $$
    
    $$
    P(\bigcup^\infty_{i=1}A_i) = P(\sum^\infty_{i=1}A_i)
    $$
    

## 2. 확률 변수(random variable)

### 확률 변수 정의

- 확률 현상을 통해 값이 확률적으로 정해지는 변수
- 확률 현상 : 발생 가능한 결과들은 알지만 가능한 결과들 중 어떤 결과가 나올지는 모르는 현상
- 확률 변수 : 변수인데 확률 현상을 통해 확률적으로 변하는 수
    
    $$
    P(X = x) \quad or \quad P_x(X)
    $$
    
- 이산형 확률 변수 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 있는 것
- 연속형 확률 변수 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 없는 것

### 모집단(population)과 표본(sample)

- 모집단 : 관심 있는 대상이 되는 모든 측정값의 집합
- 표본 : 모집단에서 추출한 측정값의 집합
- 모수(population parameter) : 모집단의 분포 특성을 규정 짓는 척도, 관심의 대상이 되는 모집단의 대푯값
- 표본 통계량(sample statistic) : 표본의 대푯값

### 히스토그램(histogram)

- 표 형태로 되어 있는 빈도표(frequency table)를 그래프 형태로 나타낸 것

## 3. 확률 분포

### 확률 분포(probability distribution) 정의

- 확률 변수가 특정 값을 가질 확률을 나타내는 함수
- 확률 변수와 특정 값을 매핑시켜 주는 함수
- 이산형 확률 분포 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 있는 것
- 연속형 확률 분포 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 없는 것

### 이산형 확률 분포

- 확률 질량 함수(probability mass function , pmf) : 이산형 확률 변수가 특정 값을 가질 확률
    - $P_x(X) \geq 0$
    - $\Sigma_xP_x(X) = 1$
- 누적 분포 함수(cummulative distribution function, cdf) : 확률 변수가 취할 수 있는 값들을 누적해서 구하는 확률 분포
    - $F_x(-\infty) = 0$
    - $F_x(+\infty) = 1$
    - $x \leq y \Rightarrow F_x(X) \leq F_x(Y)$
    - $\lim_{y \rarr x, y > x}F_x(Y) = F(X)$

### 연속형 확률 분포

- 확률 밀도 함수(probability density function, pdf) : 연속형 확률 변수가 특정 값을 가질 확률
    - $f_x(X) \geq 0 \ for \ all \ x$
    - $\int_{-\infty}^{\infty}f_x(X) = 1$
    
    $$
    P(a < X < b) = \int^a_b f_X(t)dt
    $$
    
    $$
    P(a < X < b) = P(a < X \leq b) = P(a \leq X < b) = P(a \leq X \leq b)
    $$
    
    $$
    F_x(X) = \int^x_{-\infty}f_x(t)dt
    $$
    

### 확률 질량과 확률 밀도의 차이

- 확률 질량(probability mass) : 각 이산형 확률 변수가 가지는 확률의 양
- 확률 밀도(probability density) : 단위 길이 당 질량

### 독립 항등 분포(independent and identically distributed, iid)

- 확률 변수가 서로 독립이고 동일한 분포를 따르는 것

## 4. 평균과 기댓값

### 평균(mean)과 기댓값(expected value) 정의

- 평균
    - 데이터의 중심을 나타낼 때 사용
    - 표본 데이터가 실제로 주어졌을 때, 데이터의 평균을 직접 계산하는 것
- 기댓값
    - 확률 분포의 평균을 계산하는 것
    - 데이터가 주어지기 전에 계산하는 것
- 모평균 : 모집단의 평균, $\mu$
- 표뵨 평균 : 표본의 평균, $\bar{x}$

### 이산형 확률 변수의 기댓값

$$
E(X) = \sum^\infty_{i=1}x_iP(X = x_i) = \sum^\infty_{i=1}x_iP_X(x_i)
$$

- 지시 함수(indicator function) : 1 혹은 0 값을 가질 수 있으며 X가 A에 포함되면 1, 포함되지 않으면 0 값을 가지는 함수
    
    $$
    I_A(X) = \begin{cases} 1, \quad if \ X \in A \\ 0, \quad if \ X \in A^C \end{cases}
    $$
    
    $$
    E(I_A) = P(A)
    $$
    

### 연속형 확률 변수의 기댓값

$$
E(X) = \int^b_a xf_X(x)dx
$$

### 기댓값의 성질

- $E(a) = a$
- $E(aX) = aE(X)$
- $E(X + Y) = E(X) + E(Y)$
- $E(X - Y) = E(X) - E(Y)$
- $E(aX + bY) = aE(X) + bE(Y)$
- $E(aX - bY) = aE(X) - bE(Y)$

### 표본 평균의 개념

- 표본 평균 : 모평균의 추정치로 사용 가능
    
    $$
    \hat{\mu} = \frac{1}{n}\sum^n_{i=1}x_i = \bar{x}
    $$
    
- 표본 평균이 확률 변수임 → 고정된 값이 아님, 평균과 분산을 가짐

### 표본 평균의 성질

- 표본 평균의 기댓값 = 모평균
    
    $$
    E(\bar{X}) = \mu
    $$
    
- iid를 만족하는 표본 평균의 분산
    
    $$
    Var(\bar{X}) = \frac{\sigma^2}{n}
    $$
    

## 5. 분산

### 분산(variance) 정의

- 분포가 중심으로부터 얼마나 흩어져 있는지 알 수 있음
    
    $$
    Var(X) = E[(X - \mu)^2]
    $$
    
- 표준 편차(standard deviation) : 분산의 양의 제곱근
    
    $$
    \sqrt{E[(X - \mu)^2]}
    $$
    

### 이산형 확률 변수의 분산

$$
\sigma^2 = Var(X) = E[(X - \mu)^2] = \sum^\infty_{i=1}(x_i - \mu)^2P(X = x_i)
$$

$$
\sigma = \sqrt{Var(X)}
$$

### 연속형 확률 변수의 분산

$$
\sigma^2 = Var(X) = E[(X - \mu)^2] = \int^b_a (x-\mu)^2f_X(x)dx
$$

$$
\sigma = \sqrt{Var(X)}
$$

### 분산의 성질

- $Var(X) = \sigma^2 = Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2 = E(X^2) - \mu^2$
- $Var(aX + b) = a^2Var(X)$
- $Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)$
- $Var(X - Y) = Var(X) + Var(Y) - 2Cov(X, Y)$
- $Var(aX + bY) = a^2Var(X) + b^2Var(Y) + 2abCov(X, Y)$

### 표본 분산 정의

- 모분산의 추정치로 사용 가능
- 모분산의 추정치 : $\widehat{\sigma^2}$
- 표분 분산 : $s^2$
    
    $$
    s^2 = \frac{1}{n - 1}\sum^n_{i=1}(x_i - \bar{x})^2
    $$
    

### 표본 분산의 성질

$$
E(s^2) = \sigma^2
$$

### 자유도(degree of freedom)

- 자유로운 데이터의 개수

## 6. 공분산과 상관관계

### 공분산(covariance) 정의

- 두 확률 변수의 상관 관계를 나타내는 값
- 두 개의 확률 변수 중 하나의 값이 상승할 때 다른 값도 상승 → 공분산 양수
- 두 개의 확률 변수 중 하나의 값이 상승할 때 다른 값은 하락 → 공분산 음수
    
    $$
    Cov(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = \frac{1}{n - 1}\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})
    $$
    
    $$
    Cov(X, Y) = E(XY) - E(X)E(Y)
    $$
    

### 공분산의 성질

- $Cov(X, X) = Var(X)$
- $Cov(X, Y) = Cov(Y, X)$
- $Cov(aX, bY) = abCov(X, Y)$
- $Cov(X + Y, Z) = Cov(X, Z) + Cov(Y, Z)$

### 상관 계수 정의

- 상관 계수 : 공분산을 각 변수의 표준 편차로 나눈것
- 모집단 상관 계수(population coefficient of correlation)
    
    $$
    Corr(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}
    $$
    
- 표본 상관 계수(sample coefficient of correlation)
    
    $$
    r_{xy} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2(y_i - \bar{y})^2}}
    $$
    

## 7. 조건부 확률

### 조건부 확률(conditional probability)

- 주어진 사건이 발생한다는 가정하에 다른 한 사건이 발생할 확률
    
    $$
    P(A|B) = \frac{P(A\cap B)}{P(B)}
    $$
    
    $$
    P(A\cap B) = P(A|B)P(B)
    $$
    

### 조건부 독립(conditional independence)

- 사건 A, B, C가 존재할 때, 다음 식을 만족하는 사건 C가 주어지면 사건 A, B는 조건부 독립임
    
    $$
    P(A|B, C) = P(A|C)
    $$
    
    $$
    P(A, B|C) = P(A|C)P(B|C)
    $$
    

### 전확률 공식(law of total probability)

- 표본 공간을 서로 배반인 부분 공간으로 나누었을 때, 한 사건이 발생할 확률은 부분 공간에 대한 조건부 확률의 합 형태로 나타낼 수 있음
    
    $$
    P(A) = P(A|B)P(B) + P(A|B^C)P(B^C)
    $$
    

### 전평균 공식(law of total expectation)

- 표본 공간을 서로 배반인 부분 공간으로 나누었을 때, 한 확률 변수의 기댓값은 서로 배반인 부분 공간의 조건부 기댓값의 합 형태로 나타낼 수 있음
    
    $$
    E_Y(E_X(X|Y)) = E(X)
    $$
    

### 베이즈 정리

- 파라미터를 확률 변수로 보는 방법
- 사전 확률 밀도 함수(prior probability density function) : 사건이 발생하기 전 파라미터의 확률
    
    $$
    P(\theta, x) = P(x|\theta)P(\theta)
    $$
    
- 사후 확률 밀도 함수(posterior probability density function) : 사건이 발생한 후 파라미터의 확률
    
    $$
    P(\theta|x) = \frac{P(x|\theta)P(\theta)}{\sum_{\theta}P(x|\theta)P(\theta)}
    $$
    
    $$
    P(\theta|x) \propto P(x|\theta)P(\theta)
    $$
    

## 8. 적률 생성 함수(moment generation function, mgf)

- 0 근방의 t에 대해 기댓값이 존재하는 것
    
    $$
    M_X(t) = E(e^{tx})
    $$
    
- 이산 확룰 변수에서의 적률 생성 함수
    
    $$
    M_X(t) = \sum_xe^{tx}P(X = x)
    $$
    
- 연속 확률 변수에서의 적률 생성 함수
    
    $$
    M_X(t) = \int^\infty_{-\infty}e^{tx}f_X(x)dx
    $$
    
- 확률 변수의 n차 적률
    
    $$
    E(X^n) = M_X^{(n)}(0)
    $$
    
    $$
    Var(X) = E(X^2) - [E(X)]^2
    $$
    
    $$
    E(X^2) = M_X^{''}(0)
    $$
    

# 3. 이산형 확률 분포

## 1. 이산형 균일 분포

### 이산형 균일 분포 정의

- 균일 분포(uniform distribution) : 이산형 확률 분포의 한 종류, 확률 변수가 특정 값을 가질 확률이 모두 동일한 분포
- 이산형 균일 분포(discrete uniform distribution)
    
    $$
    X \sim U(1, N) \\ P(X = x) = \frac{1}{N}, \quad x = 1, 2, \cdots, N
    $$
    

### 이산형 균일 분포의 기댓값

$$
E(X) = \frac{N + 1}{2}
$$

### 이산형 균일 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \frac{(N + 1)(2N + 1)}{6}
$$

$$
Var(X) = \frac{(N + 1)(N - 1)}{12}
$$

### 이산형 균일 분포 일반화 형태

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

## 2. 베르누이 분포

### 베르누이 분포(Bernoulli distribution) 정의

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
    

### 베르누이 분포의 기댓값

$$
E(X) = p
$$

### 베르누이 분포의 분산

$$
Var(X) = p(1 - p)
$$

## 3. 이항 분포

### 이항 분포(binomial distribution) 정의

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
    

### 이항 분포의 적률 생성 함수

$$
M_X(t) = [pe^t + (1 - p)]^n
$$

### 이항 분포의 기댓값

$$
E(X) = np
$$

### 이항 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = n(n - 1)p^2 + np
$$

$$
Var(X) = np(1 - p)
$$

## 4. 포아송 분포

### 포아송 분포(Poisson distribution) 정의

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
    

### 포아송 분포의 적률 생성 함수

$$
M_X(t) = e^{\lambda(e^{t} - 1)}
$$

### 포아송 분포의 기댓값

$$
E(X) = \lambda
$$

### 포아송 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \lambda^2 + \lambda
$$

$$
Var(X) = \lambda
$$

### 이항 분포의 포아송 근사

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

## 5. 기하 분포

### 기하 분포(geometric distribution) 정의

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
    

### 기하 분포의 누적 분포 함수

$$
P(X \leq x) = 1 - (1 - p)^x \\ P(X > x) = (1 - p)^x
$$

### 기하 분포의 적률 생성 함수

$$
M_X(t) = \frac{pe^t}{1 - (1 - p)e^t}
$$

### 기하 분포의 무기억성(memoryless property)

- 만약 확률 변수가 기하 분포를 따름 → 확률 변수는 무기억성을 가짐
    
    $$
    X \sim Geometric(p) \\ P(X > y + z|X > y) = P(X > z), \quad for \ all \ y, z > 0 \\ P(X > y + z) = P(X > y) P(X > z), \quad for \ all \ y, z > 0
    $$
    
- 만약 확률 변수가 이산형 확률 변수이고 무기억성을 가짐 → 확룰 변수는 기하 분포를 따름

### 기하 분포의 기댓값

$$
E(X) = \frac{1}{p}
$$

### 기하 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \frac{2 -p}{p^2}
$$

$$
Var(X) = \frac{1 - p}{p^2}
$$

## 6. 음이항 분포

### 음이항 분포(negative binomial distribution) 정의

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
    

### 음이항 분포와 기하 분포의 관계

$$
X_r = X_1 + (X_2 - X_1) + (X_3 - X_2) + \cdots + (X_r - X_{r - 1})
$$

$$
X_1 \sim Geometric(p) \\ X_2 - X_1 \sim Geometric(p) \\ X_3 - X_2 \sim Geometric(p) \\ \vdots \\ X_r - X_{r - 1} \sim Geometric(p)
$$

### 음이항 분포의 기댓값

$$
E(Y) = \frac{r(1-p)}{p}
$$

### 음이항 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(Y^2) = E[Y(Y - 1)] + E(Y)
$$

$$
Var(Y) = \frac{r(1 - p)}{p^2}
$$

# 4. 연속형 확률 분포

## 1. 연속형 균일 분포

### 연속형 균일 분포(continuous uniform distribution) 정의

- 연속형 균일 분포의 확률 밀도 함수
    
    $$
    X \sim U(a, b) \\ f_X(x) = \frac{1}{b - a}, \quad x \in [a, b]
    $$
    
    $$
    E(X) = \frac{b + a}{2}
    $$
    
    $$
    Var(X) = \frac{(b - a)^2}{12}
    $$
    

### 연속형 균일 분포의 기댓값

$$
E(X) = \frac{b + a}{2}
$$

### 연속형 균일 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \frac{a^2 + ab + b^2}{3}
$$

$$
Var(X) = \frac{(b - a)^2}{12}
$$

## 2. 정규 분포

### 정규 분포(normal distribution) 정의

- 연속형 확률 분포에서 가장 기본이 되는 분포
    
    $$
    X \sim N(\mu, \sigma^2) \\ f_X(x) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2}, \quad -\infty < x < \infty
    $$
    
    $$
    E(X) = \mu
    $$
    
    $$
    Var(X) = \sigma^2
    $$
    
- $\pm1\sigma$ → 68% 범위
- $\pm2\sigma$ → 95% 범위
- $\pm3\sigma$ → 99.7% 범위

### 표준 정규 분포(standard normal distribution) 정의

- 정규 분포에서 평균이 0, 분산이 1인 경우
    
    $$
    X \sim N(0, 1) \\ f_X(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}, \quad -\infty < x < \infty
    $$
    
    $$
    E(X) = 0
    $$
    
    $$
    Var(X) = 1
    $$
    

### 정규 근사(normal approximation)

- 주어진 데이터가 정규 분포를 따르지 않더라도, 데이터의 개수 n이 커지면 정규 분포에 가까워지는 현상
- 이항 분포의 정규 근사
    
    $$
    X \sim Binomial(n, p) \\ X \sim N(np, np(1 - p)) \quad as \ n \rarr \infty
    $$
    
- 포아송 분포의 정규 근사
    
    $$
    X \sim Poisson(n, p) \\ X \sim N(\lambda, \lambda) \quad as \ \lambda \rarr \infty
    $$
    

## 3. 감마 분포

### 감마 함수(gamma function)

- 팩토리얼 함수를 확장시킨 함수
- 팩토리얼 함수를 연속 함수화한 것
    
    $$
    \Gamma(\alpha) = \int^\infty_{-\infty}x^{\alpha - 1}e^{-x}dx, \quad \alpha > 0
    $$
    
- 감마 함수의 성질
    - $\Gamma(\alpha) = (\alpha - 1)!$
    - $\Gamma(\alpha + 1) = \alpha\Gamma(\alpha)$
    - $\Gamma(\frac{1}{2}) = \sqrt{\pi}$
    - $\Gamma(1) = 1$

### 감마 분포(gamma distribution) 정의

- 확률 변수가 a번째 성공할 때까지의 대기 시간
    
    $$
    X \sim Gamma(\alpha, \beta) \\ f_X(x) = \frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha - 1}e^{-\frac{1}{\beta}x}, \quad 0 < x < \infty, \quad \alpha > 0, \quad \beta > 0
    $$
    
    $$
    E(X) = \alpha\beta
    $$
    
    $$
    Var(X) = \alpha\beta^2
    $$
    

### 감마 분포의 적률 생성 함수

$$
M_X(t) = (1 - \beta t)^{-\alpha}
$$

### 감마 분포의 기댓값

$$
E(X) = \alpha\beta
$$

### 감마 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \alpha^2\beta^2 + \alpha\beta^2
$$

$$
Var(X) = \alpha\beta^2
$$

## 4. 지수 분포

### 지수 분포(exponential distribution) 정의

- 감마 분포에서 알파가 1인 특수한 경우
- 확률 변수가 첫 번째 성공할 때까지의 대기 시간
    
    $$
    X \sim Exponential(\beta) \\ f_X(x) = \frac{1}{\beta}e^{-\frac{1}{\beta}x}, \quad x > 0
    $$
    
    $$
    E(X) = \beta
    $$
    
    $$
    Var(X) = \beta^2
    $$
    

### 지수 분포의 무기억성

- 만약 확률 변수가 지수 분포를 따름 → 확률 변수는 무기억성을 따름
    
    $$
    X \sim Exp(\beta) \\ P(X > s + t|X > t) = P(X > s), \quad for \ all \ s, t > 0 \\ P(X > s + t) = P(X > s)P(X > t), \quad for \ all \ s, t > 0
    $$
    
- 만약 확률 변수가 연속형 확률 변수이고 무기억성을 가짐 → 확률 변수는 지수 분포를 따름

### 지수 분포의 적률 생성 함수

$$
M_X(t) = (1 - \beta t)^{-1}
$$

### 지수 분포의 기댓값

$$
E(X) = \beta
$$

### 지수 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = 2\beta^2
$$

$$
Var(X) = \beta^2
$$

## 5. 카이제곱 분포(chi-square distribution)

- 감마 분포의 특수한 형태
- 감마 분포에서 $\alpha$가 p / 2, $\beta$가 2인 경우
    
    $$
    X \sim X^2(p) \\ f_X(x) = \frac{1}{\Gamma(\frac{p}{2})2^{\frac{p}{2}}}x^{\frac{p}{2} - 1}e^{-\frac{1}{2}x}, \quad 0 < x < \infty
    $$
    
    $$
    E(X) = p
    $$
    
    $$
    Var(X) = 2p
    $$
    

## 6. 베타 분포

### 베타 함수(beta function)

- 이항 계수를 실수 범위로 확장한 것
    
    $$
    \Beta(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}
    $$
    
    $$
    \Beta(\alpha, \beta) = \int^1_0x^{\alpha - 1}(1 - x)^{\beta - 1}dx
    $$
    

### 베타 분포(beta distribution) 정의

$$
X \sim Beta(\alpha, \beta) \\ f_X(x) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}x^{\alpha - 1}(1 - x)^{\beta - 1}dx, \quad 0 < x < 1, \quad \alpha > 0, \quad \beta > 0
$$

$$
E(X) = \frac{\alpha}{\alpha + \beta}
$$

$$
Var(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
$$

### 베타 분포의 기댓값

$$
E(X) = \frac{\alpha}{\alpha + \beta}
$$

### 베타 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X) = \frac{(\alpha + 1)\alpha}{(\alpha + \beta)(\alpha + \beta + 1)}
$$

$$
Var(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
$$

## 7. 확률 분포와 관련된 이론

### 확률 변수의 변환

$$
g(X) : X \rarr Y
$$

$$
P(Y \in A) = P(X \in g^{-1}(A))
$$

$$
f_Y(y) = \frac{1}{\Gamma(\alpha)\beta^\alpha}(\frac{1}{y})^{\alpha + 1}e^{-\frac{1}{\beta y}}
$$

### 확률 수렴(convergence in probability)

- 확률 수렴 : 확률 변수가 다음 식에서 모든 $\epsilon > 0$에 대해 성립하는 것
    
    $$
    \lim_{n \rarr \infty}P(|X_n - X| \geq \epsilon) = 0 \\ \lim_{n \rarr \infty}P(|X_n - X| < \epsilon) = 1
    $$
    
    $$
    X_n \rarr^p X
    $$
    
- 약대수의 법칙(weak law of large numbers)
    
    $$
    \bar{X_n} = \frac{1}{n}\sum^n_{i=1}x_i \\ \lim_{n \rarr \infty}P(|\bar{X_n} - \mu| < \epsilon) = 1
    $$
    
- 거의 확실한 수렴(converges almost surely)
    
    $$
    P(\lim_{n \rarr \infty}|X_n - X| < \epsilon) = 1
    $$
    
- 강대수의 법칙(strong law of large numbers)
    
    $$
    \bar{X_n} = \frac{1}{n}\sum^n_{i=1}x_i \\ P(\lim_{n \rarr \infty}|\bar{X_n} - \mu| < \epsilon) = 1
    $$
    
- 분포 수렴(convergence in distribution)
    
    $$
    \lim_{n \rarr \infty}F_{x_{n}}(x) = F_X(x)
    $$
    

### 중심 극한 정리(central limit theorem)

- 확률 변수가 어떤 분포를 따르느냐에 상관없이 표본 평균은 평균이 $\mu$이고 분산이 $\sigma^2/n$인 정규 분포를 따르는 것
    
    $$
    \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \rarr^d N(0, 1)
    $$
    
    $$
    \bar{X} \rarr^d N(\mu, \frac{\sigma^2}{n})
    $$
    

### 델타 메소드(delta method)

- 슬러츠키 정리(Slutsky’s Theorem)
    
    $$
    Y_nX_n \rarr^d aX \\ X_n + Y_n \rarr^d X + a
    $$
    
- 테일러 정리(Taylor’s Theorem)
    
    $$
    \lim_{x \rarr a}h_k(x) = 0
    $$
    
- 델타 메소드
    
    $$
    \sqrt{n}(Y_n - \theta) \rarr^d N(0, \sigma^2)
    $$
    
    $$
    \sqrt{n}[g(Y_n) - g(\theta)] \rarr^d N(0, \sigma^2[g'(\theta)]^2)
    $$
    

# 5. 추정

## 1. MME

### 적률 추정량(Method of Moment Estimator, MME) 정의

- 적률 개념을 사용해서 추정하는 방법
- 확률 변수가 확률 밀도 함수의 표본이라고 했을 때 k차 표본 적률과 모적률 일치 → 모수 추정 가능
- 1차 표본 적률
    
    $$
    m_1 = \frac{1}{n}\sum^n_{i=1}X_i^1
    $$
    
- 2차 표본 적률
    
    $$
    m_2 = \frac{1}{n}\sum^n_{i=1}X_i^2
    $$
    
- k차 표본 적률
    
    $$
    m_k = \frac{1}{n}\sum^n_{i=1}X_i^k
    $$
    
- 1차 모젹률
    
    $$
    M_1 = E(X^1)
    $$
    
- 2차 모적률
    
    $$
    M_2 = E(X^2)
    $$
    
- k차 모적률
    
    $$
    M_k = E(X^k)
    $$
    
- 적률 추정법 : 표본 적률과 모적률을 일치시킴으로써 모수를 추정하는 방법
- 1차 적률 추정
    
    $$
    \frac{1}{n}\sum^n_{i=1}X_i^1 = m_1 =  M_1 = E(X^1)
    $$
    
- 2차 적률 추정
    
    $$
    \frac{1}{n}\sum^n_{i=1}X_i^2 = m_2 =  M_2 = E(X^2)
    $$
    
- k차 적률 추정
    
    $$
    \frac{1}{n}\sum^n_{i=1}X_i^k = m_k =  M_k = E(X^k)
    $$
    

## 2. MLE

### likelihood 정의

- MLE : Maximum Likelihood Estimation
- likelihood를 최대화하는 방법으로 추정
- 가능도, 우도

### probability vs likelihood

- 확률(probability) : 고정된 확률 분포에서 우리가 관심 있는 영역
- 가능도(likelihood) : 우리가 얻은 샘플은 고정되어 있는 상황에서 확률 분포를 정의하는 파라미터가 바뀔 때마다 측정하는 값

### 최대 가능도 추정량(Maximum Likelihood Estimation, MLE) 정의

- 주어진 샘플 데이터의 가능도를 이용해 모집단의 분포를 추정하는 것
- 가장 그럴듯한 추정
- 확률 변수의 확률 밀도 함수
    
    $$
    g(x_1, x_2, \cdots, x_n) = f(x_1|\theta)f(x_2|\theta)\cdots f(x_n|\theta) = \prod^n_{i=1}f(x_i|\theta)
    $$
    
- 가능도 함수(likelihood function) : 파라미터 $\theta$의 함수
    
    $$
    L(\theta|x) = \prod^n_{i=1}f(x_i|\theta)
    $$
    
    $$
    \hat{\theta} = \argmax_\theta L(\theta|x) = \argmax_\theta\prod^n_{i=1}f(x_i|\theta)
    $$
    
- 로그 가능도 함수
    
    $$
    l(\theta|x) = \log L(\theta|x) = \log(\prod^n_{i=1}f(x_i|\theta)) = \sum^n_{i=1}\log f(x_i|\theta)
    $$
    

## 3. MAP

### 최대 사후 추정(Maximum A Posteriori estimation, MAP)

- 사전 확률 밀도 함수(prior probability density function) : 사건이 발생하기 전 파라미터 $\theta$의 확률
    
    $$
    f(\theta, x) = f(x|\theta)f(\theta)
    $$
    
- 사후 확률 밀도 함수(posterior probability density function) : 표본이 주어질 때 파라미터가 얻어질 확률
    
    $$
    f(\theta|x) = \frac{f(x|\theta)f(\theta)}{\int f(x|\theta)f(\theta)d\theta}
    $$
    
    $$
    f(\theta|x) \propto f(x|\theta)f(\theta)
    $$
    
- 최대 사후 추정 : 사후 확률 밀도 함수를 최대화시키는 파라미터 $\theta$를 추정값으로 구하는 것
    
    $$
    \hat{\theta}_{MAP} = \argmax_\theta f(\theta|x) \propto \argmax_\theta f(x|\theta)f(\theta)
    $$
    

# 6. 확률 과정

## 1. 확률 과정

### 확률 과정(stochastic process) 정의

- 시간과 관련된 확률 변수의 집합
- 확률 과정을 구성하는 확률 변수 → 모두 시간 혹은 시점과 관련되어 있음

### 마팅게일(martingale)

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
    

## 2. 마르코프 체인

### 마르코프 체인(Markov chain) 정의

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

### one-step 전이 확률 행렬

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
    

### n-step 전이 확률 행렬

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
    

## 3. First Step Analysis

### 3 x 3 행렬의 First Step Analysis

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
        

### 4 x 4 행렬의 First Step Analysis

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
    

### n x n 행렬의 First Step Analysis

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
    

## 4. 랜덤 워크

### 랜덤 워크(random walk) 정의

- 임의의 상태 $i$에서 시작했을 때 다음 스텝에서 상태 $i$에 그대로 머물거나 혹은 이웃에 존재하는 상태 $i - 1$ 혹은 $i + 1$로 이동하는 마르코프 체인
- 0, $N$ → absorption
- 1 ~ $N - 1$ → transient

### 랜덤 워크의 전이 확률 행렬

$$
P = \begin{bmatrix} P_{00} & P_{01} & P_{02} & P_{03} & \cdots & P_{0N - 1} & P_{0N} \\ P_{10} & P_{11} & P_{12} & P_{13} & \cdots & P_{1N - 1} & P_{1N} \\ P_{20} & P_{21} & P_{22} & P_{23} & \cdots & P_{2N - 1} & P_{2N} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ P_{N - 1 0} & P_{N - 11} & P_{N - 12} & P_{N - 13} & \cdots & P_{N - 1N - 1} & P_{N - 1N} \\ P_{N0} & P_{N1} & P_{N2} & P_{N3} & \cdots & P_{NN - 1} & P_{NN} \end{bmatrix} \\ = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 & 0 \\ q_1 & r_1 & p_1 & 0 & \cdots & 0 & 0 \\ 0 & q_2 & r_2 & p_2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & r_{N - 1} & p_{N - 1} \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}
$$

$$
P(X_{n + 1} = i + 1|X_n = i) = p_i \\ P(X_{n + 1} = i - 1|X_n = i) = q_i \\ P(X_{n + 1} = i|X_n = i) = r_i
$$

### 랜덤 워크에서 파산 확률

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

### 파산할 때까지 걸리는 평균 시간

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

### 일반화 랜덤 워크의 파산 확률

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

### 일반화 랜덤 워크의 파산까지 걸리는 시간

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

## 5. 포아송 과정

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

## 6. 브라운 운동

### 브라운 운동(Brownian motion) 정의

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
    

### Geometric Brownian Motion(GBM)

$$
X(t) = xe^{drift+diffusion}t = xe^{(\mu - \frac{1}{2}\sigma^2)t+\sigma B(t)}
$$

# 7. 몬테카를로 시뮬레이션

## 1. 몬테카를로 시뮬레이션 기초

### 몬테카를로 시뮬레이션(Monte Carlo simulation) 정의

- 컴퓨터를 이용해 반복적인 랜덤 샘플링 방법
- 수리적 결과를 얻는 시뮬레이션 방법

### 몬테카를로 시뮬레이션으로 기댓값 추정

$$
E(X) = \mu
$$

$$
\hat{\mu} = \frac{1}{n}\sum^n_{i=1}X_i
$$

### 대수의 법칙

- 약대수의 법칙
    
    $$
    \lim_{n \rarr \infty}P(|\hat{\mu}_n - \mu| < \epsilon) = 1
    $$
    
- 강대수의 법칙
    
    $$
    P(\lim_{n \rarr \infty}|\hat{\mu}_n - \mu| < \epsilon) = 1
    $$
    
- 몬테카를로 시뮬레이션을 통해 모수 추정 → $n$이 커질수록 에러가 적어지고 정확해짐
- 확률 변수의 기댓값
    
    $$
    E(\hat{\mu}_n) = \mu
    $$
    
- 확률 변수의 분산
    
    $$
    Var(\hat{\mu}_n) = \frac{\sigma^2}{n}
    $$
    

### 몬테카를로 시뮬레이션으로 적분 값 구하기

- 일반 영역 적분
    
    $$
    \int^b_a f(x)dx
    $$
    
- 몬테카를로 시뮬레이션 적분 → 전체 영역을 일정 지점으로 분리 후 각 지점의 영역을 모두 더해 구함
    
    $$
    \int^b_a f(x)dx = \frac{1}{n}(b - a)\sum^n_{i=1}f(x_i)
    $$
    

## 2. uniform 난수 생성

### 유사 랜덤(pseudo random)

- 물리학적 랜덤 : 방사성 양자 방출을 통해 만드는 랜덤 숫자
- 프로그래밍을 통해 랜덤한 숫자 : 유사 랜덤, 랜덤처럼 보이는 숫자

### 랜덤 주기(random period)

- 유사 랜덤으로 만드는 숫자 → 랜덤 주기를 따름
    
    $$
    x_i = x_{i - P}
    $$
    
- 짧은 주기 → 랜덤 숫자의 랜덤성 감소
- 긴 주기 → 랜덤성 증가
- 주기 $P$에 대해 $\sqrt{P}$개 이하의 난수 생성 권장

### 랜덤 시드(random seed)

- 정수값으로 설정
- 동일한 랜덤 시드값은 동일한 난수 발생을 유도
- 유사 랜덤 함수의 상태를 결정하는 값

### 유사 랜덤 알고리즘

- Linear Congruential Generator(LCG)
    
    $$
    x_i = a_0 + a_1x_{i - 1} \ \text{mod} \ M
    $$
    
- Multiplicative Congruential Generator(MCG) : $a_0 = 0$인 경우
    
    $$
    x_i = a_1x_{i - 1} \ \text{mod} \ M
    $$
    
- Multiple Recursive Generator(MRG) : MCG를 일반적인 표현식으로 나타낸 것
    
    $$
    x_i = a_1x_{i - 1} + a_2x_{i - 2} + \cdots + a_kx_{i - k} \ \text{mod} \ M
    $$
    
- 랜덤 숫자가 가질 수 있는 값의 범위 : $x_i \in \{0, 1, \cdots, M - 1\}$
- 주기 : $P \leq M^k - 1$

### 균일 분포를 따르는 난수 생성

- 균일 분포 난수 생성
    
    $$
    x_i = a_1x_{i - 1} + 1 \ \text{mod} \ M
    $$
    
    $$
    x_i = (seed * x_{i - 1} + 1) \ \text{mod} \ (2^{31} - 1)
    $$
    
    $$
    u_i = \frac{x_i}{2^{31} - 1}
    $$
    

## 3. non-uniform 난수 생성

### 누적 분포 함수의 역함수

- 균일 분포 → 특이한 분포 : 누적 붆포 함수의 역함수를 이용하여 변경
    
    $$
    X \sim F^{-1}(U)
    $$
    
    $$
    P(X \leq x) = F(x) \\ U \sim U(0, 1), \quad X = F^{-1}(U) \Rightarrow X \sim F
    $$
    
- complementary unversion
    
    $$
    U \sim U(0, 1) \Rightarrow 1 - U \sim U(0, 1) \\ F^{-1}(1 - U) \sim F
    $$
    

### Acceptance-Rejection

- 분포 G를 따르는 난수 생성 → 일부 난수를 분포 F의 샘플로 채택하거나 버림
    
    $$
    f(x) \leq cg(x) \\ \frac{f(x)}{cg(x)} \leq 1
    $$
    
- $c$와 $g$ 설정
- 확률 밀도 함수 $g$를 따르는 샘플 $Y$ 생성
    
    $$
    Y \sim g
    $$
    
- $U(0, 1)$를 따르는 샘플 $U$ 생성
    
    $$
    U \sim U(0, 1)
    $$
    
- 다음 식 판정
    
    $$
    U \leq \frac{f(Y)}{cg(Y)}
    $$
    
    - 참인 경우 $X = Y$, $Y$를 샘플로 채택
    - 거짓인 경우 샘플 생성으로 돌아감, 새로운 후보 $Y$ 생성
- 원하는 샘플 수를 채울 때까지 반복

## 4. 마르코프 체인 몬테카를로

### 마르코프 체인 몬테카를로(Markov chain Monte Carlo, MCMC) 정의

- $x$ 분포를 마르코프 체인으로부터 샘플링한 것
- 메트로폴리스 알고리즘 사용
- $\mu$ 추정
    
    $$
    \mu = \int f(x)\pi(x)dx
    $$
    
    $$
    \hat{\mu} = \frac{1}{n}\sum^n_{i=1}f(x_i)
    $$
    

### 마르코프 체인 몬테카를로의 필요성

- 머신러닝 문제 해결 → 매우 복잡한 계산 과정 필요
- 적분 계산 → 0과 1 사이의 수를 곱함 → 0에 수렴 가능성 존재

### detailed balance

$$
\sum_{x \in \Omega} \pi(x)P(x \rarr y) = \pi(y) = \sum_{x \in \Omega}\pi(y)P(y \rarr x)
$$

$$
\sum_{x : x \neq y} \pi(x)P(x \rarr y) = \sum_{x : x \neq y} \pi(y)P(y \rarr x)
$$

$$
\pi(x)P(x \rarr y) = \pi(y)P(y \rarr x)
$$

- $x$와 $y$ 사이의 흐름이 방향에 상관없이 동일함

### 메트로폴리스 헤이스팅스(Metropolis-Hastings)

- acceptance-rejection 샘플링 방법의 연장선
- 직접적으로 표본을 얻기 어려운 확률 분포로부터 표본의 수열을 생성하는 데 사용하는 기각 표본 추출 알고리즘
- 함수의 입력값에 해당하는 초깃값 $x$, stationary 분포 $\pi$, 후보 분포 $Q$, 뽑고 싶은 샘플 수 $n$ 설정
- 후보 분포에서 하나의 샘플 추출
- 비율 계산
    
    $$
    R = \frac{\pi(y)Q(y \rarr x)}{\pi(x)Q(x \rarr y)}
    $$
    
- 0과 1 사이의 균일 분포에서 샘플 하나 추출 → accept 여부 판단
    
    $$
    U \sim U(0, 1)
    $$
    
- $U \leq R$이라면 $y$가 실제 분포를 따른다고 보고 $y$를 샘플로 채택
    
    $$
    X_{i + 1} = y
    $$
    
- $U > R$이라면 $y$가 실제 분포를 따른다고 보지 않고 이전 값 $x$를 채택
    
    $$
    X_{i + 1} = x
    $$
    
- $n$개의 샘플을 뽑을 때까지 반복