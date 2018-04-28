//various ways of defining functions
fun sum(a: Int, b: Int): Int {
  return a + b
}

fun new_sum(a: Int, b: Int) = a + b

fun print_sum(a: Int, b: Int): Unit{
  println("sum of $a and $b is ${a + b}")
}
fun main(args: Array<String>){
  print("Sum of 3 and 5 is ")
  println(sum(3, 5))
  println("sum of 19 and 23 is ${new_sum(19, 23)}")
}
