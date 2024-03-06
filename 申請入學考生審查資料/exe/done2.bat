Set-QuickEdit -DisableQuickEdit
@echo off
set "exe1=folder_create.exe"

set "exe2=index.exe"

set "exe3=indexhtml_generate.exe"

set "exe4=folder_name.exe"

set "exe5=number_name.exe"

set "exe6=dephtml_generate.exe"

set "exe7=grade_sem.exe"
set "exe8=data.exe"
set "exe9=generate_css.exe"
set "exe10=list.exe"

set "exe11=generate_html.exe"
set "exe12=generate_list_html.exe"

set "exe13=generate_score_html.exe" 

REM 依序執行每1個 exe  
@echo 1
call %exe1% 
@echo 2
call %exe2%  
@echo 3
call %exe3%  
@echo 4
call %exe4% 
@echo 5
call %exe5% 
@echo 6
call %exe6% 
@echo 8
call %exe7% 
@echo 9
call %exe8% 
@echo 10
call %exe9% 
@echo 11
call %exe10% 
@echo 12
call %exe11% 
@echo 13
call %exe12% 
@echo 14
call %exe13% 
@echo all are done


pause
