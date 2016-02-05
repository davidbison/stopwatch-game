# Convert time as integer to A:BC.D
def format(t):
  # Set state of stopwatch at start and reset
  milliseconds = 0
  seconds = 0
  minutes = 0

  # Split into minutes, seconds, and milliseconds
  if t < 600:
    milliseconds += (t % 10)
  if t < 6000 and t > 9:
    seconds += (t / 10)

  # Convert to strings
  milliseconds_str = str(milliseconds)
  seconds_str = str(seconds)

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

print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
# print format(600)
# print format(602)
# print format(667)
# print format(1325)
# print format(4567)
# print format(5999)



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