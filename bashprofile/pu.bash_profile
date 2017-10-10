alias cdc="cd /Users/gauravds/GDS/punchh/codes/ios/noodles-ios"
alias opc="cdr; open noodles.xcodeproj; op"
alias ebp="nano ~/.bash_profile"
alias sbp="source ~/.bash_profile"
alias pl="pwd; ls"
alias rm_ds="find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch"
alias pbx="/usr/bin/python -mxUnique -c"

# Setting PATH for Python 3.5
# The orginal version is saved in .bash_profile.pysave
alias python="python3"
alias python27="/usr/bin/python"
alias py="/usr/bin/python"
PATH="/Users/gauravds/.composer/vendor/laravel/installer:/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# shell 
alias op="open ."
alias pc="pwd ; pwd |  pbcopy"
alias cdd="cd ~/Desktop"

# git related codes 
PATH="/Applications/GitX.app/Contents/MacOS:${PATH}"
alias gitx="GitX"
alias gx="GitX ."
alias gpo="git push origin"
alias gpu="git push upstream"
alias cdcodes="cd /Users/gauravds/GDS/punchh; ls"
alias gfa="git fetch --all"
alias grv="git remote -v"
alias gc="git clone"
