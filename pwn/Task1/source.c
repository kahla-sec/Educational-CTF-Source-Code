#include <stdio.h>
#include <stdlib.h>
void ignore_me_init_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}
void print_header(){
printf(" ____    _  _____ _____   ____  ____   ___   ____ \n");
printf("|  _ \\  / \\|_   _| ____| |  _ \\|  _ \\ / _ \\ / ___|\n");
printf("| | | |/ _ \\ | | |  _|   | |_) | |_) | | | | |  _ \n");
printf("| |_| / ___ \\| | | |___  |  __/|  _ <| |_| | |_| |\n");
printf("|____/_/   \\_\\_| |_____| |_|   |_| \\_\\\\___/ \\____|\n\n\n");
}

void print_flag(){
char ch;
FILE *fp;
printf("Woow how did u changed it ?");
fp=fopen("flag.txt","r");
if (fp == NULL)
   {
      perror("Flag.txt not found! Try this on the server.\n");
      exit(EXIT_FAILURE);
   }
while((ch = fgetc(fp)) != EOF)
      printf("%c", ch);
fclose(fp);
}

int main(void){
ignore_me_init_buffering();
print_header();
char buff[60];
int win=0xffffffff;
printf("Okay I will help you :D win is at %p\n",&win);
printf("Enter your name i want to know you ;) ");
fgets(buff,59,stdin);
printf("Nice to meet you ");
printf(buff);
if (win==0xdeadfeed){
	print_flag();
}
else {
printf("your name is good but u are not a good hacker!\nwin is still %x\n",win);
}
return 0;
}
