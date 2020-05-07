#!/bin/bash
figlet "BASH JAIL 3"
echo "Welcome To lvl3"
while true;do
read -p ">> " input ;
if echo $input| grep -i -E "cat|ls|sh|bash|head|tail|vi|vim|flag" ;then 
        exec 1>&2
        echo "Heey man it's a jail, it won't be that easy o//"
        exit
fi
eval $input
done
