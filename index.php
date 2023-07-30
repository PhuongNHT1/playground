<?php

require "utils.php";
require "router.php";
require "Database.php";
// connect to the database and execute a query



function printShortcuts() {

    dd($_GET);

    $config = (require("config.php"))['database'];
    $db = new Database($config);

    $query = "select * from shortcuts";
    $statement = $db->query($query);
    $shortcuts = $statement->fetchAll();

    foreach ($shortcuts as $shortcut) {
        echo "<li>". $shortcut['combo'].": ". $shortcut['explain'] ."</li>";
    }
}


printShortcuts();



?>