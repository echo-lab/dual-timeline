library(dplyr)

myDataSus = valid_just_sus_scores
print(myDataSus)

pid_list = c("147906122", "148060312", "148063802", "148063804", "148063806", "148063807", "148063808", "148072624", "148087855", "148088832", "148121369", "148121371", "148121544", "148121549", "148191331", "148225108", "148242096", "148250834", "148355343", "148379134", "148457705", "148463769", "148516311", "148547931", "148551719", "148552210", "148558714", "148743058", "148768751", "148784892", "148786365", "148796085", "148822625", "148904494", "148958404", "149094645", "149140946", "149185311", "149215102", "149353591", "149439530", "149466211", "149508537")

filteredMyDataSus = myDataSus %>% filter(PID %in% pid_list)

# Show the group levels
print(levels(myDataSus$TimelineType))

result = kruskal.test(SUS ~ TimelineType,
                      data = myDataSus)
print(result)

boxPlot <- boxplot(SUS ~ TimelineType,
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

# averages
aggregate(myDataSus$SUS, list(myDataSus$TimelineType), FUN=mean)

filteredResult = kruskal.test(SUS ~ TimelineType,
                      data = filteredMyDataSus)
print(filteredResult)

