library(ARTool)
library(emmeans)
library(readxl)
library(MASS)

questionResponsesAndAnswers <- read_xlsx("/Users/aluu/git/dual-timeline/post-data/finalFinalData.xlsx", sheet = "SCORES")

questionResponsesAndAnswers <- questionResponsesAndAnswers[questionResponsesAndAnswers$TIMELINE != "Other" & questionResponsesAndAnswers$VALID == "TRUE" & questionResponsesAndAnswers$TIME != 0 & !is.na(questionResponsesAndAnswers$PID), ]

questionResponsesAndAnswers$TIMELINE <- factor(questionResponsesAndAnswers$TIMELINE)
questionResponsesAndAnswers$FREQ <- factor(questionResponsesAndAnswers$FREQ)
questionResponsesAndAnswers$VIDEO <- factor(questionResponsesAndAnswers$VIDEO)
questionResponsesAndAnswers$PID <- factor(questionResponsesAndAnswers$PID)
questionResponsesAndAnswers$NUM_CORRECT_ANSWER <- factor(questionResponsesAndAnswers$NUM_CORRECT_ANSWER)

model2 <- art(SUS ~ TIMELINE * FREQ + (1 | PID), data = questionResponsesAndAnswers)

summary(model2)

anova(model2)

model3 <- art(TIME ~ TIMELINE * FREQ + (1 | PID), data = questionResponsesAndAnswers)

summary(model3)

anova(model3)

# Fit an ordinal logistic regression model
model1 <- polr(NUM_CORRECT_ANSWER ~ TIMELINE + FREQ + VIDEO, data = questionResponsesAndAnswers, Hess = TRUE)

# Print the model summary
summary(model1)

## store table
(ctable <- coef(summary(model1)))

## calculate and store p values
p <- pnorm(abs(ctable[, "t value"]), lower.tail = FALSE) * 2

## combined table
(ctable <- cbind(ctable, "p value" = p))

View(ctable)

