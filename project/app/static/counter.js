function counterFactory(elem){
  count = 0;
  elem.val(0); // reset view
  return {
    inc(){
      count++;
      this.updateView();
    },
    dec(){
      count--;
      this.updateView();
    },
    updateView(){
      elem.val(count);
    }
  };
}

counter = counterFactory($('#interruptions'));
