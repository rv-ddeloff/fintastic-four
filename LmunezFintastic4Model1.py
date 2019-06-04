def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width
    
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1 and all_wheels_on_track:
        reward = 1.0
    elif distance_from_center <= marker_2 and all_wheels_on_track:
        reward = 0.9
    elif distance_from_center <= marker_3 and all_wheels_on_track:
        reward = 0.8
    elif distance_from_center <= marker_4 and all_wheels_on_track:
        reward = 0.7
    elif distance_from_center <= marker_5 and all_wheels_on_track:
        reward = 0.6
    elif distance_from_center <= marker_1:
        reward = 0.5
    elif distance_from_center <= marker_2:
        reward = 0.45
    elif distance_from_center <= marker_3:
        reward = 0.4
    elif distance_from_center <= marker_4:
        reward = 0.
    elif distance_from_center <= marker_5:
        reward = 0.3
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)

