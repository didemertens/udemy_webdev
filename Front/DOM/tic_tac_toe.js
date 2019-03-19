// Restart button

var restart = document.querySelector("#b");
var squares = document.querySelectorAll("td");

function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}

restart.addEventListener('click',clearBoard)

// Make game

var cellOne = document.querySelector("#one")

cellOne.addEventListener("click",function(){
  if (cellOne.textContent === ''){
    cellOne.textContent = 'X';
  }else if (cellOne.textContent === 'X'){
    cellOne.textContent = 'O';
    }else{
      cellOne.textContent = '';
    }
  })

var cellTwo = document.querySelector("#two")

cellTwo.addEventListener("click",function(){
  if (cellTwo.textContent === ''){
    cellTwo.textContent = 'X';
  }else if (cellTwo.textContent === 'X'){
    cellTwo.textContent = 'O';
    }else{
      cellTwo.textContent = '';
    }
  })

var cellThree = document.querySelector("#three")

cellThree.addEventListener("click",function(){
  if (cellThree.textContent === ''){
    cellThree.textContent = 'X';
  }else if (cellThree.textContent === 'X'){
    cellThree.textContent = 'O';
    }else{
      cellThree.textContent = '';
    }
  })

var cellFour = document.querySelector("#four")

cellFour.addEventListener("click",function(){
  if (cellFour.textContent === ''){
    cellFour.textContent = 'X';
  }else if (cellFour.textContent === 'X'){
    cellFour.textContent = 'O';
    }else{
      cellFour.textContent = '';
    }
  })

var cellFive = document.querySelector("#five")

cellFive.addEventListener("click",function(){
  if (cellFive.textContent === ''){
    cellFive.textContent = 'X';
  }else if (cellFive.textContent === 'X'){
    cellFive.textContent = 'O';
    }else{
      cellFive.textContent = '';
    }
  })

var cellSix = document.querySelector("#six")

cellSix.addEventListener("click",function(){
  if (cellSix.textContent === ''){
    cellSix.textContent = 'X';
  }else if (cellSix.textContent === 'X'){
    cellSix.textContent = 'O';
    }else{
      cellSix.textContent = '';
    }
  })

var cellSeven = document.querySelector("#seven")

cellSeven.addEventListener("click",function(){
  if (cellSeven.textContent === ''){
    cellSeven.textContent = 'X';
  }else if (cellSeven.textContent === 'X'){
    cellSeven.textContent = 'O';
    }else{
      cellSeven.textContent = '';
    }
  })

var cellEight = document.querySelector("#eight")

cellEight.addEventListener("click",function(){
  if (cellEight.textContent === ''){
    cellEight.textContent = 'X';
  }else if (cellEight.textContent === 'X'){
    cellEight.textContent = 'O';
    }else{
      cellEight.textContent = '';
    }
  })

var cellNine = document.querySelector("#nine")

cellNine.addEventListener("click",function(){
  if (cellNine.textContent === ''){
    cellNine.textContent = 'X';
  }else if (cellNine.textContent === 'X'){
    cellNine.textContent = 'O';
    }else{
      cellNine.textContent = '';
    }
  })
