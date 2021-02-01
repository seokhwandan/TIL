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
  - `<hr>`
  - `<ol>`, `<ul>`
  - `<pre>`, `<blockquote>`
  - `<div>`

- 텍스트 관련 요소

  - `<a>`
  - `<b>` vs `<strong>`
    - `<b>` 는 그냥 굵게 / `strong` 은 굵게 + 의미를 강조
  - `<i>` vs `<em>`
  - `<span>`, `<br>`, `<img>`
    - `<br>` 줄바꿈 / `<img>` 이미지 태그
  - 기타 등등

- table

  - `<tr>`, `<td>`, `<th>`
  - `<thead>`, `<tbody>`, `<tfoot>`
  - `<caption>`
  - 셀 병합 속성 : `colspan`, `rowspan`
  - scope 속성
  - `<col>`, `<colgroup>`

- form

  - `<form>` 은 서버에서 처리될 데이터를 제공하는 역할
  - input 데이터를 받아서 서버로 보내주는 역할
  - `<form>` 의 기본 속성
    - `action`
    - `method`

- input

  - 다양한 타입을 가지는 입력 데이터 필드

  - `<label>` : 서식 입력 요소의 캡션

  - `<input>`  공통 속성

    - `name`, `placeholder`

    - `required`
    - `autofocus`