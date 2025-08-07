以下是根据 Homebrew 常用指令整理的 **带案例的速查表**，方便保存使用：

---

### **一、基础操作**
| 指令 | 案例 | 说明 |
|------|------|------|
| **安装命令行工具** | `brew install wget` | 安装下载工具 wget |
| **安装图形应用** | `brew install --cask visual-studio-code` | 安装 VS Code |
| **搜索软件** | `brew search python` | 查找所有 Python 相关包 |
| **查看已安装列表** | `brew list` | 输出所有通过 brew 安装的软件 |
| **卸载软件** | `brew uninstall --cask firefox` | 卸载 Firefox 浏览器 |

---

### **二、更新与升级**
| 指令 | 案例 | 说明 |
|------|------|------|
| **更新 Homebrew** | `brew update` | 获取最新软件列表 |
| **检查可更新软件** | `brew outdated` | 显示可升级的软件（如：`git (1.0.0) < 1.1.0`） |
| **升级所有软件** | `brew upgrade` | 一次性更新所有可升级软件 |
| **升级指定软件** | `brew upgrade git` | 仅升级 Git |
| **锁定软件版本** | `brew pin python@3.11` | 禁止 Python 3.11 自动更新 |

---

### **三、信息查询**
| 指令 | 案例 | 说明 |
|------|------|------|
| **查看软件信息** | `brew info node` | 显示 Node.js 的版本、依赖、文档路径等 |
| **查看依赖关系** | `brew deps python` | 显示 Python 的所有依赖包 |
| **检查依赖使用** | `brew uses openssl` | 查看哪些软件依赖 OpenSSL |

---

### **四、维护与清理**
| 指令 | 案例 | 说明 |
|------|------|------|
| **清理所有旧版本** | `brew cleanup` | 删除所有软件的旧版本缓存 |
| **清理指定软件** | `brew cleanup python` | 只删除 Python 的旧版本 |
| **自动移除无用依赖** | `brew autoremove` | 删除孤立依赖包（如卸载 Python 后残留的包） |
| **诊断环境问题** | `brew doctor` | 检查 Homebrew 健康状态（权限/配置错误） |

---

### **五、高级技巧**
#### 1. 服务管理（MySQL/Redis）
```bash
brew services start mysql    # 启动 MySQL 服务
brew services stop redis     # 停止 Redis 服务
brew services list           # 查看运行状态（输出：mysql started, redis stopped）
```

#### 2. 安装旧版本 Node.js
```bash
brew install node@18         # 安装 Node.js 18.x
brew link --overwrite node@18 # 设为默认版本
```

#### 3. 环境迁移（Brewfile）
```bash
# 导出当前安装的所有软件
brew bundle dump --file=~/Desktop/Brewfile

# 在新电脑一键恢复所有软件
brew bundle install --file=~/Desktop/Brewfile
```

#### 4. 解决安装卡顿（换国内源）
```bash
# 替换中科大源加速
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
```

---

### **六、高频场景组合命令**
| 场景 | 命令 |
|------|------|
| **一键更新所有软件** | `brew update && brew upgrade` |
| **彻底卸载 Chrome 并清理** | `brew uninstall --cask google-chrome && brew cleanup` |
| **开发环境初始化** | `brew install git node@20 python@3.12 mysql` |
| **修复权限错误** | `sudo chown -R $(whoami) $(brew --prefix)/*` |

---

### **速记提示**
1. **命令行工具**：直接 `brew install <包名>`（如 `htop`）  
2. **图形应用**：必须加 `--cask`（如 `brew install --cask zoom`）  
3. 遇到问题先跑 `brew doctor` 自检！

> 将此页保存为 `brew-cheatsheet.md`，终端输入 `open ~/Desktop` 即可在桌面找到文件。  
> 更多帮助：`man brew` 或访问 [Homebrew 官方文档](https://docs.brew.sh)

