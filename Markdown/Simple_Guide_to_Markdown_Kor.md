# 마크다운

- 마크다운은 기반의 마크업 언어로 가능한 읽을 수 있도록 최소한의 문법으로 구조화
- 마크다운은 단순 텍스트 문법으로 작성하며 다양한 기술블로그에서는 정적사이트생성기로 사용한다.
- 마크다운은 최소한의 문법으로 구조화하기 때문에 문서를 정렬하거나 색을 바꾸는 등의 꾸미는 기능이 전무하다.



# 마크다운 문법

## Heading

- Heading은 문서의 제목, 소제목으로 사용되며 #의 개수에 따라 글자의 크기가 달라진다.
- H1~6까지의 사이즈가 있고 H1이 제일 큰 사이즈이다.
- 문서의 구조를 위해 작성되며 쓰게 될 경우 단락이 나뉘어지므로 문서내 단순히 글자의 크기를 조절하기 위해 사용해서는 안된다. 
- Heading의 사용 방법은 '# '이다. '#'표시뒤에 반드시 스페이스를 눌러줘야한다.



## Listing

Listing is divided to Ordered List and Unordered List.

1. Ordered List 

- Ordered List 는 '1. '형식으로 숫자로 표현해준다.
- 1. 딸기
  2. 복숭아

2. Unorderd List

- Unordered List 는 '- ' 형식으로 표현해준다.



OL 과 UL 둘다 '1. ' 혹은 '- '형식으로 기호 뒤에는 스페이스가 있어야 하며 리스트에서도 Breakdown 을 위해서는 `tab`을 눌러주면 된다.

- 딸기
- 복숭아
  - 신비복숭아
  - 선도복숭아



## Code Block

1. Fenced Code Block

- FCB 는 backtick '`' 기호 3개로 표시한다. ('```')

- '```'

- ```pyton
  print Hello World
  ```

2. Inline Code Block

- ICB 는 backtick '`' 기호 1개로 표시한다.  
- '`'
- `Print Hello World`



## Link

- [문자열] (url) 형식으로 링크 시킬 수 있다. '[]+()' 형식으로 [] 과 () 사이에는 빈 공간이 없이 바로 붙여서 쓴다.
- 사이트 뿐만 아니라 문서나 이미지 등의 특정 파일들도 연결 시킬 수 있다.
- 링크에는 절대경로와 상대경로가 있는데 타인에게도 보이기 위해서는 상대경로를 써야한다.
  - i.e. `[Name](./Relative path.md)`
  - `[E-mail](Somebody's@email.com)`




## Blockquote

- `>` 를 통해 인용문을 작성하고 기호뒤에는 스페이스가 필요없이 바로 글을 쓰면 된다.

- > "이 세상에서 보고 싶은 변화를 보기 위해서는 스스로 그 변화가 되어야 한다." - 간디



## Cross Out (Strkiethrough)

- 취소선은 취소하고 싶은 내용 앞뒤로 `**~~**`  를 표시해주면 된다.
- i.e.
  - `~~Text~~`
  - ~~Text~~



## Highlights

- Bold 기호 ** 를 단어 혹은 문장 앞 뒤에 넣어준다 혹은 `ctrl+b` ex) **Bold**
- Italic 기호 * 를 단어 혹은 문장 앞 뒤에 넣어준다 혹은 `ctrl+i`ex) *Italic*



## Horizontal Rule

- 문서내에 수평선을 긋기 위해서는 3개 이상의 asterisk `*`, dashe `-`, or underscore `_` 를 사용하고 `enter` 를 눌러주면된다.

- i.e.

  - asterisks `***`, dashes `---`, or underscores `___` + `enter`

    ___



## Table

- 표를 그리기 위해서는 `ctrl+t` 를 눌러준다.

- i.e.

  - `ctrl` + `t`

  - | Syntax    | Description |
    | --------- | ----------- |
    | Header    | Title       |
    | Paragraph | Text        |



