library(ARTool)
library(emmeans)
library(readxl)
library(MASS)

susScores <- read_xlsx("/Users/aluu/git/dual-timeline/post-data/finalFinalData.xlsx", sheet = "susScores")

susScores <- susScores[susScores$TIMELINE != "Other" & susScores$VALID == "TRUE", ]

susScores$TIMELINE <- factor(susScores$TIMELINE)
susScores$FREQUENCY <- factor(susScores$FREQUENCY)
susScores$PID <- factor(susScores$PID)

model2 <- art(SUS ~ TIMELINE * FREQUENCY + (1 | PID), data = susScores)

summary(model2)

anova(model2)
