<?php
require "./coder_format.inc";
$buffer = file_get_contents('php://stdin');
$stdout = fopen('php://stdout', 'w');
fwrite($stdout, coder_format_string_all($buffer));
fclose($stdin);
fclose($stdout);
exit(0);

