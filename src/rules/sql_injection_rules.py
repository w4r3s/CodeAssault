SQL_INJECTION_RULES = [
    {"pattern": "mysql_query\\(", "reason": "Use of deprecated mysql_query function can lead to SQL Injection."},
    {"pattern": "mysqli::query\\(", "reason": "Ensure that queries to mysqli::query are parameterized to avoid SQL Injection."},
    {"pattern": "mysqli_query\\(", "reason": "Ensure that queries to mysqli_query are parameterized to avoid SQL Injection."},
    {"pattern": "pg_query\\(", "reason": "Ensure that queries to pg_query are parameterized to avoid SQL Injection."},
    {"pattern": "db2_exec\\(", "reason": "Ensure that queries to db2_exec are parameterized to avoid SQL Injection."},
    {"pattern": "\\.\s*\\$\\w+\\s*\\.\\s*\'", "reason": "String concatenation with variables may lead to SQL Injection."},
    {"pattern": "sprintf\\(.+,\\s*\\$\\w+\\)", "reason": "Use of sprintf with user-supplied variables may lead to SQL Injection."}
]
