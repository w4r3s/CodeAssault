<?php
// 触发SQL注入警告
$query = mysql_query("SELECT * FROM users WHERE username = '" . $_GET['username'] . "' AND password = '" . $_GET['password'] . "'");
?>
