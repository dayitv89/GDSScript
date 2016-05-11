
# Setting PATH for Python 3.5
# The orginal version is saved in .bash_profile.pysave
alias python="python3"
alias python27="/usr/bin/python"
alias py="/usr/bin/python"
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
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
alias gpo="git push origin"
alias gpu="git push upstream"
alias cdcodes="cd /Users/gauravds/GDS/punchh; ls"
alias gfa="git fetch --all"
alias grv="git remote -v"
alias gc="git clone"
