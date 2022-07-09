# Markdown Related

pwd : 현재 디렉토리 출력
cd 디렉토리이름 : 디렉토리 이동

cd . : 현재 디렉토리 

cd .. : 상위 디렉토리로 이동
ls (list) : 목록
mkdir (make directory) : 디렉토리 생성
touch : 파일 생성
rm 파일명: 파일 삭제하기
rm –r 폴더명 : 폴더 삭제하기


파일 디렉토리에서 파일 이름 중간에 빈공간이 있는경우는　새\폴더 와같이 backslash를 이용해준다

~~practice~~ 

add 스테이징 commit 버전 기록



## 저장소 처음 만들때
$ git init

버전을 기록할 때
$ git add .
$ git commit -m '커밋메시지'

상태 확인할 때
$ git status : 1통, 2통
$ git log : 커밋 확인

$ git log --oneline : 한줄로 커밋 상태 확인


git init (master) 를 삭제하려면
rm -rf .git



### View existing remotes

git remote -v

### change the 'origin' remote's url

git remote set-url origin https://github.com/user/repo2.git

### Verify new remote url

git remote -v





```
git remote add origin https://github.com/1-1-LJS/Fork_Pull_Practice.git
```
