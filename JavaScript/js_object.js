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

myObj.greet()
