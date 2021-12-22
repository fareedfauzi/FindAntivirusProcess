# What's new
- Python3 version
- Include FindServices.py
- Up-to-date AV process and services name (add about 800++ new process name)

# Usage:
Targeted Windows box (shell):
```
C:\Users\target> tasklist
C:\Users\target> sc queryex type=service state=all | find /i "SERVICE_NAME:"
```

Our box:
```
python3 ./FindProcess.py <filename>
python3 ./FindProcess.py tasklist.txt

python3 ./FindService.py <filename>
python3 ./FindService.py services.txt
```

To get the `<filename>`, run these command on the targetted Windows machine and write it into a file.
- `tasklist` = List all processes
- `sc queryex type=service state=all | find /i "SERVICE_NAME:"` = List and filter all active services

Copy and paste the output into a file, for example tasklist.txt

# Example:
```
fareed@github$ python3 FindProcess.py tasklist-examples.txt
0 avguard.exe AviraAntiVir
1 avshadow.exe Avira
2 avwebgrd.exe AVIRAPersonalEditionClassic

fareed@github$ python3 FindService.py services-example.txt
0 WinDefend WindowsDefender
```

# Todo:
Keep up to date AntivirusProcess.txt and AntivirusServices.txt.
