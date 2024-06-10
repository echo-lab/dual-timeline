import json
import random


def findEventLinesInCSV(video_name, event_ID, rect_csv_lines):
    linesToReturn = []

    current_line_num = 0

    for rect_csv_line in rect_csv_lines:
        if current_line_num == 0:
            current_line_num += 1
        else:
            rect_csv_line = rect_csv_line.strip().split(", ")

            curr_video_name = rect_csv_line[0]
            curr_event_id = rect_csv_line[1]

            if video_name == curr_video_name and event_ID == curr_event_id:
                linesToReturn.append(rect_csv_line)

    return linesToReturn


fixed_events_times_json = open("VIRAT_S_0400_FIXED_EVENT_TIMES.json", "r")
rect_csv = open("VIRAT_S_0400_EVENT_RECT.csv", "r")

fixed_events_times_json_dict = json.loads(fixed_events_times_json.read())

# print(fixed_events_times_json_dict)

rect_csv_lines = rect_csv.readlines()

# print(rect_csv_lines)

fixed_events_times_and_rect_json = open("VIRAT_S_0400_FIXED_EVENT_TIMES_RECT.json", "w")

current_line_num = 0

events_list = []

for fixed_event_time_json in fixed_events_times_json_dict:

    event = fixed_event_time_json

    curr_video_name = str(fixed_event_time_json["currentEventVideoName"])
    curr_event_id = str(fixed_event_time_json["currentEventID"])

    currEventRectLines = findEventLinesInCSV(
        curr_video_name, curr_event_id, rect_csv_lines
    )

    event["currentEventVideoWidth"] = int(currEventRectLines[0][2])
    event["currentEventVideoHeight"] = int(currEventRectLines[0][3])

    currEventStartFrame = int(fixed_event_time_json["currentEventStartFrame"])

    currEventEndFrame = int(fixed_event_time_json["currentEventEndFrame"])

    event["currentEventRectWidthMin"] = {}
    event["currentEventRectWidthMax"] = {}
    event["currentEventRectHeightMin"] = {}
    event["currentEventRectHeightMax"] = {}

    for i in range(currEventStartFrame, currEventStartFrame + len(currEventRectLines)):
        print(currEventRectLines[i - currEventStartFrame])
        event["currentEventRectWidthMin"][int(i)] = int(
            currEventRectLines[i - currEventStartFrame][4]
        )
        event["currentEventRectHeightMin"][int(i)] = int(
            currEventRectLines[i - currEventStartFrame][5]
        )
        event["currentEventRectWidthMax"][int(i)] = int(
            currEventRectLines[i - currEventStartFrame][6]
        )
        event["currentEventRectHeightMax"][int(i)] = int(
            currEventRectLines[i - currEventStartFrame][7]
        )

    events_list.append(event)

json.dump(events_list, fixed_events_times_and_rect_json)

fixed_events_times_and_rect_json.close()
fixed_events_times_json.close()
rect_csv.close()

# Should have 90 in result file
