import simplegui



# define global variables
width = 300
height = 200
interval = 100
incrementer = 0



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass



# define event handlers for buttons; "Start", "Stop", "Reset"




# define event handler for timer with 0.1 sec interval
def timer_handler():
    global incrementer
    incrementer += 0.1
    print incrementer



# define draw handler




# create frame
frame = simplegui.create_frame("Stopwatch Game", width, height)



# register event handlers
timer = simplegui.create_timer(interval, timer_handler)



# start frame
frame.start()
timer.start()