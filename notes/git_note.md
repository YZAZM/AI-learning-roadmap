# GIT-notes

## 1 day
下载git，拉取仓库上传更新文件，主要步骤在以下：

1. 首先要在GitHub上创建一个仓库，不然无法在本地远程进行拉取。
2. 下载git，让后默认安装。

``` git
#首次提交
git --version #检查是否配置完成
git config --global user.name "youer name" #配置你自己的身份
git config --global user.email "your email"
cd 本地端文件所在目录
git init
git status
git add .
git commit -m "first commit: setup AI learning environment"
git remote add origin 仓库地址
#如果反复提交会出现error：要使用 git remote set-url origin 仓库地址
#使用 git remote -v 验证
git push -u origin main
#二次提交
git status #检查更新文件是否被git检测到
git add 文件 #将这个文件的改动纳入版本管理
git commit -m "备注信息" #给这次改动添加备注信息，方便回顾
git push #前面以及绑定origin/main，所以直接执行
```
