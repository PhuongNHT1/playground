<?php
class Database {
    public $connection;
    public function __construct($config){

        // $dsn = "mysql:host={$config['host']};port={$config['port']};dbname={$config['dbname']};charset=utf8mb4";
        $dsn = 'mysql:' . http_build_query($config, '', ';');
        $this->connection = new PDO($dsn, $config['username'], $config['password'], [
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
        ]);
    }

    public function query($query){
        $statement = $this->connection->prepare($query);
        $statement->execute();
        return $statement;
    }
}

?>