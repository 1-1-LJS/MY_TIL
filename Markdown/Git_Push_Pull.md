# Branch



## Merge 방법

### Github 내

1. 원하는 상대의 원격 저장소에서 .git 파일을 fork 해온다
2. 자신의 원격 저장소에 저장될 이름을 작성하고 fork를 생성한다.



### (Local) Clone & Branch

1. 원하는 상대의 원격 저장소에서 .git 파일을 fork 해온다
2. git clone '상대방 .git' 으로 클론을 만든다
3. git branch '브랜치 이름' 으로 브랜치를 만든다.
4. git checkout '브랜치 이름' 으로 해당 브랜치로 이동한다.
5. git add .
6. git commit -m '원하는 커밋 메세지 명' 을 작성한다.
7. git push origin '브랜치 이름'  으로 브랜치로 push 해준다.
8. github 또는 해당하는 상대의 원격 저장소에 pull request 를 보낸다.
   	- head repository 와 base repository 를 확인한다.
   	- head 에서 base 방향으로 merge 된다.

