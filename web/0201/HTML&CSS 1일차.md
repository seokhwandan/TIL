## HTML

### 태그(tag)

```html
<head>
<body>
</body>
</head>
```

- html 은 기본적으로 `head` 태그와 `body` 태그가 있다.

  - 일반적으로 `head` 와 `body` 는 html 의 자식 태그이기는 하나 들여쓰기는 하지 않는다.
  - `body` 는 브라우저 화면에 나타나는 정보이다.

- `meta` 태그는 닫는 태그가 없다.

  ```html
  <meta charset="UTF-8">
    >> 전체 문서에 대해 문자 인코딩을 어떤 type으로 할 것인지 설정
  ```

### 요소(element)

```html
<h1>contents</h1>
```

- HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

### 속성(attribute)

```html
<a href="https://google.com">contents</a>
```

- key 에 해당하는 `href` 는 속성명 이라고 한다.
- `https://google.com` 는 속성값 이라고 한다.

- `href` 는 `a` 태그가 가지고 있는 속성명이다.
- `a` 태그는 하이퍼링크를 만들어주는 태그이다. (anchor 의 약자이다)

#### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 속성(몇몇 요소에는 아무 효과가 없을 수 있다)
  - id, class
  - hidden
  - lang
  - style
  - tabindex
  - title

### 시맨틱 태그

- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 `의미` 를 가지는 태그들을 활용하기 위한 노력
- Non semantic 요소는 `div`, `span` 등이 있으며 `h1`, `table` 태그들도 시맨틱 태그로 볼 수 있다.
- 검색엔진최적화(SEO) 를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 할 필요가 있다.
- 대표적인 태그
  - `header` : 문서 전체나 섹션의 헤더(머릿말 부분)
  - `nav` : 네비게이션
  - `aside` : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - `section` : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - `article` : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - `footer` : 문서 전체나 섹션의 푸터(마지막 부분)

### HTML 문서 구조화

- 그룹 컨텐츠

  - `<p>` 
    -  문장 그룹 (paragraph)
  - `<hr>` 
    - 가로줄 태그
  - `<ol>`, `<ul>` 
    - list tag
  - `<pre>`, `<blockquote>` 
    - `<pre>` 는 문장의 있는 그대로를 보여주고 싶을 때 쓰는 태그
  - `<div>`

- 텍스트 관련 요소

  - `<a>` : 하이퍼 링크 태그
  - `<b>` vs `<strong>`
    - `<b>` 는 그냥 굵게 / `strong` 은 굵게 + 의미를 강조
  - `<i>` vs `<em>`
  - `<span>`, `<br>`, `<img>`
    - `<br>` 줄바꿈 / `<img>` 이미지 태그
  - 기타 등등

- table

  - `<tr>`, `<td>`, `<th>`
  - `<thead>`, `<tbody>`, `<tfoot>`
    - table 전체의 머릿말, 몸통, 마지막 부분
  - `<caption>`
  - 셀 병합 속성 : `colspan`, `rowspan`
    - colspan 은 좌우의 열 병합, rowspan 은 위 아래의 행 병합
  - scope 속성
  - `<col>`, `<colgroup>`

- form

  - `<form>` 은 서버에서 처리될 데이터를 제공하는 역할
  - input 데이터를 받아서 서버로 보내주는 역할
  - `<form>` 의 기본 속성
    - `action`
      - 요청할 주소(입력된 데이터와 함께 요청)
    - `method`
      - http 메소드

- input

  - 다양한 타입을 가지는 입력 데이터 필드

  - `<label>` : 서식 입력 요소의 캡션

  - `<input>`  공통 속성

    - `name`, `placeholder`
      - input 에서의 `name` 은 python 에서 변수명과 동일하다고 생각하면 된다.
      - `placeholder` 입력을 돕기위한 helper text (ex : id를 입력하세요.)

    - `required`
      - 입력창을 비워둘 수 없게 끔 하는 속성
    - `autofocus`

- select

  - dropdown 박스 생성
  - `option` 을 이용해 dropdown 박스안의 내용을 채울 수 있다.
    - `option` *n 을 입력하면 한번에 n개의 `option` 을 생성할 수 있다.
    - `disabled` 사용 시 선택할 수 없게 할 수 있다.



## CSS

스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

html 은 css 없이 작성할 수 있지만, css 는 html 없이 작성할 수 없다.

### CSS 정의 방법

- `inline` : html 내부에 작성하는 방법(html 내부에 style 태그 사용)
- `내부참조(embedding)` : html 의 head 에 style 태그 사용
- `외부참조(link file)` : 분리된 CSS 파일(head 에 link 태그를 사용하여 참조주소를 작성)

### 선택자

- HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요
- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinarors)
  - 자손 결합자, 자식 결합자
  - 일반 형제, 인접 형제 결합자
- 의사 클래스/요소(pseudo class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

#### class 선택자

- 클래스 선택자는 마침표(`.`) 문자로 시작하며 해당 클래스가 적용된 문서의 모든 항목을 선택

#### id 선택자

- `#` 문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용
- 문서당 한번만 사용할 수 있으며, 요소에는 단일 id 값만 적용할 수 있다.

### CSS 적용 우선순위(cascading order)

- 중요도(Importance)
  - `!important`
- 우선 순위(Sepcificity)
  - `인라인` / `id선택자` / `class 선택자` / `요소 선택자`
- 소스 순서

### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.

  - 상속되는 것 

    > Text 관련 요소(font, color, text-align), opacity, visibility 등

  - 상속 되지 않는 것

    > Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)

    > position 관련 요소(position, top/right/bottom/left/z-index 등)

### CSS 단위

> **(상대) 크기 단위**

- `px` (픽셀)
- `%`
- `em` : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가진다. (부모의 사이즈를 기준으로)
- `rem` : 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가진다. (html의 사이즈를 기준으로)
  - html의 기본 폰트 사이즈는 16px 즉, 어디에 작성하던 기준은 16px

- `Viewport` 기준 단위
  - `vw`, `vh`, `vmin`, `vmax`

> **색상 단위**

- 색상 키워드
- RGB 색상
  - `#` + 16진수 표기법
  - `rgb()` 함수형 표기법
- HSL 색상
  - 색상, 채도, 명도
- `a` 를 붙이면 투명도를 표현할 수 있다.
  - `rgba`, `hsla`

>**CSS 문서 표현**

- 텍스트
  - 변형 서체
  - 자간, 단어 간격, 행간, 들여쓰기
  - 기타 꾸미기
- 컬러(color), 배경(background-image, background-color)
- 목록꾸미기
- 표 꾸미기

### Box model 구성

- `Margin` : 테두리 바깥의 외부 여백으로, 배경색을 지정할 수 없다

  - 상하좌우(top, right, bottom, left) 네방향

    ```css
    margin {
    	margin: 10px; >> 상하좌우
    	margin: 10px 20px; >> 상하 / 좌우
    	margin: 10px 20px 30px; >> 상 / 좌우 / 하
    	margin: 10px 20px 30px 40px; >> 상 / 우 / 하 / 좌 top/right/bottom/left
    }
    ```

- `Border` : 테두리 영역
  - 상하좌우(top,right, bottom, left) 네방향
- `Padding` : 테두리 안쪽의 내부 여백
  - 상하좌우(top, right, bottom, left) 네방향
- `Content` : 글이나 이미지 등 요소의 실제 내용

#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box로 설정

### CSS Display

모든 요소는 네모(박스모델)이고, 어떻게 보여지는지(display)에 따라 문서에서의 배치가 달라질 수 있다.

#### display

- `display`: `block`
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다.
- `display`: `inline`
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지
  - width, height, margin-top, margin-bottom을 지정할 수 없음
  - 상하 여백은 line-height 로 지정
- `display`: `inline-block`
  - block과 inline 레벨 요소의 특징을 모두 갖는다.
  - inline 처럼 한 줄에 표시 가능
  - block 처럼 width, height, margin  속성을 모두 지정할 수 있다.
- `display`: `none`
  - 해당 요소를 화면에 표시하지 않음(공간도 사라짐)
  - 비슷한 `visiblility`: `hidden` 은 공간은 차지하지만 화면에 표시만 하지 않는다.

#### 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분
- 대표적인 블록 레벨 요소
  - `div` / `ul`, `ol`, `li` / `p` / `hr` / `form` 등
- 대표적인 인라인 레벨 요소
  - `span` / `a` / `img` / `input`, `label` / `b`, `em`, `i`, `strong` 등