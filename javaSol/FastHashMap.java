import java.util.Scanner;
import java.util.HashMap;

public class FastHashMap
{
    public static void main(String[] args)
    {
	Scanner S= new Scanner(System.in);
	int N = Integer.parseInt(S.nextLine());
	long[] vals = new long[N];
	for(int i= 0; i < N; i+= 1) vals[i] = Long.parseLong(S.nextLine());

        HashMap<Long,Integer>H = new HashMap<Long,Integer>();
	for (int j = 0; j < N; j+= 1) // i goes through {0, ..., N-1}
	    for (int i = 0; i<j; ++i) 
                H.putIfAbsent(vals[i]+vals[j],j);
        
	for (int l = 0; l < N; l+= 1) // i goes through {0, ..., N-1}
	    for (int k = 0; k<l; ++k) {
                Integer jj = H.get(-vals[l]-vals[k]);
                if (jj != null && jj < k) {
                    System.out.println("true");
                    System.exit(0);                    
                }
            }
        System.out.println("false");
    }
}
