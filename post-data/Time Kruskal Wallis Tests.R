myDataTime = valid_time_no_dups
print(myDataTime)

# Show the group levels
print(levels(myDataTime$TimelineType))

result = kruskal.test(TimeBetweenClicks ~ TimelineType,
                      data = myDataTime)
print(result)

boxplot(TimeBetweenClicks ~ TimelineType,
        data=myDataTime,
        main="Different boxplots for each Timeline Type",
        xlab="Time Between First and Last Click",
        ylab="Timeline Type",
        col="orange",
        border="red",
        horizontal=TRUE,
        notch=TRUE
)

