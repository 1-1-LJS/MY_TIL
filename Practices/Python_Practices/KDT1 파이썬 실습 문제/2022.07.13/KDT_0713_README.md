예제 01. 기초 함수

- 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 

- cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

```python
예제 01. 기초 함수

def cube(x):
    return x * x * x
n = int(input())
print(cube(n))
```



예제 02. 기초 함수

- 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오.  사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오. 

- 사각형 넓이 : 가로 * 세로 

- 사각형 둘레 : (가로 + 세로) * 2

```python
예제 02. 기초 함수

a = int(input())
b = int(input())
def w(a ,b):
    return a*b
def r(a, b):
    return (a+b)*2
def rectangle(a, b):
    return (w(a,b), r(a,b))
print(rectangle(a,b))
```



문제 09. 득표수 구하기

- 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

```python
문제 09. 득표수 구하기

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
n = (input())
print(students.count(n))
```



문제 10. 5의 개수 구하기

- 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

```python
문제 10. 5의 개수 구하기

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
n = int((input()))
print(numbers.count(n))
```



문제 11. 구구단 출력하기

- 2단부터 9단까지 반복하여 구구단을 출력하세요. 

- 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

```python
문제 11. 구구단 출력하기

for n in range(2, 10):
    print(n, ' 단', sep='')
    for m in range(1, 10):
        print(n, 'X', m, '=', n*m)
```



문제 12. 문자열 조작하기

- 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오

```python
문제 12. 문자열 조작하기

c = input()
s = c.replace("a","")
print(s)
```



문제 13. 문자열 조작하기

- 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

```python
문제 13. 문자열 조작하기

def reverse(s):
    s = s[::-1]
    return s
s=input()
print(reverse(s))
```