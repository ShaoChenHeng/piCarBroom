#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct _TONE{
	int freq;
	int t_ms;
} TONE,*PTONE;

#define ONESEC 600/2

#define SO0 1498
#define LA0 1772
#define XI0 1967
#define DO 2093
#define DOsharp 2221
#define RE  2349
#define MI 2637
#define FA 2794
#define SO 3136
#define LA 3520
#define XI 3951
#define DO1 4186
#define RI1 4698

TONE star_notation[]=
{
	{SO0,ONESEC},
	{DO,ONESEC},
	{RE,ONESEC},

	{MI, ONESEC},
	{SO0,ONESEC},
	{DO,ONESEC*2},
	//{SO0,ONESEC},

	{784,ONESEC},
	{RE,ONESEC},
	{MI, ONESEC},
	{SO,ONESEC},

	{LA,ONESEC},
	{LA0,ONESEC},
	{RE,ONESEC},
	{XI0,ONESEC},

	{DOsharp,ONESEC*4},
};


void beep(int freq,int t_ms)
{
	int range;
	if(freq<10||freq>5000)
	{
		printf("invalid freq");
		return;
	}
	range=600000/freq;
	pwmSetRange(range);
	pwmWrite(23,range/2);
	if(t_ms>0)
	{
		delay(t_ms);
	}
}

void init()
{
	if (wiringPiSetup () == -1)
		exit (1) ;
	pinMode (23, PWM_OUTPUT) ;
	pwmSetMode(PWM_MODE_MS);
	pwmSetClock(45);
}



int main (void)
{
	int index=0 ;

	init();

	for (;index<sizeof(star_notation)/sizeof(TONE);index++) 
	{
		beep(star_notation[index].freq,star_notation[index].t_ms);
		pwmWrite(23,0);
		delay(5);
	}

	pwmWrite(23,0);


	return 0 ;
}

