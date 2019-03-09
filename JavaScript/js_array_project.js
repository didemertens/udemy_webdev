function addStudent(){
  var name = prompt("Enter the name you want to add:")
  students.push(name)
}

function delStudent(){
  var delName = prompt("Enter the name you want to delete:")
  for (var i = 0; i < students.length; i++) {
  if (students[i] === delName){
    students.splice(i, 1)
    }
  }
}

function displayRoster(){
  console.log(students)
}

students = []

var start = prompt("Would you like to start the roster web app? y/n")

if (start === "y"){
  app = true
  while (app == true){
    var userInput = prompt("Please select an action: add, remove, display, or quit.")

    if (userInput === "add"){
      addStudent()
    }else if (userInput === "remove"){
      delStudent()
    }else if (userInput === "display"){
      displayRoster()
    }else if (userInput === 'quit'){
      break
    }else{
      alert("Sorry, we didn't get that. Please try again.")
      app = true
    }
  }
}else {
  app = false
}
alert("See you later!")
