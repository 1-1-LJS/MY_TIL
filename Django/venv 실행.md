user@DESKTOP-4PH3TD0 MINGW64 ~/Desktop
$ cd ..

user@DESKTOP-4PH3TD0 MINGW64 ~
$ mkdir server

user@DESKTOP-4PH3TD0 MINGW64 ~
$ cd server/

user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ pip list
Package            Version

------------------ ---------
appnope            0.1.3
asgiref            3.5.2
asttokens          2.0.8
backcall           0.2.0
certifi            2022.6.15
charset-normalizer 2.1.0
click              8.1.3
colorama           0.4.5
decorator          5.1.1
Django             4.0.6
django-extensions  3.2.0
executing          0.10.0
idna               3.3
ipython            8.4.0
jedi               0.18.1
matplotlib-inline  0.1.6
mypy-extensions    0.4.3
parso              0.8.3
pathspec           0.9.0
pexpect            4.8.0
pickleshare        0.7.5
pip                22.0.4
platformdirs       2.5.2
prompt-toolkit     3.0.30
ptyprocess         0.7.0
pure-eval          0.2.2
Pygments           2.13.0
requests           2.28.1
setuptools         58.1.0
six                1.16.0
sqlparse           0.4.2
stack-data         0.4.0
tomli              2.0.1
traitlets          5.3.0
typing_extensions  4.3.0
tzdata             2022.2
urllib3            1.26.10
wcwidth            0.2.5
WARNING: You are using pip version 22.0.4; however, version 22.2.2 is available.
You should consider upgrading via the 'C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe -m pip install --upgrade pip' command.

user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ python -m venv server-venv

user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ ls -a
./  ../  server-venv/

user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ source server-venv/Scripts/activate
(server-venv)
user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ pip install django==3.2.13
Collecting django==3.2.13
  Downloading Django-3.2.13-py3-none-any.whl (7.9 MB)
     ---------------------------------------- 7.9/7.9 MB 3.5 MB/s eta 0:00:00
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting pytz
  Downloading pytz-2022.2.1-py2.py3-none-any.whl (500 kB)
     -------------------------------------- 500.6/500.6 KB 3.5 MB/s eta 0:00:00
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
Installing collected packages: pytz, sqlparse, asgiref, django
Successfully installed asgiref-3.5.2 django-3.2.13 pytz-2022.2.1 sqlparse-0.4.2
WARNING: You are using pip version 22.0.4; however, version 22.2.2 is available.
You should consider upgrading via the 'C:\Users\user\server\server-venv\Scripts\python.exe -m pip install --upgrade pip' command.
(server-venv)
user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ pip list
Package    Version

---------- --------
asgiref    3.5.2
Django     3.2.13
pip        22.0.4
pytz       2022.2.1
setuptools 58.1.0
sqlparse   0.4.2
WARNING: You are using pip version 22.0.4; however, version 22.2.2 is available.
You should consider upgrading via the 'C:\Users\user\server\server-venv\Scripts\python.exe -m pip install --upgrade pip' command.
(server-venv)
user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ django-admin startproject firstpjt .
(server-venv)
user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ code .
(server-venv)
user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ python manage.py runserver
Watching for file changes with StatReloader
[21/Sep/2022 11:19:29] "GET / HTTP/1.1" 200 10697
[21/Sep/2022 11:19:30] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[21/Sep/2022 11:19:30] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[21/Sep/2022 11:19:30] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[21/Sep/2022 11:19:30] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
Not Found: /favicon.ico
[21/Sep/2022 11:19:30] "GET /favicon.ico HTTP/1.1" 404 2112
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 21, 2022 - 11:18:02
Django version 3.2.13, using settings 'firstpjt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
(server-venv)





http://localhost:8000/