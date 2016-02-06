import simplegui



# define global variables
width = 300
height = 200
interval = 100
stopwatch = 0



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
  # Split into minutes, seconds, and milliseconds
  minutes = t / 600
  seconds = (t - minutes * 600) / 10
  milliseconds = (t - minutes * 600) % 10

  # Convert to strings
  milliseconds_str = str(milliseconds)
  seconds_str = str(seconds)
  minutes_str = str(minutes)

  # Account for padding if seconds is less than 10
  if seconds < 10:
    seconds_str = "0" + seconds_str

  # Return composite string
  return minutes_str + ":" + seconds_str + "." + milliseconds_str



# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    print "start test"



def stop():
    timer.stop()
    print "stop test"



def reset():
    global stopwatch
    stopwatch = 0
    timer.stop()
    print "reset test"



# define event handler for timer with 0.1 sec interval
def tick():
    global stopwatch
    stopwatch += 1
    print stopwatch



# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(stopwatch), [125, 100], 36, "orange")



# create frame
frame = simplegui.create_frame("Stopwatch Game", width, height)



# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw_handler)
start = frame.add_button("Start", start, 100)
stop = frame.add_button("Stop", stop, 100)
reset = frame.add_button("Reset", reset, 100)



# start frame
frame.start()