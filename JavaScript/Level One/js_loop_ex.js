/// PART 8 - LOOP EXERCISES

///////////////////
//// PROBLEM 1 ///
/////////////////

// print (console.log()) out the word "hello" 5 times.
// Do this with a While Loop and a For Loop


num = 1

while (num < 6){
  console.log("hello")
  num++
}


// For Loop

for (var i = 1; i < 6; i++) {
  console.log("hello with for")
}


/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

var num = 1

while (num < 26){
  if (num % 2 !== 0){
    console.log(num)
  }
  num++
}


for (var i = 0; i < 26; i++) {
  if (i % 2 !==0){
    console.log(i)
  }
}
