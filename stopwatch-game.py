# Stopwatch Reflex Game

import simplegui



# Define global variables
width = 300
height = 200
interval = 100
stopwatch = 0
reflex_test_total = 0
reflex_test_success = 0
milliseconds = 0
ticking = False



# Helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
  global milliseconds
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



# Event handlers for Start, Stop, and Reset buttons
def start():
  global ticking
    timer.start()
    ticking = True



def stop():
  global reflex_test_total, reflex_test_success, milliseconds, ticking
  timer.stop()
  if ticking:
    reflex_test_total += 1
    if milliseconds == 0:
      reflex_test_success += 1
  ticking = False



def reset():
  global stopwatch, reflex_test_total, reflex_test_success, ticking
  stopwatch = 0
  reflex_test_total = 0
  reflex_test_success = 0
  ticking = False
  timer.stop()



# Event handler for timer with 0.1 sec interval
def tick():
  global stopwatch
  stopwatch += 1



# Define draw handler
def draw_handler(canvas):
  canvas.draw_text(format(stopwatch), [(width/3), (height/2)], 36, "orange")
  canvas.draw_text(str(reflex_test_success) + "/" + str(reflex_test_total), [(width-50), 30], 25, "orange")



# Create frame
frame = simplegui.create_frame("Stopwatch Game", width, height)



# Register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw_handler)
start = frame.add_button("Start", start, 100)
stop = frame.add_button("Stop", stop, 100)
reset = frame.add_button("Reset", reset, 100)



# Start frame
frame.start()