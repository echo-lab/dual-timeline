myDataSus = valid_just_sus_scores
print(myDataSus)

# Show the group levels
print(levels(myDataSus$TimelineType))

result = kruskal.test(SUS ~ TimelineType,
                      data = myDataSus)
print(result)

boxplot(SUS ~ TimelineType,
        data=myDataSus,
        main="Different boxplots for each Timeline Type",
        xlab="SUS Score",
        ylab="Timeline Type",
        col="orange",
        border="red",
        horizontal=TRUE,
        notch=TRUE
)

