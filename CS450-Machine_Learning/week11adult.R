library(ucimlr)
library(mlr)
library(mlrMBO)
library(tidyverse)

adult <- read_ucimlr("adult")

adult <- adult[,-9]
summarizeColumns(adult)

adult <- adult %>% 
  mutate_at(vars(workclass, education, marital_status, occupation, realtionship, native_country, income), as.factor)

task <- makeClassifTask(id = "adult", data = adult, target = "income") %>%
  mergeSmallFactorLevels(min.perc = 0.02)


task.train <- makeClassifTask(id = "adult.train", data = getTaskData(task)[(1:345 * 2), ], target = "income")
task.test <- makeClassifTask(id = "adult.test", data = getTaskData(task)[(1:345 * 2 - 1), ], target = "income")

dt <- makeLearner("classif.rpart", predict.type = "prob") %>%
  makeDummyFeaturesWrapper() 
dt1 <- makeLearner("classif.ksvm", predict.type = "prob") %>%
  makeDummyFeaturesWrapper()
dt2 <- makeLearner("classif.nnet", predict.type = "prob") %>%
  makeDummyFeaturesWrapper() 
dt3 <- makeLearner("classif.randomForest", predict.type = "prob") %>%
  makeDummyFeaturesWrapper() 
dt4 <- makeLearner("classif.gbm", predict.type = "prob") %>%
  makeDummyFeaturesWrapper() 

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