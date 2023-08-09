<?php
// 触发SQL注入警告
$query = mysqli::query("SELECT * FROM products WHERE id = " . $_POST['id']);
?>
