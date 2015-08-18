<?php
	$password = $argv[1];
	$hashed_password = $argv[2];

	$final = password_verify($password, $hashed_password);
	echo $final;
	return $final;
?>
