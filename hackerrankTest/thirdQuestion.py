3.  write a function that takes in an array as input removes any duplicate found in the array and returns 
the resulting array without any duplicate

Answer:

<?php
$a=array("a"=>"red","b"=>"green","c"=>"red");
print_r(array_unique($a));
?>