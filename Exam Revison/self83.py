"""L"""

def get_input():
    """L"""
    
    circumference = float(input("Circumference (m)? "))
    times_string = input("Times (msecs, space separated)? ")
    
    return circumference, times_string

def get_times(times_string):
    """L"""
    
    times_list = times_string.split()
    times = [] # In seconds
    for time_string in times_list:
        times.append(int(time_string) / 1000)  
    
    return times

def get_speed(times, circumference):
    """LL"""
    
    speeds = []
    for i in range(len(times) - 1):
        speed_m_per_s = circumference / ((times[i + 1] - times[i]))
        speeds.append(speed_m_per_s)
    
    return speeds

def print_stuff(times, speeds):
    """L"""
    
    print("Time (s)  Speed (m/s)")
    for i in range(0, len(speeds)):
        print("{:6.2f}  {:9.2f}".format(times[i], speeds[i]))
        
def main():
    """L"""
    
    circumference, times_string = get_input()
    times = get_times(times_string)
    speeds = get_speed(times, circumference)
    print_stuff(times, speeds)
    
main()