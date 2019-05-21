<?php
include "Crud.php";

require('PHPExcel/Classes/PHPExcel.php');

$data = json_decode(file_get_contents("php://input"));
if($data!=null){

    $loanAmout = $data->loanAmount;
    $period = $data->period;
    $emi = $data->EMI;
    $purpose =$data->purposeofLoan;
    $security = $data->securityType;
    $crib =$data->crib;
    $profitAfterTax = $data->profitAfterTax;
    $typeofEntity =$data->typeOfEntity;
    $periodOfService =$data->periodOfService;
    $totalAssets = $data->totalAssets;
    $burrowings = $data->totalBurrowings;
    $loanInst = $data->loanInst;
    $taxPaying = $data->taxPaying;


    $phpExcel = new PHPExcel;

    $phpExcel->getDefaultStyle()->getFont()->setName('Calibri');

    $phpExcel->getDefaultStyle()->getFont()->setSize(11);

    $writer = PHPExcel_IOFactory::createWriter($phpExcel, 'CSV');

    $sheet = $phpExcel ->getActiveSheet();

    $sheet->setTitle('testBank');

    $sheet ->getCell('A1')->setValue($loanAmout);
    $sheet ->getCell('B1')->setValue($period);
    $sheet ->getCell('C1')->setValue($emi);
    $sheet ->getCell('D1')->setValue($purpose);
    $sheet ->getCell('E1')->setValue($security);
    $sheet ->getCell('F1')->setValue($crib);
    $sheet ->getCell('G1')->setValue($typeofEntity);
    $sheet ->getCell('H1')->setValue($periodOfService);
    $sheet ->getCell('I1')->setValue($totalAssets);
    $sheet ->getCell('J1')->setValue($loanInst);
    $sheet ->getCell('K1')->setValue($taxPaying);

    $writer->save('../Textfiles/testBank.csv');

    $command = escapeshellcmd('python PredictingCode2.py 2>&1');
    $output = exec($command);
    $file = file_get_contents('../Textfiles/prediction.txt');
    echo (json_encode(strval($file)));
}
?>