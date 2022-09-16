
JavaScript는 웹 페이지에서 복잡한 기능을 구현할 수 있도록 하는 스크립팅 언어 또는 프로그래밍 언어로 표준 웹 기술이라는 케이크의 세 번째 층이라고 할 수 있다.

![img](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/cake.png)

- `HTML` 은 웹 콘텐츠의 구조를 짜고 의미를 부여하는 마크업 언어로  페이지의 어디가 문단이고, 헤딩이고, 데이터 표와 외부 이미지/비디오인지 정의한다.

- `CSS` 는 HTML 콘텐츠에 스타일을 적용할 수 있는 스타일 규칙 언어로, 배경색을 추가하고, 글꼴을 바꾸고, 콘텐츠를 신문처럼 다열 레이아웃으로 배치할 수 있다.

- `JavaScript` 는 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어이다. 또한, **애플리케이션 프로그래밍 인터페이스**(**API**) 라고 부르는 기능들은 JavaScript 코드에서 사용할 수 있는 많은 기능들을 추가로 제공한다.

  



HTML로, 아래처럼 텍스트에 구조와 목적을 부여할 수 있습니다.

```
<p>Player 1: Chris</p>
```

Copy to Clipboard

![img](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/just-html.png)

CSS를 추가하면 보기 좋게 꾸밀 수 있습니다.

```
p {
  font-family: 'helvetica neue', helvetica, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  text-align: center;
  border: 2px solid rgba(0, 0, 200, 0.6);
  background: rgba(0, 0, 200, 0.3);
  color: rgba(0, 0, 200, 0.6);
  box-shadow: 1px 1px 2px rgba(0, 0, 200, 0.4);
  border-radius: 10px;
  padding: 3px 10px;
  display: inline-block;
  cursor: pointer;
}
```

Copy to Clipboard

![img](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/html-and-css.png)

마지막으로는 JavaScript를 곁들여 동적인 기능을 추가할 수 있습니다.

```
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

Copy to Clipboard

<iframe class="sample-code-frame" title="둘러보기 sample" id="frame_둘러보기" width="100%" height="80" src="https://yari-demos.prod.mdn.mozit.cloud/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript/_sample_.%EB%91%98%EB%9F%AC%EB%B3%B4%EA%B8%B0.html" loading="lazy" style="box-sizing: content-box; border: 1px solid var(--border-primary); max-width: 100%; width: calc((100% - 2rem) - 2px); background: rgb(255, 255, 255); border-radius: var(--elem-radius); padding: 1rem; color: rgb(27, 27, 27); font-family: Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"></iframe>





**브라우저 API** - 웹 브라우저에 내장된 API

- [DOM (Document Object Model) API] - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있습니다. 
- [Geolocation API] 지리정보를 가져올 수 있습니다.
- [Canvas] 와 [WebGL API] 로 애니메이션을 적용한 2D와 3D 그래픽을 만들 수 있습니다. 
- [`HTMLMediaElement`] 와 [`WebRTC`]를 포함하는 [오디오와 비디오 API] 로는 멀티미디어를 사용한 흥미로운 일을 할 수 있습니다. 예를 들어 오디오나 비디오를 웹 페이지에서 바로 재생하거나, 여러분의 웹캠으로 비디오를 찍어 다른 사람의 화면에 보여줄 수 있습니다. 





**서드파티 API** - 브라우저에 탑재되지 않은 API

- [Twitter API]로 여러분의 최신 트윗을 웹 사이트가 보여주도록 구현할 수 있습니다.
- [Google 지도 API] 와 [OpenStreetMap API]로 웹 사이트에 지도를 삽입하고, 지도 관련 기능을 추가할 수 있습니다.





### [JavaScript 실행 순서]

브라우저가 JavaScript 블록을 마주치면, 일반적으로는 순서대로 위에서 아래로 실행합니다. 따라서 코드 배치 순서에도 주의를 기울여야 합니다.

```
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

Copy to Clipboard

위 코드는 텍스트 문단을 선택(1번 줄)해서 이벤트 수신기를 부착(3번 줄)하여, 사용자가 문단을 클릭하면 `updateName()` 코드 블록(5번 ~ 8번 줄)을 실행하도록 합니다. `updateName()` 코드 블록(이렇게 재사용 가능하도록 나눠놓은 코드 블록을 "함수"라고 합니다)은 사용자에게 새로운 이름을 물어보고, 그 이름을 문단에 삽입해서 화면을 업데이트합니다.

만약 1번 줄의 코드와 3번 줄의 코드 순서를 서로 바꿔서 실행했으면 원하는 동작 대신 [브라우저 개발자 콘솔 (en-US)]에 오류, `TypeError: para is undefined`가 나타나며, `para` 객체가 아직 존재하지 않으므로 이벤트 수신기를 부착할 수도 없다는 뜻입니다.





## Java Script - 문법



JavaScript는 문법의 대부분을 Java와 C, C++로부터 차용하고 있으며, Awk, Perl, Python의 영향도 받았다. JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용한다. 예를 들면, Früh(독일어로 "이른")을 변수명으로 사용할 수도 있다.

```
var 갑을 = "병정";
var Früh = "foobar";
```

하지만 대소문자를 구분하기 때문에 `Früh`는 `früh`와 다르다.

JavaScript에서는 명령을 [명령문(statement) (en-US)] 이라고 부르며, 세미콜론(;)으로 구분한다. 명령문이 한 줄을 다 차지할 경우에는 세미콜론이 필요하지 않지만, 한 줄에 두 개 이상의 명령문이 필요하다면 반드시 세미콜론으로 구분해야 한다.
JavaScript의 스크립트 소스는 왼쪽에서 오른쪽으로 탐색하면서 토큰, 제어 문자, 줄바꿈 문자, 주석이나 공백으로 이루어진 입력 요소의 시퀀스로 변환된다. (스페이스, 탭, 줄바꿈 문자는 공백으로 간주된다.)





## Java Script - 선언
JavaScript의 선언에는 3가지 방법이 있다.

- var - 변수를 선언. 추가로 동시에 값을 초기화.
- let - 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.
- const - 블록 스코프 읽기 전용 상수를 선언.







표: JavaScript 특수 문자


| 문자          | 뜻                                                           |
| :------------ | :----------------------------------------------------------- |
| `\0`          | Null Byte                                                    |
| `\b`          | Backspace                                                    |
| `\f`          | Form feed                                                    |
| `\n`          | New line                                                     |
| `\r`          | Carriage return                                              |
| `\t`          | Tab                                                          |
| `\v`          | Vertical tab                                                 |
| `\'`          | Apostrophe 혹은 작은 따옴표                                  |
| `\"`          | 큰 따옴표                                                    |
| `\\`          | 백슬래시                                                     |
| `\*XXX*`      | Latin-1 인코딩 문자는 `0` - `377` 사이 8진수 3자리 *XXX*까지 지정될 수 있습니다. 예를 들어, `\251`은 copyright 심볼을 표현하는 8진수 시퀀스입니다. |
| `\x*XX*`      | Latin-1 인코딩 문자는 `00` - `FF` 사이의 16진수 2자리 *XX*로 지정될 수 있습니다. 예를 들어, `\xA9`는 copyright 심볼을 표현하는 16진수 시퀀스입니다. |
| `\u*XXXX*`    | 유니코드 문자는 16진수 4자리 *XXXX*로 지정될 수 있습니다. 예를 들어, `\u00A9`는 copyright 심볼을 표현하는 유니코드 시퀀스입니다. [Unicode escape sequences](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Lexical_grammar#string_literals)를 참고하세요. |
| `\u*{XXXXX}*` | 유니코드 코드 포인트 이스케이프. 예를 들어, `\u{2F804}`는 간단한 유니코드 이스케이프 `\uD87E\uDC04`와 같습니다. |







## Java Script - 연산자



### 연산자 우선순위

연산자의 우선순위는 표현식을 평가할 때 연산자를 적용하는 순서를 결정합니다. 괄호를 사용하면 우선순위를 바꿀 수 있습니다.

아래 표는 우선순위가 높은 순서에서 낮은 순서로 연산자를 나열합니다.

| 연산자 유형        | 개별 연산자                                                  |
| :----------------- | :----------------------------------------------------------- |
| 맴버 접근          | `.` `[]`                                                     |
| 인스턴스 호출/생성 | `()` `new`                                                   |
| 증감               | `!` `~` `-` `+` `++` `--` `typeof` `void` `delete`           |
| 거듭제곱           | `**`                                                         |
| 곱하기/나누기      | `*` `/` `%`                                                  |
| 더하기/빼기        | `+` `-`                                                      |
| 비트 시프트        | `<<` `>>` `>>>`                                              |
| 관계               | `<` `<=` `>` `>=` `in` `instanceof`                          |
| 동등/일치          | `==` `!=` `===` `!==`                                        |
| 비트 AND           | `&`                                                          |
| 비트 XOR           | `^`                                                          |
| 비트 OR            | `|`                                                          |
| 논리 AND           | `&&`                                                         |
| 논리 OR            | `||`                                                         |
| 조건               | `?:`                                                         |
| 할당               | `=` `+=` `-=` `**=` `*=` `/=` `%=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `&&=` `||=` `??=` |
| 쉼표               | `,`                                                          |



























https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript

https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types

https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling

https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration

https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions

https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators