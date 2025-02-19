# 1. 경우의 수

## 1. 팩토리얼(factorial)

- 1부터 N까지의 모든 자연수의 곱
- $!$

## 2. 조합(combination)

- 서로 다른 N개의 원소를 가지는 어떤 집합에서 순서에 상관없이 x개의 원소를 선택할 수 있는 가짓수
    
    $$
    \binom{n}{x} = \frac{n!}{x!(n-x)!}
    $$
    

# 2. 함수

## 1. 함수(function) 정의

- 어떤 집합의 각 원소를 다른 집합의 유일한 원소에 대응시키는 것
- 대응 : 서로 다른 집합의 원소끼리 짝지어주는 것
    
    $$
    f : X \rarr Y
    $$
    
    $$
    y = f(x)
    $$
    

## 2. 단조 함수(monotone function)

- 단조 증가 함수와 단조 감소 함수를 포함하는 함수
- 단조 증가 함수 : 주어진 구간에서 감소하는 구간이 없는 함수, $x_1 \leq  x_2 \rarr f(x_1) \leq f(x_2)$
- 단조 감소 함수 : 주어진 구간에서 증가하는 구간이 없는 함수, $x_1 \leq  x_2 \rarr f(x_1) \geq f(x_2)$

# 3. 수열

## 1. 수열(sequence) 정의

- 차례대로 나열된 수의 열
    
    $$
    a_1, a_2, a_3, \cdots, a_n
    $$
    

## 2. 등차수열(arithmetic sequence)

- 첫째 항부터 차례대로 특정 수를 더해서 만든 수열
- 공차(common difference) : 더하는 특정 수
    
    $$
    a_n = a_1 + (n - 1)d
    $$
    

## 3. 등비수열(geometric sequence)

- 첫째 항부터 차례대로 일정한 수를 곱해 만든 수열
- 공비(common ratio) : 곱하는 일정한 수
    
    $$
    a_n = ar^{n-1}
    $$
    
    $$
    S_n = \frac{a_1(1-r^n)}{1 - r}
    $$
    

## 4. 무한급수(infinite series)

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