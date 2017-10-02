const clock = cf($('#clock'));
clock.generate_clock();

function toggle_mode_indicator(){
  const indicator = $('#timermode')[0];
  if (indicator.innerHTML == "Pomodoro"){
    indicator.innerHTML = "Break";
  } else {
    indicator.innerHTML = "Pomodoro";
  }
}

function clock_hit_zero_update_ui(){
  setTimeout(() => {
    toggle_mode_indicator();
    clock.toggle_mode();
    clock.reset();
    clock.clock.start();
  }, 2000);
}

function gather_and_send_pomdoro(){
  const context = $('#context').val();
  const interruptions = parseInt($('#interruptions').val(), 10);
  const payload = {context, interruptions};
  $.post('/pomodoro', payload);
}

function reset_interruption_counter(){
  $('#interruptions').val("0");
}

//Actions to perform once the clock hits zero
clock.add_end_listener(clock_hit_zero_update_ui);
clock.add_end_listener(gather_and_send_pomdoro);
clock.add_end_listener(reset_interruption_counter);

$('#start-button').click(function(){
  clock.clock.start();
  $('.context').prop('readonly', true);
});

$('#stop-button').click(function(){
  clock.clock.stop();
});

$('#reset-button').click(function(){
  clock.clock.stop(function(){
    clock.reset();
    $('.context').prop('readonly', false);
  });
});

$('#toggle-button').click(function(){
  clock.clock.stop(function(){
    clock.toggle_mode();
    clock.reset();
    toggle_mode_indicator();
  });
});
