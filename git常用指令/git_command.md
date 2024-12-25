#  1 基本命令

<img src=".\img\流程.png" style="zoom:70%;" />

1. git init （初始化）
2. git add . (提交到暂存区)
3. git commit -m "提交日志" (上传）
4. git log (查看修改日志)
5. git reflog
6. ~~git reset --hard <commitID>~~(版本回退)  
   - 直接搜索 git reset 的使用，使用危险

---

## 1.1 分支

### 1.1.1查看本地分支

- git branch

### 1.1.2创建本地分支

- git branch 分支名

### 1.1.3切换分支

- git checkout 分支名
- git checkout -b 分支名 （创建并切换）

### 1.1.4删除分支

- git branch -d 分支名字
- git breach -D 分支名字（强制删除，不做检查）

### 分支合并

*merge：在主分支上，合并其它分支*

- git merge 分支名 

- git merge --no-ff  分支名

  > git config merge.ff no (当前项目，合并都不使用 快速合并)
  >
  > git config --global merg.ff no (全局，都不使用 快速合并)

### 修改上一次的提交记录

- ### 最后一次提交且未push

```
git commit --amend
```

git会打开$EDITOR编辑器，它会加载这次提交的日志，这样我们就可以在上面编辑，编辑后保存即完成此次的修改。



- ### 最后一次提交且已push到服务器

```
git commit --amend
git push origin master --force
```

使用push推送到远程服务器是需要加上--force，让服务器更新历史记录。




# 2 ssh密钥

## 2.1 配置SSH公钥

​	*会覆盖已经生成的密钥*

- ssh-keygen -t rsa (生成公钥)

- cat  ~/.ssh/id_rsa.pub (查看生成的公钥)

- ssh -T git@gitee.com (测试配置)

## 2.2 远程仓库

### 2.2.1 配置

- git remote add origin  ***ssh连接地址*** （要链接到的远程仓库的地址，取名origin）

- git remote （查看链接的远程仓库）

- git <--set-upstream(与远端仓库形成绑定关系)> push *origin*  master:master (当本地与远端一致时，只写一个maste也行)



- git branch -vv （查看远端仓库绑定关系）

### 2.2.2 克隆

- git clone 仓库ssh路径 <本地目录>

### 2.2.3 拉取与合并

- git fetch (拉取，但<mark>不会合并</mark>)
- git pull (拉取，并<mark>合并</mark>)
- git push <-f （强制覆盖）>  origin master



# 3 git 缓存区

- git rm -r --cached <文件名>
  - 从仓库中删除文件夹，*不会删除原文件*



# 4 标签

## 打标签

- 打标签(本地)
  - git tag  <v1.0>  <24f92f4>

- 推送标签
  - git push origin  <v1.0>  *(只推送一个版本)*
  - git push origion --tags *(推送所有)*

- 查看标签
  - git tag

## 删除标签

- 删除标签(本地)
  - git tag -d  <v1.0>

- 删除标签（远程）

  *（需要先删除本地标签）*

  - git push origin :refr/tags/<v2.0>



# 5 commit 规范

- feat：新功能（Feature）

> "feat"用于表示引入新功能或特性的变动。这种变动通常是在代码库中新增的功能，而不仅仅是修复错误或进行代码重构。



- fix/to：修复bug。这些bug可能由QA团队发现，或由开发人员在开发过程中识别。
  - fix关键字用于那些直接解决问题的提交。当创建一个包含必要更改的提交，并且这些更改能够直接修复已识别的bug时，应使用fix。这表明提交的代码引入了解决方案，并且问题已被立即解决。
  - to关键字则用于那些部分处理问题的提交。在一些复杂的修复过程中，可能需要多个步骤或多次提交来完全解决问题。在这种情况下，初始和中间的提交应使用to标记，表示它们为最终解决方案做出了贡献，但并未完全解决问题。最终解决问题的提交应使用fix标记，以表明问题已被彻底修复。

- docs：文档（Documentation）

> “docs” 表示对文档的变动，这包括对代码库中的注释、README 文件或其他文档的修改。这个前缀的提交通常用于更新文档以反映代码的变更，或者提供更好的代码理解和使用说明。

- style: 格式（Format）

> “style” 用于表示对代码格式的变动，这些变动不影响代码的运行。通常包括空格、缩进、换行等风格调整。

- refactor：重构（即不是新增功能，也不是修改bug的代码变动）

> “refactor” 表示对代码的重构，即修改代码的结构和实现方式，但不影响其外部行为。重构的目的是改进代码的可读性、可维护性和性能，而不是引入新功能或修复错误。

- perf: 优化相关，比如提升性能、体验

>  “perf” 表示与性能优化相关的变动。这可能包括对算法、数据结构或代码实现的修改，以提高代码的执行效率和用户体验。

- test：增加测试

>  “test” 表示增加测试，包括单元测试、集成测试或其他类型的测试。

- chore：构建过程或辅助工具的变动

> “chore” 表示对构建过程或辅助工具的变动。这可能包括更新构建脚本、配置文件或其他与构建和工具相关的内容。

- revert：回滚到上一个版本

> “revert” 用于回滚到以前的版本，撤销之前的提交。

- merge：代码合并

> “merge” 表示进行代码合并，通常是在分支开发完成后将代码合并回主线。

- sync：同步主线或分支的Bug

> “sync” 表示同步主线或分支的 Bug，通常用于解决因为合并而引入的问题。





#  \*keil   .gitignor

```
.vscode
*.bak
*.ddk
*.edk
*.lst
*.lnp
*.mpf
*.mpj
*.obj
*.omf
# del *.opt /s  ::不允许删除JLINK的设置
*.plg 
*.rpt 
*.tmp 
*.__i 
*.crf 
*.o 
*.d 
*.axf 
*.tra 
*.dep     
JLinkLog.txt
*.iex
*.htm
*.sct
*.map
*.hex
*.bin


```



# git 文件夹

- dist 

  >  编译出来的发布版，可以理解为压缩发布版

- src 

  >  源码文件

- docs 

  >  文档

- examples 

  >  示例文件

- test 

  >  测试脚本

- assets文件夹

  >  储存js、css、图片等静态资源

- static文件夹

  >  储存第三方静态资源（例如jquery.js, bootstrap.css等）

- .gitignore 

  >  告诉git不要上传到 GitHub上的文件，可以是单个文件也可以是目录

- LICENSE.txt 

  >  授权协议

- README.md 

  >  自述文件，整个项目的简介、使用方法等

