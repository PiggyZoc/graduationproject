<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
$country = $_GET['country'];

$output = shell_exec("C:/Python34/python.exe C:/inetpub/wwwroot/sentiment_analysis.py {$country}");

echo $output;
/*
$servername = "localhost";
$username = "root";
$password = "3327";
$dbname = "wedding";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT name FROM stu_info";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row["name"].".";
    }
} else {
    echo "0 results";
}
$conn->close();*/
?>