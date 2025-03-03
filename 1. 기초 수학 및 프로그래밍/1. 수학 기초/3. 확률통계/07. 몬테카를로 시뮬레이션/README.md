# 1. 몬테카를로 시뮬레이션 기초

## 1. 몬테카를로 시뮬레이션(Monte Carlo simulation) 정의

- 컴퓨터를 이용해 반복적인 랜덤 샘플링 방법
- 수리적 결과를 얻는 시뮬레이션 방법

## 2. 몬테카를로 시뮬레이션으로 기댓값 추정

$$
E(X) = \mu
$$

$$
\hat{\mu} = \frac{1}{n}\sum^n_{i=1}X_i
$$

## 3. 대수의 법칙

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
    

## 4. 몬테카를로 시뮬레이션으로 적분 값 구하기

- 일반 영역 적분
    
    $$
    \int^b_a f(x)dx
    $$
    
- 몬테카를로 시뮬레이션 적분 → 전체 영역을 일정 지점으로 분리 후 각 지점의 영역을 모두 더해 구함
    
    $$
    \int^b_a f(x)dx = \frac{1}{n}(b - a)\sum^n_{i=1}f(x_i)
    $$
    

# 2. uniform 난수 생성

## 1. 유사 랜덤(pseudo random)

- 물리학적 랜덤 : 방사성 양자 방출을 통해 만드는 랜덤 숫자
- 프로그래밍을 통해 랜덤한 숫자 : 유사 랜덤, 랜덤처럼 보이는 숫자

## 2. 랜덤 주기(random period)

- 유사 랜덤으로 만드는 숫자 → 랜덤 주기를 따름
    
    $$
    x_i = x_{i - P}
    $$
    
- 짧은 주기 → 랜덤 숫자의 랜덤성 감소
- 긴 주기 → 랜덤성 증가
- 주기 $P$에 대해 $\sqrt{P}$개 이하의 난수 생성 권장

## 3. 랜덤 시드(random seed)

- 정수값으로 설정
- 동일한 랜덤 시드값은 동일한 난수 발생을 유도
- 유사 랜덤 함수의 상태를 결정하는 값

## 4. 유사 랜덤 알고리즘

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

## 5. 균일 분포를 따르는 난수 생성

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
    

# 3. non-uniform 난수 생성

## 1. 누적 분포 함수의 역함수

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
    

## 2. Acceptance-Rejection

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

# 4. 누적 분포 함수를 이용한 이산형 난수 생성

- 베르누이 분포를 따르는 난수 생성
- 이항 분포를 따르는 난수 생성
- 포아송 분포를 따르는 난수 생성
- 음이항 분포를 따르는 난수 생성