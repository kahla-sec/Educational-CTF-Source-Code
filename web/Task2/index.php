<?php
require("flag.php");
highlight_file(__FILE__);
if(isset($_GET['naruto'])){
	$in=$_GET['naruto'];
	$secret="I_want_to_become_a_hockage";
	if($in=preg_replace("/$secret/",'',$in)){
		if ($in===$secret){
			echo "Arigato :D\n"; 
			echo $flag ;
		}
		else {
			die("Heey search a little bit please it's EZ");
		}
	}
	else {
		die("Are u understanding the code ?");
	}
}

?>
