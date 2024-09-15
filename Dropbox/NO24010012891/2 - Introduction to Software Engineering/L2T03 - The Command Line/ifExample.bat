@echo off


REM Set folder names
set "existingFolder = new_folder"
set "ifFolder = if_folder"
set "hyperionDevFolder=hyperionDev"
set "newProjectsFolder=new_projects"

REM Check if the existing folder exists
if not exist "existingFolder" (
    mkdir "ifFolder"
    echo Created new folder "ifFolder".
) else (
    echo Folder "existingFolder" already exists.
)

REM Check if the if_folder exists
if exist "ifFolder" (
    mkdir "hyperionDevFolder"
    echo Created new folder "hyperionDevFolder".
) else (
    mkdir "newProjectsFolder"
    echo Created new folder "newProjectsFolder".
)


