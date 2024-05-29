namespace Factorials
{
    class Factorial {
        static void Main(int[] args)
        {
            var output = args;
            var range = new Range(1, output);
            for(int i=output; i<=range; i++)
            {
                output *= i;
            }
            System.Console.WriteLine(output);
            return output;
        }
    }
}