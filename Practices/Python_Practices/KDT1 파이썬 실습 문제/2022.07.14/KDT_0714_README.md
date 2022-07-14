문제 14. 문자의 갯수 구하기

> 문자열 word가 주어질 때, 해당 문자열에서 `a` 개수를 구하세요. **`count()` 메서드 사용 금지**

```python
# 문제 14. 문자의 갯수 구하기

s = input()
c = 0
for i in s:
    if i == 'a':
        c += 1
print(c)
```





문제 15. 문자의 위치 구하기

> 문자열 word가 주어질 때, 해당 문자열에서 `a` 가 처음으로 등장하는 위치(index)를 출력해주세요. `a` 가 없는 경우에는 `-1`을 출력해주세요. `**find()` `index()` 메서드 사용 금지**

```python
# 문제 15. 문자의 위치 구하기

s = input()
c = 0
for i in s:
    if i == 'a':
        print(c)
        break
    elif not 'a' in s:
        print('-1')
        break
    else:
        c += 1
```



문제 15. 문자의 위치 구하기 - 추가문제

> 문자열 word가 주어질 때, 해당 문자열에서 `a` 의 모든 위치(index)를 출력해주세요. **`find()` `index()` 메서드 사용 금지**

```python
# 문제 15. 문자의 위치 구하기 - 추가문제 (index)

s = input()
c = 0
for i in s:
    if i == 'a':
        print(c, end=' ')
        c += 1
    else:
        c += 1
```



문제 16. 모음 등장 여부 확인하기

> 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오. 모음 : a, e, i, o, u `**count()` 사용 금지**

```python
# 문제 16. 모음 등장 여부 확인하기

vowel = ['a', 'e', 'i', 'o', 'u']
word = input()
c = 0
for i in word:
    for ia in vowel:
        if i == ia:
            c += 1
print(c)
```



문제 17. 소문자-대문자 변환하기

소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오. `**.upper()`, `.swapcase()` 사용 금지**

특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다

해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다.

```python
# 문제 17. 소문자-대문자 변환하기

s = input()
result = 0
for i in s:
    print(chr(ord(i)-32),end='')
```



문제 18.  알파벳 등장 갯수 구하기

> 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

```python
# 문제 18.  알파벳 등장 갯수 구하기

word = input()

result = {}
for char in word:
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1

for key in result:
    print(key, result[key])
```