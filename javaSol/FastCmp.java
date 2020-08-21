import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class FastCmp
{
    private static long[] vals;
    private static boolean running = true;
    static synchronized void found(int i, int j, int k, int l) {
        if(running){
            running = false;
            System.out.println("true");
            //            System.err.println(i+" "+j+" "+k+" "+l);
            System.err.println(String.format("[%d,%d,%d,%d] %d+%d+%d+%d=%d",
                                             i,j,k,l,vals[i],vals[j],vals[k],vals[l],
                                             vals[i]+vals[j]+vals[k]+vals[l]));
            System.exit(0);
        }
    }    
    static class pair implements Comparable<pair> {
        public final long sum;
        public final int i,j;
        public pair(int ii, int jj, long sm) {
            assert( ii < jj);
            sum = sm; i=ii; j=jj; }
        public int compareTo( pair b) {
            if(sum > b.sum) return 1;
            if(sum < b.sum) return -1;
            //            int  k=b.i, l=b.j;
            //            if( i!=k && i!=l && j!=k && j!=l )
            if( j<b.i && 0 == vals[i]+vals[j]+vals[b.i]+vals[b.j])
                found(i,j,b.i,b.j);
            return 0;
        }
    }
    public static void main(String[] args)
    {
	Scanner S= new Scanner(System.in);
	int N = Integer.parseInt(S.nextLine());
        vals = new long[N];
	for(int i= 0; i < N; i+= 1) vals[i] = Long.parseLong(S.nextLine());

        pair [] pp = new pair[N*(N-1)];

        int p=0;
	for (int i = 0; i < N; i+= 1) // i goes through {0, ..., N-1}
	    for (int j = i+1; j<N; ++j) {
                pp[p++] = new pair(i,j, vals[i]+vals[j]);
                pp[p++] = new pair(i,j, -vals[i]-vals[j]);
            }
        //System.err.println("inserted");
        //        Arrays.sort(pp);
        Arrays.parallelSort(pp);
        for(int q=0;q<pp.length-1;q++){
            int r=q+1;
            while( r < pp.length && pp[q].sum == pp[r].sum ) {
                int i=pp[q].i, j=pp[q].j, k=pp[r].i, l=pp[r].j;
                if( j<k && 0 == vals[i]+vals[j]+vals[k]+vals[l])
                    found(i,j,k,l);
                q++;
            }
        }
        System.out.println(false);
    }
}
