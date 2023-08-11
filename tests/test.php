<?php

// Command Injection Examples
exec($_GET['cmd']);
shell_exec($_POST['cmd']);
system($_REQUEST['cmd']);
passthru($_COOKIE['cmd']);
$command = `ls -al $_GET['dir']`;
proc_open($_POST['cmd'], array(), $pipes);
pcntl_exec('/bin/sh', array('-c', $_POST['cmd']));
assert('$_POST["assert_code"]');
create_function('', $_GET['function_code']);
$interpolation = "$_GET[command]";
file_put_contents('file.php', $_POST['data']);
fopen($_GET['filename'], 'w');
fwrite($handle, $_REQUEST['data']);
move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $_GET['destination']);
$appendToVariable .= $_POST['data'];
include $_GET['file'];
require $_POST['file'];
eval($_COOKIE['code']);
call_user_func($_GET['function_name'], $_GET['parameter']);
?>
