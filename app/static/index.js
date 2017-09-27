var clock = new FlipClock($('.your-clock'), 1500, {
  clockFace: "HourlyCounter",
  countdown: true,
  autoStart: false
})

$('.start-button').click(function(){
    clock.start();
    $('.context').prop('readonly', true);
});

$('.stop-button').click(function(){
    clock.stop();
});

$('.reset-button').click(function(){
    clock.stop(function(){
      clock.setTime(1500);
      $('.context').prop('readonly', false);
    });
});
