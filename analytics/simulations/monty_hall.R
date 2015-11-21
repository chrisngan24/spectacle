n <- 500
i <- 1

y_switch <- c()
n_switch <- c()
while (i < n + 1){
  doors <- c(0,0,0)
  # Assign the prize to one of the doors at random
  doors[floor(runif(1, min=1,max=4))] <- 1
  
  
  # assume that the revelaed door is 2 or 3 that does not have the prize
  if (doors[1] == 1) y_switch[i] <- 0 else y_switch[i] <- 1
  n_switch[i] <- doors[1]
  i <- i + 1
  #}
}
