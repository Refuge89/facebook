#!/bin/bash

var=673298000

while :	;
	var=$((var+1));
do python facebook.py $var; 
	sleep 1; done
