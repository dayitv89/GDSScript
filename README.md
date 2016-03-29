# GDSScript
shell script git codes with submodule check

1. gitXDownload.sh
It will clone remote repo
add origin and upstream
add submodule
add origin and upstream of submodule (framework only)
print the remote at last.

  `$ chmod +x gitXDownload.sh`

  `$ ./gitXDownload.sh /Users/gauravds/Desktop repo-ios`


1. CCArc.py

  It will add -fno-objc-arc (arc disable flag) for cocos game in xcode project.
  ```
  cd Project_path
  python CCArc.py
  ```

1. env check script

1. Fixtypo script  `fNr.py`

1. PBXedit scripts mod_pbxproj uses in HT_exec

1. `HyperTerminal` python script testing. use HT_exec which is just exec permission and placed at  `/usr/bin/HT_exec`

1. `xcode_clean.sh` for clean derived data and other stuff which is not clear by cmd+shift+k

1. find_all.py to find file names with complete path, recursively search in given argument `$ python find_all.py /Users/gds/Desktop/ > data.json`

1. `neural_network.py` for testing purspose to show demo of one layer NN, demo of *xor gate*.

