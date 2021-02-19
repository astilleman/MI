seconds = int(input("Time in seconds: "))

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
seconds_per_hour = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
seconds_per_day = seconds_per_hour * HOURS_PER_DAY

# // : is a floor division
# % : modulo operator
days = seconds // seconds_per_day
seconds_remaining = seconds % seconds_per_day

hours = seconds_remaining // seconds_per_hour
seconds_remaining = seconds_remaining % seconds_per_hour

minutes = seconds_remaining // SECONDS_PER_MINUTE
seconds_remaining = seconds_remaining % SECONDS_PER_MINUTE

message = str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds_remaining) + " seconds"
print(message)
