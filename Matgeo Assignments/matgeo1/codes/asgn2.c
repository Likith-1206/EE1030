struct points{
    int A[2];
    int B[2];
	int P[2];
	int Q[2];
};

struct points get(){
    struct points temp;
    temp.A[0] = 7 ;
    temp.A[1] = -2;
    temp.B[0] = 1;
    temp.B[1] = -5;
	temp.P[0] = 5;
	temp.P[1] = -3;
	temp.Q[0]=3;
	temp.Q[1]=-4;
    return temp;
}
