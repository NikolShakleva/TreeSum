import java.util.Scanner;
import java.util.HashMap;

public class HashPairs
{
    public static void main(String[] args)
    {
        HashMap<Long,Integer>H = new HashMap<Long,Integer>();

    Scanner S = new Scanner(System.in);
     //Scanner S = new Scanner("3\n10\n10\n-20");
	int N = Integer.parseInt(S.nextLine());
	long[] vals = new long[N];
	for(int i= 0; i < N; i+= 1) {
        vals[i] = Long.parseLong(S.nextLine());
        H.put(vals[i],i);
    }

        // the variables are ordered l < k < j < i; sorry
        for (int i = 0; i<N; ++i) 
            for (int j = 0; j < i; j+= 1) {// i goes through {0, ..., N-1}
                Integer l = H.get(-vals[i]-vals[j]);
                if (l != null && j<l ) {
                    // if you dont have the && j<l then the code will execute found
                    // without you having a triple. You might have a double and the code will execute
                    // found as you had a triple
                    System.out.println("Found");
                    System.exit(0);                    
                }
            }
        System.out.println("None");
    }
}
