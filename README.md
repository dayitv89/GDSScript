# PunchhScript
shell script git codes for punchh

1. gitXDownload.sh
It will clone remote repo
add origin and upstream
add submodule
add origin and upstream of submodule (framework only)
print the remote at last.

`$ chmod +x gitXDownload.sh`

`$ ./gitXDownload.sh /Users/gauravds/Desktop repo-ios`


2. CCArc.py
It will add -fno-objc-arc (arc disable flag) for cocos game in xcode project.
cd Project_path
python CCArc.py

3. iconVersioning.sh
Script for stop making ipa without live environment.
environment not case insensitive comapre
environment = "live/LIVE/Live/LiVe" 
