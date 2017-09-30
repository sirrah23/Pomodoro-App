const clock = cf($('.your-clock'));
clock.generate_clock();

$('.start-button').click(function(){
  clock.clock.start();
  $('.context').prop('readonly', true);
});

$('.stop-button').click(function(){
  clock.clock.stop();
});

$('.reset-button').click(function(){
  clock.clock.stop(function(){
    clock.toggle_mode();
    clock.reset();
    $('.context').prop('readonly', false);
  });
});
