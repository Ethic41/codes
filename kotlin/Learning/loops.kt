//for loops
fun main(args: Array<String>){
  val items = listOf("rock", "paper", "scissors")
  for (item in items){
    println(item)
  }
  loop_index()
}

fun loop_index(){
  val items = listOf("tahir", "phaux", "Raliya")
  for (item in items.indices){
    println("Positions: $item ==> ${items[item]}")
  }
  loop_while()
}

//while loops
fun loop_while(){
  val items = listOf("an", "at", "am")
  var index = 0
  while (index < items.size){
    println("item at $index is ${items[index]}")
    index++

  }
}
