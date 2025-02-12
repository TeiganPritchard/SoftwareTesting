import statistics


def validate_temperature(value):
    # You have to complete this function
    try:
        if value >= -50 and value <= 150:
            return value
        else:
            return"Out-of-bound value detected"
    except:
        return"Invalid input detected"
    


def process_temperatures(temp_list):
    """Process the list of temperatures and return min, max, and avg."""
    valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]
    
    if not valid_temps:
        return "No input provided."

    for temp in valid_temps:
        if isinstance(temp,(int,float)) == False:
            return temp



    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

# test_cases = [
#     [20], 
#     [15,35],
#     [],
#     [10,-10,30],
#     [-50,20,150,25],
#     [10, "abc",30],
#     [2**31 -1, -2**31],
#     [10,10,10]
# ]

# # Running the test cases
# for i, case in enumerate(test_cases, start=1):
#     print(f"Test Case {i}: {case}")
#     print(process_temperatures(case))
#     print("-" * 40)

print(process_temperatures( []))