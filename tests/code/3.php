<?php
// 触发XSS警告
echo "Hello, " . $_GET['name'] . "!";
?>
