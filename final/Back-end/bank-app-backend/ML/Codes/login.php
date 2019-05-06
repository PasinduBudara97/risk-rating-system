<?php
include "Crud.php";
$crud = new Crud();
$logindata = json_decode(file_get_contents("php://input"));
if (!empty($logindata)) {
    $username = $logindata->username;
    $password = $logindata->password;
    $query = "SELECT username,password FROM user where username='$username' and password=MD5('$password')";
    $data = $crud->getData($query);

    if(!empty($data)){
        echo json_encode($data[0]);
    }
    else{
        echo ("-1");
    }
}