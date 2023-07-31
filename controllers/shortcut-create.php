<?php

$heading = "Create Shortcut";
require "views/shortcut-create.view.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    dd($_POST);
}

?>