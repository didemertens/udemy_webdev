alert("Hello there! Can you answer these questions?")

var first_name = prompt("What is your first name?")
var last_name = prompt("What is your last name?")
var age = prompt("How old are you?")
var height = prompt("How tall are you?")
var pet = prompt("What is the name of your pet?")

alert(("Thanks for the information!"))

var namecond = null
var agecond = null
var heightcond = null
var petcond = null

if (first_name[0] === last_name[0]){
    namecond = true;
  }else {
    namecond = false;
  }

if (age > 20 && age <30){
    agecond = true;
  }else {
    agecond = false;
  }

if (height >= 170){
    heightcond = true;
  }else {
    heightcond = false;
  }

if (pet[pet.length-1] === "y"){
    petcond = true;
  }else {
    petcond = false;
  }

if (namecond && agecond && heightcond && petcond){
  console.log("The code is 456.")
  }else {
    console.log("Nothing here.")
  }

console.log(namecond)
console.log(petcond)
console.log(heightcond)
console.log(petcond)
