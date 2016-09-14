#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>
char *UpdateDB = "python UpdateDB.py";
char *FacebookUpload = "python FacebookUpload.py";

void call_UpdateDB(int sig);
void call_FacebookUpload(int sig);

int main(void)
{
	signal(SIGALRM, call_UpdateDB);
	alarm(11*60*60);
	while(1);

	return 0;
}

void call_UpdateDB(int sig)
{
	if(sig==SIGALRM){
		system(UpdateDB);
		signal(SIGALRM, call_FacebookUpload);
		puts("\n\n---------- After 30min second call UpdateDB.py ----------\n\n");
		alarm(30*60);
	}
}
void call_FacebookUpload(int sig){
	if(sig==SIGALRM){
		system(FacebookUpload);
		signal(SIGALRM, call_UpdateDB);
		puts("\n\n---------- After 23h 30min call UpdateDB.py ----------\n\n");
		alarm(23*60*60 + 30*60);
	}
}
