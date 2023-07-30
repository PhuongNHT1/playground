<?php

class Person {
    public $name;
    public $age;

    public function breathe() {
        echo $this->name . " is breathing";
    }
}

$person = new Person();
$person->name = 'Phuong';
$person->age = 31;

$person->breathe();

?>