popdata <- read.csv('popestscsv.csv', nrows=1, skip=39, header = F, sep = ',', dec=',', stringsAsFactors = F) # THIS IMPORTS THE LINE FROM THE CSV WITH THE NJ DATA #
yeardata <- read.csv('popestscsv.csv', nrows=1, skip=3, header = F, sep = ',', dec=',', stringsAsFactors = F) # IMPORTS THE LINE FROM THE CSV WITH THE YEAR DATA #


NJpop <- popdata[4:11] #CAPTURES THE NECESSARY COLUMNS FOR THE REGRESSION MODEL#
year <- yeardata[4:11]

NJdf <- data.frame(year=unlist(year),NJpop=unlist(NJpop)) #CREATES A DATA FRAME OF THE POPULATION AND YEAR DATA, UNLIST MAKES THEM NUMERIC INSTEAD OF LISTS#

popmodel <- lm(NJpop ~ year, data = NJdf) #CREATES A LINEAR REGRESSION MODEL FOR PREDICTING THE POPULATION #
popmodel
summary(popmodel) # SUMMARIZES POPULATION MODEL #

pred2020 <- predict.lm(popmodel, data.frame("year" = 2020)) # PREDICTS POPULATION FOR 2020 #
pred2023 <- predict.lm(popmodel, data.frame("year" = 2023)) # PREDICTS POPULATION FOR 2023 #
pred2020
pred2023
