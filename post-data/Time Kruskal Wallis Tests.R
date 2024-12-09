library(FSA)
library(dplyr)

myDataTime = finalTime
print(myDataTime)

# Show the group levels
print(levels(myDataTime$TIMELINE))

result = kruskal.test(TIME ~ TIMELINE,
                      data = myDataTime)
print(result)

print(boxplot(TIME ~ TIMELINE,
        data=myDataTime,
        main="Different boxplots for each Timeline Type",
        xlab="Time Between First and Last Click",
        ylab="Timeline Type",
        col="orange",
        border="red",
        horizontal=TRUE,
        notch=TRUE
))


dunnResult = dunnTest(TIME ~ TIMELINE,
                      data = myDataTime,
                      method="bh")

print(dunnResult)

summary_data_time = myDataTime %>% group_by(TIMELINE) %>% summarise(mean = mean(TIME), se = sd(TIME) / sqrt(n()))

print(summary_data_time)

# averages
aggregate(myDataTime$TIME, list(myDataTime$TIMELINE), FUN=mean)

PIDs = unique(myDataTime$PID)

