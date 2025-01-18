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