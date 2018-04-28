//Allowed variable declaration techniques


fun main(args: Array<String>){
  val a: Int = 2
  val b = 3
  val c: Int
  c = 5
  var x = 6
  x += 1
  println("a = $a, b = $b, c = $c, x = $x")
  callback()

}
val PI = 3.14 // top level variables
var y = 0

fun incrementX(){
  y += 1
}
fun callback(){
  println("y = $y, PI = $PI")
  incrementX()
  println("incrementX()")
  println("y = $y, PI = $PI")
}
