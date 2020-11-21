library(mlbench)
library(arules)
library(dplyr)
library(stringr)
library(magrittr)
library(arulesViz)


######## Data Load  ########
setwd('/Users/indy/Documents/MSDS/git/DS7331_termProject/work\ in\ progress\ copies')
data = read.csv('selectionDF.csv', header = TRUE)
head(data)


data$age_group <- cut(data$age, breaks=c(0,18,65,999), labels=c("<18","18-64","65+"))

data$age_group = as.factor(data$age)
data$det_ind_code = as.factor(data$det_ind_code)
data$det_occ_code = as.factor(data$det_occ_code)
data$major_occ_code = as.factor(data$major_occ_code)
data$sex = as.factor(data$sex)
data$education = as.factor(data$education)
data$marital_stat = as.factor(data$marital_stat)
data$race = as.factor(data$race)
data$tax_filer_stat = as.factor(data$tax_filer_stat)
data$citizenship = as.factor(data$citizenship)
data$graduated = as.factor(data$graduated)
data$income_50k = as.factor(data$income_50k)

income_data = data %>% select(
  age_group, det_ind_code, det_occ_code, major_occ_code, sex, education,
  marital_stat, race, tax_filer_stat, citizenship, income_50k
  )
grad_data = data %>% select(
  age_group, det_ind_code, det_occ_code, major_occ_code, sex,
  marital_stat, race, tax_filer_stat, citizenship, graduated,income_50k
)


######## ARules ########

#isets = apriori(selection, parameter = list(target ="frequent", support = 0.5))

rules_grad = apriori(grad_data, parameter = list(support = 0.03, confidence = 0.65), appearance = list(default="lhs",rhs="graduated=yes"))
inspect(head(rules, n = 10))
quality(head(rules)) #print the quality of the measures

is_max_grad = rules_grad[is.maximal(rules_grad)]
inspect(head(sort(is_max_grad, by = "support")))
length(is_max_grad)


rules_income = apriori(
  income_data, 
  parameter = list(support = 0.01, confidence = 0.4), appearance = list(default="lhs",rhs="income_50k= 50000+.")
  )
inspect(head(rules_income, n = 10))
quality(head(rules_income)) #print the quality of the measures


is_max = rules_income[is.maximal(rules_income)]
inspect(head(sort(is_max, by = "support")))
length(is_max)


######  Vizualization  #####
plot(rules_grad)

# a great plot
plot(rules_grad, method="grouped")

