# 1. 확률의 기초

## 1. 확률을 배우는 이유

- 무작위로 일어나는 사건들을 이해하고 해석하기 위함
- 사건이 발생할 수 있는 확률을 기반으로 어떤 일을 계획하거나 결정 가능

## 2. 확률(probability) 정의

- 표본 공간(sample space) : 발생 가능한 모든 결과의 집합, $\Omega$
- 사건(event) : 표본 공간의 부분 집합, 표본 공간을 구성하는 집합의 일부분
- 확률 : 어떤 사건이 발생할 가능성을 0과 1 사이의 숫자로 수치화시킨 것
    
    $$
    P(A) = \frac{\text{사건 A의 결과 개수}}{\text{발생 가능한 모든 경우의 개수}}
    $$
    
- 모든 확률이 0과 1 사이에 존재함 → 확률은 0보다 작은 값이 나올 수 없음
- 발생 가능한 모든 사건의 확률의 합은 1
- 동시에 발생할 수 없는 사건들에 대해 각 사건의 합의 확률은 개별 확률이 일어난 확률의 합과 같음

## 3. 확률의 종류

- 이론적 확률(theoretical probability)
    - 이론에 기반한 확률
    - 아직 발생하지 않은 미래에 초점을 맞추는 방법
- 경험적 확률(empirical probability)
    - 과거의 경험에 기반한 확률
    - 과거에 얻은 데이터를 기반으로 함

## 4. 독립(independent)

- 각각의 두 사건이 발생할 확률을 곱한 결과가 두 사건이 동시에 발생할 확률과 동일
    
    $$
    P(A \cap B) = P(A)P(B)
    $$
    

## 5. 배반(disjoint)

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
    

# 2. 확률 변수(random variable)

## 1. 확률 변수 정의

- 확률 현상을 통해 값이 확률적으로 정해지는 변수
- 확률 현상 : 발생 가능한 결과들은 알지만 가능한 결과들 중 어떤 결과가 나올지는 모르는 현상
- 확률 변수 : 변수인데 확률 현상을 통해 확률적으로 변하는 수
    
    $$
    P(X = x) \quad or \quad P_x(X)
    $$
    
- 이산형 확률 변수 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 있는 것
- 연속형 확률 변수 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 없는 것

## 2. 모집단(population)과 표본(sample)

- 모집단 : 관심 있는 대상이 되는 모든 측정값의 집합
- 표본 : 모집단에서 추출한 측정값의 집합
- 모수(population parameter) : 모집단의 분포 특성을 규정 짓는 척도, 관심의 대상이 되는 모집단의 대푯값
- 표본 통계량(sample statistic) : 표본의 대푯값

## 3. 히스토그램(histogram)

- 표 형태로 되어 있는 빈도표(frequency table)를 그래프 형태로 나타낸 것

# 3. 확률 분포

## 1. 확률 분포(probability distribution) 정의

- 확률 변수가 특정 값을 가질 확률을 나타내는 함수
- 확률 변수와 특정 값을 매핑시켜 주는 함수
- 이산형 확률 분포 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 있는 것
- 연속형 확률 분포 : 확률 변수가 가질 수 있는 값의 종류를 셀 수 없는 것

## 2. 이산형 확률 분포

- 확률 질량 함수(probability mass function , pmf) : 이산형 확률 변수가 특정 값을 가질 확률
    - $P_x(X) \geq 0$
    - $\Sigma_xP_x(X) = 1$
- 누적 분포 함수(cummulative distribution function, cdf) : 확률 변수가 취할 수 있는 값들을 누적해서 구하는 확률 분포
    - $F_x(-\infty) = 0$
    - $F_x(+\infty) = 1$
    - $x \leq y \Rightarrow F_x(X) \leq F_x(Y)$
    - $\lim_{y \rarr x, y > x}F_x(Y) = F(X)$

## 3. 연속형 확률 분포

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
    

## 4. 확률 질량과 확률 밀도의 차이

- 확률 질량(probability mass) : 각 이산형 확률 변수가 가지는 확률의 양
- 확률 밀도(probability density) : 단위 길이 당 질량

## 5. 독립 항등 분포(independent and identically distributed, iid)

- 확률 변수가 서로 독립이고 동일한 분포를 따르는 것

# 4. 평균과 기댓값

## 1. 평균(mean)과 기댓값(expected value) 정의

- 평균
    - 데이터의 중심을 나타낼 때 사용
    - 표본 데이터가 실제로 주어졌을 때, 데이터의 평균을 직접 계산하는 것
- 기댓값
    - 확률 분포의 평균을 계산하는 것
    - 데이터가 주어지기 전에 계산하는 것
- 모평균 : 모집단의 평균, $\mu$
- 표뵨 평균 : 표본의 평균, $\bar{x}$

## 2. 이산형 확률 변수의 기댓값

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
    

## 3. 연속형 확률 변수의 기댓값

$$
E(X) = \int^b_a xf_X(x)dx
$$

## 4. 기댓값의 성질

- $E(a) = a$
- $E(aX) = aE(X)$
- $E(X + Y) = E(X) + E(Y)$
- $E(X - Y) = E(X) - E(Y)$
- $E(aX + bY) = aE(X) + bE(Y)$
- $E(aX - bY) = aE(X) - bE(Y)$

## 5. 표본 평균의 개념

- 표본 평균 : 모평균의 추정치로 사용 가능
    
    $$
    \hat{\mu} = \frac{1}{n}\sum^n_{i=1}x_i = \bar{x}
    $$
    
- 표본 평균이 확률 변수임 → 고정된 값이 아님, 평균과 분산을 가짐

## 6. 표본 평균의 성질

- 표본 평균의 기댓값 = 모평균
    
    $$
    E(\bar{X}) = \mu
    $$
    
- iid를 만족하는 표본 평균의 분산
    
    $$
    Var(\bar{X}) = \frac{\sigma^2}{n}
    $$
    

# 5. 분산

## 1. 분산(variance) 정의

- 분포가 중심으로부터 얼마나 흩어져 있는지 알 수 있음
    
    $$
    Var(X) = E[(X - \mu)^2]
    $$
    
- 표준 편차(standard deviation) : 분산의 양의 제곱근
    
    $$
    \sqrt{E[(X - \mu)^2]}
    $$
    

## 2. 이산형 확률 변수의 분산

$$
\sigma^2 = Var(X) = E[(X - \mu)^2] = \sum^\infty_{i=1}(x_i - \mu)^2P(X = x_i)
$$

$$
\sigma = \sqrt{Var(X)}
$$

## 3. 연속형 확률 변수의 분산

$$
\sigma^2 = Var(X) = E[(X - \mu)^2] = \int^b_a (x-\mu)^2f_X(x)dx
$$

$$
\sigma = \sqrt{Var(X)}
$$

## 4. 분산의 성질

- $Var(X) = \sigma^2 = Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2 = E(X^2) - \mu^2$
- $Var(aX + b) = a^2Var(X)$
- $Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)$
- $Var(X - Y) = Var(X) + Var(Y) - 2Cov(X, Y)$
- $Var(aX + bY) = a^2Var(X) + b^2Var(Y) + 2abCov(X, Y)$

## 5. 표본 분산 정의

- 모분산의 추정치로 사용 가능
- 모분산의 추정치 : $\widehat{\sigma^2}$
- 표분 분산 : $s^2$
    
    $$
    s^2 = \frac{1}{n - 1}\sum^n_{i=1}(x_i - \bar{x})^2
    $$
    

## 6. 표본 분산의 성질

$$
E(s^2) = \sigma^2
$$

## 7. 자유도(degree of freedom)

- 자유로운 데이터의 개수

# 6. 공분산과 상관관계

## 1. 공분산(covariance) 정의

- 두 확률 변수의 상관 관계를 나타내는 값
- 두 개의 확률 변수 중 하나의 값이 상승할 때 다른 값도 상승 → 공분산 양수
- 두 개의 확률 변수 중 하나의 값이 상승할 때 다른 값은 하락 → 공분산 음수
    
    $$
    Cov(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = \frac{1}{n - 1}\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})
    $$
    
    $$
    Cov(X, Y) = E(XY) - E(X)E(Y)
    $$
    

## 2. 공분산의 성질

- $Cov(X, X) = Var(X)$
- $Cov(X, Y) = Cov(Y, X)$
- $Cov(aX, bY) = abCov(X, Y)$
- $Cov(X + Y, Z) = Cov(X, Z) + Cov(Y, Z)$

## 3. 상관 계수 정의

- 상관 계수 : 공분산을 각 변수의 표준 편차로 나눈것
- 모집단 상관 계수(population coefficient of correlation)
    
    $$
    Corr(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}
    $$
    
- 표본 상관 계수(sample coefficient of correlation)
    
    $$
    r_{xy} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2(y_i - \bar{y})^2}}
    $$
    

# 7. 조건부 확률

## 1. 조건부 확률(conditional probability)

- 주어진 사건이 발생한다는 가정하에 다른 한 사건이 발생할 확률
    
    $$
    P(A|B) = \frac{P(A\cap B)}{P(B)}
    $$
    
    $$
    P(A\cap B) = P(A|B)P(B)
    $$
    

## 2. 조건부 독립(conditional independence)

- 사건 A, B, C가 존재할 때, 다음 식을 만족하는 사건 C가 주어지면 사건 A, B는 조건부 독립임
    
    $$
    P(A|B, C) = P(A|C)
    $$
    
    $$
    P(A, B|C) = P(A|C)P(B|C)
    $$
    

## 3. 전확률 공식(law of total probability)

- 표본 공간을 서로 배반인 부분 공간으로 나누었을 때, 한 사건이 발생할 확률은 부분 공간에 대한 조건부 확률의 합 형태로 나타낼 수 있음
    
    $$
    P(A) = P(A|B)P(B) + P(A|B^C)P(B^C)
    $$
    

## 4. 전평균 공식(law of total expectation)

- 표본 공간을 서로 배반인 부분 공간으로 나누었을 때, 한 확률 변수의 기댓값은 서로 배반인 부분 공간의 조건부 기댓값의 합 형태로 나타낼 수 있음
    
    $$
    E_Y(E_X(X|Y)) = E(X)
    $$
    

## 5. 베이즈 정리

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
    

# 8. 적률 생성 함수(moment generation function, mgf)

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