## github 仓库中的手顺


echo "# LearningNotes" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/wuenhao/LearningNotes.git
git push -u origin main


git remote add origin https://github.com/wuenhao/LearningNotes.git
git branch -M main
git push -u origin main

---
将VSCode工程上传到GitHub的步骤如下：

---

### **1. 准备工作**
- **安装Git**  
  下载地址：[https://git-scm.com/](https://git-scm.com/)  
  安装后验证（终端输入）：
  ```bash
  git --version
  ```

- **配置Git账户**（VSCode终端执行）  
  ```bash
  git config --global user.name "你的GitHub用户名"
  git config --global user.email "你的GitHub邮箱"
  ```

- **登录GitHub账号**  
  确保已在GitHub官网注册账号。

---

### **2. 在GitHub创建仓库**
1. 登录GitHub，点击右上角 **"+ New repository"**  
2. 填写仓库名（Repository name），选择 **Public/Private**  
3. **不要勾选** "Initialize this repository with a README"（避免冲突）  
4. 点击 **"Create repository"**，保存生成的仓库URL（类似 `https://github.com/用户名/仓库名.git`）

---

### **3. 在VSCode中操作**
#### **步骤1：初始化本地仓库**
1. 在VSCode中打开你的工程文件夹  
2. 打开终端（快捷键：<kbd>Ctrl</kbd> + <kbd>`</kbd>）  
3. 执行：
   ```bash
   git init
   ```

#### **步骤2：添加文件到暂存区**
```bash
git add .         # 添加所有文件
# 或选择性添加
git add 文件名     # 添加特定文件
```

#### **步骤3：提交更改**
```bash
git commit -m "提交描述（如：Initial commit）"
```

#### **步骤4：关联远程仓库**
```bash
git remote add origin https://github.com/用户名/仓库名.git
```

#### **步骤5：推送到GitHub**
```bash
git push -u origin master   # 如果默认分支是master
# 或
git push -u origin main     # 如果默认分支是main（GitHub新仓库默认分支）
```

---

### **4. 验证上传**
- 刷新GitHub仓库页面，确认文件已出现。
- 后续修改代码后，重复以下流程：
  ```bash
  git add .
  git commit -m "描述"
  git push
  ```

---

### **常见问题解决**
#### **1. 首次推送失败（分支冲突）**
若GitHub仓库有初始化文件（如README）而本地没有：
```bash
git pull origin main --allow-unrelated-histories
# 解决冲突后重新提交
git push -u origin main
```

#### **2. 认证失败**
- 使用SSH替代HTTPS（需配置SSH密钥）  
  生成SSH密钥：
  ```bash
  ssh-keygen -t ed25519 -C "邮箱"
  ```
  将公钥（`~/.ssh/id_ed25519.pub`内容）添加到GitHub的 **Settings > SSH and GPG keys**。

- 修改远程仓库地址为SSH：
  ```bash
  git remote set-url origin git@github.com:用户名/仓库名.git
  ```

#### **3. 忽略文件（如node_modules）**
在项目根目录创建 `.gitignore` 文件，写入要忽略的文件夹/文件：
```
node_modules/
.env
*.log
```

---

### **图形化操作（VSCode内置Git）**
1. 左侧点击 **源代码管理图标**（Ctrl+Shift+G）  
2. 点击 **"初始化仓库"** → 提交更改（输入描述）  
3. 点击 **"..."** → **"推送"** → 输入远程仓库URL  
   ![VSCode推送示意图](https://code.visualstudio.com/assets/docs/sourcecontrol/overview/commit-toolbar.png)

---

通过以上步骤，你的工程已成功同步到GitHub！