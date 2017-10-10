# editors
alias at="atom ."
alias sl="subl ."
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
alias elct="/Applications/Electron.app/Contents/MacOS/Electron"

# react-native 
alias rn="react-native"
alias rnpid="sudo lsof -n -i4TCP:8081 | grep LISTEN"
alias install-eslint="echo '{ \"extends\": \"rallycoding\" }' > .eslintrc; npm install eslint-config-rallycoding --save-dev"
alias rnrun="react-native run-ios"
alias rnlog="react-native log-ios"
alias simu="xcrun simctl list devices"
alias rnrun-clearCache="./node_modules/react-native/packager/packager.sh start --resetCache"
alias rn-open-ios-proj="open /Users/gauravds/GDS/codes/punchh/v2/react-components/LocationDetails/LocationDetail/ios/LocationDetail.xcodeproj"
export ANDROID_HOME=~/Library/Android/sdk
export PATH=${PATH}:${ANDROID_HOME}/tools
export PATH=${PATH}:${ANDROID_HOME}/platform-tools

# finders
alias os="cd /Users/gauravds/GDS/codes/opensource; ls"
alias f8="cd /Users/gauravds/GDS/codes/opensource/common/facebook/f8app; ls"
alias rntuts="cd /Users/gauravds/GDS/codes/opensource/common/others/react-native/ReactNativeReduxCasts; ls"
alias v1="cd /Users/gauravds/GDS/codes/punchh/v1; ls"
alias v2="cd /Users/gauravds/GDS/codes/punchh/v2; ls"
alias ios="cd /Users/gauravds/GDS/codes/punchh/ios; ls"
alias punchh="cd /Users/gauravds/GDS/codes/punchh; ls"
alias codes="cd /Users/gauravds/GDS/codes; ls"
alias opfr="open /Users/gauravds/GDS/codes/punchh/v1/mooyah-ios/mooyah.xcworkspace"
alias opps="open /Users/gauravds/GDS/codes/punchh/punchh-server; subl /Users/gauravds/GDS/codes/punchh/punchh-server"
alias olo="cd /Users/gauravds/GDS/codes/punchh/v2/olo-framework-reactnative/OloIntegration; pwd; ls"
alias rnm1="cd /Users/gauravds/GDS/meetups/RN1/react-native-jaipur-meetup-1; ls"

# Carthage 
alias cart-frame="carthage build --no-skip-current"

# bash
alias cbp="cat ~/.bash_profile"
alias ebp="nano ~/.bash_profile"
alias sbp="source ~/.bash_profile"
alias op="open ."
alias pl="pwd; ls"
alias la="ls -a"
alias pc="pwd ; pwd |  pbcopy"
alias cdd="cd ~/Desktop"
alias ip="ifconfig | grep 10.1.1;ifconfig | grep 192.168"

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
alias gur="git update-ref refs/heads/master"
alias gs="git stash"
alias gsd="git stash apply; git stash drop"
alias mrs="gs;mr;gsd"

# gitx
PATH="/Applications/GitX.app/Contents/MacOS:${PATH}"
alias gitx="GitX"
alias gx="GitX ."

# git master rebase
alias mr="git checkout master;gfa;gru;gpg master" 
alias d3="v2;cd punchh-core-ios;git checkout Development-3;gfa;git rebase upstream/Development-3; gpg Development-3"

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

gitMasterRebaseWithDeleteCurrentBranch() {
	currentBranch=$(gb)
	mrs
	git branch -d $currentBranch
	git branch -dr GDS/$currentBranch
}
alias dmrs=gitMasterRebaseWithDeleteCurrentBranch
