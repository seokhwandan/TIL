## SQL 문법

### DDL

- ##### 데이터 정의 언어 ( Data Definition Language )

  - 데이터를 정의하기 위한 언어
  - 관게형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE, DROP, ALTER

### DML

- ##### 데이터 조작 언어 ( Date Manipulation Language )

  - 데이터를 저장, 수정, 삭제, 조회 등을 하기 위한 언어
  - INSERT, UPDATE, DELETE, SELECT

### DCL

- ##### 데이터 제어 언어 ( Date Control Language )

  - 데이터베이스 사용자의 권한 제어를 위해 사용되는 언어
  - GRANT, REVOKE, COMMIT, ROLLBACK



```bash
$ vim ~/.bashrc

i

alias sqlite3="winpty sqlite3"

esc

:wq

$ source ~/.bashrc
```



##### csv 파일을 db에 넣기

```sqlite
.mode csv
.import csv파일명.csv table명
```



##### db조회

```sqlite
.headers on -- column명 보기
.mode column -- column명과 데이터 나누기
SELECT * FROM (table명); -- 모든 정보 조회
SELECT column1, column2 FROM table LIMIT num OFFSET num;
WHERE column=value;

.tables -- 테이블 조회
.schema table명 -- schema 조회
```



##### 테이블 생성

```sqlite
CREATE TABLE classmates (
 id INTEGER PRIMARY KEY,
 name TEXT
);
```

- `id` 값을 생성하지 않으면 `rowid` 값을 생성하여 관리한다.

- PRIMARY KEY를 생성하면 `rowid`는 생성되지 않는다.



##### 테이블 삭제

```sqlite
DROP TABLE table;
```



##### 데이터 추가

```sqlite
INSERT INTO table (column1, column2, ...)
VALUES (value1, value2, ...);

INSERT INTO table
VALUES (value1, value2, ..), (value1, value2, ...), (value1, value2, ...);
```



##### 데이터 조회

```sqlite
SELECT column1, column2 FROM table LIMIT num OFFSET num;
WHERE column=value;
```



##### 데이터 삭제

```sqlite
DELETE FROM table; -- 모든 데이터 삭제

DELETE FROM table -- 조건에 맞는 데이터 삭제
WHERE condition; 
```

- 일반적으로 sql은 삭제된 id 값이 있으면 다음 데이터 추가시 재사용한다.

- 재사용하지 않기 위해선 AUTOINCREMENT 속성을 사용
  - id INTERGER PRIMARY KEY AUTOINCREMENT
  - Django: 불필요한 데이터로 처리하는 게 더 중요
  - SQLite: 불필요한 리소스의 사용이므로 사용하지 특별한 조건이 없을 시 사용하지 않음
  - 

##### 데이터 수정

```sqlite
UPDATE tables
SET column=value
WHERE condition;
```



##### LIKE

```sqlite
SELECT * FROM table
WHERE column LIKE '';
```

##### %

- 2% : 2로 시작하는 값
- %2 : 2로 끝나는 값
- %2% : 2가 들어가는 값

##### _

- _2% : 아무값이나 들어가고 두번째가 2로 시작하는 값
- 1_ _ _ : 1로 시작하고 4자리인 값
- 2_ % _ % / 2_ _% : 2로 시작하고 적어도 3자리인 값



##### ORDER

```sqlite
SELECT * FROM table
ORDER BY column1, column2 ASC|DESC;
```

- ASC : 오름차순
- DESC : 내림차순



GROUP

```sqlite
SELECT COUNT(last_name) FROM users
GROUP BY last_name;

SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name;
-- AS 는 단순히 COUNT(*) 의 별명이다
```

