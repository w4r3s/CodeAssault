import re
import os
import importlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获取scanner.py的绝对路径
RULES_DIR = os.path.join(BASE_DIR, 'rules')  # 连接scanner.py的路径和'rules'得到rules的绝对路径

def load_all_rules_from_directory(directory_path=RULES_DIR):
    all_rules = {}
    # 获取rules目录下的所有.py文件
    for rule_file in os.listdir(directory_path):
        if rule_file.endswith('_rules.py'):
            module_name = rule_file[:-3]  # 移除.py后缀
            module = importlib.import_module(f"rules.{module_name}")
            rule_key = module_name.upper()
            rules_list = getattr(module, rule_key, [])
            all_rules[rule_key] = rules_list
    return all_rules

RULES = load_all_rules_from_directory()

def determine_rule_type(rule_key):
    """
    Determine the rule type based on the rule_key.
    This will convert something like "SQL_INJECTION_RULES" to "SQL Injection Warning".
    """
    rule_type = rule_key.replace("_RULES", "").title().replace("_", " ") + " Warning"
    return rule_type

def scan_file(file_path):
    # 确保文件存在并且是PHP文件
    if not file_path.endswith('.php') or not os.path.exists(file_path):
        print(f"Invalid file path: {file_path}")
        return None

    results = []
    with open(file_path, 'r') as file:
        # 按行读取文件内容
        for line_number, line in enumerate(file.readlines(), start=1):
            for rule_key, rules in RULES.items():
                rule_type = determine_rule_type(rule_key)
                for rule in rules:
                    pattern = rule['pattern']
                    reason = rule['reason']
                    # 使用正则表达式检查该行是否匹配规则
                    if re.search(pattern, line):
                        results.append((file_path, str(line_number), rule_type, reason))
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
