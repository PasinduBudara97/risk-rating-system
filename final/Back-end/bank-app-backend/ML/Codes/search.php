<?php
include "Crud.php";
$crud = new Crud();
$data = json_decode(file_get_contents("php://input"));

if($data!=null){
    $searchtxt = $data->searchtxt;
    
    if ($fh = fopen('users.txt', 'r')) {
        while (!feof($fh)) {
            $line = fgets($fh);
            $temp=explode(" ",$line);
            if($temp[0]==$searchtxt){
                echo json_encode('1');
                break;
            }
        }
        fclose($fh);
    }
}

?>