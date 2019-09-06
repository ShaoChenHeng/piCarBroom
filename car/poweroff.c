#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct _TONE{
	int freq; 
	int t_ms;
	//控制单个音的音高和速度
} TONE,*PTONE;

#define ONESEC 800/2
//控制总速度

//音高宏定义
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

//谱子
TONE star_notation[]=
{
{XI,ONESEC},
    {LA,ONESEC},
    {SO,ONESEC},    
    {SO-126,ONESEC}, 
    
    {SO,ONESEC},
    {LA,ONESEC},
    {MI,ONESEC*2},

    {LA/2,ONESEC},    
    {DOsharp,ONESEC},
    {MI,ONESEC},
    {SO+135,ONESEC*2},
};


void beep(int freq,int t_ms)
{
	int range;
	if(freq < 10 || freq > 5000)//可自定义freq所在区间，根据实际蜂鸣器的“音域”来调整
	{
		printf("invalid freq");//说明这个音已经听不见了
		return;
	}
	range=500000/freq; //控制总音高
	pwmSetRange(range);
	pwmWrite(23,range/2);//23是wiringPi定义的gpio接口编号
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
	pwmSetClock(45);//延音
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

