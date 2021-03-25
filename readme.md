本代码用于将markdonw引用的本地图片同步到远程Gitee图床.
1. vscode安装**PasteImage**插件,将setting.json中的pasteImage.path按照下列设置配置
   ```json
    "pasteImage.path": "${currentFileDir}/imgs",
   ```
   配置完成后, 截图后, vscode 中创建markdown文件demo.md, 随便截图一张, 然后**ctrl+shift+P**输入**paste image**命令即可粘贴图片, 此时图片会保存到markdown文件夹下的**imgs**目录.
2. 注册gitee, 并创建一个图床项目比如叫pics, 注意要将Gitee的pages服务打开, 同时为了避免输入密码, 将本机的ssh key复制到gitee设置选项中, 并将项目clone到本地(假设为GIT_ROOT).
3. 脚本sync.py中, 将**GIT_ROOT**修改为你2中pics目录, **REMOTE_PREFIX**中的**lyyiangang**改为你的用户名, **pics**改为你仓库的名字.
4. 使用下列命令同步图片到gitee.
   ```bash
    python sync.py demo.md
   ```
   同步完成后会在/tmp/目录下创建一个tmp.md文件, 这个文件中引用的图片就从本地文件转换为远程Gitee上的图片了. 