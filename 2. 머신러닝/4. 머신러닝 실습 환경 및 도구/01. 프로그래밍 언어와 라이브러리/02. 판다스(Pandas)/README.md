# 1. 판다스 들어가기

## 1. 개요

- 관계형 혹은 레이블이 된 데이터로 쉽고 직관적으로 작업할 수 있도록 설계
- 빠르고 유연한 데이터 구조를 제공하는 파이썬 라이브러리
- 가장 강력하고 유연한 오픈소스 데이터 분석 도구

## 2. 데이터 종류에 따른 패키지

- SQL 테이블 혹은 엑셀 스프레드 시트에서와 같은 행과 열로 이루어진 테이블 형식 데이터
- 정렬, 미정렬 시계열 데이터
- 다른 형태의 관찰, 통계 데이터 세트

## 3. 사용법

- `import pandas` : 판다스 임포트
- `pandas.__version__` : 판다스 버전 확인
- `import pandas as pd` : 판다스 별칭 적용

# 2. Series

- 데이터를 담는 차원 배열 구조
- 인덱스 사용 가능
- 데이터 타입 보유

## 1. Series 생성

- numpy array로 생성한 경우
    
    ```python
    arr = np.arange(100, 105)
    arr
    
    s = pd.Series(arr)
    s
    ```
    
- dtype을 지정한 경우
    
    ```python
    s = pd.Series(arr, dtype='int32')
    s
    ```
    
- list로 생성한 경우
    
    ```python
    s = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
    s
    ```
    
- 다양한 타입의 데이터를 섞은 경우
    
    ```python
    s = pd.Series([91, 2.5, '스포츠', 4, 5.16])
    s
    ```
    

## 2. Index

- 기본 인덱스 : 0부터 숫자형 인덱스 부여
- 기본 부여된 인덱스로 값 조회 가능
- 인덱싱, 슬라이싱 전부 사용 가능
- fancy indexing, boolean indexing 전부 사용 가능

## 3. values

- Series 데이터 값만 numpy array 형식으로 가져옴
    
    ```python
    s.values
    ```
    

## 4. ndim

- 차원 출력
    
    ```python
    s.ndim
    ```
    

## 5. shape

- 데이터의 모양 확인
- Series의 shape → 데이터의 개수 출력
- 튜플 형식으로 출력
    
    ```python
    s.shape
    ```
    

## 6. NaN(Not a Number)

- 비어있는 결측치 데이터를 나타냄
- 임의로 비어있는 값 대입 → numpy의 nan 입력
    
    ```python
    s = pd.Series(['선화', '강호', np.nan, '소정', '우영'])
    s
    ```
    

## 7. 결측치 값 처리

- `isnull()` : NaN 값을 찾는 함수
- `isna()` : NaN 값을 찾는 함수
- `notnull()` : 비어있지 않은 데이터를 찾는 함수

# 3. DataFrame

## 1. 들어가기

- `pd.DataFrame`
- 2차원 데이터 구조
- 행과 열로 구성
- 각 열은 각각의 데이터 타입을 가짐

## 2. 생성

- list를 통한 생성
    
    ```python
    pd.DataFrame([[1, 2, 3],
    							[4, 5, 6],
    							[7, 8, 9]])
    							
    pd.DataFrame([[1, 2, 3],
    							[4, 5, 6],
    							[7, 8, 9]], columns=['가', '나', '다')
    ```
    
- dictionary를 통한 생성
    
    ```python
    data = {
    		'name': ['Kim', 'Lee', 'Park'],
    		'age': [24, 27, 34],
    		'children': [2, 1, 3]
    }
    pd.DataFrame(data)
    ```
    

## 3. 속성

- `index` : 인덱스
- `columns` : column 명
- `values` : numpy array 형식의 데이터 값
- `dtypes` : column 별 데이터 타입
- `T` : DataFrame 전치