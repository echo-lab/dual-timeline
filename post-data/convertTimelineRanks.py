timeline_ranks_csv = open("timelineRanks.csv", "r")

timeline_ranks = timeline_ranks_csv.readlines()

timeline_name_and_rank_csv = open("timelineNameAndRank.csv", "w")

current_line_num = 0

for timeline_ranks_line in timeline_ranks:
    timeline_ranks_line = timeline_ranks_line.strip().split(",")
    if current_line_num == 0:

        timeline_name_and_rank_csv.write("Timeline Name, Rank\n")

        current_line_num += 1
    else:

        timeline1_name = "Timeline 1 (Base Interface)"
        timeline1_rank = timeline_ranks_line[0]
        print(timeline1_rank)

        timeline_name_and_rank_csv.write(timeline1_name + ", " + timeline1_rank + "\n")

        timeline2_name = "Timeline 2 (Density Graph)"
        timeline2_rank = timeline_ranks_line[1]
        print(timeline2_rank)

        timeline_name_and_rank_csv.write(timeline2_name + ", " + timeline2_rank + "\n")

        timeline3_name = "Timeline 3 (Event Blocks)"
        timeline3_rank = timeline_ranks_line[2]
        print(timeline3_rank)

        timeline_name_and_rank_csv.write(timeline3_name + ", " + timeline3_rank + "\n")

        timeline4_name = "Timeline 4 (Density Graph + Event Blocks)"
        timeline4_rank = timeline_ranks_line[3]
        print(timeline4_rank)

        timeline_name_and_rank_csv.write(timeline4_name + ", " + timeline4_rank + "\n")

        timeline5_name = "Timeline 5 (Event Thumbnails)"
        timeline5_rank = timeline_ranks_line[4]
        print(timeline5_rank)

        timeline_name_and_rank_csv.write(timeline5_name + ", " + timeline5_rank + "\n")

timeline_ranks_csv.close()
timeline_name_and_rank_csv.close()
