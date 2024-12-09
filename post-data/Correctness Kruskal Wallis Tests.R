library(ggplot2)
library(dplyr)
library(FSA)

myData = timelineCorrectnessScores
print(myData)

# Show the group levels
print(levels(myData$TIMELINE))

result = kruskal.test(SCORE ~ TIMELINE,
                      data = myData)
print(result)

dunnResult = dunnTest(SCORE ~ TIMELINE,
                      data = myData,
                      method="bh")

print(dunnResult)

summary_data = myData %>% group_by(TIMELINE) %>% summarise(mean = mean(SCORE), se = sd(SCORE) / sqrt(n()))

print(summary_data)

ggplot(summary_data, aes(x = TIMELINE, y = mean, fill = mean)) +
  geom_bar(stat = "identity", position = position_dodge(), width=0.7) +
  labs(title = "Correctness Bar Chart",
       x = "Timeline Type",
       y = "Average Correctness") +
  geom_errorbar(aes(ymin = mean - se, ymax = mean + se))
              

print(levels(myData$TIMELINE))

#ggplot(myData, aes(fill=SCORE, y=TIMELINE, x=PID)) + 
#  geom_bar(position='stack', stat='identity')

# Select the columns of interest
selected_data <- myData %>% select(TIMELINE, SCORE)

# Create a contingency table for TIMELINE AND SCORE
contingency_table <- table(selected_data$SCORE, selected_data$TIMELINE)

# View the contingency table
print(contingency_table)

# Perform chi-square test
chi_square_test <- chisq.test(contingency_table)

# View the results
print(chi_square_test)

# averages
aggregate(myData$SCORE, list(myData$TIMELINE), FUN=mean)

#filteredResult = kruskal.test(SCORE ~ TIMELINE,
#                      data = filteredMyDataCorrectness)
#print(filteredResult)

# Select the columns of interest
#selected_data <- filteredMyDataCorrectness %>% select(TIMELINE, SCORE)

# Create a contingency table for TIMELINE AND SCORE
#contingency_table <- table(selected_data$SCORE, selected_data$TIMELINE)

# View the contingency table
#print(contingency_table)

# Perform chi-square test
#chi_square_test <- chisq.test(contingency_table)

# View the results
#print(chi_square_test)

