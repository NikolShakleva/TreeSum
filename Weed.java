import java.util.Random;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class Weed
{

	public static long mynextLong(Random R) {
		return R.nextLong() / 4;
	}
    public static void main(final String[] args) {
		final int N = Integer.parseInt(args[0]);
		final List<Long> vals = new ArrayList<>();

		final Random R = new Random(Integer.parseInt(args[1]));
		if(args.length > 1){
			R.setSeed(Long.parseLong(args[1]) + N);			
		} 

		vals.add(mynextLong(R));
		vals.add(mynextLong(R));
		// vals.add(-(vals.get(0) + vals.get(1) ));
		vals.add(mynextLong(R));
		// if ( R.nextBoolean())  vals.set(2,vals.get(2)+1);
		for (int i = 3; i<N; ++i)
				vals.add(mynextLong(R));
		
		Collections.shuffle(vals,R);

		System.out.println(N);
		for (int i = 0; i<N; ++i) System.out.println(vals.get(i));

//	for (int i = 0; i<N; ++i)
//	    for (int j = i+1; j<N; ++j)
//		for (int k = j+1; k<N; ++k)
//		    for (int l = k+1; l<N; ++l)
//			if (vals.get(i) + vals.get(j) + vals.get(k) + vals.get(l) == 0) 
//			{
//			 System.out.println(i+" "+j+" "+k+" "+l);
//			 //System.exit(0);
//			}
    }
}
