<?php
include "Crud.php";
$crud = new Crud();
$data = json_decode(file_get_contents("php://input"));

if($data!=null){
    $username = $data->username;
    $name = $data->name;
    $email=$data->email;
    $t = TRUE;
    if ($fh = fopen('users.txt', 'r')) {
        while (!feof($fh)) {
            $line = fgets($fh);
            if(strlen($line)>0){
                $temp=explode(" ",$line);
                if($temp[0]==$username || $temp[1]==$email){
                    echo json_encode('1');
                    $t=FALSE;
                    break;
                }
            } 
        }
        fclose($fh);
    }
    if($t){
        $myfile = fopen("users.txt", "a+");
        $txt = $username." ".$email." ".$name."\n";
        fwrite($myfile, $txt);
        fclose($myfile);
    }
}

?>