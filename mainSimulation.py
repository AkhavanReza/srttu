import os
import sys
import traci
import SimClass

from sumolib import checkBinary

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = checkBinary('sumo')

zone1 = SimClass.Zones("zone1", "F:\Final Simulation\Zone1\Zone1.sumocfg")
zone2 = SimClass.Zones("zone2", "F:\Final Simulation\Zone2\Zone2.sumocfg")

sensor_z1il500m2 = SimClass.Sensors("z1il500m2")
sensor_z2il500m2 = SimClass.Sensors("z2il500m2")

zone1.add_sensor(sensor_z1il500m2)
zone2.add_sensor(sensor_z2il500m2)

# run zone1
sumoCmd = [sumoBinary, "-c", zone1.zone_path]
traci.start(sumoCmd)

step = 0
myList = ""
myVehID = ""
curVehID = ""

while step <= 3600:
    traci.simulationStep()

    if traci.inductionloop.getLastStepVehicleNumber("z1il500m2") > 0:
        myList = traci.inductionloop.getLastStepVehicleIDs("z1il500m2")
        myVehID = myList[0]

        if curVehID != myVehID:     # for coaches and trailers
            passed_veh = SimClass.Vehicles(myVehID)
            passed_veh.speed_v = traci.vehicle.getSpeed(myVehID)

            sensor_z1il500m2.add_vehicle(passed_veh)

            curVehID = myVehID
    step += 1

traci.close()
