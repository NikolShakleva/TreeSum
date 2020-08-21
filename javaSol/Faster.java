import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
 
import java.util.Arrays;
 
public class Faster {
    private static int binarySearch(long[] a, long key) {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if      (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }
 
    public static void main(String[] args) {
        int l = 0;
        int N = StdIn.readInt();
        long[] a = StdIn.readAllLongs();
        Arrays.sort(a);
 
        for (int i = 0; i < N; i++)
            for (int j = i + 1; j < N; j++)
                for (int k = j + 1; k < N; k++) {
                    l = binarySearch(a, -a[i] - a[j] - a[k]);
                    if (l > k) {
                        if (a[i] + a[j] + a[k] + a[l] == 0) {
                            System.err.println(i+" "+j+" "+k+" "+l);
                            StdOut.println(true);
                            System.exit(0);
                        }
                    }
                }
        StdOut.println(false);
    }
}
