library(tidyverse)
dat <- read_csv("https://byuistats.github.io/M335/data/rcw.csv", 
                col_types = cols(Semester_Date = col_date(format = "%m/%d/%y"), Semester = col_factor(levels = c("Winter", "Spring", "Fall"))))

ggplot(dat, aes(Semester_Date, Count, colour = Department)) +
  geom_line() + geom_point()

