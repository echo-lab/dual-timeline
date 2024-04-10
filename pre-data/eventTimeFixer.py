import json
import random

videos_csv = open("VIRAT_S_0400_VIDEO_INFO.csv", "r")
events_csv = open("VIRAT_S_0400_EVENTS_INFO.csv", "r")

videos_data = videos_csv.readlines()
events_data = events_csv.readlines()

fixed_events_times_json = open("VIRAT_S_0400_FIXED_EVENT_TIMES.json", "w")

current_line_num = 0

current_duration = 0

events_list = []

for video_data in videos_data:
    if current_line_num == 0:
        current_line_num += 1
    else:
        print("---")
        video_data = video_data.strip().split(", ")
        video_file_name = video_data[0]
        video_frame_rate = float(video_data[1])
        print(video_file_name)
        print(current_duration)

        video_events = [event for event in events_data if video_file_name in event]
        if len(video_events) == 0:
            print("No Events")
        else:
            for video_event_data in video_events:
                video_event_data = video_event_data.strip().split(", ")
                current_event_video_name = video_event_data[0]
                current_event_id = int(video_event_data[1])
                current_event_name = video_event_data[2]
                current_event_duration = int(video_event_data[-2])
                current_event_start_frame = current_duration + int(video_event_data[-1])
                current_event_end_frame = (
                    current_event_start_frame + current_event_duration
                )
                current_event_start_frame_s = (
                    current_event_start_frame / video_frame_rate
                )
                current_event_end_frame_s = current_event_end_frame / video_frame_rate
                print(
                    "{}, {}, {}, {}, {}, {}, {}, {}".format(
                        current_event_video_name,
                        current_event_id,
                        current_event_name,
                        current_event_duration,
                        current_event_start_frame,
                        current_event_end_frame,
                        current_event_start_frame_s,
                        current_event_end_frame_s,
                    )
                )
                events_list.append(
                    {
                        "currentEventVideoName": current_event_video_name,
                        "currentEventID": current_event_id,
                        "currentEventName": current_event_name,
                        "currentEventDuration": current_event_duration,
                        "currentEventStartFrame": current_event_start_frame,
                        "currentEventEndFrame": current_event_end_frame,
                        "currentEventStartFrameSeconds": current_event_start_frame_s,
                        "currentEventEndFrameSeconds": current_event_end_frame_s,
                    }
                )

        current_duration += int(video_data[-1])
        print(current_duration)

json.dump(events_list, fixed_events_times_json)

fixed_events_times_json.close()
videos_csv.close()
events_csv.close()
