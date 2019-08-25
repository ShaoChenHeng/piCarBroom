#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

int W,H,N;
int X1[1000],X2[1000],Y1[1000],Y2[1000];
int fld[1000][1000];

int compress( int *x1, int *x2, int w )
{
    vector<int> xs;
    for( int i = 0; i < N; i++ )
    {
        for( int d = -1; d <= 1; d++ )
        {
            int tx1 = x1[i] + d;
            int tx2 = x2[i] + d;
            if ( 1 <= tx1 && tx1 <= w ) xs.push_back( tx1 );
            if ( 1 <= tx2 && tx2 <= w ) xs.push_back( tx2 );
        }
    }
    sort( xs.begin(), xs.end() );
    xs.erase( unique( xs.begin(), xs.end() ), xs.end() );

    for( int i = 0; i < N; i++ )
    {
        x1[i] = find( xs.begin(), xs.end(), x1[i] ) - xs.begin();
        x2[i] = find( xs.begin(), xs.end(), x2[i] ) - xs.begin();
    }

    return xs.size();
}

int compress2(int *xx1,int *xx2,int w)//开始坐标，结束坐标 
{
	vector<int>v;
	
	for(int i=0;i<N;i++){
        for(int d=-1;d<=1;d++)
            {
                int nx1=xx1[i]+d;
                int nx2=xx2[i]+d;
                if(nx1>=1&&nx1<=w) v.push_back(nx1);
                if(nx2>=1&&nx2<=w) v.push_back(nx2);
            }
    }//将横线本身以及附近两横线存储 
	
	//去重
	sort(v.begin(),v.end());
	v.erase(unique(v.begin(),v.end()),v.end()); 
	 
	//离散化后的坐标
	for(int i=0;i<N;i++)
	{
		xx1[i]=find(v.begin(),v.end(),xx1[i])-v.begin();
		xx2[i]=find(v.begin(),v.end(),xx2[i])-v.begin();
	 } 
	return v.size();	
}

/* 
0000100000
0000100000
1111111111
0000100000
0000100000 

10 5 2
1 5
10 5
3 1
3 5

10 10 5
1 1 4 9 10
6 10 4 9 10
4 8 1 1 6
4 8 10 5 10


*/


int main()
{
    scanf("%d %d %d", &W,&H,&N);
    for ( int j = 0; j < N; j ++ ) scanf("%d",&X1[j]);
    for ( int j = 0; j < N; j ++ ) scanf("%d",&X2[j]);
    for ( int j = 0; j < N; j ++ ) scanf("%d",&Y1[j]);
    for ( int j = 0; j < N; j ++ ) scanf("%d",&Y2[j]);
    //printf( "%d ", compress2( X1, X2, W ) );
    //printf( "%d ", compress2( Y1, Y2, H ) );
    memset(fld,0,sizeof(fld));

    W = compress( X1, X2, W ) ;
    H = compress( Y1, Y2, H );
    for ( int i = 0; i < N; i++ )
    {
        for ( int y = Y1[i]; y <= Y2[i]; y ++ )
        {
            for ( int x = X1[i]; x <= X2[i]; x ++ )
            {
                fld[y][x] = 1;
            }
        }
    }
        printf("\n");
        printf("\n");
    
    for(int i=0;i<H;i++)
		 {
		 	for(int j=0;j<W;j++)
		 	{
		 		if(fld[i][j])cout<<1<<" ";
		 		else cout<<0<<" ";
			 }
			 cout<<endl;
		 }

    return 0;
}
