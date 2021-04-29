#### 식별자

- 변수를 구분할 수 있는 변수명

- 식별자는 반드시 숫자, 달러($) 또는 밑줄(_)로 시작

- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

- 예약어 사용 불가능

- ##### 식별자 작성 스타일

  - 카멜 케이스(camelCase, lower-camel-case)
    - 변수, 객체, 함수에 사용
  - 파스칼 케이스(PascalCase, upper-camel-case)
    - 클래스, 생성자에 사용
  - 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수(constants) 에 사용



#### 블록 스코프

- if, for, 함수 등의 중괄호 내부를 가리키며, 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

  

#### 호이스팅 

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환



#### 데이터 타입 종류

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가진다.
- 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류 된다.
  - 원시 타입 (Primitive type)
    - 객체(object)가 아닌 기본 타입
    - 변수에 해당 타입의 값이 담기고, 복사할 때 실제 값이 복사된다.
  - 참조 타입(Reference type)
    - 객체(object) 타입의 자료형
    - 변수에 해당 객체의 참조 값이 담기고, 복사할 때 참조 값이 복사된다.



#### 조건문 또는 반복문에서 결과의 참/거짓

- Undefined : 항상 거짓
- Null : 항상 거짓
- Number : 거짓 `0, -0, NaN`, 나머지 모든 경우 참
- String : 빈 문자열의 경우 거짓, 나머지 모든 경우 참
- Object : 항상 참



#### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

- 다양한 연산에 대한 단축 연산자 지원

  - Increment(++) : 피연산자의 값을 1 증가시키는 연산자

  - Decrement(--) : 피연산자의 값을 1 감소시키는 연산자
  - Airbnb Style Guide 에서는 `+=` 또는 `-=` 와 같이 더 분명한 표현으로 적을 것을 권장



#### 비교 연산자

- python 과 동일함



#### 동등 비교 연산자(==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 불리언 값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음



#### 일치 비교 연산자(===)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 불리언 값을 변환
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별



#### 논리 연산자

- 세 가지 논리 연산자로 구성
  - and 연산은 `&&` 연산자를 이용
  - or 연산은 `||` 연산자를 이용
  - not 연산은 `!` 연산자를 이용
- 단축 평가 지원
  - false && true => false
  - true || false => true



#### 삼항 연산자(Ternary Operator)

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자

- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고, 그렇지 않으면 콜론(:) 뒤의 갑승ㄹ 사용

- 삼항 연산자의 결과는 변수에 할당 가능

- 한 줄에 표기하는 것을 권장

  ex) 5 > 4 ? 'YES' : 'NO'



#### 조건문

- ##### if, else if, else

  - 조건은 소괄호(condition) 안에 작성하고, 실행할 코드는 중괄호{} 안에 작성

- ##### switch

  - 표현식(expression)의 결과값을 이용한 조건문
  - 표현식의 결과값과 case문의 오른쪽 값을 비교
  - break 및 default문은 [선택적]으로 사용 가능
  - break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행



#### 반복문

- ##### while

  - 조건문이 참(true)인 동안 반복 시행
  - 조건은 소괄호(condition) 안에 작성
  - 실행할 코드는 중괄호{} 안에 작성

- ##### for

  - 세미콜론(;)으로 구분되는 세 부분으로 구성
  - initialization
    - 최초 반복문 진입시 1회만 실행되는 부분 (초기값)
  - condition
    - 매 반복 시행 전 평가되는 부분 (조건)
  - expression
    - 매 반복 시행 이후 평가되는 부분 (값의 증감 정도를 많이 사용)

- ##### for in

  - 객체(object)의 속성들을 순회할 때 사용
  - 배열도 순회 가능하지만 권장하지 않음
  - 실행할 코드는 중괄호 안에 작성

- ##### for of

  - 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
  - 실행할 코드는 중괄호 안에 작성



### 함수

- 참조 타입 중 하나로써 function 타입에 속함
- 자바스크립트에서 함수를 정의하는 방법은 주로 2가지로 구분
  - 함수 선언식 (function declaration)
  - 함수 표현식 (function expresson)
- 자바스크립트의 함수는 일급 객체(First-class citizens)에 해당
  - 일급 객체
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환 값으로 사용 가능

#### 선언식(statement, declaration)

```javascript
function add (num1, num2) {
	return num1 + num2
}

add(2, 7)
```



#### 표현식(expression)

- 표현식 내에서 함수를 정의하는 방식 (변수에 함수를 정의해 사용한다.)
- 이름이 없는 함수를 **익명함수(anonymous function)** 라고 명명

- 익명함수는 함수 표현식에서만 사용 가능

  ```javascript
  const sub = function (num1, num2) {
      return num1 - num2
  }
  
  sub(7, 2)
  ```

  

#### 기본 인자(default arguments)

- 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능



#### 함수의 타입

- 함수도 하나의 값으로 평가된다.
- 선언식 함수와 표현식 함수 모두 타입은 `function` 으로 동일



#### 호이스팅(hoisting) - 함수 선언식

- 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생

- 함수 호출 이후에 선언해도 동작

  ```javascript
  add(2, 7)
  
  function add (num1, num2) {
  	return num1 + num2
  }
  ```

- 반면, 함수 표현식으로 선언한 함수는 hoisting 시 에러 발생

  - 함수를 변수에 할당함으로 변수로 평가되어 변수의 scope 규칙을 따르기 때문

- 함수 표현식을 var 키워드로 작성한 경우, 변수가 선언 전 undefined 로 초기화 되어 다른 에러가 발생



#### Arrow Function

- function 키워드 생략 가능

- 함수의 매개변수가 단 하나 뿐이라면, `()` 도 생략 가능

- 함수 바디가 표현식 하나라면 `{}` 과 return 도 생략 가능

  ```javascript
  const arrow = function (name) {
      return `hello! ${name}`
  }
  
  // 1. function 키워드 삭제
  const arrow (name) => { return `hello! ${name}` }
  
  // 2. () 생략 (함수 매개변수가 하나일 경우만)
  const arrow = name => { return `hello! ${name}` }
  
  // 3. {} & return 생략 (바디가 표현식 1개인 경우만)
  const arrow = name => `hello! ${name}`
  ```

  

### 배열 (Arrays)

#### 배열의 정의와 특징

- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능



#### 배열 관련 주요 메서드

- `array.reverse()` : 원본 배열의 요소들의 순서를 반대로 정렬
- `array.push()` : 배열의 가장 뒤에 요소 추가
- `array.pop()` : 배열의 마지막 요소 제거
- `array.unshift()` : 배열의 가장 앞에 요소 추가
- `array.shift()` : 배열의 첫번째 요소 제거
- `array.includes(value)` : 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

- `array.indexOf(value)` : 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환

  - 만약 해당 값이 없을 경우 -1 반환

- `array.join([separator])` : 배열의 모든 요소를 연결하여 반환

  - seperator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

- 배열을 순회하며 특정 로직을 수행하는 메서드로, 메서드 호출 시 인자로 callback 함수를 받는 것이 특징

  - `array.forEach((element, index, array) => { do something })`

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - element : 배열의 요소, index : 배열 요소의 인덱스, array : 배열 자체

    - 반환 값(return)이 없는 메서드

      ```js
      const array = ['광주', '대전', '구미', '서울']
      
      array.forEach((region, index) => {
          console.log(region, index)
      })
      // 광주 0
      // 대전 1
      // 구미 2
      // 서울 3
      ```

  - `array.map((element, index, array) => { do something })`

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

    - 기존 배열 전체를 다른 형태로 바꿀 때 유용

      ```js
      const numbers = [1, 2, 3, 4, 5]
      
      const doubleNums = numbers.map((num) => {
          return num * 2
      })
      
      console.log(doubleNums)
      // [2, 4, 6, 8, 10]
      ```

  - `array.filter((element, index, array) => { do something })`

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

    - 기존 배열의 요소들을 필터링할 때 유용

      ```js
      const numbers = [1, 2, 3, 4, 5]
      
      const oddNums = numbers.filter((num, index) => {
          return num % 2
      })
      
      console.log(oddNums)
      // 1, 3, 5
      ```

  - `array.reduce((acc, element, index, array) => { do somthing }, initialValue)`

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

    - reduce 메서드의 주요 매개변수

      - acc : 이전 callback 함수의 반환 값이 누적되는 변수

      - initialValue : 최초 callback 함수 호출 시 acc에 할당되는 값으로, 선택적으로 설정 가능

        ​						직접 제공하지 않으면, 배열의 첫번째 값 사용

    - 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

      ```js
      const numbers = [1, 2, 3]
      
      const result = numbers.reduce((acc, num) => {
          return acc + num
      }, 0)
      
      console.log(result)
      // 6
      // 0 + 1 = 1 -> 1 + 2 = 3 -> 3 + 3 = 6
      ```

  - `array.find((element, index, array) => { do something })`

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - 콜백 함수의 반환 값이 참이면 해당 요소를 반환

    - 찾는 값이 배열에 없으면 undefined 반환

      ```js
      const avengers = [
          { name: 'Tony Stark', age: 45 },
          { name: 'Steve Rogers', age: 32 },
          { name: 'Thor', age: 40 },
      ]
      
      const result = avengers.find((avenger) => {
          return avenger.name === 'Tony Stark'
      })
      
      console.log(result) // {name: "Tony Stark", age: 45}
      ```

  - `array.some((element, index, array) => { do something })`

    - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환

    - 모든 요소가 통과하지 못하면 거짓 반환

    - 빈 배열은 항상 거짓 반환

      ```js
      const numbers = [1, 3, 5, 7, 9]
      
      const hasEvenNumber = numbers.some((num) => {
          return num % 2 === 0
      })
      console.log(hasEvenNumber) // false
      
      const hasOddNumber = numbers.some((num) => {
          return num % 2
      })
      console.log(hasOddNumber) // true
      ```

  - `array.every((element, index, array) => { do something })`

    - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환

    - 모든 요소가 통과하지 못하면 거짓 반환

    - 빈 배열은 항상 참 반환

      ```js
      const numbers = [2, 4, 6, 8, 10]
      
      const isEveryNumberEven = numbers.every((num) => {
          return num % 2 === 0
      })
      console.log(isEveryNumberEven // true
      
      const isEveryNumberOdd = numbers.every((num) => {
          return num % 2
      })
      console.log(isEveryNumberOdd) // true
      ```

    

### 객체 (Objects)

#### 객체의 정의와 특징

- 객체는 속성(property)의 집합이며 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있을 경우 따옴표로 묶어서 표현
- value는 모든 타입 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있을 경우 대괄호 접근만 가능



#### 객체 관련 ES6 문법

1. ##### 속성명 축약 (shorthand)

   - 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능

     ```js
     var bookShop = {
         books: books,
         magazines: magazines,
     }
     
     var bookShop = {
         books,
         magazines,
     }
     ```

2. ##### 메서드명 축약 (shorthand)

   - 메서드 선언 시 function 키워드 생략 가능

     ```js
     var obj = {
         greeting: function () {
             console.log('Hi!')
         }
     };
     
     const newObj = {
         greeting () {
             console.log('Hi!')
         }
     }
     ```

3. ##### 계산된 속성 (computed property name)

   - 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

     ```js
     const key = 'regions'
     const value = ['광주', '대전', '구미', '서울']
     
     const result = {
         [key]: value,
     }
     
     console.log(result) // { regions: Array(4) }
     console.log(result.regions) // ["광주", "대전", "구미", "서울"]
     ```

4. ##### 구조 분해 할당 (destructing assignment)

   - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

     ```js
     const userInformation = {
         name: 'kim',
         userId: 'kim1234',
         phoneNumber: '010-1234-5678',
         email: 'kim@mail.com',
     }
     
     const name = userInformation.name
     const userId = userInformation.userId
     const phoneNumber = userInformation.phoneNumber
     const email = userInformation.email
     
     const { name } = userInformation
     const { userId } = userInformation
     const { phoneNumber } = userInformation
     const { email } = userInformation
     
     // 여러개도 가능
     const { name, userId } = userInformation
     ```



#### JSON (JavaScript Object Notation)

- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 따라서 JS의 객체로써 조작하기 위해서 구문 분석(parsing) 필수
- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드 제공
  - JSON.parse()
    - JSON => 자바스크립트 객체
  - JSON.stringify()
    - 자바스크립트 객체 => JSON

