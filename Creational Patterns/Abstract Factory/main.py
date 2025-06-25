from src.vehicle_factory import LuxuryVehicleFactory, NonLuxuryVehicleFactory, VehicleFactory

if __name__ == "__main__":
    anotherone = "1"
    while (anotherone != '0'):
        print("Type 'L' for luxury or 'NL' for non-luxury")
        category = input()
        if (category) == "L":
            category = VehicleFactory.LUXURY_VEHICLE
        else:
            category = VehicleFactory.NON_LUXURY_VEHICLE
        print("Type 'C' for Car or 'S' for SUV")
        type = input()
        factory = VehicleFactory.getVehicleFactory(category)
        if (type == "C"):
            v = factory.getCar()
        else:
            v = factory.getSUV()
        print("name",v.getName())
        print("features",v.getFeatures())
        anotherone = input("type 0 for stop\n")