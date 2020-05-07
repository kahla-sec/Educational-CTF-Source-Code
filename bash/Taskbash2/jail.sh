#!/bin/bash
figlet "BASH JAIL 2"
echo "Welcome To lvl2"
while true;do
read -p ">> " input ;
if echo $input| grep -i -E "cat|ls|sh|bash|head|tail|vi|vim" ;then 
        exec 1>&2
        echo "Heey man it's a jail, it won't be that easy o//"
        exit
fi
eval $input
done
