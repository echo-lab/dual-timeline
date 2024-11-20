timeline_types = {
    1: "Timeline 1 (Base Interface)",
    2: "Timeline 2 (Density Graph)",
    3: "Timeline 3 (Event Blocks)",
    4: "Timeline 4 (Density Graph + Event Blocks)",
    5: "Timeline 5 (Event Thumbnails)",
    6: "Other",
}

question_responses_csv = open("questionResponses.csv", "r")

question_responses = question_responses_csv.readlines()

question_responses_with_answers_csv = open("questionResponsesAndAnswers.csv", "w")

current_line_num = 0

for question_response in question_responses:
    question_response = question_response.strip().split(",")
    if current_line_num == 0:

        question_responses_with_answers_csv.write(
            "Participant/Response ID, Timeline Used Value, Timeline Used Value Decrypted, Timeline Type (TimelinesUsed), Timeline Type (User Entry), Question, Video Number, Their Answer, Correct Answer\n"
        )

        current_line_num += 1
    else:
        response_id = question_response[0]
        print(response_id)

        # VIRAT_S_0002 Data

        virat_s_0002_timelines_used_value = question_response[2]
        print(virat_s_0002_timelines_used_value)

        virat_s_0002_timelines_used_value_decrypted = int(question_response[2]) - 69368
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
        virat_s_0002_q1_response = question_response[3]
        print(virat_s_0002_q1_response)

        virat_s_0002_q2 = "Task: During which timeframe do you see this man unloading a blue shoulder bag from his car?"
        virat_s_0002_q2_correct_response = "43:00 – 45:00"
        virat_s_0002_q2_response = question_response[4]
        print(virat_s_0002_q2_response)

        virat_s_0002_video_name = "VIRAT_S_0002"

        virat_s_0002_user_timeline_type = question_response[5]
        print(virat_s_0002_user_timeline_type)

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
            + virat_s_0002_q1
            + ", "
            + virat_s_0002_video_name
            + ", "
            + virat_s_0002_q1_response
            + ", "
            + virat_s_0002_q1_correct_response
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
            + virat_s_0002_q2
            + ", "
            + virat_s_0002_video_name
            + ", "
            + virat_s_0002_q2_response
            + ", "
            + virat_s_0002_q2_correct_response
            + "\n"
        )

        # VIRAT_S_0100 Data

        virat_s_0100_timelines_used_value = question_response[7]
        print(virat_s_0100_timelines_used_value)

        virat_s_0100_timelines_used_value_decrypted = int(question_response[7]) - 69368
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
        virat_s_0100_q1_correct_response = "About two minutes"
        virat_s_0100_q1_response = question_response[8]
        print(virat_s_0100_q1_response)

        virat_s_0100_q2 = "Task: During which timeframe do you see this man unloading a blue shoulder bag from his car?"
        virat_s_0100_q2_correct_response = "48:20 – 48:30"
        virat_s_0100_q2_response = question_response[9]
        print(virat_s_0100_q2_response)

        virat_s_0100_video_name = "VIRAT_S_0100"

        virat_s_0100_user_timeline_type = question_response[10]
        print(virat_s_0100_user_timeline_type)

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
            + virat_s_0100_q1
            + ", "
            + virat_s_0100_video_name
            + ", "
            + virat_s_0100_q1_response
            + ", "
            + virat_s_0100_q1_correct_response
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
            + virat_s_0100_q2
            + ", "
            + virat_s_0100_video_name
            + ", "
            + virat_s_0100_q2_response
            + ", "
            + virat_s_0100_q2_correct_response
            + "\n"
        )

        # VIRAT_S_0102 Data

        virat_s_0102_timelines_used_value = question_response[12]
        print(virat_s_0102_timelines_used_value)

        virat_s_0102_timelines_used_value_decrypted = int(question_response[12]) - 69368
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
        virat_s_0102_q1_response = question_response[13]
        print(virat_s_0102_q1_response)

        virat_s_0102_q2 = "Task: During which timeframe does the owner of this golf cart return and drive away?"
        virat_s_0102_q2_correct_response = "22:00 – 23:00"
        virat_s_0102_q2_response = question_response[14]
        print(virat_s_0102_q2_response)

        virat_s_0102_video_name = "VIRAT_S_0102"

        virat_s_0102_user_timeline_type = question_response[15]
        print(virat_s_0102_user_timeline_type)

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
            + virat_s_0102_q1
            + ", "
            + virat_s_0102_video_name
            + ", "
            + virat_s_0102_q1_response
            + ", "
            + virat_s_0102_q1_correct_response
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
            + virat_s_0102_q2
            + ", "
            + virat_s_0102_video_name
            + ", "
            + virat_s_0102_q2_response
            + ", "
            + virat_s_0102_q2_correct_response
            + "\n"
        )

        # VIRAT_S_0400 Data

        virat_s_0400_timelines_used_value = question_response[17]
        print(virat_s_0400_timelines_used_value)

        virat_s_0400_timelines_used_value_decrypted = int(question_response[17]) - 69368
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
        virat_s_0400_q1_response = question_response[18]
        print(virat_s_0400_q1_response)

        virat_s_0400_q2 = "Task: During which timeframe does a couple run across the screen starting from this house carrying a pizza?"
        virat_s_0400_q2_correct_response = "50:00 – 51:00"
        virat_s_0400_q2_response = question_response[19]
        print(virat_s_0400_q2_response)

        virat_s_0400_video_name = "VIRAT_S_0400"

        virat_s_0400_user_timeline_type = question_response[20]
        print(virat_s_0400_user_timeline_type)

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
            + virat_s_0400_q1
            + ", "
            + virat_s_0400_video_name
            + ", "
            + virat_s_0400_q1_response
            + ", "
            + virat_s_0400_q1_correct_response
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
            + virat_s_0400_q2
            + ", "
            + virat_s_0400_video_name
            + ", "
            + virat_s_0400_q2_response
            + ", "
            + virat_s_0400_q2_correct_response
            + "\n"
        )

        # VIRAT_S_0500 Data

        virat_s_0500_timelines_used_value = question_response[22]
        print(virat_s_0500_timelines_used_value)

        virat_s_0500_timelines_used_value_decrypted = int(question_response[22]) - 69368
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
        virat_s_0500_q1_response = question_response[23] + ":" +  question_response[24] + ":" +  question_response[25]
        print(virat_s_0500_q1_response)

        virat_s_0500_q2 = "Task: What is the object unloaded from the white truck with a flatboard trailer?"
        virat_s_0500_q2_correct_response = "A slow-down sign"
        virat_s_0500_q2_response = question_response[26]
        print(virat_s_0500_q2_response)

        virat_s_0500_video_name = "VIRAT_S_0500"

        virat_s_0500_user_timeline_type = question_response[27]
        print(virat_s_0500_user_timeline_type)

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
            + virat_s_0500_q1
            + ", "
            + virat_s_0500_video_name
            + ", "
            + virat_s_0500_q1_response
            + ", "
            + virat_s_0500_q1_correct_response
            + "\n"
        )

        question_responses_with_answers_csv.write(
            response_id
            + ", "
            + virat_s_0500_timelines_used_value
            + ", "
            + str(virat_s_0500_timelines_used_value_decrypted)
            + ", "
            + virat_s_0500_user_timeline_type
            + ", "
            + virat_s_0500_timeline_from_timelines_used
            + ", "
            + virat_s_0500_q2
            + ", "
            + virat_s_0500_video_name
            + ", "
            + virat_s_0500_q2_response
            + ", "
            + virat_s_0500_q2_correct_response
            + "\n"
        )

question_responses_csv.close()
question_responses_with_answers_csv.close()
