
fun main(args: Array<String>){
  val y = 9
  for (i in 1..y+1){
    print("fits")
    println(" in")
  }
  checkOutOfRange()
}

fun checkOutOfRange(){
  val items = listOf('a', 'b', 'c')
  if (-1 !in 0..items.lastIndex){
    println("item is out of range")
  }
  if (items.size !in items.indices){
    println("list size is out of valid list indices range too")

  }
  last()
}

fun last(){
  for (x in 1..5){
    println(x)
  }

  for (x in 1..10 step 2){
    print(x)
  }
  println()

  for (x in 9 downTo 0 step 3){
    println(x)
  }
}
