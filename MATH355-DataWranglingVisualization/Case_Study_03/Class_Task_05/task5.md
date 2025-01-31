---
title: "Task 5"
author: "Caleb Spear"
date: "May 04, 2020"
output:
  html_document:  
    keep_md: true
    toc: true
    toc_float: true
    code_folding: hide
    fig_height: 6
    fig_width: 12
    fig_align: 'center'
---






```r
# Use this R-Chunk to import all your datasets!
dataset <- read.csv("covid.csv")
dataset2 <- child_mortality
```

## Plots

Plot 1 is a plot of testing done by country yesterday. Plot 2 is a plot of child mortality vs poverty.

## Data Wrangling


```r
# Use this R-Chunk to clean & wrangle your data!
datatoday <- filter(dataset, Date == "May 3, 2020")
datadesc <- arrange(datatoday, desc(Total.tests.per.thousand))
datafinal <- head(datadesc, n = 21)
datafinal <- datafinal[-c(18),]
datasetf <- filter(dataset2, year > 2000)
dataave2 <- datasetf %>% group_by(continent,country) %>% summarize(aveChildmort = mean(child_mort, na.rm = TRUE), avepoverty = mean(poverty, na.rm = TRUE), pop = mean(population, na.rm = TRUE) / 100000)
datagood <- na.omit(dataave2)
biggest <- datagood %>% group_by(continent) %>% filter(row_number(desc(pop)) == 1)
```

## Data Visualization


```r
# Use this R-Chunk to plot & visualize your data!
ggplot(datafinal, aes(x = Total.tests.per.thousand, y = reorder(Entity, Total.tests.per.thousand), fill = Entity)) + geom_col() + labs(title = "Total COVID-19 tests per 1,000 people", subtitle = "The most recent figures for selection of countries is shown.", caption = "Source:https://ourworldindata.org/what-can-data-on-testing-tell-us-about-the-pandemic", x = "", y = "") + theme(legend.position = "none", panel.background = element_rect(fill = "white"), panel.border = element_blank(), panel.grid.major = element_line(linetype = "dashed", colour = "grey80"), panel.grid.major.y = element_blank(), panel.grid.minor.y = element_blank()) + geom_text(aes(label = Total.tests.per.thousand), hjust = -0.24) + scale_x_continuous(limits = c(0, 175),expand = c(0,0))
```

![](task5_files/figure-html/plot_data-1.png)<!-- -->

```r
ggplot(datagood, aes(x = avepoverty, y = aveChildmort)) + geom_point(aes(color = continent,size = pop)) + scale_x_sqrt() + geom_text_repel(aes(label = country), data = biggest) + labs(title = "Child Mortality Rate vs Poverty Rate", subtitle = "Average Child Mortality Rate per Year by Country since 2000 vs Avergave Poverty Rate",y = "Average Child Mortality Rate", x = "Average Mortality Rate")
```

![](task5_files/figure-html/plot_data-2.png)<!-- -->

