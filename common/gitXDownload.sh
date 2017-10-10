#!/bin/bash
my_git_name='gauravds' #put your github username
t_red_start=`tput setab 1`
t_start=`tput setab 7`
t_end=`tput sgr 0`
echo ${t_red_start}Cloning git repo by git user: ${my_git_name}${t_end}
echo ${t_start}cd $1${t_end}
cd $1

echo ${t_start}git clone git@github.com:punchh/$2.git${t_end}
git clone git@github.com:punchh/$2.git

echo ${t_start}cd $2${t_end}
cd $2

echo ${t_start}git remote rename origin upstream${t_end}
git remote rename origin upstream

echo ${t_start}git remote add origin git@github.com:${my_git_name}/$2.git${t_end}
git remote add origin git@github.com:${my_git_name}/$2.git

echo ${t_start}git fetch --all${t_end}
git fetch --all

echo ${t_start}git submodule update --init${t_end}
git submodule update --init

echo ${t_start}cd framework-ios${t_end}
cd framework-ios

echo ${t_start}git remote rename origin upstream${t_end}
git remote rename origin upstream

echo ${t_start}git remote add origin git@github.com:${my_git_name}/framework-ios.git${t_end}
git remote add origin git@github.com:${my_git_name}/framework-ios.git

echo ${t_start}git fetch --all${t_end}
git fetch --all

echo ------------------------------------------------------------------
echo
echo
echo framework remote
echo ${t_start}git remote -v${t_end}
git remote -v
echo
echo
cd ..
echo project remote
echo ${t_start}git remote -v${t_end}
git remote -v
echo
echo done.
echo
echo
