
'''
This file contains the definitions to interface with:
    Dronekit to interface with the pixhawk
    OpenCV to perform object detection
'''

#function for detecting object containing aruco code


# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):   

    print ("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
      print (" Waiting for vehicle to initialise...")
      time.sleep(1)

    print ("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True  
    while not vehicle.armed:
      print (" Waiting for arming...")
      time.sleep(1) 
    print ("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude   
    # Check that vehicle has reached takeoff altitude
    while True:
      print (" Altitude: "), vehicle.location.global_relative_frame.alt 
      #Break and return from function just below target altitude.        
      if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
        print("Take off complete")
        print("Reached target altitude")
        break
      time.sleep(1) 


#GOTO function 
def goto(d_north, d_east, gotoFunction=vehicle.simple_goto):
    """
    Local navigation with GPS:
    A convenience function that can use Vehicle.simple_goto (default) or goto_position_target_global_int to
    travel to a specific position in metres
    North and East from the current location.
    This method reports distance to the destination.
    Moves the vehicle to a position dNorth metres North and dEast metres East of the current position.
    The method takes a function pointer argument with a single `dronekit.lib.LocationGlobal` parameter for
    the target position. This allows it to be called with different position-setting commands.
    By default it uses the standard method: dronekit.lib.Vehicle.simple_goto().
    The method reports the distance to target every two seconds.
    """

    currentLocation = vehicle.location.global_relative_frame
    targetLocation = get_location_metres(currentLocation, d_north, d_east)
    targetDistance = get_distance_metres(currentLocation, targetLocation)
    gotoFunction(targetLocation)

    # print "DEBUG: targetLocation: %s" % targetLocation
    # print "DEBUG: targetLocation: %s" % targetDistance

    while vehicle.mode.name == "GUIDED":  # Stop action if we are no longer in guided mode.
        # print "DEBUG: mode: %s" % vehicle.mode.name
        remainingDistance = get_distance_metres(vehicle.location.global_relative_frame, targetLocation)
        print("Distance to target: ", remainingDistance)
        if remainingDistance <= targetDistance * 0.01:  # Just below target, in case of undershoot.
            print("Reached target")
            break
        time.sleep(2)