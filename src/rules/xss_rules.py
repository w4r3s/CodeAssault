XSS_INJECTION_RULES = [
    {"pattern": "echo\s+\$_(GET|POST|REQUEST|COOKIE)", "reason": "Directly echoing user input can lead to XSS."},
    {"pattern": "print\s+\$_(GET|POST|REQUEST|COOKIE)", "reason": "Directly printing user input can lead to XSS."},
    {"pattern": "echo\s+\$\w+;", "reason": "Ensure that variables are properly sanitized or escaped to prevent XSS."},
    {"pattern": "print\s+\$\w+;", "reason": "Ensure that variables are properly sanitized or escaped to prevent XSS."},
    {"pattern": "innerHTML\s*=\s*\$\w+", "reason": "Using innerHTML with user-supplied data can lead to XSS."},
    {"pattern": "addslashes\(\$\w+\)", "reason": "addslashes is not sufficient to prevent XSS; consider using htmlspecialchars."},
    {"pattern": "extract\(\$\_", "reason": "Using extract on superglobals can lead to variable tampering and potential XSS."},
    {"pattern": "href\s*=\s*\"\s*\$\w+\s*\"", "reason": "Ensure that href attributes are properly sanitized to prevent XSS."},
    {"pattern": "src\s*=\s*\"\s*\$\w+\s*\"", "reason": "Ensure that src attributes are properly sanitized to prevent XSS."},
    {"pattern": "on\w+\s*=\s*\"\s*\$\w+\s*\"", "reason": "Ensure that event handler attributes are properly sanitized to prevent XSS."},  
    {"pattern": r"echo\s+.*\$_(GET|POST|REQUEST|COOKIE)\[.*\].*;", "reason": "Directly echoing user input can lead to XSS."},
]
