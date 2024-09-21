# SALES AND ORDERS ANALYSIS
# LOADING REQUIRED LIBRARIES
library(readxl)
library(dplyr)
library(tidyverse)
library(kableExtra)
library(mosaic)
library(ggplot2)
library(scales)
library(plotrix)

options(scipen = 999) # Don't display scientific notations
Sys.setenv(LANGUAGE="en") # SET SYSTEM LANGUAGE TO ENGLISH
rm(list = ls()) # CLEARS r environment

# Create a folder (EMASTER) on computer desktop
dir.create("C:/Users/ACAPE CONSULTANT/Desktop/EMASTER")
setwd("C:/Users/ACAPE CONSULTANT/Desktop/EMASTER")# Set EMASTER as working directory

# Copy data to the EMASTER Folder then import to r environment
OSData <- read_xlsx("C:/Users/ACAPE CONSULTANT/Desktop/EMASTER/RawData.xlsx")

# Write back raw data as csv file
write.table(OSData,
            file = "RawData.csv",
            row.names = FALSE,
            sep = ",") # SAVING RAW DATA AS CSV FILE IN EMASTER FOLDER

# Preliminary: Data cleaning
# DATA CLEANING ON STRING VARIABLES (TRIMMING EXTRA SPACES & CHANGE CASE)
OSData %>%
  str_replace_all("\\s+") %>% 
  str_trim(side = "both")

# CONVERTING CATEGORICAL VARIABLES INTO FACTORS.FACTORS ARE STATISTICAL DATA TYPE MENT TO STORE CATEGORICAL VARIBLES AS VECTOR OF INTERGER VALUES WITH A SET OF CHARACTER VALUES
OSData$ENTRY_TYPE = factor(OSData$ENTRY_TYPE)
OSData$SALES_REP = factor(OSData$SALES_REP)
OSData$REP_CATEGORY = factor(OSData$REP_CATEGORY)
OSData$SUPERVISOR = factor(OSData$SUPERVISOR)
OSData$CUSTOMER_NAME = factor(OSData$CUSTOMER_NAME)
OSData$CUSTOMER_CATEGORY = factor(OSData$CUSTOMER_CATEGORY)
OSData$LOCATION_NAME = factor(OSData$LOCATION_NAME)
OSData$ROUTE_NAME = factor(OSData$ROUTE_NAME)
OSData$REGION_NAME = factor(OSData$REGION_NAME)
OSData$PRODUCT_CATEGORY = factor(OSData$PRODUCT_CATEGORY)
OSData$PRODUCT_NAME = factor(OSData$PRODUCT_NAME)
OSData$`STAGE NAME` = factor(OSData$`STAGE NAME`)

# CONVERTING LOWER CASE OBSERVATION STRING VARIABLES INTO UPPER CASE FOR UNIFORMITY
OSData$ENTRY_TYPE = toupper(OSData$ENTRY_TYPE)
OSData$SALES_REP = toupper(OSData$SALES_REP)
OSData$REP_CATEGORY = toupper(OSData$REP_CATEGORY)
OSData$SUPERVISOR = toupper(OSData$SUPERVISOR)
OSData$CUSTOMER_NAME = toupper(OSData$CUSTOMER_NAME)
OSData$CUSTOMER_CATEGORY = toupper(OSData$CUSTOMER_CATEGORY)
OSData$LOCATION_NAME = toupper(OSData$LOCATION_NAME)
OSData$ROUTE_NAME = toupper(OSData$ROUTE_NAME)
OSData$REGION_NAME = toupper(OSData$REGION_NAME)
OSData$PRODUCT_CATEGORY = toupper(OSData$PRODUCT_CATEGORY)
OSData$PRODUCT_NAME = toupper(OSData$PRODUCT_NAME)
OSData$`STAGE NAME` = toupper(OSData$`STAGE NAME`)

# DATA CLEANING ON ENTRY_TYPE
OSData$ENTRY_TYPE = trimws(OSData$ENTRY_TYPE, which = "both",
                           whitespace = "[\t\r\n]")
ENTRY_TYPE <- data.frame(table(OSData$ENTRY_TYPE))
ENTRY_TYPE <- rename(
  ENTRY_TYPE,
  c("ENTRY_TYPE" = "Var1",
    "FREQUENCY" = "Freq"))
ENTRY_TYPE

#OSData$ENTRY_TYPE[OSData$ENTRY_TYPE == "All"] <- "Sale"

# DATA CLEANING ON SALES_REP
OSData$SALES_REP = trimws(OSData$SALES_REP, which = "both",
                          whitespace = "[\t\r\n]")
SALES_REP <- data.frame(table(OSData$SALES_REP))
SALES_REP <- SALES_REP %>% arrange(desc(Freq))
SALES_REP <- rename(
  SALES_REP,
  c("SALES_REP" = "Var1",
    "FREQUENCY" = "Freq"))
SALES_REP

# DATA CLEANING ON REP_CATEGORY
OSData$REP_CATEGORY = trimws(OSData$REP_CATEGORY, which = "both",
                             whitespace = "[\t\r\n]")
REP_CATEGORY <- data.frame(table(OSData$REP_CATEGORY))
REP_CATEGORY <- REP_CATEGORY %>% arrange(desc(Freq))
REP_CATEGORY <- rename(
  REP_CATEGORY,
  c("REP_CATEGORY" = "Var1",
    "FREQUENCY" = "Freq"))
REP_CATEGORY

# DATA CLEANING ON SUPERVISOR
OSData$SUPERVISOR = trimws(OSData$SUPERVISOR, which = "both",
                           whitespace = "[\t\r\n]")
SUPERVISOR <- data.frame(table(OSData$SUPERVISOR))
SUPERVISOR <- SUPERVISOR %>% arrange(desc(Freq))
SUPERVISOR <- rename(
  SUPERVISOR,
  c("SUPERVISOR" = "Var1",
    "FREQUENCY" = "Freq"))
SUPERVISOR

# DATA CLEANING ON CUSTOMER_NAME
OSData$CUSTOMER_NAME = trimws(OSData$CUSTOMER_NAME, which = "both",
                              whitespace = "[\t\r\n]")
CUSTOMER_NAME <- data.frame(table(OSData$CUSTOMER_NAME))
CUSTOMER_NAME <- CUSTOMER_NAME %>% arrange(desc(Freq))
CUSTOMER_NAME <- rename(
  CUSTOMER_NAME,
  c("CUSTOMER_NAME" = "Var1",
    "FREQUENCY" = "Freq"))
CUSTOMER_NAME

# DATA CLEANING ON CUSTOMER_CATEGORY
OSData$CUSTOMER_CATEGORY = trimws(OSData$CUSTOMER_CATEGORY, which = "both",
                                  whitespace = "[\t\r\n]")
CUSTOMER_CATEGORY <- data.frame(table(OSData$CUSTOMER_CATEGORY))
CUSTOMER_CATEGORY <- CUSTOMER_CATEGORY %>% arrange(desc(Freq))
CUSTOMER_CATEGORY <- rename(
  CUSTOMER_CATEGORY,
  c("CUSTOMER_CATEGORY" = "Var1",
    "FREQUENCY" = "Freq"))
CUSTOMER_CATEGORY

# DATA CLEANING ON LOCATION_NAME
OSData$LOCATION_NAME = trimws(OSData$LOCATION_NAME, which = "both",
                              whitespace = "[\t\r\n]")
LOCATION_NAME <- data.frame(table(OSData$LOCATION_NAME))
LOCATION_NAME <- LOCATION_NAME %>% arrange(desc(Freq))
LOCATION_NAME <- rename(
  LOCATION_NAME,
  c("LOCATION_NAME" = "Var1",
    "FREQUENCY" = "Freq"))
LOCATION_NAME

# DATA CLEANING ON ROUTE_NAME
OSData$ROUTE_NAME = trimws(OSData$ROUTE_NAME, which = "both",
                           whitespace = "[\t\r\n]")
ROUTE_NAME <- data.frame(table(OSData$ROUTE_NAME))
ROUTE_NAME <- ROUTE_NAME %>% arrange(desc(Freq))
ROUTE_NAME <- rename(
  ROUTE_NAME,
  c("ROUTE_NAME" = "Var1",
    "FREQUENCY" = "Freq"))
ROUTE_NAME

# DATA CLEANING ON REGION_NAME
OSData$REGION_NAME = trimws(OSData$REGION_NAME, which = "both",
                            whitespace = "[\t\r\n]")
REGION_NAME <- data.frame(table(OSData$REGION_NAME))
REGION_NAME <- REGION_NAME %>% arrange(desc(Freq))
REGION_NAME <- rename(
  REGION_NAME,
  c("REGION_NAME" = "Var1",
    "FREQUENCY" = "Freq"))
REGION_NAME

# DATA CLEANING ON PRODUCT_CATEGORY
OSData$PRODUCT_CATEGORY = trimws(OSData$PRODUCT_CATEGORY, which = "both",
                                 whitespace = "[\t\r\n]")
PRODUCT_CATEGORY <- data.frame(table(OSData$PRODUCT_CATEGORY))
PRODUCT_CATEGORY <- PRODUCT_CATEGORY %>% arrange(desc(Freq))
PRODUCT_CATEGORY <- rename(
  PRODUCT_CATEGORY,
  c("PRODUCT_CATEGORY" = "Var1",
    "FREQUENCY" = "Freq"))
PRODUCT_CATEGORY

# DATA CLEANING ON PRODUCT_NAME
OSData$PRODUCT_NAME = trimws(OSData$PRODUCT_NAME, which = "both",
                             whitespace = "[\t\r\n]")
PRODUCT_NAME <- data.frame(table(OSData$PRODUCT_NAME))
PRODUCT_NAME <- PRODUCT_NAME %>% arrange(desc(Freq))
PRODUCT_NAME <- rename(
  PRODUCT_NAME,
  c("PRODUCT_NAME" = "Var1",
    "FREQUENCY" = "Freq"))
PRODUCT_NAME

# DATA CLEANING ON `STAGE NAME`
OSData$`STAGE NAME` = trimws(OSData$`STAGE NAME`, which = "both",
                             whitespace = "[\t\r\n]")
`STAGE NAME` <- data.frame(table(OSData$`STAGE NAME`))
`STAGE NAME` <- `STAGE NAME` %>% arrange(desc(Freq))
`STAGE NAME` <- rename(
  `STAGE NAME`,
  c("`STAGE NAME`" = "Var1",
    "FREQUENCY" = "Freq"))
`STAGE NAME`

# Subset Data
Orders <- OSData[OSData$ENTRY_TYPE=="ORDER",] # Orders Data
Sales <- OSData[OSData$ENTRY_TYPE=="SALE",] # Sales Data
Others1 <- OSData[OSData$ENTRY_TYPE!="SALE",]
Others <- Others1[Others1$ENTRY_TYPE!="ORDER",] # Data which are neither Orders nor Sales

# 1. SALES AND ORDERS TALLY
OStally <- data.frame(table(OSData$ENTRY_TYPE))
OStally # View categorical data tally under OSData

OStally <-
  OStally[-1,] # DROPPING ALL IN THE DATA FRAME

OS_PERCENT <- round((OStally$Freq)/sum(OStally$Freq)*100, 2)

OS <- data.frame(cbind(OStally, OS_PERCENT))
OS <- OS[,-1]
TOTALS <- as.numeric(colSums(OS))

OS <- data.frame(rbind(OS, TOTALS))
OS$Var1 <- c("ORDERS", "SALES", "TOTALS")

OS <- rename(
  OS,
  c("ENTRY.TYPE" = "Var1",
    "FREQUENCY" = "Freq",
    "PERCENT" = "OS_PERCENT")
)

OS <- OS[, c("ENTRY.TYPE", "FREQUENCY", "PERCENT")] # REORDERING COLUMNS
write.table(OS, file="OrderSales.csv", row.names=FALSE, sep=",")

OStally$Var1 <- as.factor(OStally$Var1)
lbls <- as.character(OStally$Var1)
lbls <- paste(lbls, OS_PERCENT)
lbls <- paste(lbls, "%", sep = "") # ADDING PERCENTAGES TO LABELS

pie3D(
  OS_PERCENT,
  labels = lbls,
  col = c("red", "aquamarine"),
  main = "PERENTAGE VALUES OF ORDERS AND SALES",
  explode = 0
)

# PIE CHART ON PERENTAGE VALUES OF ORDERS AND SALES
png(filename = "PERENTAGEVALUESOFORDERSANDSALESPieChart.jpg",
    width = 400,
    height = 400)

#SALES AND ORDERS ANALYSIS
#Table 1: Summary of Sales and Orders Data

OStally <- data.frame(table(OSData$ENTRY_TYPE))

OStally <-
  OStally[-1,]

OS_PERCENT <- round((OStally$Freq)/sum(OStally$Freq)*100, 2)

OS <- data.frame(cbind(OStally, OS_PERCENT))
OS <- OS[,-1]
TOTALS <- as.numeric(colSums(OS))

OS <- data.frame(rbind(OS, TOTALS))
OS$Var1 <- c("ORDERS", "SALES", "TOTALS")

OS <- rename(
  OS,
  c("ENTRY.TYPE" = "Var1",
    "FREQUENCY" = "Freq",
    "PERCENT" = "OS_PERCENT")
)

OS <- OS[, c("ENTRY.TYPE", "FREQUENCY", "PERCENT")]
OS

write.table(OS, file="OrderSales.csv", row.names=FALSE, sep=",")

# Figure 1: Pie Chart Showing Summary of Sales and Orders Data
OStally$Var1 <- as.factor(OStally$Var1)
lbls <- as.character(OStally$Var1)
lbls <- paste(lbls, OS_PERCENT)
lbls <- paste(lbls, "%", sep = "")

png(filename = "PERENTAGEVALUESOFORDERSANDSALESPieChart.jpg",
    width = 400,
    height = 400)

pie3D(
  OS_PERCENT,
  labels = lbls,
  col = c("red", "aquamarine"),
  main = "PERENTAGE VALUES OF ORDERS AND SALES",
  explode = 0
)

# Table 2: Summary of Value Sold Per Sales Rep
Sales <- OSData[OSData$ENTRY_TYPE=="SALE",]

SALESREP_VALUE <- Sales %>% 
  group_by(SALES_REP) %>% 
  summarise(TRANSACTIONS_COUNT=n(),
            SUM_SOLDVALUE=sum(VALUE_SOLD, na.rm=TRUE))
SALESREP_VALUE <- data.frame(SALESREP_VALUE)
SALESREP_VALUE <- SALESREP_VALUE %>% arrange(desc(SUM_SOLDVALUE))
SALESREP_VALUESOLD <- as.array(SALESREP_VALUE$SUM_SOLDVALUE)

SALESREP_VALUE$PERCENT <- round((SALESREP_VALUESOLD/sum(SALESREP_VALUE$SUM_SOLDVALUE))*100,1)
TOTALS <- c("TOTALS", sum(SALESREP_VALUE$TRANSACTIONS_COUNT),
            sum(SALESREP_VALUE$SUM_SOLDVALUE), round(sum(SALESREP_VALUE$PERCENT),0))

SALESREP_VALUE <- data.frame(rbind(SALESREP_VALUE, TOTALS))
SALESREP_VALUE

write.table(SALESREP_VALUE, file="SalesRepValueSold.csv", row.names=FALSE, sep=",")

# Figure 2: Bar Chart Summary of Climate Data
SR <- SALESREP_VALUE[SALESREP_VALUE$SALES_REP!="TOTALS",]
SR <- SR %>% arrange(desc(SUM_SOLDVALUE))
SR <- SR[1:20,] # The bar chart only capture the top 20 leading sale reps per value sold
SR <- SR %>% arrange(desc(SUM_SOLDVALUE))
SR_SOLD <- as.numeric(SR$SUM_SOLDVALUE)
SR_NAMES <- as.character(SR$SALES_REP)

png(filename = "VALUESOLDPERSALESREPBarChart.jpg",
    width = 400,
    height = 400)

ggplot(data = SR,
       mapping = aes(x = reorder(SR_NAMES,SR_SOLD),
                     y = SR_SOLD)) +
  geom_bar(stat = "identity", fill = "blue", col = "red") +
  labs(
    title = "VALUE SOLD PER SALES REP",
    x = "Sales Rep",
    y = "Value sold in KES",
    caption = "KETEPA",
    x = SR_NAMES,
    y = SR_SOLD
  ) +
  theme_bw() +
   geom_text(stat = "identity", aes(label = SR_SOLD), hjust = 0.05) +
  theme(plot.title = element_text(
    hjust = 0.5,
    face = "bold",
    colour = "cadetblue"
  ))+
  ylim(0, max(SR_SOLD) * 1.2) +
  coord_flip()
