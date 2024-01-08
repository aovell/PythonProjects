#Alyn Ovell
#lab3
    # Function that converts time in the format hh:mm:ss to seconds
def time_to_seconds(time):
    hours, minutes, seconds = time.split(":")
    return int(hours)*3600 + int(minutes)*60 + int(seconds)

#Function that converts seconds to time in the format hh:mm:ss
def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

# Function that calculates the average time for a list of times
def calculate_average_time(times):
    total_seconds = sum(time_to_seconds(time) for time in times)
    return seconds_to_time(total_seconds // len(times))

athlete = []
for i in range(4):
    name = input("Enter competitor's name: ")
    run_time = input("Enter running time (hh:mm:ss): ")
    bike_time = input("Enter biking time (hh:mm:ss): ")
    swim_time = input("Enter swimming time (hh:mm:ss): ")
    athlete.append({
        "name": name,
        "run_time": run_time,
        "bike_time": bike_time,
        "swim_time": swim_time,
        "total_time": time_to_seconds(run_time) + time_to_seconds(bike_time) + time_to_seconds(swim_time)
    })

# This calculates the average time for each event
run_times = [competitor["run_time"] for competitor in athlete]
bike_times = [competitor["bike_time"] for competitor in athlete]
swim_times = [competitor["swim_time"] for competitor in athlete]
#calls the average time function
avg_run_time = calculate_average_time(run_times)
avg_bike_time = calculate_average_time(bike_times)
avg_swim_time = calculate_average_time(swim_times)

# Determine the winner based on fastest total time. Uses lambda function to sort through the times in athlete list
winner = min(athlete, key=lambda x: x["total_time"])

# Prints the results
print("\nCompetitor times and averages:")
#This for loop loops through all the athlete lists and prints them and then will call the funtion that converts the time back to hh:mm:ss
for competitor in athlete:
    print("{}: run time = {}, bike time = {}, swim time = {}, total time = {}".format(
        competitor["name"],
        competitor["run_time"],
        competitor["bike_time"],
        competitor["swim_time"],
        seconds_to_time(competitor["total_time"])
    ))
print("Average run time = {}, average bike time = {}, average swim time = {}".format(
    avg_run_time,
    avg_bike_time,
    avg_swim_time
))
print("Overall winner: {}, total time = {}".format(
    winner["name"],
    seconds_to_time(winner["total_time"])
))
