
## 🌟 UV 超快速 Python 包管理工具速查手册
*Astral 团队出品（Ruff/Uvicorn 同源），比 pip 快 10-100 倍*

### 🔧 安装与配置
```bash
# 一键安装
curl -LsSf https://astral.sh/uv/install.sh | sh

# 验证安装
uv --version

# 设置国内镜像（加速下载）
uv config set pip.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

---

### 🛠️ 核心工作流
![](./assets/uv使用指南/2025-08-03-01-18-09.png)

#### 1. 虚拟环境管理
```bash
# 创建默认环境 (.venv)
uv venv

# 创建指定名称环境
uv venv myenv

# 指定 Python 版本
uv venv --python python3.12

# 激活环境 (创建后手动激活)
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

# 退出环境
deactivate
```

#### 2. 包安装与管理
```bash
# 安装单个包
uv pip install requests

# 安装多个包
uv pip install numpy pandas matplotlib

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 安装开发模式 (本地包)
uv pip install -e .

# 卸载包
uv pip uninstall package_name

# 更新包
uv pip install --upgrade package_name
```

#### 3. 依赖管理
```bash
# 生成 requirements.txt
uv pip freeze > requirements.txt

# 生成精确锁文件 (推荐)
uv pip compile requirements.in -o requirements.txt

# 仅检查更新
uv pip list --outdated
```

---

### ⚡ 性能技巧
```bash
# 快速重建环境
rm -rf .venv && uv venv && uv pip install -r requirements.txt

# 并行安装加速
uv pip install -r requirements.txt --parallel

# 清理缓存
uv clean
```

---

### 🔍 信息查看
```bash
# 查看已安装包
uv pip list

# 查看包详情
uv pip show requests

# 检查依赖冲突
uv pip check
```

---

### 🚀 高级用法
```bash
# 生成最小依赖约束
uv pip compile --min-requirements requirements.in

# 仅下载包不安装
uv pip download requests

# 指定平台安装 (跨平台兼容)
uv pip install --platform manylinux2014_x86_64 package
```

---

### ❓ 常见问题解决

#### 1. 权限错误
```bash
# 使用 --user 安装到用户目录
uv pip install --user package
```

#### 2. 依赖冲突
```bash
# 生成精确依赖锁
uv pip compile requirements.in -o requirements.txt
```

#### 3. 恢复损坏环境
```bash
# 重新创建环境并安装
uv venv --force
uv pip install -r requirements.txt
```

---

### 💡 最佳实践
1. **始终使用虚拟环境**：每个项目独立 `.venv`
2. **版本控制**：
   - 提交 `requirements.txt` 或 `requirements.in`
   - 忽略 `.venv/` (添加到 `.gitignore`)
3. **重建环境命令**：
   ```bash
   rm -rf .venv && uv venv && uv pip install -r requirements.txt
   ```
4. **定期更新**：
   ```bash
   uv pip install --upgrade -r requirements.txt
   uv pip freeze > requirements.txt  # 更新版本
   ```

> 官方文档：[astral.sh/uv](https://astral.sh/uv)  
> 完整命令：`uv --help` 或 `uv pip --help`

---

将此指南保存为 `uv_cheatsheet.md` 放在项目根目录，或打印出来贴在工位旁，再也不怕忘记命令！


