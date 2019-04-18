# fman-open-jetbrains-alias
[fman](https://fman.io) plugin for opening up JetBrains IDEs installed via the 
[JetBrains Toolbox](https://www.jetbrains.com/toolbox/) in Windows.

**Requires an initial setup of making copies of the shortcut to a folder**

Since the JB toolbox auto updates, you don't want to make static links to the app's 
`183.5912.18\bin\pycharm64.exe` and if I hardlink to the shortcuts in 
`C:\Users\rob\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\JetBrains Toolbox` in the 
plugin I get weird behavior. Anyways simple hack is to make shortcuts to the shortcuts in 
non privilaged locaion. For me, I put them in `C:\Aliases\pycharm.lnk` as you can see in the 
simple enough script. 

Maybe somone else can figure this out a simpler way but its simple enough to work around for me. 

This has helped my workflow **immensly** and hope you enjoy

## Usage
- Intellij - `Ctrl+Alt+I`
- PyCharm - `Ctrl+Alt+P`
- GoLand - `Ctrl+Alt+G`
- WebStorm - `Ctrl+Alt+W`
- CLion -  - `Ctrl+Alt+C`

## Installation
Use fman's
[built-in command for installing plugins](https://fman.io/docs/installing-plugins).