# GDSScript

Available scripts:

1. aws scripts @ `aws/`

1. find VC names and changed to some desired named: as `MyLocationDetailViewController` to `Location Detail Screen`

1. `env.sh` env check script for iOS apps.

1. Fixtypo script  `fNr.py` @ `SpellFix`. used to fix typo in source project. I used this for apple/swift repo.

1. PBXedit scripts mod_pbxproj uses in HT_exec

1. `HyperTerminal` python script testing. use HT_exec which is just exec permission and placed at  `/usr/bin/HT_exec`

1. `xcode_clean.sh` for clean derived data and other stuff which is not clear by cmd+shift+k

1. find_all.py to find file names with complete path, recursively search in given argument `$ python find_all.py /Users/gds/Desktop/ > data.json`

1. `neural_network.py` for testing purspose to show demo of one layer NN, demo of *xor gate*.

1. `gitXDownload.sh` for download the whole src project from git with submodule

1. `.bash_profile` for our shell home made system.

1. `CCArc.py` It will add -fno-objc-arc (arc disable flag) for cocos game in xcode project.

### shell script git codes with submodule check

1. gitXDownload.sh
It will clone remote repo
add origin and upstream
add submodule
add origin and upstream of submodule (framework only)
print the remote at last.

  `$ chmod +x gitXDownload.sh`

  `$ ./gitXDownload.sh /Users/gauravds/Desktop repo-ios`

### .bash_profile
 `.bash_profile` or `._profile` @ ~/ directory for custom terminal shortcuts; either restart terminal or run `source .bash_profile` for immediate changes'

### `CCArc.py`

  It will add -fno-objc-arc (arc disable flag) for cocos game in xcode project.
  ```
  cd Project_path
  python CCArc.py
  ```
