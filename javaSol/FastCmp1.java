import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class FastCmp1
{
    private static int N;
    private static long[] vals;
    private static boolean running = true;
    static synchronized void found(long sum, int ii, int jj) {
        if(running){
            running = false;
            int i=0,j, k,l=N-1;
            if(ii<jj) {j =-ii;k=jj; } else {j=-jj; k=ii;}
            assert(0<=ii && ii < jj && jj< N ) ; //
            System.err.println(i+" "+j+" "+k+" "+l);
            while( vals[i] +vals[j] != sum ) i++;
            while( vals[k] +vals[l] != -sum ) l--;
            System.out.println("true");
            System.err.println(i+" "+j+" "+k+" "+l);
            System.err.println(String.format("[%d,%d,%d,%d] %d+%d+%d+%d=%d",
                                             i,j,k,l,vals[i],vals[j],vals[k],vals[l],
                                             vals[i]+vals[j]+vals[k]+vals[l]));
            System.exit(0);
        }
    }    
    static class pair implements Comparable<pair> {
        public final long sum;
        public final int i;
        public pair(int ii, long sm) {
            sum = sm; i=ii; }
        public int compareTo( pair b) {
            if(sum > b.sum) return 1;
            if(sum < b.sum) return -1;
            if( (i^(b.i) ) < 0 && i+b.i > 0 )  // xor of sign bit -- negative means different
                found(sum,i,b.i);
            return i - b.i;
        }
    }
    public static void main(String[] args)
    {
	Scanner S= new Scanner(System.in);
        N = Integer.parseInt(S.nextLine());
        vals = new long[N];
	for(int i= 0; i < N; i+= 1) vals[i] = Long.parseLong(S.nextLine());

        pair [] pp = new pair[N*(N-1)];

        int p=0;
	for (int i = 0; i < N; i+= 1) // i goes through {0, ..., N-1}
	    for (int j = i+1; j<N; ++j) {
                pp[p++] = new pair(-j, vals[i]+vals[j]);
                pp[p++] = new pair(i, -vals[i]-vals[j]);
            }
        System.err.println("inserted");
        //        Arrays.sort(pp);
        Arrays.parallelSort(pp);
        System.out.println(false);
    }
}
