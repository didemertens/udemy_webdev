var carInfo = {make:"Toyota",year:1990,model:"Camry"}

carInfo["make"]

carInfo['year'] = 2005
carInfo['year'] += 2

// for (key in carInfo){
//   console.log(key);
//   console.log(carInfo[key]);
// }

var myNewO = {a:"hello", b:[1,2,3], c:{inside:['a','b']}}

myNewO['a']
myNewO['b'][1]
myNewO['c']['inside'][1]

var simple = {
  prop : "Hello",
  myMethod : function(){
    console.log("The myMethod was called")
  }
}

// simple.myMethod()

var myObj = {
  name : "Dide",
  greet : function(){
    console.log("Hello " + this.name)
  }
}

// myObj.greet()

// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength : function(){
    console.log(this.name.length)
  }
}

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employ = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  report : function(){
    alert("Name is " + this.name + ", Job is " + this.Job + ", Age is " + this.age)
  }
}


// // Write program that will create an Alert in the browser of each of the
// // object's values for the key value pairs. For example, it should alert:

// // Name is John Smith, Job is Programmer, Age is 31.



// ///////////////////
// // PROBLEM 3 /////
// /////////////////

// // Given the object:
var employeeThree = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName : function(){
    console.log(this.name.split(" ")[1])
  }
}

// // Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
