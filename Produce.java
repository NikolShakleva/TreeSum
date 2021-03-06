import java.util.Random;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class Produce
{

	public static long mynextLong(Random R) {
		return R.nextLong() / 4;
	}
    public static void main(final String[] args) {
		 final String mode = args[0];
		//final String mode = "plant";
		 final int N = Integer.parseInt(args[1]);
		//final int N = 10;
		final Random R = new Random();
		 R.setSeed(Long.parseLong(args[2]) + N);	
		//R.setSeed(Long.parseLong("12" + N));
		
	//if two instances of Random are created with the same seed, and the same sequence of
	// method calls is made for each, they will generate and return identical sequences of numbers.
	//In order to guarantee this property, particular algorithms are specified for the class Random.
	//Java implementations must use all the algorithms shown here for the class Random, for the sake
	//of absolute portability of Java code. However, subclasses of class Random are permitted to use other algorithms, 
	//so long as they adhere to the general contracts for all the methods.

		if( N <= 3) {
			System.err.println("N is too small: "+N);
			System.exit(1);
		}

		final List<Long> vals = new ArrayList<>();

		vals.add(mynextLong(R));
		vals.add(mynextLong(R));

		switch (mode) {
			case "no": vals.add(mynextLong(R));
				break;
			case "plant": vals.add(-vals.get(0)-vals.get(1));
				break;
			case "mistake":  vals.add(-2*vals.get(0));
				break;
			default:
				System.err.println("Unknown mode: "+mode);
		}
		for (int i = 3; i<N; ++i)
			vals.add(mynextLong(R));
		
		Collections.shuffle(vals,R);

		System.out.println(N);
		for (int i = 0; i<N; ++i) System.out.println(vals.get(i));
    }
}
