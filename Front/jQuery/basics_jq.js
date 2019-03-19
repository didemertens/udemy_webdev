// $('h1').click(function(){
//   $(this).text('I was changed')
// })

// Key Press

$('input').eq(0).keypress(function(event){
  if (event.which === 13){
    $('h3').toggleClass('turnBlue');
  }
})

// on()
$('h1').on('dblclick',function(){
  $(this).toggleClass('turnRed');
})

// mouse hover

$('h1').on('mouseenter',function(){
  $(this).toggleClass('turnRed');
})

// animation

$('input').eq(1).on('click',function(){
  $('.container').fadeOut(3000)
})
