
fun getStringLength(obj: Any): Int?{
  if (obj is String){
    return obj.length
  }
  return null
}

fun main(args: Array<String>){
  fun printLength(obj: Any){
    println("'$obj' string length is ${getStringLength(obj) ?: "...error not a string"}")
  }
  printLength("Incomprehensibilities")
  printLength(1000)
  printLength(listOf(Any()))
}
