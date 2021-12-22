# What's new
- Python3 version
- Include FindServices.py
- Up-to-date AV process and services name

Usage:
```
python3 ./FindProcess.py <filename>
python3 ./FindProcess.py tasklist.txt

python3 ./FindService.py <filename>
python3 ./FindService.py services.txt
```

To get the filename, run these command on the targetted Windows machine and write it into a file.
- `tasklist` = List all processes
- `sc queryex type=service state=all | find /i "SERVICE_NAME:"` = List and filter all active services

`tasklist` output sample:

![image](https://user-images.githubusercontent.com/56353946/147062713-d8470a22-d69b-40c7-bc71-9ebee384d17f.png)

`sc queryex type=service state=all | find /i "SERVICE_NAME:"` output sample:

![image](https://user-images.githubusercontent.com/56353946/147062863-2e6d9556-495a-40a4-974d-9a9a62d038b9.png)
