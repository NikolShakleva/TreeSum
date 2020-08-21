import java.util.Scanner;
import java.util.HashMap;

public class HashTriples
{
    public static void main(String[] args)
    {
        HashMap<Long,Integer>H = new HashMap<Long,Integer>();

	Scanner S= new Scanner(System.in);
	int N = Integer.parseInt(S.nextLine());
	long[] vals = new long[N];
	for(int i= 0; i < N; i+= 1) {
            vals[i] = Long.parseLong(S.nextLine());
            H.put(vals[i],i);
        }

        // the variables are ordered l < k < j < i; sorry
        for (int i = 0; i<N; ++i) 
            for (int j = 0; j < i; j+= 1) // i goes through {0, ..., N-1}
                for (int k = 0; k<j; ++k) {
                    Integer l = H.get(-vals[i]-vals[j]-vals[k]);
                    if (l != null && l<k ) {
                        System.out.println("true");
                        System.exit(0);                    
                    }
                }
        System.out.println("false");
    }
}
