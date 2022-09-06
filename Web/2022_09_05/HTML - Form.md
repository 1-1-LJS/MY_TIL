## HTML - Form

HTML폼은 사용자와 웹사이트 또는 어플리케이션이 서로 상호 작용하는 것 중 중요한 기술 중에 하나이다. 폼은 사용자가 웹사이트에 데이터를 전송하는 것을 허용한다. 일반적으로 데이터는 웹 서버로 전송되지만 웹페이지가 데이터를 사용하기 위하여 사용할 수 도 있다.



## HTML - Form Control

HTML 폼에서는 `<form>` , `<label>` , `<input>` , `<textarea>` , and `<button>` 같은 HTML 요소들을 사용할 수 있다.



## HTML - Form Control Atributes

HTML `<Form>`



e.g. 

```html
<form action="/my-handling-form-page" method="post">

</form>
```




이 요소는 폼의 공식적인 형태로 모든 폼은 이 요소로 시작한다. 이 요소는 다음 `<div>` 나 `<p>` 요소와 같이 사용되고,뿐만 아니라 폼이 동작하는 방식을 설정하는 일부 속성들을 지정 해야 한다. 이러한 모든 속성은 선택적이지만 `action` 속성과 `method` 속성은 필수적으로 설정해야 한다.

- `action` 속성은 데이터를 보낼 URL을 지정한다.
- `method` 속성은 어떤 HTTP 방식을 사용할 것인지 지정한다.(GET 이나 POST)



HTML - Textfield

HTML 은 `<label>` , `<input>` , `<textarea>` 의 세 개의 텍스트 필드를 가지고 있다.



e.g.

```html
<form action="/my-handling-form-page" method="post">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" />
    </div>
    <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail" />
    </div>
    <div>
        <label for="msg">Message:</label>
        <textarea id="msg"></textarea>
    </div>
</form>
```



`<input>` 요소의 가장 중요한 속성은 `type` 속성이다. 이 속성은 `<input>` 요소가 어떻게 입력을 받을 것인지 정의하기 떄문에 매우 중요하다. 이것은 아예 요소를 변경하기 떄문에 주의 해야한다. 

`<textarea>` 에한 태그에 대해 주의할 점은, `<input>`태그는 자동 닫힘 태그로 끝날 때 반드시 `/` 를 태그에 추가해 `<input />` 와 같은 모양이 되야 한다. 하지만 `<textarea>` 은 자동 닫힘 태그가 아니다. 따라서 반드시 엔딩 태그를 사용하여   `<textarea>` ,  ` </textarea>` 의 형식으로 요소를 종료해야 한다.

그러므로 요소의 기본 값 정의는 반드시 value 속성을 다음과 같이 지정 해야 한다.



e.g.

```html
<input type="text" value="by default this element is filled with this text" />
```



반대로 <textarea>요소 에서 기본값을 정의하고 싶다면, <textarea>요소의 시작 태그와 끝 태그 사이에 문자들을 다음과 같이 입력 하면된다.



e.g.

```html
<textarea>by default this element is filled with this text</textarea>
```



# Bootstrap

## Bootstrap - CDN

CDN(Content Delivery(Distribution) Network) 은 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템이다. CDN 을 이용하면 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)하고 외부 서버를 활용함으로써 본인 서버의 부하가 적어진다



## Bootstrap - Layout

- **Breakpoints are the building blocks of responsive design.** 
- **Use media queries to architect your CSS by breakpoint.** 
- **Mobile first, responsive design is the goal.** 

| Breakpoint        | Class infix | Dimensions |
| ----------------- | ----------- | ---------- |
| Extra small       | *None*      | <576px     |
| Small             | `sm`        | ≥576px     |
| Medium            | `md`        | ≥768px     |
| Large             | `lg`        | ≥992px     |
| Extra large       | `xl`        | ≥1200px    |
| Extra extra large | `xxl`       | ≥1400px    |



e.g. breakpoints customized via Sass

```scss
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);
```



## Bootstrap - Customize

scss/_variables.scss 파일에서 가능한 Sass map 의 테마 색의 목록

```css
$theme-colors: (
  "primary":    $primary,
  "secondary":  $secondary,
  "success":    $success,
  "info":       $info,
  "warning":    $warning,
  "danger":     $danger,
  "light":      $light,
  "dark":       $dark
);
```







## Bootstrap - Table

Bootstrap 에서 `.table` 을 사용했을 시의 테이블 형태와 그 코드

| #    | First          | Last     | Handle |
| ---- | -------------- | -------- | ------ |
| 1    | Mark           | Otto     | @mdo   |
| 2    | Jacob          | Thornton | @fat   |
| 3    | Larry the Bird | @twitter |        |

테이블의 코드

```css
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```









## Bootstrap - Colors



```css
<p class="text-primary">.text-primary</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-success">.text-success</p>
<p class="text-danger">.text-danger</p>
<p class="text-warning bg-dark">.text-warning</p>
<p class="text-info bg-dark">.text-info</p>
<p class="text-light bg-dark">.text-light</p>
<p class="text-dark">.text-dark</p>
<p class="text-body">.text-body</p>
<p class="text-muted">.text-muted</p>
<p class="text-white bg-dark">.text-white</p>
<p class="text-black-50">.text-black-50</p>
<p class="text-white-50 bg-dark">.text-white-50</p>
```

