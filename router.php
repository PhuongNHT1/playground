<?php
$uri = parse_url($_SERVER['REQUEST_URI'])['path'];
$routes = [
    '/' => 'controllers/index.php',
    '/about.php' => 'controllers/about.php',
    '/contact.php' => 'controllers/contact.php',
    '/mission.php' => 'controllers/mission.php'
];

function abort($code = 404) {
    http_response_code($code);
    require "views/{$code}.php";
    die();
}

function routeToController($uri, $routes) {
    if (array_key_exists($uri, $routes)) {
        require $routes[$uri];
    } else {
        abort();
    }
}

routeToController($uri, $routes);

?>