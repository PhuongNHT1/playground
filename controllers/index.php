<?php

// $books = [
//     [
//         'name' => 'Laravel10',
//         'year' => 2023,
//         'author' => 'Phuong Ng',
//         'itemUrl' => 'http://example.com'
//     ],
//     [
//         'name' => 'UIUX Design',
//         'year' => 1995,
//         'author' => 'Thanh Dang',
//         'itemUrl' => 'http://example.com'
//     ],
//     [
//         'name' => 'Microservice',
//         'year' => 2018,
//         'author' => 'Phuong Ng',
//         'itemUrl' => 'http://example.com'
//     ]
// ];

// $filteredBook = array_filter($books, function($book){
//     return (($book['year'] >= 1995) && ($book['year'] <= 2020));
// });

$heading = "Home";
require "views/index.view.php"

?>