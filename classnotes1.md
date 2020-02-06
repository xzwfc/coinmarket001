Last login: Tue Jan 14 15:29:17 on ttys000
53:~ xzw$ python3 --version
Python 3.8.1
53:~ xzw$ git --version
git version 2.23.0
53:~ xzw$ git --versionb
unknown option: --versionb
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
53:~ xzw$ ls
Applications		Movies			Untitled.ipynb
Desktop			Music			Untitled1.ipynb
Documents		Pictures		anaconda3
Downloads		Public			百度云同步盘
HD_log.txt		R-Companion
Library			Research Design
53:~ xzw$ open.
-bash: open.: command not found
53:~ xzw$ open .
53:~ xzw$ cd Machine learning
-bash: cd: Machine: No such file or directory
53:~ xzw$ Machine Learning
Machine: Can't find any plists for Machine
53:~ xzw$ cd ml/
53:ml xzw$ ls
53:ml xzw$ ls
try 1
53:ml xzw$ mkdir try1
53:ml xzw$ ls
try 1	try1
53:ml xzw$ mkdir try2
53:ml xzw$ ls
try 1	try1	try2
53:ml xzw$ cd try2
53:try2 xzw$ ls
53:try2 xzw$ cd ..
53:ml xzw$ ls
try 1	try1	try2
53:ml xzw$ pwd
/Users/xzw/ml
53:ml xzw$ touch
usage:
touch [-A [-][[hh]mm]SS] [-acfhm] [-r file] [-t [[CC]YY]MMDDhhmm[.SS]] file ...
53:ml xzw$ touch a.md
53:ml xzw$ ls
a.md	try 1	try1	try2
53:ml xzw$ cd try1
53:try1 xzw$ ls
53:try1 xzw$ touch b.md
53:try1 xzw$ ls
b.md
53:try1 xzw$ delete try 1
-bash: delete: command not found
53:try1 xzw$ subl b.md
-bash: subl: command not found
53:try1 xzw$ subl b.md
-bash: subl: command not found
53:try1 xzw$ ls
b.md
53:try1 xzw$ cat b.md
53:try1 xzw$ b.md
-bash: b.md: command not found
53:try1 xzw$ cd ..
53:ml xzw$ ls
a.md	try1	try2
53:ml xzw$ subl a.md
-bash: subl: command not found
53:ml xzw$ cd try1
53:try1 xzw$ cat b.md
53:try1 xzw$ ls
b.md
53:try1 xzw$ open .
53:try1 xzw$ touch c.md
53:try1 xzw$ touch hello.py
53:try1 xzw$ subl c.md
-bash: subl: command not found
53:try1 xzw$ python3 hello.py
53:try1 xzw$ python hello.py
53:try1 xzw$ ls
b.md		c.md		hello.py
53:try1 xzw$ python3 hello.py
53:try1 xzw$ python3 hello.py
53:try1 xzw$ open .
53:try1 xzw$ python3 hello.py
53:try1 xzw$ python3 hello.py
  File "hello.py", line 1
    print ("hello world!"op)
                         ^
SyntaxError: invalid syntax
53:try1 xzw$ python3 hello.py
  File "hello.py", line 1
    print ("hello world!"op)
                         ^
SyntaxError: invalid syntax
53:try1 xzw$ python3 hello.py
hello world!
10
53:try1 xzw$ subl c.md
-bash: subl: command not found
53:try1 xzw$ touch 1.txt
53:try1 xzw$ subl 1.txt
-bash: subl: command not found
53:try1 xzw$ 1.txt
-bash: 1.txt: command not found
53:try1 xzw$ subl 1.txt
-bash: subl: command not found
53:try1 xzw$ python3 hello.py
hello world!
10
2020-01-14 16:28:48.554970
53:try1 xzw$ subl b.md
-bash: subl: command not found
53:try1 xzw$ sublime_text c.md
-bash: sublime_text: command not found
53:try1 xzw$ python3 -m pip install pandas
Collecting pandas
  Downloading https://files.pythonhosted.org/packages/52/ca/f986280226b62da6ae5474589a369b0d240f9a61a99144a501b45f108883/pandas-0.25.3-cp38-cp38-macosx_10_9_x86_64.whl (10.3MB)
     |████████████████████████████████| 10.3MB 837kB/s 
Collecting pytz>=2017.2 (from pandas)
  Downloading https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl (509kB)
     |████████████████████████████████| 512kB 4.1MB/s 
Collecting numpy>=1.13.3 (from pandas)
  Downloading https://files.pythonhosted.org/packages/a7/06/6d616fb5fb423db595b1502cbd873f3f2025f2fd8509046c771a20c4302a/numpy-1.18.1-cp38-cp38-macosx_10_9_x86_64.whl (15.2MB)
     |████████████████████████████████| 15.2MB 722kB/s 
Collecting python-dateutil>=2.6.1 (from pandas)
  Downloading https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl (227kB)
     |████████████████████████████████| 235kB 2.7MB/s 
Collecting six>=1.5 (from python-dateutil>=2.6.1->pandas)
  Downloading https://files.pythonhosted.org/packages/65/26/32b8464df2a97e6dd1b656ed26b2c194606c16fe163c695a992b36c11cdf/six-1.13.0-py2.py3-none-any.whl
Installing collected packages: pytz, numpy, six, python-dateutil, pandas
Successfully installed numpy-1.18.1 pandas-0.25.3 python-dateutil-2.8.1 pytz-2019.3 six-1.13.0
WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
53:try1 xzw$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 3.5MB/s 
distributed 1.21.8 requires msgpack, which is not installed.
Installing collected packages: pip
  Found existing installation: pip 10.0.1
    Uninstalling pip-10.0.1:
      Successfully uninstalled pip-10.0.1
Successfully installed pip-19.3.1
53:try1 xzw$ python3 -m pip install numpy
Requirement already satisfied: numpy in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (1.18.1)
WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
53:try1 xzw$ python3 -m pip install sklearn
Collecting sklearn
  Downloading https://files.pythonhosted.org/packages/1e/7a/dbb3be0ce9bd5c8b7e3d87328e79063f8b263b2b1bfa4774cb1147bfcd3f/sklearn-0.0.tar.gz
Collecting scikit-learn (from sklearn)
  Downloading https://files.pythonhosted.org/packages/5a/5b/520ed622a1896ac320c19fe8f32ae13258ec72d884e8c6c9753e2b60197e/scikit_learn-0.22.1-cp38-cp38-macosx_10_9_x86_64.whl (7.0MB)
     |████████████████████████████████| 7.0MB 1.1MB/s 
Collecting joblib>=0.11 (from scikit-learn->sklearn)
  Downloading https://files.pythonhosted.org/packages/28/5c/cf6a2b65a321c4a209efcdf64c2689efae2cb62661f8f6f4bb28547cf1bf/joblib-0.14.1-py2.py3-none-any.whl (294kB)
     |████████████████████████████████| 296kB 10.0MB/s 
Collecting scipy>=0.17.0 (from scikit-learn->sklearn)
  Downloading https://files.pythonhosted.org/packages/90/d2/44b70a930ad28da8f65d8c294ac88b20f561e5d650b85efea80381566db1/scipy-1.4.1-cp38-cp38-macosx_10_9_x86_64.whl (28.8MB)
     |████████████████████████████████| 28.8MB 2.2MB/s 
Requirement already satisfied: numpy>=1.11.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from scikit-learn->sklearn) (1.18.1)
Installing collected packages: joblib, scipy, scikit-learn, sklearn
  Running setup.py install for sklearn ... done
Successfully installed joblib-0.14.1 scikit-learn-0.22.1 scipy-1.4.1 sklearn-0.0
WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
53:try1 xzw$ python3 -m pip install bs4
Collecting bs4
  Downloading https://files.pythonhosted.org/packages/10/ed/7e8b97591f6f456174139ec089c769f89a94a1a4025fe967691de971f314/bs4-0.0.1.tar.gz
Collecting beautifulsoup4 (from bs4)
  Downloading https://files.pythonhosted.org/packages/cb/a1/c698cf319e9cfed6b17376281bd0efc6bfc8465698f54170ef60a485ab5d/beautifulsoup4-4.8.2-py3-none-any.whl (106kB)
     |████████████████████████████████| 112kB 1.4MB/s 
Collecting soupsieve>=1.2 (from beautifulsoup4->bs4)
  Downloading https://files.pythonhosted.org/packages/81/94/03c0f04471fc245d08d0a99f7946ac228ca98da4fa75796c507f61e688c2/soupsieve-1.9.5-py2.py3-none-any.whl
Installing collected packages: soupsieve, beautifulsoup4, bs4
  Running setup.py install for bs4 ... done
Successfully installed beautifulsoup4-4.8.2 bs4-0.0.1 soupsieve-1.9.5
WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
53:try1 xzw$ cat .c.md
cat: .c.md: No such file or directory
53:try1 xzw$ cat .hello
cat: .hello: No such file or directory
53:try1 xzw$ cat hellow.py
cat: hellow.py: No such file or directory
53:try1 xzw$ ls
1.txt		b.md		c.md		hello.py
53:try1 xzw$ cat 1.txt
fdsfsdafdsf53:try1 xzw$ 
53:try1 xzw$ cat b.md
fndsfnkasfjkldsf53:try1 xzw$ subl b.md
-bash: subl: command not found
53:try1 xzw$ cat c.md
kdjfklsjfklds53:try1 xzw$ cat hello.py
print ("hello world!")

print (10)

from datetime import datetime
print (datetime.now())53:try1 xzw$ touch classnotes1.md
53:try1 xzw$ subl classnotes1.md
-bash: subl: command not found
53:try1 xzw$ 




classnotes 2

53:~ xzw$ open .
53:~ xzw$ cd ml
53:ml xzw$ ls
a.md  try1  try2
53:ml xzw$ mkdir econ807
53:ml xzw$ cp -r try1 econ807
53:ml xzw$ ls
a.md  econ807 try1  try2
53:ml xzw$ cd econ807/
53:econ807 xzw$ ls
try1
53:econ807 xzw$ cd ..
53:ml xzw$ pwd
/Users/xzw/ml
53:ml xzw$ rm -r try1
53:ml xzw$ ls
a.md  econ807 try2
53:ml xzw$ cd econ807/
53:econ807 xzw$ ls
try1
53:econ807 xzw$ mkdir try_python
53:econ807 xzw$ ls

