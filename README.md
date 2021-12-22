# FindAntivirusProcess
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

To get the filename, run command `tasklist` (for processes) or `sc queryex type=service state=all | find /i "SERVICE_NAME:"` (for services) on the targetted Windows machine and write it into a file.