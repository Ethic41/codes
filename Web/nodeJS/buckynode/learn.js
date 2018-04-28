var strategy = require("./game")
var action = require("./game")
/* ---Multiple Request Handling---
function placeOrder(orderNumber){
  console.log("Placed Order "+orderNumber);
  cook_deliverOrder(function(){
    console.log("Delivered Order:"+orderNumber);
  });
}

function cook_deliverOrder(callback){
  setTimeout(callback, 1);
}
placeOrder(1);
placeOrder(2);
placeOrder(3);
placeOrder(4);
placeOrder(5);
*/

/* ---Reference To Object---
var tahir = {
  name:"Taheer",
  age:"21",
  class:"400"
}

var person = tahir;
person.age = "24";
console.log(tahir.age)
*/
/* ==
var object = {
  printfirst: function(){
    console.log("Object is here...");
    console.log(object === this);
  }
}

function anon(){
  console.log("Anonymous...");
  console.log(this === global);
}
object.printfirst();
anon();
*/

/*
function Player(){
  this.name = "";
  this.life = 100;
  this.giveLife = function giveLife(target){
    target.life += 1;
    this.life -= 1;
    console.log(this.name+" Gave one life to "+target.name);
  }
}

var Bucky = new Player;
var Wendy = new Player;
Bucky.name = "Bucky";
Wendy.name = "Wendy";
Bucky.giveLife(Wendy);
console.log(Bucky.life);
console.log(Wendy.life);

Player.prototype.kick = function kick(target){
  target.life -= 3;
  this.life += 1;
  console.log(this.name+" has kicked "+target.name);
};

Bucky.kick(Wendy);
console.log(Bucky.life);
console.log(Wendy.life);

Player.prototype.magic = 15;
console.log(Bucky.magic);
console.log(Wendy.magic);
*/
/* ---Modules---
strategy.strategy();
action.action();
*/
