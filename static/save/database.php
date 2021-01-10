
<?php
	            if(isset($_POST['editor']))
	            {
	            	$text=$_POST['editor'];
	            	echo "$text";
	            	$con=mysqli_connect('localhost','root','','ckeditor') or die("error");
	            	$query=mysqli_query($con, "INSERT INTO content (content) VALUES ('$text));
	            	if($query)
	            	{
	            		echo "saved";
	            	}
	            	else
	            	{
	            		echo "not"
	            	}
	            }   
?>