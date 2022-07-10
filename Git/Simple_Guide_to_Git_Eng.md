# Git

## Git - Definition

- **Git is a Version Control System (VCS)** that records changes to a file or set of files over time so that you can recall specific versions later.
  
  - Git tracks the files not the folders
  
- 1. Modify the work 
  2. Gather the modified works (add)
  3. Commit the version of the work (Commit)
  
- Git manages files in order of modified, staged, and committed. 
  - Modified: File is edited (Move to staging area by command line `git add`)
  
  - Staged: Mark the modified works that will be soon committed. 
  
    ​				(Move to repository with command line `git commit`)
  
  - committed: Files have been committed.

![Git_life_cycle](Simple_Guide_to_Git_Kor.assets/Git_life_cycle.png)



## Git - File Lifecycle

- Status로 확인할 수 있는 파일의 상태
  - Tracked : 이전부터 버전으로 관리되고 있는 파일
    - Unmodified : git status 에 나타나지 않음
    - Modified : Changes not staged for commit
    - Staged : Changes to be committed
  - Untracked : 버전으로 관리된 적 없는 파일 (파일을 새로 만든 경우)

![Git's_file_status_lifecycle](Simple_Guide_to_Git_Kor.assets/Git's_file_status_lifecycle.png)





## Git - Command Line

- `pwd` : Print working directory
- `cd Directory Name` : Change directory
- `cd .` : Current directory
- `cd ..` : To move one directory upwards (Into the current folder's parent folder)
- `ls` : list 
- `mkdir` : Make a directory, a.k.a. make a folder
- `touch` : Create a file
- `rm File Name` : Remove the file
- `rm –r Folder Name` : Remove the folder
- `git init` : Initiate git, Make a repository for the first time. (Create local repository)
- `git add .` : 특정 파일/폴더의 변경사항 추가
- `git commit -m '커밋메시지'` : 버전을 기록할 때
- `git status` : 상태확인 (1통, 2통)
- `git log` : 커밋 (버전) 확인
- `rm -rf .git` : git init (master) 를 삭제
- `git branch 브랜치 이름` : 브랜치 생성
- `git checkout 브랜치 이름` : `브랜치이름` 의 브랜치로 전환
- `git checkout -b 브랜치 이름` : 브랜치를 생성하며 바로 그 브랜치로 전환
- `ctrl+c` : Interrupts the currently running command










## Git - Fork & Pull