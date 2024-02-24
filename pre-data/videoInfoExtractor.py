from pprint import pprint
from pymediainfo import MediaInfo

def ms_to_frames(duration_ms, frame_rate):
    return (duration_ms / 1000) * frame_rate

file_name_files = open("VIRAT_S_0400.txt", "r")

file_names = file_name_files.readlines()

video_info_csv = open("VIRAT_S_0400_VIDEO_INFO.csv", "w")

video_info_csv.write(
    "Video Name, Frame Rate (f/s), Duration (ms), Duration, Frames (f)\n"
)

for video_file_name in file_names:
    video_file_name = video_file_name.strip()
    video_info = MediaInfo.parse(
        "./four-largest-annotations/VIRAT_S_0400_VIDEOS/" + video_file_name + ".mp4"
    )
    for track in video_info.tracks:
        if track.track_type == "Video":
            video_info_csv.write(
    "{}, {}, {}, {}, {}\n".format(video_file_name, track.frame_rate, track.duration,track.other_duration[1], int(ms_to_frames(float(track.duration), float(track.frame_rate))))
)

file_name_files.close()
