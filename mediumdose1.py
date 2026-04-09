import numpy as np

# Rotation about X-axis
def rot_x(ax):
    a = np.radians(ax)
    return np.array([[1,0,0],[0,np.cos(a),-np.sin(a)],[0,np.sin(a),np.cos(a)]])

# Rotation about Y-axis
def rot_y(ay):
    a = np.radians(ay)
    return np.array([[np.cos(a),0,np.sin(a)],[0,1,0],[-np.sin(a),0,np.cos(a)]])

# Rotation about Z-axis
def rot_z(az):
    a = np.radians(az)
    return np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])

# Apply rotation in order: X → Y → Z
def euler(rx, ry, rz):
    return rot_z(rz) @ rot_y(ry) @ rot_x(rx)

# Transform coordinates from Camera Frame → Rover Frame
def camera_rover(obj_cam, cam_trans, cam_rot):
    R = euler(*cam_rot)
    return R @ obj_cam + cam_trans

# Transform coordinates from Rover Frame → World Frame
def rover_world(p_rover, rover_pos, rover_rot):
    R = euler(*rover_rot)
    return R @ p_rover + rover_pos




def main():
    cam_trans  = np.array([0.5,  0.0,  1.2])
    cam_rot = np.array([0.0, -15.0, 0.0])


    print("Enter Object Coordinates (Camera Frame)")
    x_cam = float(input("  x: "))
    y_cam = float(input("  y: "))
    z_cam = float(input("  z: "))
    obj_cam   = np.array([x_cam, y_cam, z_cam])

    print("\nEnter Rover Position (World Frame)")
    x = float(input("  x: "))
    y = float(input("  y: "))
    z = float(input("  z: "))
    rover_pos = np.array([x, y, z])

    print("\nEnter Rover Rotation in degrees")
    rx = float(input("  x_angle: "))
    ry = float(input("  y_angle: "))
    rz = float(input("  z_angle: "))
    rover_rot = np.array([rx, ry, rz])

    p_rover = camera_rover(obj_cam, cam_trans, cam_rot)
    p_world = rover_world(p_rover, rover_pos, rover_rot)

    x, y, z = p_world
    print(f"\nObject Coordinates (World Frame):({x:.4f},  {y:.4f},  {z:.4f})")


if __name__ == "__main__":
    main()