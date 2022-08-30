# HTML

**HTML (HyperText Markup Language)** - 웹 콘텐츠의 의미와 구조를 정의할 때 사용

**Hypertext** - 웹 페이지를 다른 페이지로 연결하는 링크

**Markup** - 텍스트 파일이  화면에서 어떻게 보여야 할 것 인지를 표현하고 그 문서의 논리적인 구조를 묘사하기 위해서 태그 등을 이용하는 언어의 한 가지. 

**Tags (태그)** - 텍스트 파일의 특정 위치에 삽입되는 일련의 문자들 이나 기호들

**HTML**은  요소 (elements)로 구성되어 있으며, 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 마크업을 한다. 여기서 태그 (tags) 는 웹 상의 다른 페이지로 이동하게 하는 하이퍼링크 내용들을 생성하거나, 단어를 강조하는 등의 역할을 한다.



## HTML - 요소(Element)의 구조

HTML의 주요 요소는 여는 태그, 닫는 태그, 그리고 내용이 있으며 **HTML의 요소는 대소문자를 구분하지 않는다.** HTML 의 요소는 크게 인라인과 블록 요소로 나뉘는데 인라인 요소는 글자처럼 취급하고 블록 요소는 한 줄 모두 사용한다.

**여는 태그 (Opening tag)** - 요소의 이름 앞에 `<` 그리고 뒤에 `>` 기호가 붙는다.  즉, `<요소의 이름>` 으로 구성된다. 요소가 시작부터 효과가 적용되기 시작한다.

**닫는 태그 (Closing tag)** -  요소의 이름 앞에 `/` 가 붙는다. `/요소의 이름` 닫는 태그는 요소의 끝에 위치한다. 

**내용 (Content)** - 요소의 내용

**요소 (Element)** - 여는 태그, 닫는 태그, 내용을 통틀어 요소(element)라고 한다.



e.g. 

`<p>My cat is <strong>very</strong> grumpy.</p>`

위의 예시에서는 요소 `p` 가 먼저 열리고 그 안에서 `strong` 요소가 열렸으므로, 요소 `p` 를 닫기 전에 `strong` 의 요소가 먼저 닫혀야 한다. 



## HTML - 요소(Element)의 속성(Attributes)

**속성 (Attributes)** 은 요소에 실제론 나타내고 싶지 않지만 추가적인 내용을 담고 싶을 때 사용한다.

**속성 (Attributes) 의 규칙**

1. 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 되고, 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백이 있어야 한다.
2. 속성 이름 다음엔 등호 `=` 가 붙는다.
3. 속성 값은 열고 닫는 따옴표 `"` 로 감싸야 한다 큰 따옴표와 작은 따옴표 둘 다 사용 가능하지만 섞어서 쓰면 안되고 한 종류만 사용해야 한다.



## HTML - 문서의 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```



1. `<!DOCTYPE html>` - 유효한 문서 형식을 나타낸다.

2. `<html></html>` -  ` <html>` 의 요소. 이 요소는 전체 페이지의 콘텐츠를 포함하며, 기본 요소로도 알려져 있다.

3. `<head></head>` - `<head>` 의 요소로 홈페이지 이용자에게는 보이지 않지만 검색 결과에 노출 될 키워드, 홈페이지 설명, CSS 스타일, character setdeclaration 등 HTML 페이지의 모든 내용을 담고 있다.

4. `<meta charset="utf-8">` - 이 요소는 HTML 문서의 문자 인코딩 설정을 UTF-8로 지정하는 것이다. 이 설정을 사용하면 페이지에 포함 된 모든 텍스트 내용을 처리 할 수 있고 나중에 문자 인코딩과 관련된 일부 문제를 피하는 데 도움이 될 수 있으므로 문자 인코딩 설정을 하지 않을 이유가 없다.

5. `<title></title>` - `<title>` 의 요소로 페이지 제목이 설정된다. 페이지가 로드되는 브라우저 탭에 표시되는 제목으로 사용되며, 페이지 제목은 페이지가 책갈피 될 때 페이지를 설명하는 데에도 사용된다.

6. `<body></body>` - `<body>`  요소에는 텍스트, 이미지, 비디오, 게임, 재생 가능한 오디오 트랙 등을 비롯하여 페이지에 표시되는 모든 콘텐츠가 포함된다.



## HTML - HTML 의 주요 태그들 (tags)

`<html>` -  HTML 문서의 루트 요소(root element)로, 웹페이지의 시작과 끝을 정의합니다.

`<head>` -  head는 해당 html 문서의 전반적인 내용을 담고 있는 태그입니다.  title, link, meta 등의 tag 포함

`<body>` - 해당 문서의 콘텐츠 영역, 즉 브라우저에 실제로 표시되는 내용들을 정의합니다.

`<title>` - `<head>` tag 하위 tag로 문서의 제목을 정의합니다. 웹브라우저의 탭에 표시됩니다. 

`<meta>` - 해당 문서에 대한 정보를 정의합니다. e.g.) `<meta charset="utf-8">` = 문자 인코딩 방식은 "utf-8"로 지정

`<div>` - HTML 문서에서 특정 영역이나 구획을 block 단위로 정의합니다. 목적에 따라 묶는 의미입니다.

`<span>` - HTML 문서에서 인라인 요소(inline-element)들을 하나로 묶을 때 사용합니다.

**`<span>` 과  `<div>` 차이** - 두 tag 모두 어떤 목적에 따라 내용을 묶기 위한 tag입니다.  다만, div의 경우 block 단위로 묶이기에 줄 바꿈이 되지만 span의 경우는 인라인 요소를 묶기 때문에 줄 바꿈이 적용되지 않습니다



`<a>` - 다른 콘텐츠와 연결되는 하이퍼링크(hyperlink)를 정의합니다.

​		 e.g.) <a href="링크"> 내용 </a> = `<a href="링크"> 내용 </a>`

 

`<script>` - 실행 가능한 자바스크립트 코드 삽입을 위한 태그입니다. 

`<link>` - 외부 파일을 연결할 때 사용합니다. e.g.) `<link href='외부 CSS 파일 경로" rel="stylesheet" type="static/css">`

`<img>` - 이미지 삽입을 위한 태그입니다. e.g.) <img src="이미지 경로"> 이때 이미지 경로는 주소도 가능하다.

`<p>`  - paragraph의 줄임말로 단락을 만드는 태그입니다. 

`<li>` - HTML 리스트(list)에 포함되는 아이템(item)을 정의합니다.

`<ul>` - unordered list의 줄임말로, 순서가 없는 HTML 리스트(list)를 정의합니다.

`<ol>`  : ordered list의 줄임말로, 순서가 있는 HTML 리스트(list)를 정의합니다.

`<style>` - 해당 HTML 문서의 스타일 정보를 정의합니다. `<head>` tag 하위에 정의됩니다. 

`<br>`  - 줄 바꿈 기능을 의미합니다. 닫는 태그가 없는 게 특징입니다.

 `<h1~6>` - HTML 문서에서 제목(headings)을 정의합니다.

`<input>` - 사용자로부터 입력을 받을 수 있는 입력 필드(input filed)를 정의합니다.

`<form>` - 사용자로부터 입력을 받을 수 있는 HTML 입력 폼(form)을 정의합니다.

`<nav>` - 같은 사이트 안의 페이지나 다른 사이트의 페이지로 연결하는 링크를 정의하며, 위치 영향을 받지 않습니다.

`<footer>` - 웹 사이트의 제작자 정보나 연락처 정보를 정의합니다.

 `<header>` - 문서나 특정 섹션의 헤더(header)를 정의하며, 한 번만 작성되는 `<head>`와 달리 필요한 만큼 사용 가능합니다.

`<button>` - form 요소 중 하나로, 페이지에 버튼을 정의합니다. submit, reset, button의 속성을 지닙니다.

`<strong>` - 해당 콘텐츠의 중요성이나 심각함, 긴급함 등을 강조합니다. 굵은 글씨로 표시된다.

`<b>` - 글자가 굵게 표시된다.

**`<strong>` 과 `<b>` 태그의 차이** - `<b>` 태그가 html의 스타일을 정의하는 태그로 단순히 화면에 보여지는 모양을 정의한다면 `<strong>` 태그는 html의 의미를 정의하는 태그로 의미적으로 중요함을 나타낸다. 예를 들어 시각장애인들을 위한 시스템에서는 `<strong>` 태그 부분을 강조하여 설명하거나 할 수 있다.

`<li>` - 글꼴의 모양을 기울임으로 표기합니다.



주요 태그들의 출처: https://panython.tistory.com/36



## HTML - 레이아웃 (Layout)

**레이아웃 (Layout)** 은 웹페이지에 포함될 요소들을 취합할 수 있게 해주며 여러 구성 요소를 보기 좋고 효과적으로 사용할 수 있도록 배치하는 기술이다. HTML 에서는 주로 `div 요소를 이용한 레이아웃` 과 `HTML5 레이아웃` , 그리고 `table 요소를 이용한 레이아웃` 등을 사용한다. 레이아웃을 변경해주지 않을 경우에는 페이지가 기본 값으로 배치되는데 이를 `Normal flow` 방식이라 한다.



![HTML5 layout](https://www.devkuma.com/docs/html/html_layout.png)





![post-thumbnail](https://velog.velcdn.com/images/dongho18/post/b657bcaf-066f-418b-be7a-dbfa79006578/mdn-horizontal.png)



### HTML - div 요소를 이용한 레이아웃

div 요소는 CSS 스타일을 손쉽게 적용할 수 있어서 레이아웃을 작성하는데 자주 사용되지만 최근에는 HTML5의 의미 요소를 이용한 레이아웃이 가장 많이 선호된다.



e.g.

```<div id="header"><h2>Header 영역</h2></div>
<div id="header">Header</div>
<div id="nav">Nav</div>
<div id="section">
  Section
  <div id="article">Article</div>
</div>
<div id="aside">Aside</div>
<div id="footer">Footer</div>
```



### HTML - HTML5 레이아웃

HTML5에서 최근에 가장 선호되는 레이아웃으로 HTML5에서는 웹 페이지의 레이아웃만을 위한 별도의 새로운 요소들을 제공하는데, 이러한 요소들을 의미(semantic) 요소라고 한다. HTML5의 의미(semantic) 요소에는 `<header>` , `<nav>` , `<section>` , `<article>` , `<aside>` , `<footer>` 등이 있다.



e.g.

```
<header><h2>Header 영역</h2></header>

<nav><h2>Nav 영역</h2></nav>

<section><p>Section 영역</p></section>

<footer><h2>Footer 영역</h2></footer>
```



### HTML - table 요소를 이용한 레이아웃

table 요소를 이용하여 레이아웃을 작성하는 방법이다. table 요소는 레이아웃을 만들기 위해 설계된 요소가 아니므로, 테이블로 작성된 레이아웃은 수정이 매우 힘들어 최근에는 거의 사용되지 않는 방식이다.



e.g.

``` 
<table width="100%" style="text-align:center; border:none;">
  <tr>
    <td colspan="2" style="background-color:#ddd;margin:4px;padding:4px;">Header</td>
  </tr>
  <tr>
    <td colspan="2" style="background-color:#ddd;margin:4px;padding:4px;">Nav</td>
  </tr>
  <tr>
    <td style="background-color:#ddd;width:280px;">
      Section
      <p style="background-color:#efefef;width:265px;margin:10px;">Article</p>
    </td>
    <td style="background-color:#ddd;height:60px;">Aside</td>
  </tr>
  <tr>
    <td colspan="2" style="background-color:#ddd">Footer</td>
  </tr>
</table>
```






## HTML 외의 기술

**CSS (Cascading Style Sheets)** - 일반적으로 웹 페이지의 모양/표현  (예를 들어, 사용된 텍스트 크기나 폰트를 변경하고, 테두리 선, 그림자 효과를 추가하고, 페이지의 레이아웃을 다단으로 편집하고, 애니메이션이나 다른 시각적인 효과를 추가할 수 있습니다.)

**JavaScript** - 기능/동작을 설명하는 데 사용 (예를 들어, 현재 위치를 찾아 지도 위에 표시하고, 버튼을 누를 때 마다 UI 요소를 노출하거나 숨길 수 있고, 사용자의 데이터를 로컬 시스템에 저장하는 것 등의 방법을 알 수 있습니다.)