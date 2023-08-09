# CodeAssault - PHP Code Auditing Tool

CodeAssault 是一个强大的PHP代码审计工具，可以自动扫描常见的Web安全漏洞，例如SQL注入、XSS、命令注入等。此工具旨在辅助开发人员和安全专家在代码中快速发现潜在的安全隐患。 

## 功能特点 

- **多规则检测**：具有预定义的多种安全规则，涵盖了大部分常见的Web安全漏洞。
-  **扩展性强**：用户可以非常容易地添加自定义的检测规则。 
-  **易于使用**：命令行界面简单明了，易于上手。 



## 安装 

确保你的系统上已安装Python 3。

1. 克隆此仓库到本地：   

   ```bash
   git clone https://github.com/WitchWatcher/CodeAssault.git
   ```

2. 进入项目目录：

   ```bash
   cd CodeAssault
   ```

3. 安装所需依赖：

   ```bash
   pip3 install -r requirements.txt
   ```



## 使用方法

### 单文件扫描

```bash
python3 bin/cli.py yourfile.php
```

<img width="802" alt="image" src="https://github.com/WitchWatcher/CodeAssault/assets/119853210/2812f776-9273-4c81-9be5-eaa5c3ec150c">


### 文件夹扫描

```
python3 bin/cli.py -f yourdirectory
```

<img width="844" alt="image" src="https://github.com/WitchWatcher/CodeAssault/assets/119853210/89cb38fa-a14e-4ac7-a33c-c5bb46db416e">



### 显示帮助

```
python3 bin/cli.py -h
```

### 显示版本

```
python3 bin/cli.py -v
```



## 如何添加自定义规则

请参阅[docs/rules.md](xx)了解如何添加或修改检测规则。





## 许可证

本项目采用MIT许可证授权。有关详细信息，请参阅LICENSE文件。



## 贡献

欢迎提交拉取请求和问题报告！在提交前，请确保已阅读[贡献指南](#)。



## 联系作者

如有任何问题或建议，请通过[issues]([https://github.com/WitchWatcher/CodeAssault/issues](https://github.com/WitchWatcher/CodeAssault/issues)https://github.com/WitchWatcher/CodeAssault/issues)与我们联系。

