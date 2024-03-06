Set-QuickEdit -DisableQuickEdit
@echo off
set "exe1=make.exe"
 

REM 依序執行每1個 exe  
@echo 1 
call %exe1% 
@echo all are done


pause
