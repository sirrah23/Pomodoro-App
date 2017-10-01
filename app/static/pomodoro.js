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
      end_listeners: [],
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
        let that = this;
        this.clock = new FlipClock(elem, this.get_length(), {
          clockFace: "HourlyCounter",
          countdown: true,
          autoStart: false,
          callbacks: {
            stop: function(){
              if(that.clock.getTime().time !== 0)
                return;
              for(let i = 0; i < that.end_listeners.length; i++)
                that.end_listeners[i]();
            }
          }
        });
      },
      add_end_listener: function(l){
        this.end_listeners.push(l);
      }
    };
  };
  return pomodoro_factory;
})();
