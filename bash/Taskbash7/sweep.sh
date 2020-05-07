#!/bin/bash
# Header
header(){
	figlet SYSN00B
}
# Menu
read -r -d '' MENU << EOM
\nDisclaimer: This tool is only for N00b Sysadmins , young hackers stay way! \n
Welcome To our land! choose what you want to do \n
1-) List all files in a directory \n
2-) Monitor the running processes \n
3-) Nothing \n
EOM

list(){
read -p "Choose the directory you want to list: " dir
if echo $dir |grep -i -E ";|\`|&|\|";then
        echo -ne "Script kiddies stay away please!\n"
        exit
else
	eval ls -la $dir
	exit
fi
}

monitor(){
	echo -ne "Here are the current processes Maaster\n"
	eval ps
}
choose(){
	case "$1" in
		1)
		list
		;;
		2)
		monitor
		;;
		3)
		echo -ne "Okay as you want Bye Bye"
		exit
		;;
		*) 
		echo -ne "Good Bye! You cant even choose a number ?\n"
		exit
		;;
	esac
}

# Main

header
echo -en $MENU
read -p "Choose your option please >> " input
choose $input	
	
