library(ARTool)
library(emmeans)
library(readxl)
library(MASS)

questionResponsesAndAnswers <- read_xlsx("/Users/aluu/git/dual-timeline/post-data/finalFinalData.xlsx", sheet = "questionResponsesAndAnswers")

questionResponsesAndAnswers <- questionResponsesAndAnswers[questionResponsesAndAnswers$TIMELINE != "Other" & questionResponsesAndAnswers$VALID == "TRUE", ]

questionResponsesAndAnswers$TIMELINE <- factor(questionResponsesAndAnswers$TIMELINE)
questionResponsesAndAnswers$QUESTION <- factor(questionResponsesAndAnswers$QUESTION)
questionResponsesAndAnswers$FREQUENCY <- factor(questionResponsesAndAnswers$FREQUENCY)
questionResponsesAndAnswers$CORRECT <- factor(questionResponsesAndAnswers$CORRECT)
questionResponsesAndAnswers$PID <- factor(questionResponsesAndAnswers$PID)

# Fit an ordinal logistic regression model
model1 <- polr(QUESTION ~ TIMELINE + FREQUENCY + CORRECT, data = questionResponsesAndAnswers, Hess = TRUE)

# Print the model summary
summary(model)

model2 <- art(TIME ~ TIMELINE * FREQUENCY * QUESTION + (1 | PID), data = questionResponsesAndAnswers)

summary(model2)

anova(model2)

