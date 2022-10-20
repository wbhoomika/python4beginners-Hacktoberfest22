import java.util.Scanner;

public class fibonacciSeries {
    //recursive method
    static int n1=0, n2=1, n3;
    static void fibonacci(int x){
        if(x>0){
            n3=n1+n2;
            n1=n2;
            n2=n3;
            System.out.print(", "+n2);
            fibonacci(x-1);
        }
    }
    public static void main(String[] args) {
        //using loop
        System.out.println("Enter number of fibonacci elements : ");
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int t1=0, t2=1, t3;
        System.out.print(t1+", "+t2);
        for(int i=2; i<n;i++){
            t3=t1+t2;
            System.out.print(", "+t3);
            t1=t2;
            t2=t3;
        }
        System.out.println();

        //using recursion
        System.out.print(n1+", "+n2);
        fibonacci(n-2); //n-2 becoz two terms are already printed
        System.out.println();

        //using for loop
        int a = 10, firstTerm = 0, secondTerm = 1;
        System.out.println("Fibonacci Series till " + a + " terms:");
        for (int i = 1; i <= a; ++i) {
            System.out.print(firstTerm + ", ");
            // compute the next term
            int nextTerm = firstTerm + secondTerm;
            firstTerm = secondTerm;
            secondTerm = nextTerm;
        }
        System.out.println();

        //using while loop
        int i=1, term1=0, term2=1;
        while(i<=a){
            System.out.print(term1 + ", ");

            int term3 = term1 + term2;
            term1 = term2;
            term2 = term3;
            i++;
        }
    }
}
