import java.util.Scanner;

public class Simple
{
    public static void main(String[] args)
    {
	Scanner S= new Scanner(System.in);
	int N = Integer.parseInt(S.nextLine());
	long[] vals = new long[N];
	for(int i= 0; i < N; i+= 1) vals[i] = Long.parseLong(S.nextLine());

	for (int i = 0; i < N; i+= 1) // i goes through {0, ..., N-1}
	    for (int j = i+1; j<N; ++j)
			for (int k = j+1; k<N; ++k)
				if (vals[i] + vals[j] + vals[k] == 0) 
				{
					System.err.println(i+":"+vals[i]+" "+j+":"+vals[j]+" "+k+":"+vals[k] );
					System.out.println("Found");
					System.exit(0);
				}
        System.out.println("None");
    }
}
