The script reads the input file, which contains data, separated by a space: 
-the names of the files to be checked
-the hash algorithm (one of MD5/SHA1/SHA256) 
-their hash sums
Then checks the integrity of the files in the directory specified in the call

sample call:
<script> <path to input file> <path to the directory containing the files to check>