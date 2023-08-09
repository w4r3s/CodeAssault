<?php
    $mysqli = new mysqli("localhost", "username", "password", "database");

    $user_id = $_GET['user_id'];
    
    
    $result = $mysqli->query("SELECT * FROM users WHERE id = $user_id");
    
    $result_deprecated = mysql_query("SELECT * FROM users WHERE id = $user_id");

?>
