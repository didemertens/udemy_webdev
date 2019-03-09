// function helloYou(name){
//   console.log("Hello "+name);
// }

function addNum(num1=0, num2=0){
  console.log(num1 + num2);
}

function formal(name="Sam", title="Sir") {
  return title + " " +name;
}

//Local scope function

function timesFive(numInput){
  var result = numInput * 5
  return result
}

//Global scope

var v = "Global V"
var stuff = "Global Stuff"

function fun(stuff) {
  console.log(v);
  stuff = "Reassing stuff inside func"
  console.log(stuff);
}

fun()
console.log(stuff)
