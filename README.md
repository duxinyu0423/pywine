# 背景知识

* wine 如何运行exe 应用
  * https://blog.csdn.net/WJK19891106/article/details/130647609




# 环境配置

在ubuntu20.04 环境下

* python

```shell
# 安装python环境
conda create -n wine python=3.9
conda activate wine 

# 安装PyQt5和pyqt5-tools
pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple  
pip install pyqt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple
```

* pycharm 配置qt5

```web-idl
https://blog.csdn.net/pyscl01/article/details/131522183/
```

* wine 安装以及使用

```web-idl
https://wiki.winehq.org/Ubuntu_zhcn
```

官网中的命令在国内不太好用，使用curl和清华源替换

```shell
# 开启 32 bit 架构支持
sudo dpkg --add-architecture i386 
# 下载添加仓库密钥
sudo mkdir -pm755 /etc/apt/keyrings
# sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
curl https://dl.winehq.org/wine-builds/ubuntu/dists/focal/winehq-focal.sources | sudo tee /etc/apt/sources.list.d/winehq-focal.sources
sudo echo "deb [arch=amd64,i386 signed-by=/usr/share/keyrings/winehq-archive.key] https://mirrors.tuna.tsinghua.edu.cn/wine-builds/ubuntu/ focal main" > /etc/apt/sources.list.d/winehq.list
sudo apt update
sudo apt install --install-recommends winehq-stable
sudo apt install winetricks

# 配置winecfg
winecfg
# 安装依赖, 若安装失败则去除父目录 /tmp
wget -O /tmp/wine-mono-9.0.0-x86.msi https://mirrors.ustc.edu.cn/wine/wine/wine-mono/9.0.0/wine-mono-9.0.0-x86.msi
wine start /i /tmp/wine-mono-9.0.0-x86.msi
wget -O /tmp/wine-gecko-2.47.4-x86.msi https://mirrors.ustc.edu.cn/wine/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86.msi
wine start /i /tmp/wine-gecko-2.47.4-x86.msi
```



* wine 卸载 参考：https://blog.csdn.net/qq_36446887/article/details/80737877

```shell
sudo apr purge wine* -y
sudo rm -r ~/.wine
sudo apt autoremove
sudo rm -r ~/.local/share/applications
sudo rm -r ~/.config/menus/applications-merged/wine*
```

* wine 安装/运行软件

```
wine *exe
```

* wine删除软件

```shell
wine uninstaller
```

