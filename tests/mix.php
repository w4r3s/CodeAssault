<?php
$query = "SELECT * FROM users WHERE username = '" . $_GET['username'] . "' AND password = '" . $_GET['password'] . "'";
$result = mysql_query($query);

echo "Welcome, " . $_GET['name'] . "!";

$unsafe_variable = $_POST['content'];
echo $unsafe_variable;
?>
