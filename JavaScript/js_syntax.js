// var hot = false
// var temp = -10

// if (temp>25) {
//   console.log("Hot outside");
// }else if (temp <= 25 && temp >= 15){
//   console.log("It's not very hot nor cold today!")
// }else if (temp < 15 && temp >= 0) {
//   console.log("It's pretty cold outside!")
// }else {
//   console.log("It's freezing outside!")
// }


var ham = 0
var cheese = 10

var report = "blank"

if (ham >= 10 && cheese >= 10){
  report = "Strong sales of both ham and cheese!"
}else if (ham === 0 && cheese === 0){
  report = "Nothing sold!"
}else {
  report = "We had some sales of items."
}

console.log(report)
