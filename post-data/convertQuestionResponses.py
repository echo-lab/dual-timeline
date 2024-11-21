# -*- coding: utf-8 -*-
import openpyxl
import datetime

timeline_types = {
    0: "Other",
    1: "Timeline 1 (Base Interface)",
    2: "Timeline 2 (Density Graph)",
    3: "Timeline 3 (Event Blocks)",
    4: "Timeline 4 (Density Graph + Event Blocks)",
    5: "Timeline 5 (Event Thumbnails)",
    6: "Other",
}

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("rawData.xlsx")

# Define variable to read sheet
dataframe1 = dataframe.active

question_responses_with_answers_csv = open("questionResponsesAndAnswers.csv", "w")

current_line_num = 0

# Iterate the loop to read the cell values
for row in dataframe1.values:

    if current_line_num == 0:

        question_responses_with_answers_csv.write(
            "Response ID, Timeline Used Value, Timeline Used Value Decrypted, Timeline Type (TimelinesUsed), Timeline Type (User Entry), First Click Time (Seconds), Last Click Time (Seconds), Time Between First and Last Click (Seconds), Question, Video Name, Their Answer, Correct Answer, Is Correct\n"
        )

        current_line_num += 1
    else:
        row_as_list = []
        for value in row:

            if isinstance(value, long):
                row_as_list.append(str(value))
            elif isinstance(value, datetime.date):
                row_as_list.append(str(value))
            elif isinstance(value, bool):
                row_as_list.append(str(value))
            elif isinstance(value, float):
                row_as_list.append(str(value))
            elif value == None:
                row_as_list.append(str(value))
            else:
                row_as_list.append(value.encode("utf-8"))

        response_id = row_as_list[0]
        print(response_id)

        # VIRAT_S_0002 Data

        virat_s_0002_timelines_used_value = row_as_list[45]
        print(virat_s_0002_timelines_used_value)

        virat_s_0002_timelines_used_value_decrypted = (
            int(virat_s_0002_timelines_used_value) - 69368
        )
        print(virat_s_0002_timelines_used_value_decrypted)

        virat_s_0002_timelines_used_value_decrypted_last_digit = (
            virat_s_0002_timelines_used_value_decrypted % 10
        )
        print(virat_s_0002_timelines_used_value_decrypted_last_digit)

        virat_s_0002_timeline_from_timelines_used = timeline_types[
            virat_s_0002_timelines_used_value_decrypted_last_digit
        ]
        print(virat_s_0002_timeline_from_timelines_used)

        virat_s_0002_q1 = "Task: The driver of this car gets out of the car and has a conversation with another person.What is the car that the other person gets into later?"
        virat_s_0002_q1_correct_response = "Car 1"
        virat_s_0002_q1_response = row_as_list[46]
        print(virat_s_0002_q1_response)

        virat_s_0002_q1_correct_or_not = (
            virat_s_0002_q1_correct_response == virat_s_0002_q1_response
        )

        print(virat_s_0002_q1_correct_or_not)

        virat_s_0002_q2 = "Task: During which timeframe do you see this man unloading a blue shoulder bag from his car?"
        virat_s_0002_q2_correct_response = "43:00 – 45:00"
        virat_s_0002_q2_response = row_as_list[47]
        print(virat_s_0002_q2_response)

        virat_s_0002_q2_correct_or_not = (
            virat_s_0002_q2_correct_response == virat_s_0002_q2_response
        )

        print(virat_s_0002_q2_correct_or_not)

        virat_s_0002_video_name = "VIRAT_S_0002"
        print(virat_s_0002_video_name)

        virat_s_0002_user_timeline_type = row_as_list[48]
        print(virat_s_0002_user_timeline_type)

        virat_s_0002_page_timer = row_as_list[59]

        virat_s_0002_page_timer_first_click = -1

        virat_s_0002_page_timer_last_click = -1

        if virat_s_0002_page_timer != "None":

            virat_s_0002_page_timer = virat_s_0002_page_timer.split("\n")

            first_click_split = virat_s_0002_page_timer[0].split(" : ")

            first_click = first_click_split[1].replace("_x000D_", "")

            virat_s_0002_page_timer_first_click = int(first_click)

            last_click_split = virat_s_0002_page_timer[1].split(" : ")

            last_click = last_click_split[1].replace("_x000D_", "")

            virat_s_0002_page_timer_last_click = int(last_click)

        print(virat_s_0002_page_timer_first_click)

        print(virat_s_0002_page_timer_last_click)

        virat_s_0002_page_timer_time_between_clicks = (
            virat_s_0002_page_timer_last_click - virat_s_0002_page_timer_first_click
        )

        print(virat_s_0002_page_timer_time_between_clicks)

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0002_timelines_used_value
            + ", "
            + str(virat_s_0002_timelines_used_value_decrypted)
            + ", "
            + virat_s_0002_timeline_from_timelines_used
            + ", "
            + virat_s_0002_user_timeline_type
            + ", "
            + str(virat_s_0002_page_timer_first_click)
            + ", "
            + str(virat_s_0002_page_timer_last_click)
            + ", "
            + str(virat_s_0002_page_timer_time_between_clicks)
            + ", "
            + virat_s_0002_q1
            + ", "
            + virat_s_0002_video_name
            + ", "
            + virat_s_0002_q1_response
            + ", "
            + virat_s_0002_q1_correct_response
            + ", "
            + str(virat_s_0002_q1_correct_or_not)
            + "\n"
        )

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0002_timelines_used_value
            + ", "
            + str(virat_s_0002_timelines_used_value_decrypted)
            + ", "
            + virat_s_0002_timeline_from_timelines_used
            + ", "
            + virat_s_0002_user_timeline_type
            + ", "
            + str(virat_s_0002_page_timer_first_click)
            + ", "
            + str(virat_s_0002_page_timer_last_click)
            + ", "
            + str(virat_s_0002_page_timer_time_between_clicks)
            + ", "
            + virat_s_0002_q2
            + ", "
            + virat_s_0002_video_name
            + ", "
            + virat_s_0002_q2_response
            + ", "
            + virat_s_0002_q2_correct_response
            + ", "
            + str(virat_s_0002_q2_correct_or_not)
            + "\n"
        )

        # VIRAT_S_0100 Data

        virat_s_0100_timelines_used_value = row_as_list[61]
        print(virat_s_0100_timelines_used_value)

        virat_s_0100_timelines_used_value_decrypted = (
            int(virat_s_0100_timelines_used_value) - 69368
        )
        print(virat_s_0100_timelines_used_value_decrypted)

        virat_s_0100_timelines_used_value_decrypted_last_digit = (
            virat_s_0100_timelines_used_value_decrypted % 10
        )
        print(virat_s_0100_timelines_used_value_decrypted_last_digit)

        virat_s_0100_timeline_from_timelines_used = timeline_types[
            virat_s_0100_timelines_used_value_decrypted_last_digit
        ]
        print(virat_s_0100_timeline_from_timelines_used)

        virat_s_0100_q1 = "Task: How long do these two people stay in the building?"
        virat_s_0100_q1_correct_response = "Less than two minutes"
        virat_s_0100_q1_response = row_as_list[62]
        print(virat_s_0100_q1_response)

        virat_s_0100_q1_correct_or_not = (
            virat_s_0100_q1_correct_response == virat_s_0100_q1_response
        )

        print(virat_s_0100_q1_correct_or_not)

        virat_s_0100_q2 = "Task: During which timeframe do you see this man unloading a blue shoulder bag from his car?"
        virat_s_0100_q2_correct_response = "48:20 – 48:30"
        virat_s_0100_q2_response = row_as_list[63]
        print(virat_s_0100_q2_response)

        virat_s_0100_q2_correct_or_not = (
            virat_s_0100_q2_correct_response == virat_s_0100_q2_response
        )

        print(virat_s_0100_q2_correct_or_not)

        virat_s_0100_video_name = "VIRAT_S_0100"
        print(virat_s_0100_video_name)

        virat_s_0100_user_timeline_type = row_as_list[64]
        print(virat_s_0100_user_timeline_type)

        virat_s_0100_page_timer = row_as_list[75]

        virat_s_0100_page_timer_first_click = -1

        virat_s_0100_page_timer_last_click = -1

        if virat_s_0100_page_timer != "None":

            virat_s_0100_page_timer = virat_s_0100_page_timer.split("\n")

            first_click_split = virat_s_0100_page_timer[0].split(" : ")

            first_click = first_click_split[1].replace("_x000D_", "")

            virat_s_0100_page_timer_first_click = int(first_click)

            last_click_split = virat_s_0100_page_timer[1].split(" : ")

            last_click = last_click_split[1].replace("_x000D_", "")

            virat_s_0100_page_timer_last_click = int(last_click)

        print(virat_s_0100_page_timer_first_click)

        print(virat_s_0100_page_timer_last_click)

        virat_s_0100_page_timer_time_between_clicks = (
            virat_s_0100_page_timer_last_click - virat_s_0100_page_timer_first_click
        )

        print(virat_s_0100_page_timer_time_between_clicks)

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0100_timelines_used_value
            + ", "
            + str(virat_s_0100_timelines_used_value_decrypted)
            + ", "
            + virat_s_0100_timeline_from_timelines_used
            + ", "
            + virat_s_0100_user_timeline_type
            + ", "
            + str(virat_s_0100_page_timer_first_click)
            + ", "
            + str(virat_s_0100_page_timer_last_click)
            + ", "
            + str(virat_s_0100_page_timer_time_between_clicks)
            + ", "
            + virat_s_0100_q1
            + ", "
            + virat_s_0100_video_name
            + ", "
            + virat_s_0100_q1_response
            + ", "
            + virat_s_0100_q1_correct_response
            + ", "
            + str(virat_s_0100_q1_correct_or_not)
            + "\n"
        )

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0100_timelines_used_value
            + ", "
            + str(virat_s_0100_timelines_used_value_decrypted)
            + ", "
            + virat_s_0100_timeline_from_timelines_used
            + ", "
            + virat_s_0100_user_timeline_type
            + ", "
            + str(virat_s_0100_page_timer_first_click)
            + ", "
            + str(virat_s_0100_page_timer_last_click)
            + ", "
            + str(virat_s_0100_page_timer_time_between_clicks)
            + ", "
            + virat_s_0100_q2
            + ", "
            + virat_s_0100_video_name
            + ", "
            + virat_s_0100_q2_response
            + ", "
            + virat_s_0100_q2_correct_response
            + ", "
            + str(virat_s_0100_q2_correct_or_not)
            + "\n"
        )

        # VIRAT_S_0102 Data

        virat_s_0102_timelines_used_value = row_as_list[77]
        print(virat_s_0102_timelines_used_value)

        virat_s_0102_timelines_used_value_decrypted = (
            int(virat_s_0102_timelines_used_value) - 69368
        )
        print(virat_s_0102_timelines_used_value_decrypted)

        virat_s_0102_timelines_used_value_decrypted_last_digit = (
            virat_s_0102_timelines_used_value_decrypted % 10
        )
        print(virat_s_0102_timelines_used_value_decrypted_last_digit)

        virat_s_0102_timeline_from_timelines_used = timeline_types[
            virat_s_0102_timelines_used_value_decrypted_last_digit
        ]
        print(virat_s_0102_timeline_from_timelines_used)

        virat_s_0102_q1 = "Task: How long does this CHICANO employee take a break for?"
        virat_s_0102_q1_correct_response = "About four minutes"
        virat_s_0102_q1_response = row_as_list[78]
        print(virat_s_0102_q1_response)

        virat_s_0102_q1_correct_or_not = (
            virat_s_0102_q1_correct_response == virat_s_0102_q1_response
        )

        print(virat_s_0102_q1_correct_or_not)

        virat_s_0102_q2 = "Task: During which timeframe does the owner of this golf cart return and drive away?"
        virat_s_0102_q2_correct_response = "22:00 – 23:00"
        virat_s_0102_q2_response = row_as_list[79]
        print(virat_s_0102_q2_response)

        virat_s_0102_q2_correct_or_not = (
            virat_s_0102_q2_correct_response == virat_s_0102_q2_response
        )

        print(virat_s_0102_q2_correct_or_not)

        virat_s_0102_video_name = "VIRAT_S_0102"
        print(virat_s_0102_video_name)

        virat_s_0102_user_timeline_type = row_as_list[80]
        print(virat_s_0102_user_timeline_type)

        virat_s_0102_page_timer = row_as_list[91]

        virat_s_0102_page_timer_first_click = -1

        virat_s_0102_page_timer_last_click = -1

        if virat_s_0102_page_timer != "None":

            virat_s_0102_page_timer = virat_s_0102_page_timer.split("\n")

            first_click_split = virat_s_0102_page_timer[0].split(" : ")

            first_click = first_click_split[1].replace("_x000D_", "")

            virat_s_0102_page_timer_first_click = int(first_click)

            last_click_split = virat_s_0102_page_timer[1].split(" : ")

            last_click = last_click_split[1].replace("_x000D_", "")

            virat_s_0102_page_timer_last_click = int(last_click)

        print(virat_s_0102_page_timer_first_click)

        print(virat_s_0102_page_timer_last_click)

        virat_s_0102_page_timer_time_between_clicks = (
            virat_s_0102_page_timer_last_click - virat_s_0102_page_timer_first_click
        )

        print(virat_s_0102_page_timer_time_between_clicks)

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0102_timelines_used_value
            + ", "
            + str(virat_s_0102_timelines_used_value_decrypted)
            + ", "
            + virat_s_0102_timeline_from_timelines_used
            + ", "
            + virat_s_0102_user_timeline_type
            + ", "
            + str(virat_s_0102_page_timer_first_click)
            + ", "
            + str(virat_s_0102_page_timer_last_click)
            + ", "
            + str(virat_s_0102_page_timer_time_between_clicks)
            + ", "
            + virat_s_0102_q1
            + ", "
            + virat_s_0102_video_name
            + ", "
            + virat_s_0102_q1_response
            + ", "
            + virat_s_0102_q1_correct_response
            + ", "
            + str(virat_s_0102_q1_correct_or_not)
            + "\n"
        )

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0102_timelines_used_value
            + ", "
            + str(virat_s_0102_timelines_used_value_decrypted)
            + ", "
            + virat_s_0102_timeline_from_timelines_used
            + ", "
            + virat_s_0102_user_timeline_type
            + ", "
            + str(virat_s_0102_page_timer_first_click)
            + ", "
            + str(virat_s_0102_page_timer_last_click)
            + ", "
            + str(virat_s_0102_page_timer_time_between_clicks)
            + ", "
            + virat_s_0102_q2
            + ", "
            + virat_s_0102_video_name
            + ", "
            + virat_s_0102_q2_response
            + ", "
            + virat_s_0102_q2_correct_response
            + ", "
            + str(virat_s_0102_q2_correct_or_not)
            + "\n"
        )

        # VIRAT_S_0400 Data

        virat_s_0400_timelines_used_value = row_as_list[93]
        print(virat_s_0400_timelines_used_value)

        virat_s_0400_timelines_used_value_decrypted = (
            int(virat_s_0400_timelines_used_value) - 69368
        )
        print(virat_s_0400_timelines_used_value_decrypted)

        virat_s_0400_timelines_used_value_decrypted_last_digit = (
            virat_s_0400_timelines_used_value_decrypted % 10
        )
        print(virat_s_0400_timelines_used_value_decrypted_last_digit)

        virat_s_0400_timeline_from_timelines_used = timeline_types[
            virat_s_0400_timelines_used_value_decrypted_last_digit
        ]
        print(virat_s_0400_timeline_from_timelines_used)

        virat_s_0400_q1 = "Task: How long does the blue pickup truck remain parked after two men in white shirts begin unloading objects from the trunk of the blue pickup truck?"
        virat_s_0400_q1_correct_response = "About six minutes"
        virat_s_0400_q1_response = row_as_list[94]
        print(virat_s_0400_q1_response)

        virat_s_0400_q1_correct_or_not = (
            virat_s_0400_q1_correct_response == virat_s_0400_q1_response
        )

        print(virat_s_0400_q1_correct_or_not)

        virat_s_0400_q2 = "Task: During which timeframe does a couple run across the screen starting from this house carrying a pizza?"
        virat_s_0400_q2_correct_response = "50:00 – 51:00"
        virat_s_0400_q2_response = row_as_list[95]
        print(virat_s_0400_q2_response)

        virat_s_0400_q2_correct_or_not = (
            virat_s_0400_q2_correct_response == virat_s_0400_q2_response
        )

        print(virat_s_0400_q2_correct_or_not)

        virat_s_0400_video_name = "VIRAT_S_0400"
        print(virat_s_0400_video_name)

        virat_s_0400_user_timeline_type = row_as_list[96]
        print(virat_s_0400_user_timeline_type)

        virat_s_0400_page_timer = row_as_list[107]

        virat_s_0400_page_timer_first_click = -1

        virat_s_0400_page_timer_last_click = -1

        if virat_s_0400_page_timer != "None":

            virat_s_0400_page_timer = virat_s_0400_page_timer.split("\n")

            first_click_split = virat_s_0400_page_timer[0].split(" : ")

            first_click = first_click_split[1].replace("_x000D_", "")

            virat_s_0400_page_timer_first_click = int(first_click)

            last_click_split = virat_s_0400_page_timer[1].split(" : ")

            last_click = last_click_split[1].replace("_x000D_", "")

            virat_s_0400_page_timer_last_click = int(last_click)

        print(virat_s_0400_page_timer_first_click)

        print(virat_s_0400_page_timer_last_click)

        virat_s_0400_page_timer_time_between_clicks = (
            virat_s_0400_page_timer_last_click - virat_s_0400_page_timer_first_click
        )

        print(virat_s_0400_page_timer_time_between_clicks)

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0400_timelines_used_value
            + ", "
            + str(virat_s_0400_timelines_used_value_decrypted)
            + ", "
            + virat_s_0400_timeline_from_timelines_used
            + ", "
            + virat_s_0400_user_timeline_type
            + ", "
            + str(virat_s_0400_page_timer_first_click)
            + ", "
            + str(virat_s_0400_page_timer_last_click)
            + ", "
            + str(virat_s_0400_page_timer_time_between_clicks)
            + ", "
            + virat_s_0400_q1
            + ", "
            + virat_s_0400_video_name
            + ", "
            + virat_s_0400_q1_response
            + ", "
            + virat_s_0400_q1_correct_response
            + ", "
            + str(virat_s_0400_q1_correct_or_not)
            + "\n"
        )

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0400_timelines_used_value
            + ", "
            + str(virat_s_0400_timelines_used_value_decrypted)
            + ", "
            + virat_s_0400_timeline_from_timelines_used
            + ", "
            + virat_s_0400_user_timeline_type
            + ", "
            + str(virat_s_0400_page_timer_first_click)
            + ", "
            + str(virat_s_0400_page_timer_last_click)
            + ", "
            + str(virat_s_0400_page_timer_time_between_clicks)
            + ", "
            + virat_s_0400_q2
            + ", "
            + virat_s_0400_video_name
            + ", "
            + virat_s_0400_q2_response
            + ", "
            + virat_s_0400_q2_correct_response
            + ", "
            + str(virat_s_0400_q2_correct_or_not)
            + "\n"
        )

        # VIRAT_S_0500 Data

        virat_s_0500_timelines_used_value = row_as_list[109]
        print(virat_s_0500_timelines_used_value)

        virat_s_0500_timelines_used_value_decrypted = (
            int(virat_s_0500_timelines_used_value) - 69368
        )
        print(virat_s_0500_timelines_used_value_decrypted)

        virat_s_0500_timelines_used_value_decrypted_last_digit = (
            virat_s_0500_timelines_used_value_decrypted % 10
        )
        print(virat_s_0500_timelines_used_value_decrypted_last_digit)

        virat_s_0500_timeline_from_timelines_used = timeline_types[
            virat_s_0500_timelines_used_value_decrypted_last_digit
        ]
        print(virat_s_0500_timeline_from_timelines_used)

        virat_s_0500_q1 = "Task: Order the following three events: - A person carrying a backpack rode a bike on the pedestrian sidewalk.:A person wearing pants ran to catch the green light while crossing the street.:A construction worker waved their hands to their colleagues."
        virat_s_0500_q1_correct_response = "2:1:3"
        virat_s_0500_q1_response = (
            row_as_list[110] + ":" + row_as_list[111] + ":" + row_as_list[112]
        )
        print(virat_s_0500_q1_response)

        virat_s_0500_q1_correct_or_not = (
            virat_s_0500_q1_correct_response == virat_s_0500_q1_response
        )

        print(virat_s_0500_q1_correct_or_not)

        virat_s_0500_q2 = "Task: What is the object unloaded from the white truck with a flatboard trailer?"
        virat_s_0500_q2_correct_response = "A slow-down sign"
        virat_s_0500_q2_response = row_as_list[113]
        print(virat_s_0500_q2_response)

        virat_s_0500_q2_correct_or_not = (
            virat_s_0500_q2_correct_response == virat_s_0500_q2_response
        )

        print(virat_s_0500_q2_correct_or_not)

        virat_s_0500_video_name = "VIRAT_S_0500"
        print(virat_s_0500_video_name)

        virat_s_0500_user_timeline_type = row_as_list[114]
        print(virat_s_0500_user_timeline_type)

        virat_s_0500_page_timer = row_as_list[125]

        virat_s_0500_page_timer_first_click = -1

        virat_s_0500_page_timer_last_click = -1

        if virat_s_0500_page_timer != "None":

            virat_s_0500_page_timer = virat_s_0500_page_timer.split("\n")

            first_click_split = virat_s_0500_page_timer[0].split(" : ")

            first_click = first_click_split[1].replace("_x000D_", "")

            virat_s_0500_page_timer_first_click = int(first_click)

            last_click_split = virat_s_0500_page_timer[1].split(" : ")

            last_click = last_click_split[1].replace("_x000D_", "")

            virat_s_0500_page_timer_last_click = int(last_click)

        print(virat_s_0500_page_timer_first_click)

        print(virat_s_0500_page_timer_last_click)

        virat_s_0500_page_timer_time_between_clicks = (
            virat_s_0500_page_timer_last_click - virat_s_0500_page_timer_first_click
        )

        print(virat_s_0500_page_timer_time_between_clicks)

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0500_timelines_used_value
            + ", "
            + str(virat_s_0500_timelines_used_value_decrypted)
            + ", "
            + virat_s_0500_timeline_from_timelines_used
            + ", "
            + virat_s_0500_user_timeline_type
            + ", "
            + str(virat_s_0500_page_timer_first_click)
            + ", "
            + str(virat_s_0500_page_timer_last_click)
            + ", "
            + str(virat_s_0500_page_timer_time_between_clicks)
            + ", "
            + virat_s_0500_q1
            + ", "
            + virat_s_0500_video_name
            + ", "
            + virat_s_0500_q1_response
            + ", "
            + virat_s_0500_q1_correct_response
            + ", "
            + str(virat_s_0500_q1_correct_or_not)
            + "\n"
        )

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0500_timelines_used_value
            + ", "
            + str(virat_s_0500_timelines_used_value_decrypted)
            + ", "
            + virat_s_0500_timeline_from_timelines_used
            + ", "
            + virat_s_0500_user_timeline_type
            + ", "
            + str(virat_s_0500_page_timer_first_click)
            + ", "
            + str(virat_s_0500_page_timer_last_click)
            + ", "
            + str(virat_s_0500_page_timer_time_between_clicks)
            + ", "
            + virat_s_0500_q2
            + ", "
            + virat_s_0500_video_name
            + ", "
            + virat_s_0500_q2_response
            + ", "
            + virat_s_0500_q2_correct_response
            + ", "
            + str(virat_s_0500_q2_correct_or_not)
            + "\n"
        )

question_responses_with_answers_csv.close()
