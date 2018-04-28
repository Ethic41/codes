fun describe(obj: Any): String =
when (obj){
  1 -> "One"
  "Hello" -> "Greetings"
  is Long -> "Long"
  !is String -> "Not a String"
  else -> "Unknown"
}
fun main(args: Array<String>){
  println(describe(1))
  println(describe("Hello"))
  println(describe(1000L))
  println(describe(2))
  println(describe("other"))
}
