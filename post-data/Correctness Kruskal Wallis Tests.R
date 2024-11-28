library(ggplot2)
library(dplyr)

myData = valid_correctness_scores
print(myData)

# Show the group levels
print(levels(myData$TIMELINE))

result = kruskal.test(SCORE ~ TIMELINE,
                      data = myData)
print(result)

print(levels(myData$TIMELINE))

ggplot(myData, aes(fill=PID, y=SCORE, x=TIMELINE)) + 
  geom_bar(position='stack', stat='identity')

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
