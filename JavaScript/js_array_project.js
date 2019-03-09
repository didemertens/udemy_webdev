
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
    students.push(name)
  }

  if (userInput === "remove"){
    var delName = prompt("Enter the name you want to delete:")
    for (var i = 0; i < students.length; i++) {
      if (students[i] === delName){
        students.splice(i, 1)
      }
    }
  }

  if (userInput === "display"){
    console.log(students)
  }

  if (userInput === 'quit'){
    alert("See you later!")
    break
  }
}

