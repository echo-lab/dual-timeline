library(dplyr)
library(FSA)

myDataSus = finalSusScores
print(myDataSus)

# Show the group levels
print(levels(myDataSus$TIMELINE))

kwResult = kruskal.test(SUS ~ TIMELINE,
                      data = myDataSus)
print(kwResult)

boxPlot <- boxplot(SUS ~ TIMELINE,
        data=myDataSus,
        main="Different boxplots for each Timeline Type",
        xlab="SUS Score",
        ylab="Timeline Type",
        col="orange",
        border="red",
        horizontal=TRUE,
        notch=TRUE
)

boxPlot

dunnResult = dunnTest(SUS ~ TIMELINE,
         data = myDataSus,
         method="bh")

print(dunnResult)

summary_data_sus = myDataSus %>% group_by(TIMELINE) %>% summarise(mean = mean(SUS), se = sd(SUS) / sqrt(n()))

print(summary_data_sus)

ggplot(summary_data, aes(x = TIMELINE, y = mean, fill = mean)) +
  geom_bar(stat = "identity", position = position_dodge(), width=0.7) +
  labs(title = "Correctness Bar Chart",
       x = "Timeline Type",
       y = "Average SUS Score") +
  geom_errorbar(aes(ymin = mean - se, ymax = mean + se))

# averages
aggregate(myDataSus$SUS, list(myDataSus$TIMELINE), FUN=mean)

#filteredResult = kruskal.test(SUS ~ TimelineType,
#                      data = filteredMyDataSus)
#print(filteredResult)

