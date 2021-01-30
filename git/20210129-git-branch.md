# How to work with git

## branch
- branch는 main branch와 독립된 상태를 가질 수 있다. 
```
$ git branch	#현재의 local에서 사용할 수 있는 모든 branch의 리스트를 보여주며 내가 있는 위치도 알려줌
$ git branch -r	#remote에 있는 branch 조회
$ git branch -a	#현재 local 및 remote에 있는 branch 모두 조회
$ git branch {new branch name}	#새로운 브랜치 형성
# 작업할 때 branch 따기 직전에 commit까지 꼭 마칠 것. 안그러면 현재까지 한 것은 없이 이전 commit만 반영된 branch가 따진다.
$ git checkout {이동할 branch}	#해당 브랜치로 이동
$ git merge {당겨올 branch}	#main 외의 branch에서 작업을 마치고 main에 병합하기 위해서는 main으로 돌아와 해당 브랜치를 당기기 
$ git branch -D {지울 branch}	#main으로 merge 후 필요없어진 branch 지우기 
```
- commit 안하고 main으로 돌아오면, branch 딴 시점의 commit 이후 main branch에 따로 변화가 없는 경우에는 branch의 작업내용이 따라와버린다. 이런 식으로 원치 않는 작업 진행이 된 경우 지난 commit으로 돌아가려면 `$ git checkout -- {파일명}`으로 내가 작업했던 최신 파일로 돌린다. 
- git 최신버전에서는 checkout 커맨드의 다양한 쓰임을 구분하기 위해 branch 이동은 `$ git switch`로, 지난 파일버전으로 돌아가는 것은 `$ git restore {파일명}`으로 한다.

## 2 ways of merging

1. merge commit
- conflict를 만들어서 수정하고 merge commit. 중간과정들이 명확히 log에 남아 협업에 더 용이하다는 선생님의 의견.
2. rebasing
- 내가 작업한 branch의 base를 최신 main branch의 commit 시점으로 옮기는 것. linear한 개발이 가능하며 commit log가 깔끔하게 나온다. 그러나 언제 branch를 땄는지 알 수 없다.
- rebasing 하는 방법
```
$ git rebase {main branch}	#conflict가 난다는 경고가 뜨면 vi로 열어서 conflict를 해결하고 git add를 한다. commit은 하지 않는다.
$ git rebase --continue 	# rebasing 완료
```

## 3 ways of working together via git
1. git flow 
- 주 branch 2개(main, develop)를 두고 기능마다 feature branch를 따서 작업후 develop branch에 merge하며, 사용자가 보게 될 최종 소스만 main으로 반영하는 형식.
- 독립된 환경에서 과감한 test가 가능하다. 
- 기능들을 다 모아서 release branch에서 작업하고 pre-compile 등을 한다.
- hotfix branch는 사용자들이 열받았을 때 바로 main branch에서 따와서 기능 수정.
- 장점: 각 단계가 명확히 구분되어 있다.
- 단점: 너무 복잡한 구조라고 할 수 있다. (특정한 몇몇 기능의 release는 develop단에서 해도 충분한데... 복잡복잡하다) 

2. github flow
- master(main)과 feature branch로 이루어진 간단한 구조
- master branch에 내 source가 바로 들어간다는 위험

3. gitlab flow
- 잘 못 알아들었습니다. 여하튼 중요한 건 우린 git flow를 하자는 것...

## git flow 사용법
1. git flow cheat sheet 에서 다운로드 후 git flow를 사용하고자 하는 directory에 간다. 
1-1. (팀으로 작업하는 경우) 팀장님의 레포에서 fork를 한 후 fork 받아온 내 레포 주소를 클론하여 디렉토리를 만든다.
2. `$ git flow init`으로 초기설정을 한다. git flow 명령어에서 사용할 branch 이름 등을 초기설정하는데 대부분 그냥 엔터하면 된다. 
3. init을 마치면 내가 있는 곳은 develop branch이다. 작업을 시작할 파일 등을 만들거나 팀장님이 만들어둔 파일을 확인한다.
3-1. (팀으로 작업하는 경우) 팀장님의 파일에 내가 더할 것을 팀장님 레포의 issue에 작성한다. 
4. `$ git flow feature start {feature branch의 이름}`로 feature branch를 딴다.
5. feature branch로 자동으로 이동되어 있으니 작업을 하고 add&commit 한다.
5-1. (팀으로 작업하는 경우) 팀장님 레포 issue에 작성할 때 부여된 번호를 commit 할 때 기재한다. 
6. `$ git flow feature finish {feature branch 이름}`로 작업을 마친다. feature branch는 자동 삭제되고 나의 위치는 develop branch. 
7. `$ git push -u origin develop`으로 나의 remote repo에 push 한다.
7-1. (팀으로 작업하는 경우) 나의 remote repo에서 팀장님의 remote repo로 pull request를 보내야 한다. 내 repo 들어가서 pull request를 작성할 수 있다.
8. (팀으로 작업하는 경우) 팀장님이 merge 해주거나 review 하여 수정을 지시한다. 팀장님의 지시에 따라 수정하여 다시 pull request한다.
8-1. 다른 팀원의 feature가 먼저 반영된 경우 pull request 할 때 conflict가 생기는데, 이 때 팀장님의 develop branch를 당겨와 최신 파일을 받아야 한다.
```
$ git remote add pmorigin {팀장님 레포주소}	#팀장님 레포 당겨오기 위해 remote repo 주소 세팅하기
$ git pull pmorigin develop	#나의 develop branch에 팀장님의 레포 당겨오기
```
8-2. conflict 난 부분을 확인, 수정하고 merge commit 달기

## 느낀 점
conflict 해결하는 것도 아직은 귀찮고 시간이 많이 걸린다. git이라는게 뭔지 영원히 이해 못할 줄 알았는데 그래도 해보니까 이해가 된다. 여러번 더 연습해봐야겠다.  
