function addStudent(name,array){
  array.push(name)
}

function delStudent(name, array){
  for (var i = 0; i < array.length; i++) {
  if (array[i] === delName){
    array.splice(i, 1)
    }
  }
}

function displayRoster(array){
  console.log(array)
}

students = []

var start = prompt("Would you like to start the roster web app? y/n")

if (start === "y"){
  app = true
  }else if (start === "n"){
    alert("See you later!")
  }

while (app == true){
  var userInput = prompt("Please select an action: add, remove, display, or quit.")

  if (userInput === "add"){
    var name = prompt("Enter the name you want to add:")
    addStudent(name,students)
  }

  if (userInput === "remove"){
    var delName = prompt("Enter the name you want to delete:")
    delStudent(delName, students)
  }

  if (userInput === "display"){
    displayRoster(students)
  }

  if (userInput === 'quit'){
    alert("See you later!")
    break
  }
}
