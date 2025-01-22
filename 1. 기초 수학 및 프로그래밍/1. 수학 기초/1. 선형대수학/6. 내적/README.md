# 1. 내적(inner product)

## 1. 내적 공간(inner product space)

- 벡터 공간에서 다음 공리를 만족하는 벡터 공간
    - $\langle u, v \rangle = \langle v, u \rangle$
    - $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$
    - $\langle au, v \rangle = a \langle u, v \rangle$
    - $\langle u, v \rangle \geq 0$

## 2. 내적 정의

- 벡터와 벡터의 연산 결과값 → 스칼라
- 각 벡터의 동일한 위치에 있는 원소를 서로 곱한 후 더함
    
    $$
    \lang u, v \rang  = u \cdot v = u_1v_1 + u_2v_2 + \cdots + u_nv_n \\ u = \begin{pmatrix}u_1 \\ u_2 \\ u_3\end{pmatrix}, \quad v = \begin{pmatrix}v_1 \\ v_2 \\ v_3\end{pmatrix} \\ \lang u, v \rang = u^Tv = \begin{pmatrix}u_1 & u_2 & u_3\end{pmatrix} \begin{pmatrix}v_1 \\ v_2 \\ v_3\end{pmatrix} = u_1v_1 + u_2v_2 + u_3v_3
    $$
    

## 3. 내적 성질

- 벡터의 길이(norm)을 구하거나 벡터 사이 관계 파악 가능
- 두 벡터 사이의 각도 추정 가능
    - 내적 > 0 → 두 벡터 사이 각도 < 90
    - 내적 < 0 → 두 벡터 사이 각도 > 90
    - 내적 = 0 → 두 벡터 사이 각도 = 90
- 벡터의 길이 파악 가능 → 벡터의 노름(norm)
    - 자기 자신의 내적 값의 제곱근 계산
    
    $$
    u = (u_1, u_2, \cdots, u_n) \\ ||u|| = \sqrt{u_1^2 + u_2^2 + \cdots + u_n^2}
    $$
    
- 벡터의 길이와 x축과의 각도를 알고 있을 때
    - 벡터 좌표 → 길이와 두 벡터 사이의 각도로 표현 가능
    - x좌표 → 코사인, y좌표 → 사인
    
    $$
    u = (u_1, u_2) \rarr u = (||u|| \cos \theta, ||v|| \sin \theta) \\ u \cdot v = ||u|| \ ||v|| \cos \theta \\ \cos \theta = \frac{u \cdot v}{||u|| \ ||v||}
    $$
    

## 4. 정사영(projection)

- 한 벡터 공간에 속한 벡터를 부분 공간으로 수직으로 투영하는 것
- 좌표계의 종류와 상관없이 내적 값을 항상 구할 수 있음
- 한 벡터에 대한 축을 지정하고 정사영 → 2가지 종류의 정사영이 나옴
    
    $$
    ||proj_vu|| = ||u|| \ |\cos \theta|
    $$
    
    $$
    \begin{aligned} \lang u, v\rang &= ||u|| \ ||v|| \cos \theta \\ &= (||v||) \times (||u|| \cos \theta) \\ &= (length \ of  \ vector \ v) \times (length \ of \ vector \ proj_v u)\end{aligned}
    $$
    

# 2. 직교 공간과 정규 직교 공간

## 1. 직교 공간(orthogonal space)

- 직교(orthogonal) : 두 직선 또는 두 평면이 직각을 이루며 만나는 것
- 정규 직교(orthonormal) : 각 벡터의 길이가 1이면서 직교하는 것

## 2. 정규 직교 공간(orthonormal space)

- 정규 직교 벡터(orthonormal vector) : 직교 공간에 존재하는 직교 벡터의 길이가 모두 1
- 정규 직교 공간(orthonormal space) : 정규 직교 벡터가 만드는 공간
- 정규화(normalization) : 직교 벡터를 정규 직교 벡터로 바꾸는 것, 해당 벡터의 길이로 나눔
    
    $$
    v = \frac{1}{||u||}u \\ ||v|| = ||\frac{1}{||u||}u|| = 1
    $$
    

## 3. 정규 직교 벡터를 활용한 좌표 표현

- 벡터 공간의 정규 직교 기저가 존재할 때 벡터 공간에 포함되는 임의의 벡터
    
    $$
    a = \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_n \rangle v_n
    $$
    
- 임의의 벡터 → 정규 기저 벡터의 조합
    
    $$
    a = c_1v_1 + c_2v_2 + \cdots + c_nv_n
    $$
    
    $$
    \begin{aligned} a &= \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_n \rangle v_n \\ &= c_1v_1 + c_2v_2 + \cdots + c_nv_n \end{aligned}
    $$
    
- 벡터와 기저 벡터 내적
    
    $$
    \begin{aligned} \langle a, v_i \rangle &= \langle c_1v_1 \rangle + \langle c_2v_2 \rangle + \cdots + \langle c_nv_n, v_i \rangle \\ &= \langle c_1v_1, v_i \rangle + \langle c_2v_2, v_i \rangle + \cdots + \langle c_nv_n, v_i \rangle \\ &= \langle c_iv_i, v_i \rangle \\ &= c_iv_i^Tv_i \\ &= c_i \end{aligned}
    $$
    
    $$
    \begin{aligned} a &= c_1v_1 + c_2v_2 + \cdots + c_nv_n \\ &= \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_n \rangle v_n \end{aligned}
    $$
    

## 4. 직교 벡터를 활용한 좌표 표현

- 벡터 공간 내 직교 기저 표현
    
    $$
    a = \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_n \rang}{||u_n||^2}u_n
    $$
    
- 직교 기저일 때 좌표 표현
    
    $$
    a = \left \{ \frac{\lang a, u_1 \rang}{||u_1||^2}u_1, \frac{\lang a, u_2 \rang}{||u_2||^2}u_2, \cdots, \frac{\lang a, u_n \rang}{||u_n||^2}u_n \right \}
    $$
    
- 직교 기저 → 정규 직교 기저 벡터
    
    $$
    u_1, u_2, \cdots, u_n \rarr \left \{ \frac{u_1}{||u_1||}, \frac{u_2}{||u_2||}, \cdots, \frac{u_n}{||u_n||} \right \}
    $$
    
- 정규 직교 벡터를 기준으로 변환
    
    $$
    \begin{aligned} a &= \lang a, \frac{u_1}{||u_1||} \rang \frac{u_1}{||u_1||} + \lang a, \frac{u_2}{||u_2||} \rang \frac{u_2}{||u_2||} + \cdots + \lang a, \frac{u_n}{||u_n||} \rang \frac{u_n}{||u_n||} \\ &= \lang a, u_1 \rang \frac{u_1}{||u_1||^2} + \lang a, u_2 \rang \frac{u_2}{||u_2||^2} + \cdots + \lang a, u_n \rang \frac{u_n}{||u_n||^2} \\ &= \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_n \rang}{||u_n||^2}u_n \end{aligned}
    $$
    
    $$
    a = \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_n \rang}{||u_n||^2}u_n
    $$
    

# 3. 그램 슈미트 과정

## 1. 정사영 정리(projection theorem)

- 벡터 공간의 부분 공간이 존재할 때 벡터 공간에 속하는 임의의 벡터는 다음과 같음
    
    $$
    a = w_1 + w_2
    $$
    
    - $w_1$ : 부분 공간에 속하는 벡터
    - $w_2$ : 부분 공간의 직교 공간에 속하는 벡터
    
    $$
    \begin{aligned} a &= w_1 + w_2 \\ &\Leftrightarrow w_2 = a - w_1 \\ &\Leftrightarrow a = Proj_wa + Proj_{w^{\bot}} a \\ &\Leftrightarrow Proj_{w^{\bot}} a = a - Proj_wa \\ &\Leftrightarrow a = Proj_wa + (a - Proj_wa) \end{aligned}
    $$
    

## 2. 직교 정사영

- 직교 + 정사영 개념
    
    $$
    Proj_wa = \frac{\lang a, u_1 \rang}{||u_1||^2}u_1 + \frac{\lang a, u_2 \rang}{||u_2||^2}u_2 + \cdots + \frac{\lang a, u_r \rang}{||u_r||^2}u_r
    $$
    
- 직교 벡터를 활용한 좌표 표현 방법
    
    $$
    \left \{ \frac{\lang a, u_1 \rang}{||u_1||^2}, \frac{\lang a, u_2 \rang}{||u_2||^2}, \cdots, \frac{\lang a, u_r \rang}{||u_r||^2} \right \}
    $$
    
- 전체 벡터 공간의 임의의 벡터 → 정사영시킨 벡터
    
    $$
    Proj_wa = \langle a, v_1 \rangle v_1 + \langle a, v_2 \rangle v_2 + \cdots + \langle a, v_r \rangle v_r
    $$
    

## 3. 그램 슈미트 과정(Gram-Schmidt Process)

- 기저 벡터를 직교 기저 벡터로 변환하는 과정
- 새로운 직교 기저 벡터 정의
    
    $$
    u_1 = s_1
    $$
    
- 직교 기저 벡터 → 직교인 벡터 생성
    
    $$
    u_2 = s_2 - \frac{\lang s_2, u_1 \rang}{||u_1||^2}u_1
    $$
    
- 생성할 기저 벡터가 앞에서 생성한 벡터들과 직교함
    
    $$
    u_3 = s_3 - \frac{\lang s_3, u_1 \rang}{||u_1||^2}u_1 - \frac{\lang s_3, u_2 \rang}{||u_2||^2}u_2
    $$
    
- 나머지 직교 기저 벡터
    
    $$
    u_n = s_n - \frac{\lang s_n, u_1 \rang}{||u_1||^2}u_1 - \frac{\lang s_3, u_2 \rang}{||u_2||^2}u_2 - \cdots - \frac{\lang s_n, u_{n-1} \rang}{||u_{n-1}||^2}u_{n-1}
    $$
    

# 4. QR 분해

## 1. 기본적인 QR 분해 방법

- 행렬이 풀 랭크 → 열 벡터는 모두 선형 독립
    
    $$
    A = QR
    $$
    
    - $Q$ : $n \times p$ 행렬, 정규 직교 벡터
    - $R$ : 가역 상 삼각 행렬
- 열 벡터의 표현식
    
    $$
    a_1 = \langle a_1, v_1 \rangle v_1 + \langle a_1, v_2 \rangle v_2 + \cdots + \langle a_1, v_n \rangle v_n \\ a_2 = \langle a_2, v_1 \rangle v_1 + \langle a_2, v_2 \rangle v_2 + \cdots + \langle a_2, v_n \rangle v_n \\ \vdots \\ a_n = \langle a_n, v_1 \rangle v_1 + \langle a_n, v_2 \rangle v_2 + \cdots + \langle a_n, v_n \rangle v_n
    $$
    
    $$
    \begin{pmatrix}a_1 & a_2 & \cdots & a_n \end{pmatrix} \begin{pmatrix}v_1 & v_2 & \cdots & v_n \end{pmatrix} = \begin{pmatrix} \lang a_1, v_1 \rang & \lang a_2, v_1 \rang & \cdots & \lang a_n, v_1 \rang \\ \lang a_1, v_2 \rang & \lang a_2, v_2 \rang & \cdots & \lang a_n, v_2 \rang \\ \vdots & \vdots & \ddots & \vdots \\ \lang a_1, v_n \rang & \lang a_2, v_n \rang & \cdots & \lang a_n, v_n \rang \end{pmatrix}
    $$
    
- QR 분해
    
    $$
    A = QR \\ Q = \begin{pmatrix}v_1 & v_2 & \cdots & v_n \end{pmatrix} \\ R = \begin{pmatrix} \lang a_1, v_1 \rang & \lang a_2, v_1 \rang & \cdots & \lang a_n, v_1 \rang \\ 0 & \lang a_2, v_2 \rang & \cdots & \lang a_n, v_2 \rang \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lang a_n, v_n \rang \end{pmatrix}
    $$
    

## 2. 그램 슈미트 과정을 이용한 QR 분해

- 직교 기저 벡터 구하기
- 기존 직교 기저 벡터가 아닌 다른 직교 기저 벡터 구하기
- 다음 차례의 직교 기저 벡터 구하기
- 앞서 구한 직교 벡터 → 정규 직교 벡터로 변환
- Q 행렬 구하기 → R 행렬 구하기

## 3. 하우스홀더 방법을 이용한 QR 분해

- 행렬의 1열을 기준으로 벡터 노름 구하기
- 위에서 구한 벡터로 하우스홀더 행렬 구하기
- 하우스홀더 행렬과 기본 행렬 곱하기
- 앞서 구한 행렬의 1열, 1행을 없애고 새로운 행렬 생성하기
- 위 단계를 반복하면서 하우스홀더 행렬들을 구하고 이를 바탕으로 QR 행렬 구하기