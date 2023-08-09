import re
import os
from rules import sql_injection_rules
from rules import xss_rules  # 导入新的XSS规则模块

def scan_file(file_path):
    # 确保文件存在并且是PHP文件
    if not file_path.endswith('.php') or not os.path.exists(file_path):
        print(f"Invalid file path: {file_path}")
        return None

    results = []
    with open(file_path, 'r') as file:
        # 按行读取文件内容
        for line_number, line in enumerate(file.readlines(), start=1):
            # 针对每个SQL注入规则进行检查
            for rule in sql_injection_rules.SQL_INJECTION_RULES:
                pattern = rule['pattern']
                reason = rule['reason']
                # 使用正则表达式检查该行是否匹配规则
                if re.search(pattern, line):
                    results.append((file_path, str(line_number), "SQL Injection Warning", reason))

            # 针对每个XSS规则进行检查
            for rule in xss_rules.XSS_INJECTION_RULES:  # 使用新的XSS规则模块
                pattern = rule['pattern']
                reason = rule['reason']
                # 使用正则表达式检查该行是否匹配规则
                if re.search(pattern, line):
                    results.append((file_path, str(line_number), "XSS Warning", reason))  # 输出XSS警告

    return results

def scan_directory(directory_path):
    results = []
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.php'):
                file_path = os.path.join(root, file_name)
                file_results = scan_file(file_path)
                if file_results:
                    results.extend(file_results)
    return results

