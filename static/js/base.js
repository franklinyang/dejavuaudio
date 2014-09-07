$(document).ready(function(){
  $('.carousel').carousel({
  })
  $('a[data-slide="prev"]').click(function() {
    $('#myCarousel').carousel('prev');
  });
  $('a[data-slide="next"]').click(function() {
    $('#myCarousel').carousel('next');
  }); 
});
