# 1. 선형 방정식(linear equation)

## 1. 선형 방정식 정의

- 방정식 : 변수가 포함된 식에서 해당 변수가 특정 값만 가질 때만 성립하는 등식
- 선형 방정식 : 변수가 모두 일차항으로 이루어진 방정식
    
    $$
    a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
    $$
    

## 2. 선형 방정식 예

- 그래프의 각 축 : 선형 방정식의 변수
    
    $$
    2x + 4y = 8 \\ -6y + 3z = 12 \\ 2x + 3y + 4z = 5
    $$
    

## 3. 선형 방정식이 아닌 경우

- 변수가 삼각 함수, 지수 함수인 경우
- 변수끼리의 곱이나 제곱근인 경우
    
    $$
    y = \cos x \\ 1 = 2^x + y \\ x + \sqrt{y} = 2 \\ x + y + 2z + yz = 3
    $$
    

# 2. 선형 시스템(linear system)

## 1. 선형 시스템 정의

- 선형 방정식의 집합
- 연립 1차 방정식
- 선형 시스템을 만족시키는 해 : 선형 방정식의 집합이 그래프 상에서 만나는 지점
- 선형 시스템에서 발생 가능한 상화
    - 오직 하나의 해 : 두 직선이 오직 한 점에서만 만나는 경우
    - 무한개의 해 : 두 직선이 일치하는 경우
    - 해가 존재하지 않음 : 두 직선이 평행하는 경우
- 첨가 행렬(argumented matrix) : 선형 시스템의 상수 부분만 모아서 행렬 형태로 나타낸 것
    
    $$
    a_{11}x_1 + a_{12}x_2 + \cdots + a_{1p}x_p = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2p}x_p = b_2 \\ \vdots \\ a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{np}x_p = b_n
    $$
    
    $$
    \begin{pmatrix}a_{11} & a_{12} & \cdots & a_{1p} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2p} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{np} & b_n \end{pmatrix} \\ \begin{pmatrix}a_{11} & a_{12} & \cdots & a_{1p} \\ a_{21} & a_{22} & \cdots & a_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{np} \end{pmatrix} \begin{pmatrix}b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}
    $$
    

## 2. 기본 행 연산(elementary row operation)

- 한 행에 0이 아닌 상수를 모두 곱함
- 두 행을 교환함
- 한 행의 배수를 다른 행에 더함
    
    $$
    \begin{pmatrix}1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 0 & 1 & 2 & 1 \\ 3 & 2 & 0 & 1\end{pmatrix} \begin{pmatrix}1 \\ 2 \\ 3 \\ 4\end{pmatrix} \\ \begin{pmatrix}1 & 2 & 3 & 4 \\ 6 & 9 & 12 & 15 \\ 0 & 1 & 2 & 1 \\ 3 & 2 & 0 & 1\end{pmatrix} \begin{pmatrix}1 \\ 6 \\ 3 \\ 4\end{pmatrix} \\ \begin{pmatrix}1 & 2 & 3 & 4 \\ 6 & 9 & 12 & 15 \\ 0 & 1 & 2 & 1 \\ 3 & 2 & 0 & 1\end{pmatrix} \begin{pmatrix}1 \\ 6 \\ 3 \\ 4\end{pmatrix} \rarr \begin{pmatrix}6 & 9 & 12 & 15 \\ 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 1 \\ 3 & 2 & 0 & 1\end{pmatrix} \begin{pmatrix}6 \\ 1 \\ 3 \\ 4\end{pmatrix} \\ \begin{pmatrix}6 & 9 & 12 & 15 \\ 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 1 \\ 0 & -4 & -9 & -11\end{pmatrix} \begin{pmatrix}6 \\ 1 \\ 3 \\ 1\end{pmatrix}
    $$
    

## 3. 가우스 조르단 소거법(Gauss Jordan elimination)

- 가우스 행렬(Gauss matrix) : 각 행의 가장 첫 원소는 1이고 1 아래의 위치하는 원소는 모두 0인 행렬
- 행렬 구성 원소가 사다리꼴 형태로 남은 것
    
    $$
    \begin{pmatrix}1 & 2 & -1 & 2 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0\end{pmatrix}
    $$
    
- 기약 가우스 행렬(reduced Gauss matrix) : 가장 첫 원소가 1인 열에 대해 1을 제외한 나머지 행 원소가 모두 0인 형태
    
    $$
    \begin{pmatrix}1 & 0 & -1 & 2 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0\end{pmatrix}
    $$
    
- 가우스 조르단 소거법 : 기약 가우스 행렬 형태를 이용해 방정식의 해를 구하는 방법
    - 선형 시스템의 첨가 행렬 구하기
    - 기본 행 연산 결과를 첨가 행렬에 적용
    - 첨가 행렬이 기약 가우스 행렬 형태가 되면 종료
    - 첨가 행렬을 선형 시스템으로 표현
    
    $$
    \begin{pmatrix}3 & 1 & 2 \\ 2 & 6 & -1 \\ 4 & 0 & -1\end{pmatrix} \begin{pmatrix}5 \\ 1 \\ 3\end{pmatrix} \\ \begin{pmatrix}1 & 1/3 & 2/3 \\ 2 & 6 & -1 \\ 4 & 0 & -1\end{pmatrix} \begin{pmatrix}5/3 \\ 1 \\ 3\end{pmatrix} \\ \begin{pmatrix}1 & 1/3 & 2/3 \\ 0 & 16/3 & -7/3 \\ 4 & 0 & -1\end{pmatrix} \begin{pmatrix}5/3 \\ -7/3 \\ 3\end{pmatrix} \\ \begin{pmatrix}1 & \frac{1}{3} & \frac{2}{3} \\ 0 & \frac{16}{3} & -\frac{7}{3} \\ 0 & -\frac{4}{3} & -\frac{11}{3}\end{pmatrix} \begin{pmatrix}\frac{5}{3} \\ -\frac{7}{3} \\ -\frac{11}{3}\end{pmatrix} \\ \begin{pmatrix}1 & \frac{1}{3} & \frac{2}{3} \\ 0 & 1 & -\frac{7}{16} \\ 0 & -\frac{4}{3} & -\frac{11}{3}\end{pmatrix} \begin{pmatrix}\frac{5}{3} \\ -\frac{7}{16} \\ -\frac{11}{3}\end{pmatrix} \\ \begin{pmatrix}1 & \frac{1}{3} & \frac{2}{3} \\ 0 & 1 & -\frac{7}{16} \\ 0 & -4 & -11\end{pmatrix} \begin{pmatrix}\frac{5}{3} \\ -\frac{7}{16} \\ -11\end{pmatrix} \\ \begin{pmatrix}1 & \frac{1}{3} & \frac{2}{3} \\ 0 & 1 & -\frac{7}{16} \\ 0 & 0 & -\frac{51}{4}\end{pmatrix} \begin{pmatrix}\frac{5}{3} \\ -\frac{7}{16} \\ -\frac{51}{4}\end{pmatrix} \\ \begin{pmatrix}1 & \frac{1}{3} & \frac{2}{3} \\ 0 & 1 & -\frac{7}{16} \\ 0 & 0 & 1\end{pmatrix} \begin{pmatrix}\frac{5}{3} \\ -\frac{7}{16} \\ 1\end{pmatrix} \\ \begin{pmatrix}1 & 0 & \frac{39}{48} \\ 0 & 1 & -\frac{7}{16} \\ 0 & 0 & 1\end{pmatrix} \begin{pmatrix}\frac{87}{48} \\ -\frac{7}{16} \\ 1\end{pmatrix} \\ \begin{pmatrix}1 & 0 & \frac{39}{48} \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} \begin{pmatrix}\frac{87}{48} \\ 0 \\ 1\end{pmatrix} \\ \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} \begin{pmatrix}1 \\ 0 \\ 1\end{pmatrix}
    $$
    

## 4. 가우스 소거법(Gaussian elimination)

- 선형 시스템의 첨가 행렬을 가우스 행렬로 변환한 후 해를 구하는 방법
    - 선형 시스템의 첨가 행렬 구하기
    - 첨가 행렬을 가우스 행렬로 변환
    - 첨가 행렬을 선형 시스템으로 표현
    
    $$
    \begin{pmatrix}1 & 1 & 2 \\ -1 & -2 & 3 \\ 3 & -7 & 4\end{pmatrix} \begin{pmatrix}8 \\ 1 \\ 10\end{pmatrix} \\ \begin{pmatrix}1 & 1 & 2 \\ 0 & -1 & 5 \\ 3 & -7 & 4\end{pmatrix} \begin{pmatrix}8 \\ 9 \\ 10\end{pmatrix} \\ \begin{pmatrix}1 & 1 & 2 \\ 0 & -1 & 5 \\ 0 & -10 & -2\end{pmatrix} \begin{pmatrix}8 \\ 9 \\ -14\end{pmatrix} \\ \begin{pmatrix}1 & 1 & 2 \\ 0 & 1 & -5 \\ 0 & -10 & -2\end{pmatrix} \begin{pmatrix}8 \\ -9 \\ -14\end{pmatrix} \\ \begin{pmatrix}1 & 1 & 2 \\ 0 & 1 & -5 \\ 0 & 0 & -52\end{pmatrix} \begin{pmatrix}8 \\ -9 \\ -104\end{pmatrix} \\ \begin{pmatrix}1 & 1 & 2 \\ 0 & 1 & -5 \\ 0 & 0 & 1\end{pmatrix} \begin{pmatrix}8 \\ -9 \\ -2\end{pmatrix}
    $$
    

# 3. 동차 선형 시스템(homogeneous linear system)

- 선형 시스템의 우변이 모두 0인 선형 시스템
- 해가 존재하지 않는 경우가 없음 → 적어도 하나의 해가 존재함
- 선형 시스템의 선형 방정식은 상수항이 0 → 오직 하나의 해 or 무한개의 해
    
    $$
    a_{11}x_1 + a_{12}x_2 + \cdots + a_{1p}x_p = 0 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2p}x_p = 0 \\ \vdots \\ a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{np}x_p = 0
    $$