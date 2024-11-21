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

sus_answer_as_num = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5,
}

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("rawData.xlsx")

# Define variable to read sheet
dataframe1 = dataframe.active

sus_scores_csv = open("susScores.csv", "w")

current_line_num = 0

# Iterate the loop to read the cell values
for row in dataframe1.values:

    if current_line_num == 0:

        sus_scores_csv.write(
            "Response ID,"
            + "Timeline Used Value,"
            + "Timeline Used Value Decrypted,"
            + "Timeline Type (TimelinesUsed),"
            + "Timeline Type (User Entry),"
            + "Video Name,"
            + "(Original Answer) 1. I think that I would like to use this UI frequently,"
            + "(Original Answer) 2. I found the UI unnecessarily complex,"
            + "(Original Answer) 3. I thought the UI was easy to use,"
            + "(Original Answer) 4. I think that I would need the support of a technical person to be able to use this UI,"
            + "(Original Answer) 5. I found the various functions in this UI were well integrated,"
            + "(Original Answer) 6. I thought there was too much inconsistency in this UI,"
            + "(Original Answer) 7. I would imagine that most people would learn to use this UI very quickly,"
            + "(Original Answer) 8. I found the UI very cumbersome to use,"
            + "(Original Answer) 9. I felt very confident using the UI,"
            + "(Original Answer) 10. I needed to learn a lot of things before I could get going with this UI,"
            + "(Adjusted Answer) 1. I think that I would like to use this UI frequently,"
            + "(Adjusted Answer) 2. I found the UI unnecessarily complex,"
            + "(Adjusted Answer) 3. I thought the UI was easy to use,"
            + "(Adjusted Answer) 4. I think that I would need the support of a technical person to be able to use this UI,"
            + "(Adjusted Answer) 5. I found the various functions in this UI were well integrated,"
            + "(Adjusted Answer) 6. I thought there was too much inconsistency in this UI,"
            + "(Adjusted Answer) 7. I would imagine that most people would learn to use this UI very quickly,"
            + "(Adjusted Answer) 8. I found the UI very cumbersome to use,"
            + "(Adjusted Answer) 9. I felt very confident using the UI,"
            + "(Adjusted Answer) 10. I needed to learn a lot of things before I could get going with this UI,"
            + "Adjusted Answer Sum,"
            + "SUS Score\n"
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

        virat_s_0002_user_timeline_type = row_as_list[48]
        print(virat_s_0002_user_timeline_type)

        virat_s_0002_video_name = "VIRAT_S_0002"
        print(virat_s_0002_video_name)

        virat_s_0002_sus_q1_answer_as_num = sus_answer_as_num[row_as_list[49]]
        print(virat_s_0002_sus_q1_answer_as_num)

        virat_s_0002_sus_q2_answer_as_num = sus_answer_as_num[row_as_list[50]]
        print(virat_s_0002_sus_q2_answer_as_num)

        virat_s_0002_sus_q3_answer_as_num = sus_answer_as_num[row_as_list[51]]
        print(virat_s_0002_sus_q3_answer_as_num)

        virat_s_0002_sus_q4_answer_as_num = sus_answer_as_num[row_as_list[52]]
        print(virat_s_0002_sus_q4_answer_as_num)

        virat_s_0002_sus_q5_answer_as_num = sus_answer_as_num[row_as_list[53]]
        print(virat_s_0002_sus_q5_answer_as_num)

        virat_s_0002_sus_q6_answer_as_num = sus_answer_as_num[row_as_list[54]]
        print(virat_s_0002_sus_q6_answer_as_num)

        virat_s_0002_sus_q7_answer_as_num = sus_answer_as_num[row_as_list[55]]
        print(virat_s_0002_sus_q7_answer_as_num)

        virat_s_0002_sus_q8_answer_as_num = sus_answer_as_num[row_as_list[56]]
        print(virat_s_0002_sus_q8_answer_as_num)

        virat_s_0002_sus_q9_answer_as_num = sus_answer_as_num[row_as_list[57]]
        print(virat_s_0002_sus_q9_answer_as_num)

        virat_s_0002_sus_q10_answer_as_num = sus_answer_as_num[row_as_list[58]]
        print(virat_s_0002_sus_q10_answer_as_num)

        # Odd Answers Adjusted

        virat_s_0002_sus_q1_adjusted_answer = virat_s_0002_sus_q1_answer_as_num - 1
        print(virat_s_0002_sus_q1_adjusted_answer)

        virat_s_0002_sus_q3_adjusted_answer = virat_s_0002_sus_q3_answer_as_num - 1
        print(virat_s_0002_sus_q3_adjusted_answer)

        virat_s_0002_sus_q5_adjusted_answer = virat_s_0002_sus_q5_answer_as_num - 1
        print(virat_s_0002_sus_q5_adjusted_answer)

        virat_s_0002_sus_q7_adjusted_answer = virat_s_0002_sus_q7_answer_as_num - 1
        print(virat_s_0002_sus_q7_adjusted_answer)

        virat_s_0002_sus_q9_adjusted_answer = virat_s_0002_sus_q9_answer_as_num - 1
        print(virat_s_0002_sus_q9_adjusted_answer)

        # Even Answers Adjusted

        virat_s_0002_sus_q2_adjusted_answer = 5 - virat_s_0002_sus_q2_answer_as_num
        print(virat_s_0002_sus_q2_adjusted_answer)

        virat_s_0002_sus_q4_adjusted_answer = 5 - virat_s_0002_sus_q4_answer_as_num
        print(virat_s_0002_sus_q4_adjusted_answer)

        virat_s_0002_sus_q6_adjusted_answer = 5 - virat_s_0002_sus_q6_answer_as_num
        print(virat_s_0002_sus_q6_adjusted_answer)

        virat_s_0002_sus_q8_adjusted_answer = 5 - virat_s_0002_sus_q8_answer_as_num
        print(virat_s_0002_sus_q8_adjusted_answer)

        virat_s_0002_sus_q10_adjusted_answer = 5 - virat_s_0002_sus_q10_answer_as_num
        print(virat_s_0002_sus_q10_adjusted_answer)

        virat_s_0002_adjusted_answer_sum = (
            virat_s_0002_sus_q1_adjusted_answer +
            virat_s_0002_sus_q2_adjusted_answer +
            virat_s_0002_sus_q3_adjusted_answer +
            virat_s_0002_sus_q4_adjusted_answer +
            virat_s_0002_sus_q5_adjusted_answer +
            virat_s_0002_sus_q6_adjusted_answer +
            virat_s_0002_sus_q7_adjusted_answer +
            virat_s_0002_sus_q8_adjusted_answer +
            virat_s_0002_sus_q9_adjusted_answer +
            virat_s_0002_sus_q10_adjusted_answer
        )
        print(virat_s_0002_adjusted_answer_sum)

        virat_s_0002_sus_score = virat_s_0002_adjusted_answer_sum * 2.5
        print(virat_s_0002_sus_score)

        sus_scores_csv.write(
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
            + virat_s_0002_video_name
            + ", "
            + str(virat_s_0002_sus_q1_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q2_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q3_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q4_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q5_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q6_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q7_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q8_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q9_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q10_answer_as_num)
            + ", "
            + str(virat_s_0002_sus_q1_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q2_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q3_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q4_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q5_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q6_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q7_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q8_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q9_adjusted_answer)
            + ", "
            + str(virat_s_0002_sus_q10_adjusted_answer)
            + ", "
            + str(virat_s_0002_adjusted_answer_sum)
            + ", "
            + str(virat_s_0002_sus_score)
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

        virat_s_0100_user_timeline_type = row_as_list[64]
        print(virat_s_0100_user_timeline_type)

        virat_s_0100_video_name = "VIRAT_S_0100"
        print(virat_s_0100_video_name)

        virat_s_0100_sus_q1_answer_as_num = sus_answer_as_num[row_as_list[65]]
        print(virat_s_0100_sus_q1_answer_as_num)

        virat_s_0100_sus_q2_answer_as_num = sus_answer_as_num[row_as_list[66]]
        print(virat_s_0100_sus_q2_answer_as_num)

        virat_s_0100_sus_q3_answer_as_num = sus_answer_as_num[row_as_list[67]]
        print(virat_s_0100_sus_q3_answer_as_num)

        virat_s_0100_sus_q4_answer_as_num = sus_answer_as_num[row_as_list[68]]
        print(virat_s_0100_sus_q4_answer_as_num)

        virat_s_0100_sus_q5_answer_as_num = sus_answer_as_num[row_as_list[69]]
        print(virat_s_0100_sus_q5_answer_as_num)

        virat_s_0100_sus_q6_answer_as_num = sus_answer_as_num[row_as_list[70]]
        print(virat_s_0100_sus_q6_answer_as_num)

        virat_s_0100_sus_q7_answer_as_num = sus_answer_as_num[row_as_list[71]]
        print(virat_s_0100_sus_q7_answer_as_num)

        virat_s_0100_sus_q8_answer_as_num = sus_answer_as_num[row_as_list[72]]
        print(virat_s_0100_sus_q8_answer_as_num)

        virat_s_0100_sus_q9_answer_as_num = sus_answer_as_num[row_as_list[73]]
        print(virat_s_0100_sus_q9_answer_as_num)

        virat_s_0100_sus_q10_answer_as_num = sus_answer_as_num[row_as_list[74]]
        print(virat_s_0100_sus_q10_answer_as_num)

        # Odd Answers Adjusted

        virat_s_0100_sus_q1_adjusted_answer = virat_s_0100_sus_q1_answer_as_num - 1
        print(virat_s_0100_sus_q1_adjusted_answer)

        virat_s_0100_sus_q3_adjusted_answer = virat_s_0100_sus_q3_answer_as_num - 1
        print(virat_s_0100_sus_q3_adjusted_answer)

        virat_s_0100_sus_q5_adjusted_answer = virat_s_0100_sus_q5_answer_as_num - 1
        print(virat_s_0100_sus_q5_adjusted_answer)

        virat_s_0100_sus_q7_adjusted_answer = virat_s_0100_sus_q7_answer_as_num - 1
        print(virat_s_0100_sus_q7_adjusted_answer)

        virat_s_0100_sus_q9_adjusted_answer = virat_s_0100_sus_q9_answer_as_num - 1
        print(virat_s_0100_sus_q9_adjusted_answer)

        # Even Answers Adjusted

        virat_s_0100_sus_q2_adjusted_answer = 5 - virat_s_0100_sus_q2_answer_as_num
        print(virat_s_0100_sus_q2_adjusted_answer)

        virat_s_0100_sus_q4_adjusted_answer = 5 - virat_s_0100_sus_q4_answer_as_num
        print(virat_s_0100_sus_q4_adjusted_answer)

        virat_s_0100_sus_q6_adjusted_answer = 5 - virat_s_0100_sus_q6_answer_as_num
        print(virat_s_0100_sus_q6_adjusted_answer)

        virat_s_0100_sus_q8_adjusted_answer = 5 - virat_s_0100_sus_q8_answer_as_num
        print(virat_s_0100_sus_q8_adjusted_answer)

        virat_s_0100_sus_q10_adjusted_answer = 5 - virat_s_0100_sus_q10_answer_as_num
        print(virat_s_0100_sus_q10_adjusted_answer)

        virat_s_0100_adjusted_answer_sum = (
            virat_s_0100_sus_q1_adjusted_answer
            + virat_s_0100_sus_q2_adjusted_answer
            + virat_s_0100_sus_q3_adjusted_answer
            + virat_s_0100_sus_q4_adjusted_answer
            + virat_s_0100_sus_q5_adjusted_answer
            + virat_s_0100_sus_q6_adjusted_answer
            + virat_s_0100_sus_q7_adjusted_answer
            + virat_s_0100_sus_q8_adjusted_answer
            + virat_s_0100_sus_q9_adjusted_answer
            + virat_s_0100_sus_q10_adjusted_answer
        )
        print(virat_s_0100_adjusted_answer_sum)

        virat_s_0100_sus_score = virat_s_0100_adjusted_answer_sum * 2.5
        print(virat_s_0100_sus_score)

        sus_scores_csv.write(
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
            + virat_s_0100_video_name
            + ", "
            + str(virat_s_0100_sus_q1_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q2_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q3_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q4_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q5_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q6_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q7_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q8_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q9_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q10_answer_as_num)
            + ", "
            + str(virat_s_0100_sus_q1_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q2_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q3_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q4_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q5_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q6_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q7_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q8_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q9_adjusted_answer)
            + ", "
            + str(virat_s_0100_sus_q10_adjusted_answer)
            + ", "
            + str(virat_s_0100_adjusted_answer_sum)
            + ", "
            + str(virat_s_0100_sus_score)
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

        virat_s_0102_user_timeline_type = row_as_list[80]
        print(virat_s_0102_user_timeline_type)

        virat_s_0102_video_name = "VIRAT_S_0102"
        print(virat_s_0102_video_name)

        virat_s_0102_sus_q1_answer_as_num = sus_answer_as_num[row_as_list[81]]
        print(virat_s_0102_sus_q1_answer_as_num)

        virat_s_0102_sus_q2_answer_as_num = sus_answer_as_num[row_as_list[82]]
        print(virat_s_0102_sus_q2_answer_as_num)

        virat_s_0102_sus_q3_answer_as_num = sus_answer_as_num[row_as_list[83]]
        print(virat_s_0102_sus_q3_answer_as_num)

        virat_s_0102_sus_q4_answer_as_num = sus_answer_as_num[row_as_list[84]]
        print(virat_s_0102_sus_q4_answer_as_num)

        virat_s_0102_sus_q5_answer_as_num = sus_answer_as_num[row_as_list[85]]
        print(virat_s_0102_sus_q5_answer_as_num)

        virat_s_0102_sus_q6_answer_as_num = sus_answer_as_num[row_as_list[86]]
        print(virat_s_0102_sus_q6_answer_as_num)

        virat_s_0102_sus_q7_answer_as_num = sus_answer_as_num[row_as_list[87]]
        print(virat_s_0102_sus_q7_answer_as_num)

        virat_s_0102_sus_q8_answer_as_num = sus_answer_as_num[row_as_list[88]]
        print(virat_s_0102_sus_q8_answer_as_num)

        virat_s_0102_sus_q9_answer_as_num = sus_answer_as_num[row_as_list[89]]
        print(virat_s_0102_sus_q9_answer_as_num)

        virat_s_0102_sus_q10_answer_as_num = sus_answer_as_num[row_as_list[90]]
        print(virat_s_0102_sus_q10_answer_as_num)

        # Odd Answers Adjusted

        virat_s_0102_sus_q1_adjusted_answer = virat_s_0102_sus_q1_answer_as_num - 1
        print(virat_s_0102_sus_q1_adjusted_answer)

        virat_s_0102_sus_q3_adjusted_answer = virat_s_0102_sus_q3_answer_as_num - 1
        print(virat_s_0102_sus_q3_adjusted_answer)

        virat_s_0102_sus_q5_adjusted_answer = virat_s_0102_sus_q5_answer_as_num - 1
        print(virat_s_0102_sus_q5_adjusted_answer)

        virat_s_0102_sus_q7_adjusted_answer = virat_s_0102_sus_q7_answer_as_num - 1
        print(virat_s_0102_sus_q7_adjusted_answer)

        virat_s_0102_sus_q9_adjusted_answer = virat_s_0102_sus_q9_answer_as_num - 1
        print(virat_s_0102_sus_q9_adjusted_answer)

        # Even Answers Adjusted

        virat_s_0102_sus_q2_adjusted_answer = 5 - virat_s_0102_sus_q2_answer_as_num
        print(virat_s_0102_sus_q2_adjusted_answer)

        virat_s_0102_sus_q4_adjusted_answer = 5 - virat_s_0102_sus_q4_answer_as_num
        print(virat_s_0102_sus_q4_adjusted_answer)

        virat_s_0102_sus_q6_adjusted_answer = 5 - virat_s_0102_sus_q6_answer_as_num
        print(virat_s_0102_sus_q6_adjusted_answer)

        virat_s_0102_sus_q8_adjusted_answer = 5 - virat_s_0102_sus_q8_answer_as_num
        print(virat_s_0102_sus_q8_adjusted_answer)

        virat_s_0102_sus_q10_adjusted_answer = 5 - virat_s_0102_sus_q10_answer_as_num
        print(virat_s_0102_sus_q10_adjusted_answer)

        virat_s_0102_adjusted_answer_sum = (
            virat_s_0102_sus_q1_adjusted_answer
            + virat_s_0102_sus_q2_adjusted_answer
            + virat_s_0102_sus_q3_adjusted_answer
            + virat_s_0102_sus_q4_adjusted_answer
            + virat_s_0102_sus_q5_adjusted_answer
            + virat_s_0102_sus_q6_adjusted_answer
            + virat_s_0102_sus_q7_adjusted_answer
            + virat_s_0102_sus_q8_adjusted_answer
            + virat_s_0102_sus_q9_adjusted_answer
            + virat_s_0102_sus_q10_adjusted_answer
        )
        print(virat_s_0102_adjusted_answer_sum)

        virat_s_0102_sus_score = virat_s_0102_adjusted_answer_sum * 2.5
        print(virat_s_0102_sus_score)

        sus_scores_csv.write(
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
            + virat_s_0102_video_name
            + ", "
            + str(virat_s_0102_sus_q1_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q2_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q3_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q4_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q5_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q6_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q7_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q8_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q9_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q10_answer_as_num)
            + ", "
            + str(virat_s_0102_sus_q1_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q2_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q3_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q4_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q5_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q6_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q7_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q8_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q9_adjusted_answer)
            + ", "
            + str(virat_s_0102_sus_q10_adjusted_answer)
            + ", "
            + str(virat_s_0102_adjusted_answer_sum)
            + ", "
            + str(virat_s_0102_sus_score)
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

        virat_s_0400_user_timeline_type = row_as_list[96]
        print(virat_s_0400_user_timeline_type)

        virat_s_0400_video_name = "VIRAT_S_0400"
        print(virat_s_0400_video_name)

        virat_s_0400_sus_q1_answer_as_num = sus_answer_as_num[row_as_list[97]]
        print(virat_s_0400_sus_q1_answer_as_num)

        virat_s_0400_sus_q2_answer_as_num = sus_answer_as_num[row_as_list[98]]
        print(virat_s_0400_sus_q2_answer_as_num)

        virat_s_0400_sus_q3_answer_as_num = sus_answer_as_num[row_as_list[99]]
        print(virat_s_0400_sus_q3_answer_as_num)

        virat_s_0400_sus_q4_answer_as_num = sus_answer_as_num[row_as_list[100]]
        print(virat_s_0400_sus_q4_answer_as_num)

        virat_s_0400_sus_q5_answer_as_num = sus_answer_as_num[row_as_list[101]]
        print(virat_s_0400_sus_q5_answer_as_num)

        virat_s_0400_sus_q6_answer_as_num = sus_answer_as_num[row_as_list[102]]
        print(virat_s_0400_sus_q6_answer_as_num)

        virat_s_0400_sus_q7_answer_as_num = sus_answer_as_num[row_as_list[103]]
        print(virat_s_0400_sus_q7_answer_as_num)

        virat_s_0400_sus_q8_answer_as_num = sus_answer_as_num[row_as_list[104]]
        print(virat_s_0400_sus_q8_answer_as_num)

        virat_s_0400_sus_q9_answer_as_num = sus_answer_as_num[row_as_list[105]]
        print(virat_s_0400_sus_q9_answer_as_num)

        virat_s_0400_sus_q10_answer_as_num = sus_answer_as_num[row_as_list[106]]
        print(virat_s_0400_sus_q10_answer_as_num)

        # Odd Answers Adjusted

        virat_s_0400_sus_q1_adjusted_answer = virat_s_0400_sus_q1_answer_as_num - 1
        print(virat_s_0400_sus_q1_adjusted_answer)

        virat_s_0400_sus_q3_adjusted_answer = virat_s_0400_sus_q3_answer_as_num - 1
        print(virat_s_0400_sus_q3_adjusted_answer)

        virat_s_0400_sus_q5_adjusted_answer = virat_s_0400_sus_q5_answer_as_num - 1
        print(virat_s_0400_sus_q5_adjusted_answer)

        virat_s_0400_sus_q7_adjusted_answer = virat_s_0400_sus_q7_answer_as_num - 1
        print(virat_s_0400_sus_q7_adjusted_answer)

        virat_s_0400_sus_q9_adjusted_answer = virat_s_0400_sus_q9_answer_as_num - 1
        print(virat_s_0400_sus_q9_adjusted_answer)

        # Even Answers Adjusted

        virat_s_0400_sus_q2_adjusted_answer = 5 - virat_s_0400_sus_q2_answer_as_num
        print(virat_s_0400_sus_q2_adjusted_answer)

        virat_s_0400_sus_q4_adjusted_answer = 5 - virat_s_0400_sus_q4_answer_as_num
        print(virat_s_0400_sus_q4_adjusted_answer)

        virat_s_0400_sus_q6_adjusted_answer = 5 - virat_s_0400_sus_q6_answer_as_num
        print(virat_s_0400_sus_q6_adjusted_answer)

        virat_s_0400_sus_q8_adjusted_answer = 5 - virat_s_0400_sus_q8_answer_as_num
        print(virat_s_0400_sus_q8_adjusted_answer)

        virat_s_0400_sus_q10_adjusted_answer = 5 - virat_s_0400_sus_q10_answer_as_num
        print(virat_s_0400_sus_q10_adjusted_answer)

        virat_s_0400_adjusted_answer_sum = (
            virat_s_0400_sus_q1_adjusted_answer
            + virat_s_0400_sus_q2_adjusted_answer
            + virat_s_0400_sus_q3_adjusted_answer
            + virat_s_0400_sus_q4_adjusted_answer
            + virat_s_0400_sus_q5_adjusted_answer
            + virat_s_0400_sus_q6_adjusted_answer
            + virat_s_0400_sus_q7_adjusted_answer
            + virat_s_0400_sus_q8_adjusted_answer
            + virat_s_0400_sus_q9_adjusted_answer
            + virat_s_0400_sus_q10_adjusted_answer
        )
        print(virat_s_0400_adjusted_answer_sum)

        virat_s_0400_sus_score = virat_s_0400_adjusted_answer_sum * 2.5
        print(virat_s_0400_sus_score)

        sus_scores_csv.write(
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
            + virat_s_0400_video_name
            + ", "
            + str(virat_s_0400_sus_q1_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q2_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q3_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q4_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q5_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q6_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q7_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q8_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q9_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q10_answer_as_num)
            + ", "
            + str(virat_s_0400_sus_q1_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q2_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q3_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q4_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q5_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q6_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q7_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q8_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q9_adjusted_answer)
            + ", "
            + str(virat_s_0400_sus_q10_adjusted_answer)
            + ", "
            + str(virat_s_0400_adjusted_answer_sum)
            + ", "
            + str(virat_s_0400_sus_score)
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

        virat_s_0500_user_timeline_type = row_as_list[114]
        print(virat_s_0500_user_timeline_type)

        virat_s_0500_video_name = "VIRAT_S_0500"
        print(virat_s_0500_video_name)

        virat_s_0500_sus_q1_answer_as_num = sus_answer_as_num[row_as_list[115]]
        print(virat_s_0500_sus_q1_answer_as_num)

        virat_s_0500_sus_q2_answer_as_num = sus_answer_as_num[row_as_list[116]]
        print(virat_s_0500_sus_q2_answer_as_num)

        virat_s_0500_sus_q3_answer_as_num = sus_answer_as_num[row_as_list[117]]
        print(virat_s_0500_sus_q3_answer_as_num)

        virat_s_0500_sus_q4_answer_as_num = sus_answer_as_num[row_as_list[118]]
        print(virat_s_0500_sus_q4_answer_as_num)

        virat_s_0500_sus_q5_answer_as_num = sus_answer_as_num[row_as_list[119]]
        print(virat_s_0500_sus_q5_answer_as_num)

        virat_s_0500_sus_q6_answer_as_num = sus_answer_as_num[row_as_list[120]]
        print(virat_s_0500_sus_q6_answer_as_num)

        virat_s_0500_sus_q7_answer_as_num = sus_answer_as_num[row_as_list[121]]
        print(virat_s_0500_sus_q7_answer_as_num)

        virat_s_0500_sus_q8_answer_as_num = sus_answer_as_num[row_as_list[122]]
        print(virat_s_0500_sus_q8_answer_as_num)

        virat_s_0500_sus_q9_answer_as_num = sus_answer_as_num[row_as_list[123]]
        print(virat_s_0500_sus_q9_answer_as_num)

        virat_s_0500_sus_q10_answer_as_num = sus_answer_as_num[row_as_list[124]]
        print(virat_s_0500_sus_q10_answer_as_num)

        # Odd Answers Adjusted

        virat_s_0500_sus_q1_adjusted_answer = virat_s_0500_sus_q1_answer_as_num - 1
        print(virat_s_0500_sus_q1_adjusted_answer)

        virat_s_0500_sus_q3_adjusted_answer = virat_s_0500_sus_q3_answer_as_num - 1
        print(virat_s_0500_sus_q3_adjusted_answer)

        virat_s_0500_sus_q5_adjusted_answer = virat_s_0500_sus_q5_answer_as_num - 1
        print(virat_s_0500_sus_q5_adjusted_answer)

        virat_s_0500_sus_q7_adjusted_answer = virat_s_0500_sus_q7_answer_as_num - 1
        print(virat_s_0500_sus_q7_adjusted_answer)

        virat_s_0500_sus_q9_adjusted_answer = virat_s_0500_sus_q9_answer_as_num - 1
        print(virat_s_0500_sus_q9_adjusted_answer)

        # Even Answers Adjusted

        virat_s_0500_sus_q2_adjusted_answer = 5 - virat_s_0500_sus_q2_answer_as_num
        print(virat_s_0500_sus_q2_adjusted_answer)

        virat_s_0500_sus_q4_adjusted_answer = 5 - virat_s_0500_sus_q4_answer_as_num
        print(virat_s_0500_sus_q4_adjusted_answer)

        virat_s_0500_sus_q6_adjusted_answer = 5 - virat_s_0500_sus_q6_answer_as_num
        print(virat_s_0500_sus_q6_adjusted_answer)

        virat_s_0500_sus_q8_adjusted_answer = 5 - virat_s_0500_sus_q8_answer_as_num
        print(virat_s_0500_sus_q8_adjusted_answer)

        virat_s_0500_sus_q10_adjusted_answer = 5 - virat_s_0500_sus_q10_answer_as_num
        print(virat_s_0500_sus_q10_adjusted_answer)

        virat_s_0500_adjusted_answer_sum = (
            virat_s_0500_sus_q1_adjusted_answer
            + virat_s_0500_sus_q2_adjusted_answer
            + virat_s_0500_sus_q3_adjusted_answer
            + virat_s_0500_sus_q4_adjusted_answer
            + virat_s_0500_sus_q5_adjusted_answer
            + virat_s_0500_sus_q6_adjusted_answer
            + virat_s_0500_sus_q7_adjusted_answer
            + virat_s_0500_sus_q8_adjusted_answer
            + virat_s_0500_sus_q9_adjusted_answer
            + virat_s_0500_sus_q10_adjusted_answer
        )
        print(virat_s_0500_adjusted_answer_sum)

        virat_s_0500_sus_score = virat_s_0500_adjusted_answer_sum * 2.5
        print(virat_s_0500_sus_score)

        sus_scores_csv.write(
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
            + virat_s_0500_video_name
            + ", "
            + str(virat_s_0500_sus_q1_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q2_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q3_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q4_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q5_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q6_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q7_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q8_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q9_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q10_answer_as_num)
            + ", "
            + str(virat_s_0500_sus_q1_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q2_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q3_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q4_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q5_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q6_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q7_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q8_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q9_adjusted_answer)
            + ", "
            + str(virat_s_0500_sus_q10_adjusted_answer)
            + ", "
            + str(virat_s_0500_adjusted_answer_sum)
            + ", "
            + str(virat_s_0500_sus_score)
            + "\n"
        )

sus_scores_csv.close()
