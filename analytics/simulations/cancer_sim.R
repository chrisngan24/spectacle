cohorts <- 100
years <- 10
orig.pop <- 100
p <- 1/ 1000
cases.per.year <- c()
for (j in 1:cohorts){
  pop <- orig.pop
  cases.per.year[j] <- 0
  for (i in 1:years){
    k <- rbinom(1, pop, p)
    pop <- pop - k
    cases.per.year[j] <- cases.per.year[j] + k
  }
}
