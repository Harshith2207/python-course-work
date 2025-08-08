# Import Time
import time

# Initial vehicle data
Vehicle_Number = ['XXXX-XX-XXXX']
Vehicle_Type = ['Bike']
vehicle_Name = ['Intruder']
Owner_Name = ['Unknown']
Date = ['22-22-3636']
Time = ['22:22:22']

# Initial parking spaces available
bikes = 100
cars = 250
bicycles = 78

def main():
    global bikes, cars, bicycles
    try:
        while True:
            print("----------------------------------------------------------------------------------------")
            print("\t\tHarshith's Parking Management System")
            print("----------------------------------------------------------------------------------------")
            print("1. Vehicle Entry")
            print("2. Remove Entry")
            print("3. View Parked Vehicles")
            print("4. View Left Parking Space")
            print("5. Amount Details")
            print("6. Bill")
            print("7. Close Programme")
            print("+---------------------------------------------+")
            ch = int(input("\tSelect option: "))
            if ch == 1:
                no = True
                while no:
                    Vno = input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
                    if Vno == "":
                        print("###### Enter Vehicle No. ######")
                    elif Vno in Vehicle_Number:
                        print("###### Vehicle Number Already Exists ######")
                    elif len(Vno) == 12:
                        no = False
                        Vehicle_Number.append(Vno)
                    else:
                        print("###### Enter Valid Vehicle Number ######")
                typee = True
                while typee:
                    Vtype = input("\tEnter vehicle type (Bicycle=A / Bike=B / Car=C): ").lower()
                    if Vtype == "":
                        print("###### Enter Vehicle Type ######")
                    elif Vtype == "a":
                        Vehicle_Type.append("Bicycle")
                        bicycles -= 1
                        typee = False
                    elif Vtype == "b":
                        Vehicle_Type.append("Bike")
                        bikes -= 1
                        typee = False
                    elif Vtype == "c":
                        Vehicle_Type.append("Car")
                        cars -= 1
                        typee = False
                    else:
                        print("###### Please Enter Valid Option ######")
                name = True
                while name:
                    vname = input("\tEnter vehicle name - ")
                    if vname == "":
                        print("###### Please Enter Vehicle Name ######")
                    else:
                        vehicle_Name.append(vname)
                        name = False
                o = True
                while o:
                    OName = input("\tEnter owner name - ")
                    if OName == "":
                        print("###### Please Enter Owner Name ######")
                    else:
                        Owner_Name.append(OName)
                        o = False
                d = True
                while d:
                    date = input("\tEnter Date (DD-MM-YYYY) - ")
                    if date == "":
                        print("###### Enter Date ######")
                    elif len(date) != 10:
                        print("###### Enter Valid Date ######")
                    else:
                        Date.append(date)
                        d = False
                t = True
                while t:
                    t_input = input("\tEnter Time (HH:MM:SS) - ")
                    if t_input == "":
                        print("###### Enter Time ######")
                    elif len(t_input) != 8:
                        print("###### Please Enter Valid Time ######")
                    else:
                        Time.append(t_input)
                        t = False
                print("\n............................................................Record saved successfully by Harshith..................................................................")
            elif ch == 2:
                no = True
                while no:
                    Vno = input("\tEnter vehicle number to Delete (XXXX-XX-XXXX) - ").upper()
                    if Vno == "":
                        print("###### Enter Vehicle No. ######")
                    elif len(Vno) == 12:
                        if Vno in Vehicle_Number:
                            i = Vehicle_Number.index(Vno)
                            Vehicle_Number.pop(i)
                            Vehicle_Type.pop(i)
                            vehicle_Name.pop(i)
                            Owner_Name.pop(i)
                            Date.pop(i)
                            Time.pop(i)
                            no = False
                            print("\n............................................................Entry removed successfully by Harshith..................................................................")
                        else:
                            print("###### No Such Entry ######")
                    else:
                        print("###### Enter Valid Vehicle Number ######")
            elif ch == 3:
                count = 0
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParked Vehicles (Managed by Harshith)")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("Vehicle No.\tVehicle Type        Vehicle Name\t       Owner Name\t     Date\t\tTime")
                print("----------------------------------------------------------------------------------------------------------------------")
                for i in range(len(Vehicle_Number)):
                    count += 1
                    print(Vehicle_Number[i], "\t  ", Vehicle_Type[i], "\t            ", vehicle_Name[i], "\t       ", Owner_Name[i], "      ", Date[i], "          ", Time[i])
                print("----------------------------------------------------------------------------------------------------------------------")
                print("------------------------------------------ Total Records - ", count, "-------------------------------------------------------")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch == 4:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tSpaces Left For Parking (Harshith's Lot)")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\tSpaces Available for Bicycle - ", bicycles)
                print("\tSpaces Available for Bike - ", bikes)
                print("\tSpaces Available for Car - ", cars)
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch == 5:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParking Rate (Set by Harshith)")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("*1. Bicycle      Rs20 / Hour")
                print("*2. Bike         Rs40 / Hour")
                print("*3. Car          Rs60 / Hour")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch == 6:
                print(".............................................................. Generating Bill (Harshith's System) ..........................................................................")
                no = True
                while no:
                    Vno = input("\tEnter vehicle number for billing (XXXX-XX-XXXX) - ").upper()
                    if Vno == "":
                        print("###### Enter Vehicle No. ######")
                    elif len(Vno) == 12:
                        if Vno in Vehicle_Number:
                            i = Vehicle_Number.index(Vno)
                            no = False
                        else:
                            print("###### No Such Entry ######")
                    else:
                        print("###### Enter Valid Vehicle Number ######")
                print("\tVehicle Check-in time - ", Time[i])
                print("\tVehicle Check-in Date - ", Date[i])
                print("\tVehicle Type - ", Vehicle_Type[i])
                inp = True
                amt = 0
                while inp:
                    hr = input("\tEnter No. of Hours Vehicle Parked - ")
                    if hr == "":
                        print("###### Please Enter Hours ######")
                    elif int(hr) == 0 and Vehicle_Type[i] == "Bicycle":
                        amt = 20
                        inp = False
                    elif int(hr) == 0 and Vehicle_Type[i] == "Bike":
                        amt = 40
                        inp = False
                    elif int(hr) == 0 and Vehicle_Type[i] == "Car":
                        amt = 60
                        inp = False
                    elif int(hr) >= 1:
                        if Vehicle_Type[i] == "Bicycle":
                            amt = int(hr) * 20
                            inp = False
                        elif Vehicle_Type[i] == "Bike":
                            amt = int(hr) * 40
                            inp = False
                        elif Vehicle_Type[i] == "Car":
                            amt = int(hr) * 60
                            inp = False
                print("\t Parking Charge - Rs.", amt)
                ac = 0.18 * amt
                print("\tAdditional charge 18 % GST - Rs.", round(ac, 2))
                print("\tTotal Charge - Rs.", round(amt + ac, 2))
                print("..............................................................Thank you for using Harshith's Parking Service...........................................................................")
                input("\tPress Enter to Proceed - ")
            elif ch == 7:
                print("..............................................................Thank you for using Harshith's Parking Service...........................................................................")
                print("                                     **********(: Bye Bye from Harshith :)**********")
                break
    except Exception as e:
        print(f"Error occurred: {e}")
        main()

main()
