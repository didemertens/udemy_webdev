alert("Hello there! Can you answer these questions?")


var spy = false;

var first_name = prompt("What is your first name?")
var last_name = prompt("What is your last name?")

if (first_name[0] === last_name[0]){
    spy = true;
  }else {
    spy = false;
  }

var age = prompt("How old are you?")

if (age > 20 && age <30){
    spy = true;
  }else {
    spy = false;
  }

var height = prompt("How tall are you?")

if (height >= 170){
    spy = true;
  }else {
    spy = false;
  }

var pet = prompt("What is the name of your pet?")

if (pet[-1] === "y"){
    spy = true;
  }else {
    spy = false;
  }

if (spy = true){
    console.log("The code is 456.")
  }else {
    console.log("Nothing here.")
  }

alert(("Thanks for the information!"))
