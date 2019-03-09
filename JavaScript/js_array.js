var countries = ["China", "Germany", "UK"]

// console.log(countries[2])
// countries[2] = "France"
// console.log(countries[2])

var lastItem = countries.pop()
console.log(lastItem)

countries.push("Denmark")
console.log(countries)

countries[countries.length - 1]

var arr = ["A", "B", "C"]

for (var i = 0; i < arr.length; i++) {
  console.log(arr[i])
}

//for of loop

for (letter of arr){
  console.log(letter)
}

for (letter of arr){
  alert(letter)
}
// Can do this with the for each method:
arr.forEach(alert)

