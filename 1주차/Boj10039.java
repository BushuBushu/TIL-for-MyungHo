import java.util.*;

public class Boj10039 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] array = new int[5];
		for(int i = 0; i<array.length; i++) {
			array[i] = sc.nextInt();
		}
		
		int sum = 0;
		for(int i = 0; i<array.length; i++) {
			sum += array[i] >= 40 ? array[i] :40;
		}
		int avg = sum / 5;
		System.out.println(avg);
	}

}
