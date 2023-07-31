<?php

$config = (require("config.php"))['database'];
require "Database.php";


$db = new Database($config);
$id = $_GET['id'];

$query = "select * from shortcuts where id = :id";
$statement = $db->query($query, [':id' => $id]);
$shortcut = $statement->fetchOrFail();

$heading = "{$shortcut['combo']}";
require "views/shortcut.view.php";

?>