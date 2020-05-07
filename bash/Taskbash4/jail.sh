#!/bin/bash
figlet "BASH JAIL 4"
echo "Welcome To lvl4"
while true;do
read -p ">> " input ;
if echo $input| grep -i -E "cat|ls|sh|bash|head|tail|vi|ed|vim" ;then 
        exec 1>&2
        echo "Heey man it's a jail, it won't be that easy o//"
        exit
fi
exec 1>/dev/null && exec 2>/dev/null
eval $input
done
