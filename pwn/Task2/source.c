#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void ignore_me_init_buffering() {
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stdin, NULL, _IONBF, 0);
        setvbuf(stderr, NULL, _IONBF, 0);
}

void menu(){
	printf("1- Naruto\n");
	printf("2- Kimetsu No yaiba\n");
	printf("3- Fate Zero\n");
}

void lose(){
	printf("You dont deserve me\n");
}

void naruto(){
	char buff[65];
	printf("OOOW we are friends now ! Here is your gift :D Raasengan\n"); 
	printf("Tell me your name before you die: ");
	read(0,buff,64);
	printf("Shiiiinee ");
	printf(buff);
}

int main(void){
	ignore_me_init_buffering() ;
	char buffer[10];
	printf("Choose your best anime please! I'll give you a gift if we have the same taste \\o/\n\n");
	menu();
	printf("Number: ");
	fgets(buffer,9,stdin);
	if (strcmp(buffer,"1\n")==0)
		naruto();
	else
		lose();

return 0;
}
