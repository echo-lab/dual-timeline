library(ggplot2)

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

