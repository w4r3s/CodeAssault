### 如何添加更多的安全规则

> 我们的代码扫描工具允许用户自定义并添加新的安全规则，以便更好地识别潜在的安全隐患。规则的格式是正则表达式，这样可以灵活地匹配源代码中的不同模式。

#### 规则的结构

每个规则都应该是一个字典，其中包括两个键： `pattern`和`reason`。

* `pattern`: 用于匹配源代码的正则表达式。
* `reason`: 当规则被触发时，用于描述警告的原因的字符串。

#### 示例规则

以下是一个简单的XSS警告规则示例：

```
{
    "pattern": "echo\s+\$_(GET|POST|REQUEST|COOKIE)",
    "reason": "Directly echoing user input can lead to XSS."
}
```

#### 添加新规则的步骤

* 确定规则类型: 决定你的新规则是属于哪一类，例如SQL注入、XSS攻击等。

* 编写正则表达式: 设计一个正则表达式来匹配你想要警告的代码模式。

* 提供原因: 写一个明确的描述，解释为什么这个模式是有问题的。

* 将规则添加到列表: 将新规则添加到相应的规则列表中。例如，对于XSS规则，可以添加到`XSS_INJECTION_RULES`列表。

#### 规则模板

可以使用以下模板来快速创建新规则：


```
{
    "pattern": "<Your regular expression here>",
    "reason": "<Your reason for the warning here>"
}
```

只需替换尖括号及其内容，并将新规则添加到适当的列表即可。

