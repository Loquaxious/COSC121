"""L"""
def get_inputs():
    """L"""
    
    circumference = float(input("Circumference (m)? "))
    times_string = input("Times (msecs, space separated)? ") 
    
    return circumference, times_string

def get_times(times_string):
    """l"""
    times = type_times(times_string.split())
    return times

def type_times(times_list):
    """L"""
    
    times = [] # In seconds
    for time_string in times_list:
        times.append(int(time_string) / 1000)
    return times

def get_speeds(times, circumference):
    """L"""
    speeds = []
    for i in range(len(times) - 1):
        speed_m_per_s = circumference / ((times[i + 1] - times[i]))
        speeds.append(speed_m_per_s)
    return speeds

def main():
    """L"""
    
    circum, times_str = get_inputs()
    times = get_times(times_str)
    speeds = get_speeds(times, circum)
    
    print("Time (s)  Speed (m/s)")
    for i in range(0, len(speeds)):
        print("{:6.2f}  {:9.2f}".format(times[i], speeds[i]))
        
main()