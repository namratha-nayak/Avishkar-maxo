<?php
       session_start();

    	if(isset($_SESSION['MSG'])){
    	echo $_SESSION['MSG'];
    	unset $_SESSION['MSG'];

    }
    if(isset($_POST['save'])){
    $con=mysqli_connect('localhost','root','','');
    $content=$_POST['editor'];
    $added_on=date('y-m-d h:i:s');
    $sql="insert into content(content,added_on) values('%content',$added_on)"
    if(mysqli_query($con,$sql)){
    $_SESSION['MSG']='Successfully saved';
    header('location:index.php');
    die();
}
}
?>