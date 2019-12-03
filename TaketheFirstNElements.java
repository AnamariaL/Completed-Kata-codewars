/*Description:
Create a method take that accepts a list/array and a number n,
 and returns a list/array array of the first n elements from the list/array.*/
import java.util.Arrays; 

public class TaketheFirstNElements {

	
	  public static int[] take(int[] arr, int n) {
	    int[] a = Arrays.copyOf(arr, n); 
	    return  n > arr.length ? arr :a;
	    
	   }
	
}
