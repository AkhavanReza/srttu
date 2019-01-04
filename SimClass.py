import os
import sys
import traci


class Vehicles:
    speed_v = 0
    type_v = ""
    color_v = ""
    length_v = 0
    last_seen = 0
    pos_x = 0       # center of the front bumper
    pos_y = 0

    def __init__(self, v_id):
        self.v_id = v_id


class Sensors:

    MAX_VEH = 15

    def __init__(self, s_id):
        self.s_id = s_id
        self.sensor_vehicles = []

    def add_vehicle(self, v_data):
        self.sensor_vehicles.append(v_data)

        if len(self.sensor_vehicles) > self.MAX_VEH:    # don't keep unnecessary vehicle data

            self.sensor_vehicles.pop(0)

            i = 0
            sum_speed = 0.0
            as15u120 = 0.0
            for i in range(0, 14):
                sum_speed += (self.sensor_vehicles[i]).speed_v
            as15u120 = sum_speed / 14
            print(as15u120)
            if as15u120 > 23:
                print("Warning!")

    def total_vehicles(self):
        return self.len(self.sensor_vehicles)


class Zones:

    def __init__(self, z_id, zone_path):
        self.z_id = z_id
        self.zone_path = zone_path
        self.zone_sensors = []

    def add_sensor(self, s_data):
        self.zone_sensors.append(s_data)
