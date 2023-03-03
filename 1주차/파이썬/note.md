# 파이썬 기초 문법

- 변수 (Variable)
  - 값을 저장하는 장소를 말한다.
  - 변수는 메모리 주소를 가지고 있다. 
  - 메모리 주소의 특정 영역에 값이 물리적으로 할당되는 것임.
  - 예시) `a = 3` 
- 파이썬이 처리할 수 있는 데이터 유형
  - 수치 자료형 (1. integer, 2. float)
  - 문자형 string
  - 논리 자료형 boolean
- 리스트(list)
  - 시퀀스 자료형, 여러 데이터들의 집합
  - ```
    colors = ['red', 'blue', 'green']
    colors[2]
    ```
  - 길이
    - len(colors)
  - 슬라이싱
    - `colors[:1]`
  - Asterisk (*) 표시 사용법
    - 곱셈 및 거듭제곱 연산으로 사용할 때 
      - `2*3`
    - 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할 때 
    - 가변인자 (Variadic Arguments)를 사용하고자 할 때 
      - 위치에 따라 정해지는 인자인 'positional arguments'는 *로 사용하고, 
      - 키워드(=이름)을 갖는 인자인 'keyword arguments'는 **로 사용
    - 컨테이너 타입의 데이터를 Unpacking 할 때 
      - `list_data = [1,2,3,4,5]`
      - `print(*list_data)`
    
# 자료 구조
- Stack
  - push, pop
  - clear
