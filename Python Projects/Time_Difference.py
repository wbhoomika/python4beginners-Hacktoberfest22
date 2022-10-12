from datetime import datetime

# start time
start_time = "2:13:57"
end_time = "11:46:38"

t1 = datetime.strptime(start_time, "%H:%M:%S")
print('Start time:', t1.time())

t2 = datetime.strptime(end_time, "%H:%M:%S")
print('End time:', t2.time())

delta = t2 - t1

print(f"Time difference is {delta.total_seconds()} seconds")

ms = delta.total_seconds() * 1000
print(f"Time difference is {ms} milliseconds")
