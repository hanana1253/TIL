# How to work with git

## branch
- branch는 main branch와 독립된 상태를 가질 수 있다. 
- branch 관련 모든 명령은 `$ git branch`로 시작한다.
```
$ git branch #현재의 local에서 사용할 수 있는 모든 branch의 리스트를 보여주며 내가 있는 위치도 알려줌
$ git branch -r #remote에 있는 branch 조회
$ git branch -a #현재 local 및 remote에 있는 branch 모두 조회
$ git branch {new branch name} #새로운 브랜치 형성
# 작업할 때 branch 따기 직전에 commit까지 꼭 마칠 것. 안그러면 현재까지 한 것은 없이 이전 commit만 반영된 branch가 따진다.
$ git checkout {이동할 branch} #해당 브랜치로 이동
```
- main이 아닌 branch에서 작업을 마치고 main에 병합하기 위해서는 main으로 돌아와 해당 브랜치를 당기기: `$ git merge {당겨올 branch}`
- 반영 후에는 필요없어진 branch 지우기: `$ git branch -D {지울 branch}`
- commit 안하고 main으로 돌아오면, main이 branch 딴 시점의 commit 이후 변화가 없는 경우에는 branch의 작업내용이 따라와버린다.
- 지난 commit으로 돌아가려면 `$ git checkout -- {파일명}`으로 내가 작업했던 최신 파일로 돌린다. 
- git 최신버전에서는 checkout 커맨드의 다양한 쓰임을 구분하기 위해 branch 이동은 `$ git switch`로, 지난 파일버전으로 돌아가는 것은 `$ git restore {파일명}`으로 한다.

## 2 ways of merging

1. merge commit

2. rebasing

## git flow


