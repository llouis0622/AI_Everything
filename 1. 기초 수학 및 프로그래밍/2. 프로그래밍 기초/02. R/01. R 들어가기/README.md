# 1. R

- 1993년 Ross Ihaka, Robert Gentleman에 의해 개발
- 광범위한 통계와 그래픽 메소드 보유
- 통계적 추론, 데이터 분석, 머신러닝 알고리즘을 위한 언어

# 2. 데이터 타입

## 1. 기본 데이터 타입

- 스칼라(scalar)
- 벡터(수치, 문자, 논리)
- 행렬(matrix)
- 데이터프레임(data frame)
- 리스트(list)
- 수치(numeric)
- 정수(integer)
- 불리언 값(boolean value)
- 문자(character)
- `class()` : 변수 타입 확인
    
    ```r
    x <- 28
    class(x)
    
    y <- "R is Fantastic"
    class(y)
    
    z <- TRUE
    class(z)
    ```
    
- `str()` : 변수 데이터 구조 확인
    
    ```r
    x <- 28
    str(x)
    
    y <- "R is Fantastic"
    str(y)
    
    z <- TRUE
    str(z)
    ```
    

## 2. 변수(variable)

- 데이터 저장 가능
- 변수 이름 지정으로 변수 선언
- `<-` , `=` : 변수에 데이터 저장

## 3. 벡터(vector)

### 1. 벡터 생성

- 일차원 배열
- `c()` : 벡터 생성
    
    ```r
    vec_num <- c(1, 10, 49)
    vec_num
    
    vec_chr <- c("a", "b", "c")
    vec_chr
    
    vec_bool <- c(TRUE, FALSE, TRUE)
    vec_bool
    ```
    
- 변수 값 출력 방법
    
    ```r
    vec_num <- c(1, 10, 49)
    vec_num
    
    vec_chr <- c("a", "b", "c"); vec_chr
    
    (vec_bool <- c(TRUE, FALSE, TRUE))
    ```
    

### 2. 벡터 유형 검증

- `typeof()` : 벡터 유형 지정
- `is()` : 벡터 유형 검증
    - `is.character()`
    - `is.double()`
    - `is.integer()`
    - `is.numeric()`
    - `is.logical()`
    - `is.atomic()`

### 3. 벡터 형 변환

- 벡터의 모든 요소 → 같은 유형을 가져야 함
- 서로 다른 유형 결합 → 강제 형 변환(coersion) 실행
- 문자형 > 더블형 > 정수형 > 논리형
- 명시적으로 데이터 형변환 실행
    - `as.character()`
    - `as.double()`
    - `as.integer()`
    - `as.logical()`

## 4. 산술 연산자

- `+` : 덧셈(addition)
- `-` : 뺄셈(substraction)
- `*` : 곱셈(multiplication)
- `/` : 나눗셈(division)
- `^` , `**` : 제곱(exponentiation)
- `%%` : 나머지(modulo)
- `%/%` : 몫(quotient)

## 5. 논리 연산자

- `<` : 작다
- `<=` : 작거나 같다
- `>` : 크다
- `>=` : 크거나 같다
- `==` : 같다
- `!=` : 다르다
- `!x` : not x
- `x` : x
- `x|y` : 논리합(or)
- `x&y` : 논리곱(and)
- `isTRUE(x)` : x가 TRUE인가?

## 6. Subsetting, Sequence

- subsetting
    
    ```r
    slice_vector <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    slice_vector[1:5]
    
    slice_vector <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    slice_vector[which(slice_vector %% 3 == 0)]
    ```
    
- `:` : 값 범위 생성
- `seq()` : 파라미터만큼 일정 범위 값 생성
- `rep()` : 반복적 요소 생성
- 벡터 요소에 이름 붙이기
    
    ```r
    x <- c(a=1, b=1, c=3); x
    
    x <- c(1, 2, 3); x
    names(x) <- c("a", "b", "c"); x
    
    x <- setNames(1:3, c("a", "b", "c"))
    ```
    
- `length()` : 벡터 요소 개수 확인