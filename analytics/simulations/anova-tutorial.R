library(ggplot2)

ggplot(chickwts, aes(x = feed, y = weight)) +
  geom_boxplot(fill = "grey80", colour = "blue") +
  scale_x_discrete() + xlab("Treatment Group") +
  ylab("Weight of Chick")

summary(aov(weight ~ feed, data=chickwts))
# significant with anova!