# 1. MME

## 1. 적률 추정량(Method of Moment Estimator, MME) 정의

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
    

# 2. MLE

## 1. likelihood 정의

- MLE : Maximum Likelihood Estimation
- likelihood를 최대화하는 방법으로 추정
- 가능도, 우도

## 2. probability vs likelihood

- 확률(probability) : 고정된 확률 분포에서 우리가 관심 있는 영역
- 가능도(likelihood) : 우리가 얻은 샘플은 고정되어 있는 상황에서 확률 분포를 정의하는 파라미터가 바뀔 때마다 측정하는 값

## 3. 최대 가능도 추정량(Maximum Likelihood Estimation, MLE) 정의

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
    

# 3. MAP

## 1. 최대 사후 추정(Maximum A Posteriori estimation, MAP)

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