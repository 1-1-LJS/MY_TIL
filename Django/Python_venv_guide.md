1. Change Directory to Parent Directory

```git bash
user@DESKTOP-4PH3TD0 MINGW64 ~/Desktop
 $ cd ..
```

-  `..` or `../` represents the parent directory (the directory immediately above the current one).

- `.`  represents the current directory (meta-location).

- `./` is to use to execute a compiled program in the current directory.

  

2. Make Directory named `server`

```git bash
user@DESKTOP-4PH3TD0 MINGW64 ~
$ mkdir server
```



3. Change Directory named `server`

```git bash
user@DESKTOP-4PH3TD0 MINGW64 ~
$ cd server/
```



4. Check the installed package list in `server` directory via `pip list`

```git bash
user@DESKTOP-4PH3TD0 MINGW64 ~/server
$ pip list
```
- `pip` - `pip` is "**Pip Installs Packages**" or "**Pip Installs Python**". Alternatively, pip stands for "**preferred installer program**". 
- `pip list` command **returns the list of packages, including editables, in the current environment**.



5. Import Python module to create virtual environments named `server-venv`

```git bash
$ python -m venv server-venv
```
- `-m` means to execute a module or package.
- `venv` is a **virtual environments**.
- `venv` is a tool to create isolated environments.



6. Activate the `server-venv`

```git bash
$ source server-venv/Scripts/activate
```


7. To deactivate the `venv`

```git bash
$ deactivate
```


8. Install `Django` version **3.2.13** 

```git bash
$ pip install django==3.2.13
```
- `Django 3.2.13` is a Django **LTS** version (**Long Term Support)**.



9. Start the Project

```git bash
$ django-admin startproject firstpjt .
```
`firstpjt` means name of the project and `.` after project name (a.k.a. firstpjt) means that the project will be start in current location.



10. Open current directory with a code via VS Code

```git bash
$ code .
```
- `code` is a command line to run VS Code.
- You can run VS Code from the terminal by typing `code + path` 



11. Run Server

```git bash
$ python manage.py runserver
```
- After run a server, you can type either ` http://127.0.0.1:8000/` or `http://localhost:8000/` on web address to confirm.
- `127.0. 0.1` is **the IP address of the local computer**. This IP address allows the machine to connect to and communicate with itself. Therefore, localhost (127.0. 0.1) is used to establish an IP connection to the same device used by the end-user.

