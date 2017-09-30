const cf = (function(){
  const twenty_five_minutes = 1500;
  const five_minutes = 300;
  const pomodoro_length = twenty_five_minutes;
  const break_length = five_minutes;
  const timer_modes = {
    break: "break",
    pomodoro: "pomodoro"
  };
  const pomodoro_factory = function(elem){
    return {
      mode: timer_modes.pomodoro,
      get_length: function(){
        if(this.mode == timer_modes.break){
          return break_length;
        } else {
          return pomodoro_length;
        }
      },
      toggle_mode: function(){
        if(this.mode == timer_modes.break){
          this.mode = timer_modes.pomodoro;
        } else{
          this.mode = timer_modes.break;
        }
      },
      reset: function(){
        this.clock.setTime(this.get_length());
      },
      generate_clock: function(){
        if(this.clock){
          return;
        }
        this.clock = new FlipClock(elem, this.get_length(), {
          clockFace: "HourlyCounter",
          countdown: true,
          autoStart: false
        });
      },
    };
  };
  return pomodoro_factory;
})();
