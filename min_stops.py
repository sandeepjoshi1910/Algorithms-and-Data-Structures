

"""

Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

"""
# target = 1000000
# startFuel = 8663
# stations = [[31,195796],[42904,164171],[122849,139112],[172890,121724],[182747,90912],[194124,112994],[210182,101272],[257242,73097],[284733,108631],[369026,25791],[464270,14596],[470557,59420],[491647,192483],[516972,123213],[577532,184184],[596589,143624],[661564,154130],[705234,100816],[721453,122405],[727874,6021],[728786,19444],[742866,2995],[807420,87414],[922999,7675],[996060,32691]]

# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]


# target = 100
# startFuel = 50
# stations = [[25,25],[50,50]]

target = 1000
startFuel = 299
stations = [[42,39],[132,236],[166,142],[434,7],[462,80],[518,103],[545,209],[656,104],[769,137],[811,67]]



# target = 1
# startFuel = 1
# stations = []

min_stops = -1

memo = {}

def getRFS(fuel, dcov, num_stops,min_stops,memo):
    
    if dcov in memo.keys():
        return memo[dcov]
    
    if fuel >= target - dcov:
        if min_stops == -1:
            min_stops = num_stops

        elif min_stops > num_stops:
            min_stops = num_stops
        return min_stops

    else:
        min_stop_list = []
        
        for st in stations:
            if st[0] > dcov and dcov + fuel >= st[0]:
                n_fuel = fuel - (st[0]-dcov) + st[1]
                n_dcov = st[0]

                min_stop_list.append(getRFS(n_fuel, n_dcov, num_stops + 1,min_stops,memo))
        
        
        res = list(filter(lambda x: x != -1, min_stop_list))
        
        if res == []:
            return -1
        else:
            
            memo[dcov] = min(res)
            return min(res)


mini = getRFS(startFuel,0,0,-1,memo)
print(mini)
print(memo)