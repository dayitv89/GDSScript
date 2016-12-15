### location$ ~/.bash_profile

# editors
alias at="atom ."
alias sl="subl ."
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
alias elct="/Applications/Electron.app/Contents/MacOS/Electron"

# react-native 
alias rnpid="sudo lsof -n -i4TCP:8081 | grep LISTEN"
alias install-eslint="echo '{ \"extends\": \"rallycoding\" }' > .eslintrc; npm install eslint-config-rallycoding --save-dev"
alias rnrun="react-native run-ios"
alias rnlog="react-native log-ios"
alias simu="xcrun simctl list devices"

# finders
alias os="cd /Users/gauravds/GDS/codes/opensource; ls"
alias codes="cd /Users/gauravds/GDS/codes; ls"

# bash
alias ebp="nano ~/.bash_profile"
alias sbp="source ~/.bash_profile"
alias op="open ."
alias pl="pwd; ls"
alias la="ls -a"
alias pc="pwd ; pwd |  pbcopy"
alias cdd="cd ~/Desktop"

## Lang export
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# xcode
alias pbx="/usr/bin/python -mxUnique -c"

## git related codes 
alias rm_ds="find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch"
alias gpo="git push origin"
alias gpg="git push GDS"
alias gpd="git push d89"
alias gpu="git push upstream"
alias gfa="git fetch --all"
alias grv="git remote -v"
alias gc="git clone"
alias gcm="git add .;git commit -m"
alias gru="git rebase upstream/master"

# gitx
PATH="/Applications/GitX.app/Contents/MacOS:${PATH}"
alias gitx="GitX"
alias gx="GitX ."

# git master rebase
alias mr="git checkout master;gfa;gru;gpg master" 
alias d3="v2;git checkout Development-3;gfa;git rebase upstream/Development-3; gpg Development-3"

# git current branch
alias gb="git status | grep 'On branch' | cut -c 11-"  
alias gbc="gb; gb | pbcopy"

gitCommitPush() {
        gcm "$1"
        gpo master
        gpu master
}
alias gcp=gitCommitPush

gitCommitPushBranch() {
        gcm "$2"
        gpo "$1"
        gpu "$1"
}
alias gcpb=gitCommitPushBranch
