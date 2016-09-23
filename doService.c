#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>
#include<time.h>

char *UpdateDB = "python UpdateDB.py";
char *FacebookUpload = "python FacebookUpload.py";
char* makeDumpSQL="mysqldump -uroot -p1234 -h 218.150.181.131 link10th > ./dumps/%d%d%d.sql";

void call_UpdateDB(int sig);
void call_FacebookUpload(int sig);

int main(void)
{
	signal(SIGALRM, call_UpdateDB);
	alarm(24*60*60+18*60);
	// alarm(1);
	while(1);

	return 0;
}

void call_UpdateDB(int sig)
{
	if(sig==SIGALRM){
		system(UpdateDB);
		signal(SIGALRM, call_FacebookUpload);
		puts("\n>>> After 30min second call UpdateDB.py \n");
		alarm(30*60);
	}
}
void call_FacebookUpload(int sig){
	if(sig==SIGALRM){
		system(FacebookUpload);
		signal(SIGALRM, call_UpdateDB);
		puts("\n>>> After 23h 30min call UpdateDB.py \n");

		struct tm *t;
		time_t timer;

		timer=time(NULL);
		t=localtime(&timer);
		
		char buf[300];
		sprintf(buf,makeDumpSQL,t->tm_year+1900,t->tm_mon+1,t->tm_mday);
		system(buf);
		printf("%d/%d/%d %d:%d:%d dump파일 생성\n",t->tm_year + 1900, t->tm_mon + 1,t->tm_mday,t->tm_hour,t->tm_min,t->tm_sec);

		alarm(23*60*60 + 30*60);
	}
}
