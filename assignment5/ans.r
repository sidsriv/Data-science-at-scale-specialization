data = read.csv('seaflow_21min.csv',header = TRUE)


#Ans-1
sum(data$pop == 'synecho')

#Ans-2
summary(data$fsc_small)

#Ans-3
smp_size = floor(0.5*nrow(data))
set.seed(123)
train_ind <- sample(seq_len(nrow(data)), size = smp_size)
train <- data[train_ind,]
test <- data[-train_ind,]
mean(train$time)

#Ans-4
library(ggplot2)
qplot(pe,chl_small,data = data,color = pop)

#Ans-5
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=train)
print(model)

#Ans-6
print(model)

#Ans-7
print(model)

#Ans-8
predicate <- predict(model,test,type = 'class')
sum(predicate == test$pop)/nrow(test)

#Ans-9
library(randomForest)
modelrf <- randomForest(fol, data = train)
predicate <- predict(modelrf,test,type = 'class')
sum(predicate == test$pop)/nrow(test)

#Ans-10
importance(modelrf)

#Ans-11
library(e1071)
modelsvm <- svm(fol,data = train)
predicate <- predict(modelsvm,test,type = 'class')
sum(predicate == test$pop)/nrow(test)

#Ans-12
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=train)
predicate_dt <- predict(model,test,type = 'class')
table(pred = predicate_dt, true = test$pop)

library(randomForest)
modelrf <- randomForest(fol, data = train)
predicate_rf <- predict(modelrf,test,type = 'class')
table(pred = predicate_rf, true = test$pop)

library(e1071)
modelsvm <- svm(fol,data = train)
predicate_svm <- predict(modelsvm,test,type = 'class')
table(pred = predicate_svm, true = test$pop)