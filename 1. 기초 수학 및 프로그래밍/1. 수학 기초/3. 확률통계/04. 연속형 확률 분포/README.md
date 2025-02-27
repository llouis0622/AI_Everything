# 1. 연속형 균일 분포

## 1. 연속형 균일 분포(continuous uniform distribution) 정의

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
    

## 2. 연속형 균일 분포의 기댓값

$$
E(X) = \frac{b + a}{2}
$$

## 3. 연속형 균일 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \frac{a^2 + ab + b^2}{3}
$$

$$
Var(X) = \frac{(b - a)^2}{12}
$$

# 2. 정규 분포

## 1. 정규 분포(normal distribution) 정의

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

## 2. 표준 정규 분포(standard normal distribution) 정의

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
    

## 3. 정규 근사(normal approximation)

- 주어진 데이터가 정규 분포를 따르지 않더라도, 데이터의 개수 n이 커지면 정규 분포에 가까워지는 현상
- 이항 분포의 정규 근사
    
    $$
    X \sim Binomial(n, p) \\ X \sim N(np, np(1 - p)) \quad as \ n \rarr \infty
    $$
    
- 포아송 분포의 정규 근사
    
    $$
    X \sim Poisson(n, p) \\ X \sim N(\lambda, \lambda) \quad as \ \lambda \rarr \infty
    $$
    

# 3. 감마 분포

## 1. 감마 함수(gamma function)

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

## 2. 감마 분포(gamma distribution) 정의

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
    

## 3. 감마 분포의 적률 생성 함수

$$
M_X(t) = (1 - \beta t)^{-\alpha}
$$

## 4. 감마 분포의 기댓값

$$
E(X) = \alpha\beta
$$

## 5. 감마 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = \alpha^2\beta^2 + \alpha\beta^2
$$

$$
Var(X) = \alpha\beta^2
$$

# 4. 지수 분포

## 1. 지수 분포(exponential distribution) 정의

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
    

## 2. 지수 분포의 무기억성

- 만약 확률 변수가 지수 분포를 따름 → 확률 변수는 무기억성을 따름
    
    $$
    X \sim Exp(\beta) \\ P(X > s + t|X > t) = P(X > s), \quad for \ all \ s, t > 0 \\ P(X > s + t) = P(X > s)P(X > t), \quad for \ all \ s, t > 0
    $$
    
- 만약 확률 변수가 연속형 확률 변수이고 무기억성을 가짐 → 확률 변수는 지수 분포를 따름

## 3. 지수 분포의 적률 생성 함수

$$
M_X(t) = (1 - \beta t)^{-1}
$$

## 4. 지수 분포의 기댓값

$$
E(X) = \beta
$$

## 5. 지수 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X^2) = 2\beta^2
$$

$$
Var(X) = \beta^2
$$

# 5. 카이제곱 분포(chi-square distribution)

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
    

# 6. 베타 분포

## 1. 베타 함수(beta function)

- 이항 계수를 실수 범위로 확장한 것
    
    $$
    \Beta(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}
    $$
    
    $$
    \Beta(\alpha, \beta) = \int^1_0x^{\alpha - 1}(1 - x)^{\beta - 1}dx
    $$
    

## 2. 베타 분포(beta distribution) 정의

$$
X \sim Beta(\alpha, \beta) \\ f_X(x) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}x^{\alpha - 1}(1 - x)^{\beta - 1}dx, \quad 0 < x < 1, \quad \alpha > 0, \quad \beta > 0
$$

$$
E(X) = \frac{\alpha}{\alpha + \beta}
$$

$$
Var(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
$$

## 3. 베타 분포의 기댓값

$$
E(X) = \frac{\alpha}{\alpha + \beta}
$$

## 4. 베타 분포의 분산

$$
Var(X) = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

$$
E(X) = \frac{(\alpha + 1)\alpha}{(\alpha + \beta)(\alpha + \beta + 1)}
$$

$$
Var(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
$$

# 7. 확률 분포와 관련된 이론

## 1. 확률 변수의 변환

$$
g(X) : X \rarr Y
$$

$$
P(Y \in A) = P(X \in g^{-1}(A))
$$

$$
f_Y(y) = \frac{1}{\Gamma(\alpha)\beta^\alpha}(\frac{1}{y})^{\alpha + 1}e^{-\frac{1}{\beta y}}
$$

## 2. 확률 수렴(convergence in probability)

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
    

## 3. 중심 극한 정리(central limit theorem)

- 확률 변수가 어떤 분포를 따르느냐에 상관없이 표본 평균은 평균이 $\mu$이고 분산이 $\sigma^2/n$인 정규 분포를 따르는 것
    
    $$
    \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \rarr^d N(0, 1)
    $$
    
    $$
    \bar{X} \rarr^d N(\mu, \frac{\sigma^2}{n})
    $$
    

## 4. 델타 메소드(delta method)

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