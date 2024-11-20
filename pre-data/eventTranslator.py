import datetime

event_types = [
    "1: Person loading an Object to a Vehicle",
    "2: Person Unloading an Object from a Car/Vehicle",
    "3: Person Opening a Vehicle/Car Trunk",
    "4: Person Closing a Vehicle/Car Trunk",
    "5: Person getting into a Vehicle",
    "6: Person getting out of a Vehicle",
    "7: Person gesturing",
    "8: Person digging",
    "9: Person carrying an object",
    "10: Person running",
    "11: Person entering a facility",
    "12: Person exiting a facility",
]

events_files_name_file = open("VIRAT_S_0500.txt", "r")

events_file_names = events_files_name_file.readlines()

events_info_csv = open("VIRAT_S_0500_EVENTS_INFO.csv", "w")

events_info_csv.write(
    "Video Name, Event ID, Event Type, Event Duration (f), Event Start (f)\n"
)

for event_file_name in events_file_names:
    event_file_name = event_file_name.strip()
    try:
        events_file = open("./four-largest-annotations/VIRAT_S_0500_EVENTS/"+event_file_name+".viratdata.events.txt", "r")
        
        current_events = events_file.readlines()
        
        current_event_id = ""

        for current_event in current_events:
            current_event = current_event.strip().split(" ")

            if current_event_id == current_event[0]:
                continue
            else:
                current_event_id = current_event[0]
                current_event_type = event_types[int(current_event[1]) - 1]
                current_event_duration = current_event[2]
                current_event_start_frame = current_event[3]
                events_info_csv.write("{}, {}, {}, {}, {}\n".format(event_file_name, current_event_id, current_event_type,current_event_duration,current_event_start_frame))
        
        events_file.close()
    except IOError:    #This means that the file does not exist (or some other IOError)
        print("{}, {}\n".format(event_file_name, "No Events"))

events_info_csv.close()
events_file.close()
events_files_name_file.close()