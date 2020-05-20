library(ucimlr)
library(mlr)
library(mlrMBO)
library(tidyverse)

australian <- read_ucimlr("australian")

australian <- australian %>% 
  mutate_at(vars(A1, A4, A5, A6, A8, A9, A10, A11, A12, A15), as.factor)

task <- makeClassifTask(id = "australian", data = australian, target = "A15") %>%
  mergeSmallFactorLevels(min.perc = 0.02) %>%
  subsetTask(features = names(australian)[which(names(australian) != "A4")])

task.train <- makeClassifTask(id = "australian.train", data = getTaskData(task)[(1:345 * 2), ], target = "A15")
task.test <- makeClassifTask(id = "australian.test", data = getTaskData(task)[(1:345 * 2 - 1), ], target = "A15")


dt <- makeLearner("classif.rpart", predict.type = "prob")
dt1 <- makeLearner("classif.ksvm", predict.type = "prob")
dt2 <- makeLearner("classif.nnet", predict.type = "prob")
dt3 <- makeLearner("classif.randomForest", predict.type = "prob")
dt4 <- makeLearner("classif.gbm", predict.type = "prob")

resample(dt, task.train, cv10, auc)
resample(dt1, task.train, cv10, auc)
resample(dt2, task.train, cv10, auc)
resample(dt3, task.train, cv10, auc)
resample(dt4, task.train, cv10, auc)

```{r tune_learner}
getParamSet(dt)

dt.parset <- makeParamSet(
  makeIntegerParam("minsplit", lower = 1, upper = 100),
  makeNumericParam("cp", lower = 0, upper = 1),
  makeIntegerParam("maxdepth", lower = 10, upper = 50)
)

dt.tuned <- dt %>%
  makeTuneWrapper(resampling = cv5, 
                  measures = auc, 
                  par.set = dt.parset,
                  control = makeTuneControlGrid(resolution = 5))

# parallelStartSocket(cpus = 16L, level = 'mlr.resample')

rr <- resample(dt.tuned, task, cv5, auc)
rr1 <- resample(dt1, task, cv5, auc)
rr2 <- resample(dt2, task, cv5, auc)
rr3 <- resample(dt3, task, cv5, auc)
rr4 <- resample(dt4, task, cv5, auc)
# parallelStop()

print(rr)
print(rr1)
print(rr2)
print(rr3)
print(rr4)
```

```{r train_model}
# parallelStartSocket(cpus = 16L, level = 'mlr.resample')

model <- train(dt.tuned, task.train)
model1 <- train(dt1, task.train)
model2 <- train(dt2, task.train)
model3 <- train(dt3, task.train)
model4 <- train(dt4, task.train)
# parallelStop()

preds <- predict(model, newdata = getTaskData(task.test))
preds1 <- predict(model1, newdata = getTaskData(task.test))
preds2 <- predict(model2, newdata = getTaskData(task.test))
preds3 <- predict(model3, newdata = getTaskData(task.test))
preds4 <- predict(model4, newdata = getTaskData(task.test))

performance(preds, auc)
performance(preds1, auc)
performance(preds2, auc)
performance(preds3, auc)
performance(preds4, auc)
```