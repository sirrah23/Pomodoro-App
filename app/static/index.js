const clock = cf($('.your-clock'));
clock.generate_clock();

function toggle_mode_indicator(){
  const indicator = $('#timermode')[0];
  if (indicator.innerHTML == "Pomodoro"){
    indicator.innerHTML = "Break";
  } else {
    indicator.innerHTML = "Pomodoro";
  }
}

clock.add_end_listener(() => {
  setTimeout(() => {
    toggle_mode_indicator();
    clock.toggle_mode();
    clock.reset();
    clock.clock.start();
  }, 2000);
});

$('.start-button').click(function(){
  clock.clock.start();
  $('.context').prop('readonly', true);
});

$('.stop-button').click(function(){
  clock.clock.stop();
});

$('.reset-button').click(function(){
  clock.clock.stop(function(){
    clock.reset();
    $('.context').prop('readonly', false);
  });
});

$('.toggle-button').click(function(){
  clock.clock.stop(function(){
    clock.toggle_mode();
    clock.reset();
    toggle_mode_indicator();
  });
});
