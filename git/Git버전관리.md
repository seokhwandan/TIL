## git 버전관리

### 일반적인 push 과정

```bash
git add .
git commit -m ''
git push origin master
```



### add 를 취소하는 과정

```bash
git add a.txt
git rm --cached a.txt

# 커밋까지 진행한 후 수정된 경우
git add a.txt
git commit -m 'a'
git restore -- staged a.txt
```



### commit 메세지를 수정하는 과정

```bash
git add a.txt
git commit -m 'a'
git commit --amend # 입력모드와 추가모드가 생김
> i 를 누를 시 입력할 수 있는 모드
> esc 를 누를 시 취소
> :wq 저장하고 나가기
```



### commit 에 파일을 추가하는 과정

```bash
git add a.txt
git commit -m 'a, b upload' # a만 commit 했지만 c까지 입력한 상황
git add b.txt
git commit --amend # a와 b가 뭉쳐진다
:wq
```





```bash
# a.txt
git add .
git commit -m 'a'
# a.txt 수정
git add .
git commit -m 'aa'
# a.txt 수정
git add .
git commit -m 'aaa'

git log 또는 git log --oneline # 각각의 commit 고유 id와 메세지 확인

git reset --hard commit 고유 id # 이동하고 싶은 커밋시점으로 이동
# 작성한 코드도 과거로 돌아간다.
# add 했던 기록까지 삭제

git reset --soft commit 고유 id # 이동하고 싶은 커밋시점으로 이동
# 작성한 코드는 그대로
# add 했던 기록도 그대로

# mixed
git reset commit 고유 id # soft와 동일하게 과거 커밋시점으로 이동하고 코드는 그대로 남음
# 바로 add 할 수 있다.
```



