# Convert time as integer to A:BC.D
def format(t):
  # Set state of stopwatch at start and reset
  milliseconds = 0
  seconds = 0
  minutes = 0

  # Split into minutes, seconds, and milliseconds
  milliseconds = t % 10
  seconds = t / 10
  minutes = seconds / 60
  # if t < 600:
  #   milliseconds += (t % 10)
  # if t < 6000 and t > 9:
  #   seconds += (t / 10)
  # if t < 6000 and t > 599:
  #   minutes += int(round(t / 600))

  # Convert to strings
  milliseconds_str = str(milliseconds)
  seconds_str = str(seconds)
  minutes_str = str(minutes)

  # Return composite string
  if minutes == 0 and seconds == 0 and milliseconds == 0:
      return "0:00.0"
  elif minutes == 0 and seconds == 0:
      return "0:00." + milliseconds_str
  elif minutes == 0 and seconds < 10:
      return "0:0" + seconds_str + "." + milliseconds_str
  elif minutes == 0:
      return "0:" + seconds_str + "." + milliseconds_str
  else:
      return minutes_str + ":" + seconds_str + "." + milliseconds_str



###################################################
# Test code for the format function
# Note that function should always return a string with
# six characters

print format(0) == "0:00.0"
print format(7) == "0:00.7"
print format(17) == "0:01.7"
print format(60) == "0:06.0"
print format(63) == "0:06.3"
print format(214) == "0:21.4"
print format(599) == "0:59.9"
print format(600) == "1:00.0"
print format(602) == "1:00.2"
print format(667) == "1:06.7"
print format(1325) == "2:12.5"
print format(4567) == "7:36.7"
print format(5999) == "9:59.9"



###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9