fun maxOf(a: Int, b: Int): Int {
  if (a > b){
    return a
  }
  else{
    return b
  }
}

fun main(args: Array<String>){
  println("max of 0 and 42 is ${maxOf(0, 42)}")
}

fun maxOf(a: Int, b: Int) = if (a > b) a else b
