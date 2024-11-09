# a fleet consists of one or more cars that travel together to the target without overtaking each other.

def carFleet(target, position, speed) -> int:
    pairs = [(position[i], speed[i]) for i in range(len(position))]  # (position, speed) Combines position and speed into a list of pairs. EXAMPLE: [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)
    lastFleetArrivalTime = 0  # lastFleetArrivalTime represents the time it takes for the last fleet to reach the target. As you process each car from the closest to the target to the farthest, lastFleetArrivalTime is updated to the latest fleet's arrival time.
    fleets = 0 # fleets counts the number of fleets.
    #print(f"pairs= \t\t{pairs}")
   
    for position, speed in sorted(pairs, reverse=True):  # Sort the pairs based on the position in descending order. This means we process the cars starting from the one closest to the target to the one farthest.
        # print(f"sorted_pairs= \t{sorted(pairs, reverse=True)}, position={position}, speed={speed}, lastFleetArrivalTime={lastFleetArrivalTime}, fleets={fleets}, dest_time={(target - position)/speed}")
        destination_time = (target - position)/speed # For each car, calculate how long it will take to reach the target. This is done by getting the the amount left to travel (target - position) and dividing it by the car’s speed.
        if destination_time > lastFleetArrivalTime: # When a car's destination_time is greater than the lastFleetArrivalTime: It indicates that this car cannot catch up with the fleet ahead of it, and thus it must start a new fleet.
            fleets += 1
            lastFleetArrivalTime = destination_time

    return fleets

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(f"\n(#1) target: {target}, position: {position}, speed: {speed}")
result = carFleet(target, position, speed)
print(f"result: {result}")
# Output: 3
'''
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Example 2:
'''

target = 10
position = [3]
speed = [3]
print(f"\n(#2) target: {target}, position: {position}, speed: {speed}")
result = carFleet(target, position, speed)
print(f"result: {result}")
# Output: 1
'''
Explanation:
There is only one car, hence there is only one fleet.
'''

target = 100
position = [0, 2, 4]
speed = [4, 2, 1]
print(f"\n(#3) target: {target}, position: {position}, speed: {speed}")
result = carFleet(target, position, speed)
print(f"result: {result}")
# Output: 1
'''
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
'''

print("\n")
