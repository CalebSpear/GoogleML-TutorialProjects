library(tidyverse)
library(nycflights13)
library(forcats)
library(ggbeeswarm)

totalFlights <- flights %>% group_by(carrier) %>% 
  summarise(total = n())

totalFlights %>% ggplot(aes(x = fct_reorder(carrier,desc(total)), y = total)) +
  geom_col() + 
  labs(y = "# of flights",
       x = "Carrier",
       title = "NYC flights in 2013 by Carrier")

ggsave("carrier.png")
#This shows the number of flights per carrier.

flights %>% ggplot(aes(arr_delay)) + 
  geom_histogram() +
  labs(x = "Arrival Delay Time",
       y = "Number of Flights",
       title = "Number of Flights by Arrival Delay Time")

flights %>% ggplot(aes(x = carrier, y = arr_delay)) +
  geom_boxplot()

ggsave("arrivaldelay.png")
#This shows the number of flights per arrical delay time bin.

p <- flights %>%  ggplot(aes(x = carrier, y = arr_delay))
p + geom_violin() +
  coord_cartesian(ylim = c(-50,500)) +
  labs(x = "Carrier",
       y = "Arrival Delay Time",
       title = "Arrival Delay Time Distribution for Carriers")

ggsave("violin_carrier_arrivalDelay.png")

#This graph shows a violin plot comparing arrival delay times for
#each carrier. I had used quasirandom but it is slowing everything 
#too much to do again right now.
p + geom_quasirandom(alpha = 0.6, size = 0.75)
