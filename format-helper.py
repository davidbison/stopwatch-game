# Convert time as integer to A:BC.D
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
  if minutes > 9:
    return "Go outside and play."
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
print format(6000) == "Go outside and play."



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