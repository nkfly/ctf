<?php 
$test = 1;
$args = ['0' => 'aa%0Ash'];
print "implode " . implode(" ", $args);
print "\n";

for ( $i=0; $i<count($args); $i++ ){
	print $args[$i];
	print "\n";
        if ( !preg_match('/^\w+$/', $args[$i]) ) {
        	print "before exit\n";
            exit();

        }
        	
    }

exec(implode(" ", $args));
print "count " . count($args);
print "\n";
print "implode " . implode(" ", $args);
print "\n";
print 'hello';
print "\n";
?>
