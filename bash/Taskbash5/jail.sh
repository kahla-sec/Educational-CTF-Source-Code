#!/bin/bash
figlet "BASH JAIL 5"
while true;do
read -p ">> " input ;
if echo $input| grep -i -E " |/bin/bash|bash|sh|/bin/sh|flag|cat|flag.txt|vi|ed|vim|<" ;then 
	exec 1>&2
	echo "Heey man it's a jail, it won't be that easy o//"
	exit
fi
eval $input 1>/dev/null
done
