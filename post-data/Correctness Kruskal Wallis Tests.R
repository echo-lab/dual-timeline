library(ggplot2)
library(dplyr)

myData = valid_correctness_scores
print(myData)

pid_list = c("147906122", "148060312", "148063802", "148063804", "148063806", "148063807", "148063808", "148072624", "148087855", "148088832", "148121369", "148121371", "148121544", "148121549", "148191331", "148225108", "148242096", "148250834", "148355343", "148379134", "148457705", "148463769", "148516311", "148547931", "148551719", "148552210", "148558714", "148743058", "148768751", "148784892", "148786365", "148796085", "148822625", "148904494", "148958404", "149094645", "149140946", "149185311", "149215102", "149353591", "149439530", "149466211", "149508537")

filteredMyDataCorrectness = myData %>% filter(PID %in% pid_list)

# Show the group levels
print(levels(myData$TIMELINE))

result = kruskal.test(SCORE ~ TIMELINE,
                      data = myData)
print(result)

print(levels(myData$TIMELINE))

ggplot(myData, aes(fill=SCORE, y=TIMELINE, x=PID)) + 
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

# averages
aggregate(myData$SCORE, list(myData$TIMELINE), FUN=mean)

filteredResult = kruskal.test(SCORE ~ TIMELINE,
                      data = filteredMyDataCorrectness)
print(filteredResult)

# Select the columns of interest
selected_data <- filteredMyDataCorrectness %>% select(TIMELINE, SCORE)

# Create a contingency table for TIMELINE AND SCORE
contingency_table <- table(selected_data$SCORE, selected_data$TIMELINE)

# View the contingency table
print(contingency_table)

# Perform chi-square test
chi_square_test <- chisq.test(contingency_table)

# View the results
print(chi_square_test)

