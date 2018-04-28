//on string templates and information
fun main(args: Array<String>){
  var a = 1
  //simple name in template
  val s1 = "a is $a"

  a = 2
  val s2 = "${s1.replace("is", "was")}, but now is $a"
  println(s2)

}
