<?php
if (isset($__POST['flowers'],$_POST['nrflowers'], $_POST['type'])) {
	$nrflowers = $_POST['nrflowers'];
	$type = $_POST['type'];
	$flowers = $__POST['flowers'];

	print("hello this is php!!")

  $output=shell_exec('python ./backend/GetFormFromHTML.py' .$nrflowers, .$type);
    echo $output;
?>