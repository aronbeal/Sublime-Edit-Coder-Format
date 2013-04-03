<?php
// $Id$

require "./coder_format.inc";
$buffer = file_get_contents('php://stdin');
$stdout = fopen('php://stdout', 'w');
fwrite($stdout, coder_format_string_all($buffer));
fclose($stdout);
exit(0);

