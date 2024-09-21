from IPython.display import Image
Image("C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/AcapeLogo.jpg")

# AXLE LOAD MONITORING DATA ANALYSIS FOR ROADS
# DESIGNED BY: DIR. NGETICH,
# ACAPE IMPACT CONSULTANT LIMITED

# Web : http://m.facebook.com/acapeimpact ¦E-Mail:acapeimpact@gmail.com
#  (Up and Running with Python)
# DATA IMPORTATION PROCESSES:- (Use Rstudio and make sure your data imported)
#IMPORT REQUIRED MODULES/LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # For data visualization

#NAMING THE WEIGHBRIDGE
WeighbridgeName = pd.read_csv('WeighbridgeName.csv')
WeighbridgeName

Q3 = pd.ExcelFile('Q3.xlsx')

Q3 = Q3.parse(0)

#REMOVING SPECIAL CHARATERS IN DATAFRAME
for Configuration in Q3.columns:
    Q3['Configuration'] = Q3['Configuration'].str.replace(r'\W', " ")
   
for Origin in Q3.columns:
    Q3['Origin'] = Q3['Origin'].str.replace(r'\W', " ")

for Destination in Q3.columns:
    Q3['Destination'] = Q3['Destination'].str.replace(r'\W', " ")

for Transporter in Q3.columns:
    Q3['Transporter'] = Q3['Transporter'].str.replace(r'\W', " ")
    
Q3['PlateNo'].fillna(0, inplace=True)
Q3['Configuration'].fillna(0, inplace=True)
Q3['Origin'].fillna(0, inplace=True)
Q3['Destination'].fillna(0, inplace=True)
Q3['Transporter'].fillna(0, inplace=True)

Q3.head()

# DATA CLEANING PROCESSES:-

DATADEL1 = Q3[Q3.GA1 <=0] # Omitted data for GA1<=0
DATADEL2 = Q3[Q3.GA2 <=0] # Omitted data for GA2<=0
DATADEL3 = Q3[Q3.PlateNo ==0] # Omitted data missing vehicle plate number

DATADEL = pd.concat([DATADEL1, DATADEL2, DATADEL3], axis=1) # DATASET OF DISCARDED/ OMITTED/ DELETED DATA

DATADEL = pd.DataFrame(DATADEL) # ENSURING STRUCTURE IS DATASET

DATADEL

DATADEL.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/OMITTED DATA.xlsx')

# FINE TUNING AND DATA CLEANING

# CONVERTING CASE
Q3.PlateNo = Q3['PlateNo'].str.upper()
Q3.Configuration = Q3['Configuration'].str.upper()
Q3.Origin = Q3['Origin'].str.upper()
Q3.Destination = Q3['Destination'].str.upper()
Q3.Transporter = Q3['Transporter'].str.upper()

# DATA CLEANING ON AXLE CONFIGURATION
Q3.Configuration.replace("2a","2A", inplace=True)
Q3.Configuration.replace("3a","3A", inplace=True)
Q3.Configuration.replace("3*SDW","3A", inplace=True)
Q3.Configuration.replace("3d","3D", inplace=True)
Q3.Configuration.replace("3d","3D", inplace=True)
Q3.Configuration.replace("4a","4A", inplace=True)
Q3.Configuration.replace("4D","4A", inplace=True)
Q3.Configuration.replace("5c","5C", inplace=True)
Q3.Configuration.replace("5d","5D", inplace=True)
Q3.Configuration.replace("5A","5D", inplace=True)
Q3.Configuration.replace("5*SDWWW","5C", inplace=True)
Q3.Configuration.replace("6g","6G", inplace=True)
Q3.Configuration.replace("6*SSDWWW","6G", inplace=True)
Q3.Configuration.replace("6*SSDDDD","6G", inplace=True)
Q3.Configuration.replace("6*SSDDDD","6G", inplace=True)
Q3.Configuration.replace("6*SDSDDD","6G", inplace=True)
Q3.Configuration.replace("6c","6C", inplace=True)
Q3.Configuration.replace("6*SWDDDD","6C", inplace=True)
Q3.Configuration.replace("6*SDDWWW","6C", inplace=True)
Q3.Configuration.replace("6*SWDWWW","6C", inplace=True)
Q3.Configuration.replace("7a","7A", inplace=True)
Q3.Configuration.replace("7A*","7A", inplace=True)
Q3.Configuration.replace("7c*","7A", inplace=True)
Q3.Configuration.replace("7C*","7A", inplace=True)
Q3.Configuration.replace("X7c*","7A", inplace=True)
Q3.Configuration.replace("X7C*","7A", inplace=True)

# DATA CLEANING ON ORIGIN
Q3.Origin.replace("nairobi", "NAIROBI", inplace=True)
Q3.Origin.replace("Nairobi", "NAIROBI", inplace=True)
Q3.Origin.replace("WESTPOKOT", "WEST POKOT", inplace=True)
Q3.Origin.replace("nai", "NAIROBI", inplace=True)
Q3.Origin.replace("Nai", "NAIROBI", inplace=True)
Q3.Origin.replace("nrb", "NAIROBI", inplace=True)
Q3.Origin.replace("Nrb", "NAIROBI", inplace=True)
Q3.Origin.replace("NRB", "NAIROBI", inplace=True)
Q3.Origin.replace("Nrbi", "NAIROBI", inplace=True)
Q3.Origin.replace("naks", "NAKURU", inplace=True)
Q3.Origin.replace("Naks", "NAKURU", inplace=True)
Q3.Origin.replace("nks", "NAKURU", inplace=True)
Q3.Origin.replace("Nks", "NAKURU", inplace=True)
Q3.Origin.replace("NKS", "NAKURU", inplace=True)
Q3.Origin.replace("Mombasa", "MOMBASA", inplace=True)
Q3.Origin.replace("mombasa", "MOMBASA", inplace=True)
Q3.Origin.replace("msa", "MOMBASA", inplace=True)
Q3.Origin.replace("Msa", "MOMBASA", inplace=True)
Q3.Origin.replace("MSA", "MOMBASA", inplace=True)
Q3.Origin.replace("KSM", "KISUMU", inplace=True)
Q3.Origin.replace("ksm", "KISUMU", inplace=True)
Q3.Origin.replace("Ksm", "KISUMU", inplace=True)
Q3.Origin.replace("eld", "ELDORET", inplace=True)
Q3.Origin.replace("ELD", "ELDORET", inplace=True)
Q3.Origin.replace("Eld", "ELDORET", inplace=True)
Q3.Origin.replace("eldy", "ELDORET", inplace=True)
Q3.Origin.replace("ELDy", "ELDORET", inplace=True)
Q3.Origin.replace("Eldy", "ELDORET", inplace=True)
Q3.Origin.replace("kco", "KERICHO", inplace=True)
Q3.Origin.replace("Kco", "KERICHO", inplace=True)
Q3.Origin.replace("KCO", "KERICHO", inplace=True)
Q3.Origin.replace("BSA", "BUSIA", inplace=True)
Q3.Origin.replace("Bsa", "BUSIA", inplace=True)
Q3.Origin.replace("bsa", "BUSIA", inplace=True)
Q3.Origin.replace("KK", "KAKAMEGA", inplace=True)
Q3.Origin.replace("kk", "KAKAMEGA", inplace=True)
Q3.Origin.replace("Kk", "KAKAMEGA", inplace=True)
Q3.Origin.replace("Athi", "ATHI RIVER", inplace=True)
Q3.Origin.replace("ATHI", "ATHI RIVER", inplace=True)
Q3.Origin.replace("athi", "ATHI RIVER", inplace=True)
Q3.Origin.replace("A.River", "ATHI RIVER", inplace=True)
Q3.Origin.replace("A.RIVER", "ATHI RIVER", inplace=True)
Q3.Origin.replace("A/River", "ATHI RIVER", inplace=True)
Q3.Origin.replace("A/RIVER", "ATHI RIVER", inplace=True)
Q3.Origin.replace("A.River", "ATHI RIVER", inplace=True)
Q3.Origin.replace("Mlolongo", "ATHI RIVER", inplace=True)
Q3.Origin.replace("mlolongo", "ATHI RIVER", inplace=True)
Q3.Origin.replace("ug", "UGANDA", inplace=True)
Q3.Origin.replace("Ug", "UGANDA", inplace=True)
Q3.Origin.replace("UG", "UGANDA", inplace=True)
Q3.Origin.replace("Kampala", "UGANDA", inplace=True)
Q3.Origin.replace("kampala", "UGANDA", inplace=True)
Q3.Origin.replace("KAMPALA", "UGANDA", inplace=True)
Q3.Origin.replace("JINJA", "UGANDA", inplace=True)
Q3.Origin.replace("Jinja", "UGANDA", inplace=True)
Q3.Origin.replace("Jinja", "UGANDA", inplace=True)
Q3.Origin.replace("TORORO", "UGANDA", inplace=True)
Q3.Origin.replace("Tororo", "UGANDA", inplace=True)
Q3.Origin.replace("tororo", "UGANDA", inplace=True)
Q3.Origin.replace("MWANZA", "TANZANIA", inplace=True)
Q3.Origin.replace("mwanza", "TANZANIA", inplace=True)
Q3.Origin.replace("Mwanza", "TANZANIA", inplace=True)
Q3.Origin.replace("DODOMA", "TANZANIA", inplace=True)
Q3.Origin.replace("Dodoma", "TANZANIA", inplace=True)
Q3.Origin.replace("dodoma", "TANZANIA", inplace=True)
Q3.Origin.replace("DARSALAM", "TANZANIA", inplace=True)
Q3.Origin.replace("darsalam", "TANZANIA", inplace=True)
Q3.Origin.replace("Darsalam", "TANZANIA", inplace=True)
Q3.Origin.replace("DAR SALAM", "TANZANIA", inplace=True)
Q3.Origin.replace("dar salam", "TANZANIA", inplace=True)
Q3.Origin.replace("Dar salam", "TANZANIA", inplace=True)
Q3.Origin.replace("DAR SALAM", "TANZANIA", inplace=True)
Q3.Origin.replace("dar Salam", "TANZANIA", inplace=True)
Q3.Origin.replace("ARUSHA salam", "TANZANIA", inplace=True)
Q3.Origin.replace("arusha", "TANZANIA", inplace=True)
Q3.Origin.replace("Arusha", "TANZANIA", inplace=True)
Q3.Origin.replace("TZ", "TANZANIA", inplace=True)
Q3.Origin.replace("tz", "TANZANIA", inplace=True)
Q3.Origin.replace("Tz", "TANZANIA", inplace=True)
Q3.Origin.replace("JUBA", "SUDAN", inplace=True)
Q3.Origin.replace("Juba", "SUDAN", inplace=True)
Q3.Origin.replace("juba", "SUDAN", inplace=True)
Q3.Origin.replace("Sudan", "SUDAN", inplace=True)
Q3.Origin.replace("sudan", "SUDAN", inplace=True)
Q3.Origin.replace("KIGALI", "RWANDA", inplace=True)
Q3.Origin.replace("kigali", "RWANDA", inplace=True)
Q3.Origin.replace("Kigali", "RWANDA", inplace=True)
Q3.Origin.replace("RWA", "RWANDA", inplace=True)
Q3.Origin.replace("rwa", "RWANDA", inplace=True)
Q3.Origin.replace("Rwa", "RWANDA", inplace=True)
Q3.Origin.replace("Congo", "CONGO", inplace=True)
Q3.Origin.replace("congo", "CONGO", inplace=True)
Q3.Origin.replace("BRD", "BURUNDI", inplace=True)
Q3.Origin.replace("brd", "BURUNDI", inplace=True)
Q3.Origin.replace("Brd", "BURUNDI", inplace=True)
Q3.Origin.replace("Burundi", "BURUNDI", inplace=True)
Q3.Origin.replace("burundi", "BURUNDI", inplace=True)
Q3.Origin.replace("SOI", "SOY", inplace=True)
Q3.Origin.replace("soi", "SOY", inplace=True)
Q3.Origin.replace("Soi", "SOY", inplace=True)
Q3.Origin.replace("SUMEKA", "SUNEKA", inplace=True)
Q3.Origin.replace("Suneka", "SUNEKA", inplace=True)
Q3.Origin.replace("Sunek", "SUNEKA", inplace=True)
Q3.Origin.replace("AIRPORT", "AIR PORT", inplace=True)
Q3.Origin.replace("Airport", "AIR PORT", inplace=True)
Q3.Origin.replace("airport", "AIR PORT", inplace=True)
Q3.Origin.replace("M/MAHIU", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("MAIMAHIU", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("M MAHIU", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("MAI MAHIU", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("m/Mahiu", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("M/Mahiu", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("M/mahiu", "MAAI MAHIU", inplace=True)
Q3.Origin.replace("MLBA", "MALABA", inplace=True)
Q3.Origin.replace("NRBI", "NAIROBI", inplace=True)
Q3.Origin.replace("BGMA", "BUNGOMA", inplace=True)
Q3.Origin.replace("BNGMA", "BUNGOMA", inplace=True)
Q3.Origin.replace("NKURU", "NAKURU", inplace=True)
Q3.Origin.replace("MBSA", "MOMBASA", inplace=True)
Q3.Origin.replace("MONBSA", "MOMBASA", inplace=True)
Q3.Origin.replace("MOMBASAS", "MOMBASA", inplace=True)
Q3.Origin.replace("MO,MBASA", "MOMBASA", inplace=True)
Q3.Origin.replace("MOAMBASA", "MOMBASA", inplace=True)
Q3.Origin.replace("MBSA", "MOMBASA", inplace=True)
Q3.Origin.replace("KMPLA", "UGANDA", inplace=True)
Q3.Origin.replace("KPLM", "UGANDA", inplace=True)
Q3.Origin.replace("KAPALA", "UGANDA", inplace=True)
Q3.Origin.replace("KAMPAL;A", "UGANDA", inplace=True)
Q3.Origin.replace("TORORO'", "UGANDA", inplace=True)
Q3['Origin'].fillna(0, inplace=True)
Q3.Origin.replace(0, "UNSPECIFIED", inplace=True)

# DATA CLEANING ON Destination
Q3.Destination.replace("nairobi", "NAIROBI", inplace=True)
Q3.Destination.replace("Nairobi", "NAIROBI", inplace=True)
Q3.Destination.replace("WESTPOKOT", "WEST POKOT", inplace=True)
Q3.Destination.replace("nai", "NAIROBI", inplace=True)
Q3.Destination.replace("Nai", "NAIROBI", inplace=True)
Q3.Destination.replace("nrb", "NAIROBI", inplace=True)
Q3.Destination.replace("Nrb", "NAIROBI", inplace=True)
Q3.Destination.replace("NRB", "NAIROBI", inplace=True)
Q3.Destination.replace("Nrbi", "NAIROBI", inplace=True)
Q3.Destination.replace("naks", "NAKURU", inplace=True)
Q3.Destination.replace("Naks", "NAKURU", inplace=True)
Q3.Destination.replace("nks", "NAKURU", inplace=True)
Q3.Destination.replace("Nks", "NAKURU", inplace=True)
Q3.Destination.replace("NKS", "NAKURU", inplace=True)
Q3.Destination.replace("Mombasa", "MOMBASA", inplace=True)
Q3.Destination.replace("mombasa", "MOMBASA", inplace=True)
Q3.Destination.replace("msa", "MOMBASA", inplace=True)
Q3.Destination.replace("Msa", "MOMBASA", inplace=True)
Q3.Destination.replace("MSA", "MOMBASA", inplace=True)
Q3.Destination.replace("KSM", "KISUMU", inplace=True)
Q3.Destination.replace("ksm", "KISUMU", inplace=True)
Q3.Destination.replace("Ksm", "KISUMU", inplace=True)
Q3.Destination.replace("eld", "ELDORET", inplace=True)
Q3.Destination.replace("ELD", "ELDORET", inplace=True)
Q3.Destination.replace("Eld", "ELDORET", inplace=True)
Q3.Destination.replace("eldy", "ELDORET", inplace=True)
Q3.Destination.replace("ELDy", "ELDORET", inplace=True)
Q3.Destination.replace("Eldy", "ELDORET", inplace=True)
Q3.Destination.replace("kco", "KERICHO", inplace=True)
Q3.Destination.replace("Kco", "KERICHO", inplace=True)
Q3.Destination.replace("KCO", "KERICHO", inplace=True)
Q3.Destination.replace("BSA", "BUSIA", inplace=True)
Q3.Destination.replace("Bsa", "BUSIA", inplace=True)
Q3.Destination.replace("bsa", "BUSIA", inplace=True)
Q3.Destination.replace("KK", "KAKAMEGA", inplace=True)
Q3.Destination.replace("kk", "KAKAMEGA", inplace=True)
Q3.Destination.replace("Kk", "KAKAMEGA", inplace=True)
Q3.Destination.replace("Athi", "ATHI RIVER", inplace=True)
Q3.Destination.replace("ATHI", "ATHI RIVER", inplace=True)
Q3.Destination.replace("athi", "ATHI RIVER", inplace=True)
Q3.Destination.replace("A.River", "ATHI RIVER", inplace=True)
Q3.Destination.replace("A.RIVER", "ATHI RIVER", inplace=True)
Q3.Destination.replace("A/River", "ATHI RIVER", inplace=True)
Q3.Destination.replace("A/RIVER", "ATHI RIVER", inplace=True)
Q3.Destination.replace("A.River", "ATHI RIVER", inplace=True)
Q3.Destination.replace("Mlolongo", "ATHI RIVER", inplace=True)
Q3.Destination.replace("mlolongo", "ATHI RIVER", inplace=True)
Q3.Destination.replace("ug", "UGANDA", inplace=True)
Q3.Destination.replace("Ug", "UGANDA", inplace=True)
Q3.Destination.replace("UG", "UGANDA", inplace=True)
Q3.Destination.replace("Kampala", "UGANDA", inplace=True)
Q3.Destination.replace("kampala", "UGANDA", inplace=True)
Q3.Destination.replace("KAMPALA", "UGANDA", inplace=True)
Q3.Destination.replace("JINJA", "UGANDA", inplace=True)
Q3.Destination.replace("Jinja", "UGANDA", inplace=True)
Q3.Destination.replace("Jinja", "UGANDA", inplace=True)
Q3.Destination.replace("TORORO", "UGANDA", inplace=True)
Q3.Destination.replace("Tororo", "UGANDA", inplace=True)
Q3.Destination.replace("tororo", "UGANDA", inplace=True)
Q3.Destination.replace("MWANZA", "TANZANIA", inplace=True)
Q3.Destination.replace("mwanza", "TANZANIA", inplace=True)
Q3.Destination.replace("Mwanza", "TANZANIA", inplace=True)
Q3.Destination.replace("DODOMA", "TANZANIA", inplace=True)
Q3.Destination.replace("Dodoma", "TANZANIA", inplace=True)
Q3.Destination.replace("dodoma", "TANZANIA", inplace=True)
Q3.Destination.replace("DARSALAM", "TANZANIA", inplace=True)
Q3.Destination.replace("darsalam", "TANZANIA", inplace=True)
Q3.Destination.replace("Darsalam", "TANZANIA", inplace=True)
Q3.Destination.replace("DAR SALAM", "TANZANIA", inplace=True)
Q3.Destination.replace("dar salam", "TANZANIA", inplace=True)
Q3.Destination.replace("Dar salam", "TANZANIA", inplace=True)
Q3.Destination.replace("DAR SALAM", "TANZANIA", inplace=True)
Q3.Destination.replace("dar Salam", "TANZANIA", inplace=True)
Q3.Destination.replace("ARUSHA salam", "TANZANIA", inplace=True)
Q3.Destination.replace("arusha", "TANZANIA", inplace=True)
Q3.Destination.replace("Arusha", "TANZANIA", inplace=True)
Q3.Destination.replace("TZ", "TANZANIA", inplace=True)
Q3.Destination.replace("tz", "TANZANIA", inplace=True)
Q3.Destination.replace("Tz", "TANZANIA", inplace=True)
Q3.Destination.replace("JUBA", "SUDAN", inplace=True)
Q3.Destination.replace("Juba", "SUDAN", inplace=True)
Q3.Destination.replace("juba", "SUDAN", inplace=True)
Q3.Destination.replace("Sudan", "SUDAN", inplace=True)
Q3.Destination.replace("sudan", "SUDAN", inplace=True)
Q3.Destination.replace("KIGALI", "RWANDA", inplace=True)
Q3.Destination.replace("kigali", "RWANDA", inplace=True)
Q3.Destination.replace("Kigali", "RWANDA", inplace=True)
Q3.Destination.replace("RWA", "RWANDA", inplace=True)
Q3.Destination.replace("rwa", "RWANDA", inplace=True)
Q3.Destination.replace("Rwa", "RWANDA", inplace=True)
Q3.Destination.replace("Congo", "CONGO", inplace=True)
Q3.Destination.replace("congo", "CONGO", inplace=True)
Q3.Destination.replace("BRD", "BURUNDI", inplace=True)
Q3.Destination.replace("brd", "BURUNDI", inplace=True)
Q3.Destination.replace("Brd", "BURUNDI", inplace=True)
Q3.Destination.replace("Burundi", "BURUNDI", inplace=True)
Q3.Destination.replace("burundi", "BURUNDI", inplace=True)
Q3.Destination.replace("SOI", "SOY", inplace=True)
Q3.Destination.replace("soi", "SOY", inplace=True)
Q3.Destination.replace("Soi", "SOY", inplace=True)
Q3.Destination.replace("SUMEKA", "SUNEKA", inplace=True)
Q3.Destination.replace("Suneka", "SUNEKA", inplace=True)
Q3.Destination.replace("Sunek", "SUNEKA", inplace=True)
Q3.Destination.replace("AIRPORT", "AIR PORT", inplace=True)
Q3.Destination.replace("Airport", "AIR PORT", inplace=True)
Q3.Destination.replace("airport", "AIR PORT", inplace=True)
Q3.Destination.replace("M/MAHIU", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("MAIMAHIU", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("M MAHIU", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("MAI MAHIU", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("m/Mahiu", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("M/Mahiu", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("M/mahiu", "MAAI MAHIU", inplace=True)
Q3.Destination.replace("MLBA", "MALABA", inplace=True)
Q3.Destination.replace("NRBI", "NAIROBI", inplace=True)
Q3.Destination.replace("BGMA", "BUNGOMA", inplace=True)
Q3.Destination.replace("BNGMA", "BUNGOMA", inplace=True)
Q3.Destination.replace("NKURU", "NAKURU", inplace=True)
Q3.Destination.replace("MBSA", "MOMBASA", inplace=True)
Q3.Destination.replace("MONBSA", "MOMBASA", inplace=True)
Q3.Destination.replace("MOMBASAS", "MOMBASA", inplace=True)
Q3.Destination.replace("MO,MBASA", "MOMBASA", inplace=True)
Q3.Destination.replace("MOAMBASA", "MOMBASA", inplace=True)
Q3.Destination.replace("MBSA", "MOMBASA", inplace=True)
Q3.Destination.replace("KMPLA", "UGANDA", inplace=True)
Q3.Destination.replace("KPLM", "UGANDA", inplace=True)
Q3.Destination.replace("KAPALA", "UGANDA", inplace=True)
Q3.Destination.replace("KAMPAL;A", "UGANDA", inplace=True)
Q3.Destination.replace("TORORO'", "UGANDA", inplace=True)
Q3['Destination'].fillna(0, inplace=True)
Q3.Destination.replace(0, "UNSPECIFIED", inplace=True)

# DATA CLEANING ON TANSPORTER
Q3.Transporter.replace("001 INVEST", "001 INVESTMENTS", inplace=True)
Q3.Transporter.replace("001 INV", "001 INVESTMENTS", inplace=True)
Q3.Transporter.replace("001", "001 INVESTMENTS", inplace=True)
Q3.Transporter.replace("A.M ENT", "A.M ENTERPRISES", inplace=True)
Q3.Transporter.replace("A.M TRANSP", "A.M ENTERPRISES", inplace=True)
Q3.Transporter.replace("A.M TRANS", "A.M ENTERPRISES", inplace=True)
Q3.Transporter.replace("A.N TRANSP", "A.N TRANSPORTERS", inplace=True)
Q3.Transporter.replace("AHAD TRANSPORTER", "AHADI TRANSPORTER", inplace=True)
Q3.Transporter.replace("AHADI TRANS", "AHADI TRANSPORTER", inplace=True)
Q3.Transporter.replace("AHADI TRANSP", "AHADI TRANSPORTER", inplace=True)
Q3.Transporter.replace("ALUCATA SUPP", "ALUCATA SUPPLIERS", inplace=True)
Q3.Transporter.replace("ANWARALI & BROTHERS", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ANWAR ALI & BROTHERS", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ANWARALI AND BROS", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ANWARALI AND BROS LTD", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ANWARALIS", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ANWARALI", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ANWAR ALI", "ANWARALI & BROTHERS LTD", inplace=True)
Q3.Transporter.replace("ATM TRANSPORTERS", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("ATM TRANS", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("ATM TRANSP", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("ATM TRAN", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("A.T.M TRANS", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("A.T.M", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("ATM", "A.T.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("AWALE", "AWALE TRANSPORTERS", inplace=True)
Q3.Transporter.replace("AWALE TRANS", "AWALE TRANSPORTERS", inplace=True)
Q3.Transporter.replace("AWALE TRANSP", "AWALE TRANSPORTERS", inplace=True)
Q3.Transporter.replace("AYOTI DISTRIBUTORS", "AYOTI DISTRIBUTORS LIMITED", inplace=True)
Q3.Transporter.replace("BABS INVEST", "AYOTI DISTRIBUTORS LIMITED", inplace=True)
Q3.Transporter.replace("AYOTI DISTRIBUTORS", "BABS INVESTMENT", inplace=True)
Q3.Transporter.replace("BABS", "BABS INVESTMENT", inplace=True)
Q3.Transporter.replace("BADAR H/W", "BADAR HARDWARE LIMITED", inplace=True)
Q3.Transporter.replace("BADAR HARDWARE", "BADAR HARDWARE LIMITED", inplace=True)
Q3.Transporter.replace("BADAR", "BADAR HARDWARE LIMITED", inplace=True)
Q3.Transporter.replace("BADAR H/W LIMITED", "BADAR HARDWARE LIMITED", inplace=True)
Q3.Transporter.replace("BADAR H/W LTD", "BADAR HARDWARE LIMITED", inplace=True)
Q3.Transporter.replace("BASH", "BASH HAULIERS", inplace=True)
Q3.Transporter.replace("BEST INV", "BEST INVESTMENTS", inplace=True)
Q3.Transporter.replace("BEST INVEST", "BEST INVESTMENTS", inplace=True)
Q3.Transporter.replace("BLOOMIGHTON", "BLOOMITON LTD", inplace=True)
Q3.Transporter.replace("BLOOMITON", "BLOOMITON LTD", inplace=True)
Q3.Transporter.replace("BOOKER", "BOOKER ENT", inplace=True)
Q3.Transporter.replace("BRUCETRUCK", "BRUCE TRUCK", inplace=True)
Q3.Transporter.replace("CFX LTD", "C.F.X LTD", inplace=True)
Q3.Transporter.replace("CFX", "C.F.X LTD", inplace=True)
Q3.Transporter.replace("C.F.X", "C.F.X LTD", inplace=True)
Q3.Transporter.replace("COCACOLA", "COCA COLA LTD", inplace=True)
Q3.Transporter.replace("COCA COLA", "COCA COLA LTD", inplace=True)
Q3.Transporter.replace("COCACOLA", "COCA COLA LTD", inplace=True)
Q3.Transporter.replace("D.M TRANS", "D.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("D.M TRAN", "D.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("D.M", "D.M TRANSPORTERS", inplace=True)
Q3.Transporter.replace("DOTCOM", "DOT COM INV", inplace=True)
Q3.Transporter.replace("DOT COM", "DOT COM INV", inplace=True)
Q3.Transporter.replace("DULYAH INVEST", "DULYAH INV", inplace=True)
Q3.Transporter.replace("EEDI LTD", "EEDI(K)LTD", inplace=True)
Q3.Transporter.replace("ENA INVT", "ENA INV", inplace=True)
Q3.Transporter.replace("FEWA TRANS", "FEWAS TRANS", inplace=True)
Q3.Transporter.replace("FEWA TRAN", "FEWAS TRANS", inplace=True)
Q3.Transporter.replace("FEWA TRAN", "FIXED INV", inplace=True)
Q3.Transporter.replace("FIXED", "FIXED INV", inplace=True)
Q3.Transporter.replace("G4S", "G4S KENYA", inplace=True)
Q3.Transporter.replace("GILANI'S SUPERMARKET", "GILANIS SUPERMARKET", inplace=True)
Q3.Transporter.replace("GILENI SUPERMARKETS", "GILANIS SUPERMARKET", inplace=True)
Q3.Transporter.replace("GILANI", "GILANIS SUPERMARKET", inplace=True)
Q3.Transporter.replace("GILANI SUP", "GILANIS SUPERMARKET", inplace=True)
Q3.Transporter.replace("K.P LTD", "K.P. LTD", inplace=True)
Q3.Transporter.replace("KITALE INDUSTRIES", "KITALE INDUSTRIES LTD", inplace=True)
Q3.Transporter.replace("KITALE IND", "KITALE INDUSTRIES LTD", inplace=True)
Q3.Transporter.replace("LEADERS TRANS", "LEADERS TRANSPORTERS", inplace=True)
Q3.Transporter.replace("LEADERS TRAN", "LEADERS TRANSPORTERS", inplace=True)
Q3.Transporter.replace("LEADERS", "LEADERS TRANSPORTERS", inplace=True)
Q3.Transporter.replace("LEYMA  CARGO", "LEYMA CARGO", inplace=True)
Q3.Transporter.replace("LEYMA", "LEYMA CARGO", inplace=True)
Q3.Transporter.replace("LI.E CO LTD", "LI.E COMPANY LTD", inplace=True)
Q3.Transporter.replace("M INVESTMENTS", "M. INVESTMENTSD", inplace=True)
Q3.Transporter.replace("M INV", "M. INVESTMENTSD", inplace=True)
Q3.Transporter.replace("M INVEST", "M. INVESTMENTSD", inplace=True)
Q3.Transporter.replace("M", "M. INVESTMENTSD", inplace=True)
Q3.Transporter.replace("ZAWADI TRANS", "ZAWADI TRANSPORTERS", inplace=True)
Q3.Transporter.replace("ZAWADI TRANPORTES", "ZAWADI TRANSPORTERS", inplace=True)
Q3.Transporter.replace("YASMIN  VENTURES", "YASMIN VENTURES", inplace=True)
Q3.Transporter.replace("WARENG INVEST", "WARENG INVESTMENTS", inplace=True)
Q3.Transporter.replace("WARENG", "WARENG INVESTMENTS", inplace=True)
Q3.Transporter.replace("WARENG INVES", "WARENG INVESTMENTS", inplace=True)
Q3.Transporter.replace("WANDE INVEST", "WANDE INVESTMENTS", inplace=True)
Q3.Transporter.replace("WANDE INV", "WANDE INVESTMENTS", inplace=True)
Q3.Transporter.replace("WANDE", "WANDE INVESTMENTS", inplace=True)
Q3.Transporter.replace("VISION TRANSPORTER", "VISION TRANSPORTERS", inplace=True)
Q3.Transporter.replace("VISION TRANS", "VISION TRANSPORTERS", inplace=True)
Q3.Transporter.replace("VISION", "VISION TRANSPORTERS", inplace=True)
Q3.Transporter.replace("VISION TRAN", "VISION TRANSPORTERS", inplace=True)
Q3.Transporter.replace("VICTORY TRANS", "VICTORY TRANSPORTERS", inplace=True)
Q3.Transporter.replace("VICTORY TRAN", "VICTORY TRANSPORTERS", inplace=True)
Q3.Transporter.replace("VICTORY", "VICTORY TRANSPORTERS", inplace=True)
Q3.Transporter.replace("SINOTRUK", "SINOTRUCK", inplace=True)
Q3.Transporter.replace("Sinotruck", "SINOTRUCK", inplace=True)
Q3.Transporter.replace("sinotruck", "SINOTRUCK", inplace=True)
Q3.Transporter.replace("SIGINON LOGISTICS", "SIGINON GLOBAL LOGISTICS", inplace=True)
Q3.Transporter.replace("SIGINON", "SIGINON GLOBAL LOGISTICS", inplace=True)
Q3.Transporter.replace("SIGINON LOGISTIC", "SIGINON GLOBAL LOGISTICS", inplace=True)
Q3.Transporter.replace("SIGINON LOGISTIS", "SIGINON GLOBAL LOGISTICS", inplace=True)
Q3.Transporter.replace("SIGNON LOGISTICS", "SIGINON GLOBAL LOGISTICS", inplace=True)
Q3.Transporter.replace("SHREEJI LTD", "SHREEJI LIMITED", inplace=True)
Q3.Transporter.replace("SHREEJI", "SHREEJI LIMITED", inplace=True)
Q3.Transporter.replace("SHAJANAD HOLDINGS", "SHAJANAD HOLDINGS LTD", inplace=True)
Q3.Transporter.replace("SHAJANAD HOLDING", "SHAJANAD HOLDINGS LTD", inplace=True)
Q3.Transporter.replace("SHAJANAD", "SHAJANAD HOLDINGS LTD", inplace=True)
Q3.Transporter.replace("S.S.F", "S.S.F LIMITED", inplace=True)
Q3.Transporter.replace("SSF", "S.S.F LIMITED", inplace=True)
Q3.Transporter.replace("S.SF", "S.S.F LIMITED", inplace=True)
Q3.Transporter.replace("SS.F", "S.S.F LIMITED", inplace=True)
Q3.Transporter.replace("PEMBE FLOUR LIMITED", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMBE FLOUR", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMBE LIMITED", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMBE LTD", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMPE FLOUR LIMITED", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMBE FLOUR", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMBE FLOOR", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PEMBE", "PEMBE FLOUR LTD", inplace=True)
Q3.Transporter.replace("PACIFIC", "PACIFIC MILLERS", inplace=True)
Q3.Transporter.replace("NAIVAS", "NAIVAS LTD", inplace=True)
Q3.Transporter.replace("NAIVAS LIMITED", "NAIVAS LTD", inplace=True)
Q3.Transporter.replace("MULTIPLE HAULIER", "MULTIPLE HAULIERS", inplace=True)
Q3.Transporter.replace("MULTIPLE", "MULTIPLE HAULIERS", inplace=True)
Q3.Transporter.replace("MULTIPLE LOGISTICS", "MULTIPLE HAULIERS", inplace=True)
Q3.Transporter.replace("MULTIPLE LOGISTIC", "MULTIPLE HAULIERS", inplace=True)
Q3.Transporter.replace("MT. CO. LTD", "MT CO. LTD", inplace=True)
Q3.Transporter.replace("MT CO LTD", "MT CO. LTD", inplace=True)
Q3.Transporter.replace("MOTREX LIMITED", "MOTREX LTD", inplace=True)
Q3.Transporter.replace("MOTREX", "MOTREX LTD", inplace=True)
Q3.Transporter.replace("MOMBASA MILLERS", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MOMBASA MILLER", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MOMBASA M", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MMM", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("mmm", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("M.M.M", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("M.M MILLERS", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MSA MILLERS", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MSA M. MILLERS", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MSA", "MOMBASA MAIZE MILLERS", inplace=True)
Q3.Transporter.replace("MOMBASA", "MOMBASA CEMENT", inplace=True)
Q3.Transporter.replace("MODOH TRANSPORTERS", "MODOH TRANSPORTER", inplace=True)
Q3.Transporter.replace("MODOH TRANSP", "MODOH TRANSPORTER", inplace=True)
Q3.Transporter.replace("MODERN", "MODERN COACH", inplace=True)
Q3.Transporter.replace("MASAI K LTD", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("MASAI LTD", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("MASAI", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("MAASAI", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("MASAI(k) LTD", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("MASAI K LTD", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("MASAI k LTD", "MASAI (K) LTD", inplace=True)
Q3.Transporter.replace("ZAWADI TRANSPORT", "ZAWADI TRANSPORTERS", inplace=True)
Q3['Transporter'].fillna(0, inplace=True)
Q3.Transporter.replace(0, "UNSPECIFIED", inplace=True)

# GVW CALCULATION: GVW represents Gross Vehicle Weight which is total weight
Q3['GVW'] = (Q3.GA1 + Q3.GA2 + Q3.GA3 + Q3.GA4 )

# GLIMIT CALCULATION: GLIMIT implies to Gross allowable weight with 5% tolerance factored

Q3['GLIMIT'] = Q3.Configuration
Q3['GLIMIT'].replace('2A',1.05*18000, inplace=True)
Q3['GLIMIT'].replace('3A',1.05 * 26000, inplace=True)
Q3['GLIMIT'].replace('3C',1.05 * 28000, inplace=True)
Q3['GLIMIT'].replace('3D',1.05 * 26000, inplace=True)
Q3['GLIMIT'].replace('4A',1.05 * 36000, inplace=True)
Q3['GLIMIT'].replace('5C',1.05 * 40000, inplace=True)
Q3['GLIMIT'].replace('5D',1.05 * 44000, inplace=True)
Q3['GLIMIT'].replace('6G',1.05 * 48000, inplace=True)
Q3['GLIMIT'].replace('6C',1.05 * 50000, inplace=True)
Q3['GLIMIT'].replace('6A',1.05 * 52000, inplace=True)
Q3['GLIMIT'].replace('7A',1.05 * 56000, inplace=True)

#Gross Overloading/Compliance Analysis
Q3['GO'] = round((Q3.GVW-Q3.GLIMIT), 1)

Q3.sort_values(['GO'], ascending=False, inplace=True)

Q3_GO = round(pd.DataFrame(Q3[Q3.GO>0]), 1)
Q3_GCOMP = round(pd.DataFrame(Q3[Q3.GO<=0]), 1)

#Returning Non-Overloading
GCOMP = Q3['GO']<=0
Q3.loc[GCOMP, 'GO']=0

round(Q3_GO.describe(), 1)

Q3_GO.head()

#Gross Overloading per Axle Configuration
GO_Axf = Q3_GO.groupby('Configuration')['GO'].count()
GO_Axf = pd.DataFrame(GO_Axf)

GCOMP_Axf = Q3_GCOMP.groupby('Configuration')['GO'].count()
GCOMP_Axf = pd.DataFrame(GCOMP_Axf)

GO_Axf.rename(columns={'GO':'GOf'}, inplace=True)
GCOMP_Axf.rename(columns={'GO':'GCOMPf'}, inplace=True)

GO_Axp = round((GO_Axf/GO_Axf.sum())*100, 1)
GO_Axp = pd.DataFrame(GO_Axp)

GCOMP_Axp = round((GCOMP_Axf/GCOMP_Axf.sum())*100, 1)
GCOMP_Axp = pd.DataFrame(GCOMP_Axp)

GO_Axp.rename(columns={'GOf':'GOp'}, inplace=True)
GCOMP_Axp.rename(columns={'GCOMPf':'GCOMPp'}, inplace=True)

GO_Ax = pd.concat([GCOMP_Axf, GCOMP_Axp, GO_Axf, GO_Axp], axis=1)

GO_Ax['TOTALf'] = (GO_Axf['GOf'] + GCOMP_Axf['GCOMPf'])

GO_Ax['TOTALf'].fillna((GCOMP_Axf.GCOMPf), inplace=True)

GO_Ax['TOTALp'] = round(((GO_Ax.TOTALf/GO_Ax.TOTALf.sum())*100), 1)

GO_Ax.sort_values(['GOf'], ascending=False, inplace=True)

GO_Ax.fillna(0, inplace=True)

sns.barplot(data = GO_Ax, y = 'GOp', x = GO_Ax.index)
plt.title('GROSS OVERLOADING PER AXLE CONFIGURATION')
plt.xlabel('Axle Configuration')
plt.ylabel('Gross Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER AXLE CONFIGURATION.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GO_Ax.loc['TOTALS']=round(GO_Ax.sum(), 0)

GO_Ax

GO_Ax.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER AXLE CONFIGURATION.xlsx')

#Gross Overloading per Origin
GO_Orgf = Q3_GO.groupby('Origin')['GO'].count()
GO_Orgf = pd.DataFrame(GO_Orgf)

GCOMP_Orgf = Q3_GCOMP.groupby('Origin')['GO'].count()
GCOMP_Orgf = pd.DataFrame(GCOMP_Orgf)

GO_Orgf.rename(columns={'GO':'GOf'}, inplace=True)
GCOMP_Orgf.rename(columns={'GO':'GCOMPf'}, inplace=True)

GO_Orgp = round((GO_Orgf/GO_Orgf.sum())*100, 1)
GO_Orgp = pd.DataFrame(GO_Orgp)

GCOMP_Orgp = round((GCOMP_Orgf/GCOMP_Orgf.sum())*100, 1)
GCOMP_Orgp = pd.DataFrame(GCOMP_Orgp)

GO_Orgp.rename(columns={'GOf':'GOp'}, inplace=True)
GCOMP_Orgp.rename(columns={'GCOMPf':'GCOMPp'}, inplace=True)

GO_Org = pd.concat([GCOMP_Orgf, GCOMP_Orgp, GO_Orgf, GO_Orgp], axis=1)

GO_Org['TOTALf'] = (GO_Orgf['GOf'] + GCOMP_Orgf['GCOMPf'])

GO_Org['TOTALf'].fillna((GCOMP_Orgf.GCOMPf), inplace=True)

GO_Org['TOTALp'] = round(((GO_Org.TOTALf/GO_Org.TOTALf.sum())*100), 1)

GO_Org.sort_values(['GOf'], ascending=False, inplace=True)

GO_Org.fillna(0, inplace=True)

GO_Orgplot = GO_Org.head(20)
sns.barplot(data = GO_Orgplot, x = 'GOp', y = GO_Orgplot.index, palette = 'winter')
plt.title('GROSS OVERLOADING PER ORIGIN')
plt.ylabel('Origin')
plt.xlabel('Gross Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER ORIGIN.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GO_Org.loc['TOTALS']=round(GO_Org.sum(), 0)

GO_Org

GO_Org.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER ORIGIN.xlsx')

#Gross Overloading per Destination
GO_Desf = Q3_GO.groupby('Destination')['GO'].count()
GO_Desf = pd.DataFrame(GO_Desf)

GCOMP_Desf = Q3_GCOMP.groupby('Destination')['GO'].count()
GCOMP_Desf = pd.DataFrame(GCOMP_Desf)

GO_Desf.rename(columns={'GO':'GOf'}, inplace=True)
GCOMP_Desf.rename(columns={'GO':'GCOMPf'}, inplace=True)

GO_Desp = round((GO_Desf/GO_Desf.sum())*100, 1)
GO_Desp = pd.DataFrame(GO_Desp)

GCOMP_Desp = round((GCOMP_Desf/GCOMP_Desf.sum())*100, 1)
GCOMP_Desp = pd.DataFrame(GCOMP_Desp)

GO_Desp.rename(columns={'GOf':'GOp'}, inplace=True)
GCOMP_Desp.rename(columns={'GCOMPf':'GCOMPp'}, inplace=True)

GO_Des = pd.concat([GCOMP_Desf, GCOMP_Desp, GO_Desf, GO_Desp], axis=1)

GO_Des['TOTALf'] = (GO_Desf['GOf'] + GCOMP_Desf['GCOMPf'])

GO_Des['TOTALf'].fillna((GCOMP_Desf.GCOMPf), inplace=True)

GO_Des['TOTALp'] = round(((GO_Des.TOTALf/GO_Des.TOTALf.sum())*100), 1)

GO_Des.sort_values(['GOf'], ascending=False, inplace=True)

GO_Des.fillna(0, inplace=True)

GO_Desplot = GO_Des.head(20)
sns.barplot(data = GO_Desplot, x = 'GOp', y = GO_Desplot.index, palette = 'summer')
plt.title('GROSS OVERLOADING PER DESTINATION')
plt.ylabel('Destination')
plt.xlabel('Gross Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER DESTINATION.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GO_Des.loc['TOTALS']=round(GO_Des.sum(), 0)

GO_Des

GO_Des.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER DESTINATION.xlsx')

#Gross Overloading per Transporter
GO_Transf = Q3_GO.groupby('Transporter')['GO'].count()
GO_Transf = pd.DataFrame(GO_Transf)

GCOMP_Transf = Q3_GCOMP.groupby('Transporter')['GO'].count()
GCOMP_Transf = pd.DataFrame(GCOMP_Transf)

GO_Transf.rename(columns={'GO':'GOf'}, inplace=True)
GCOMP_Transf.rename(columns={'GO':'GCOMPf'}, inplace=True)

GO_Transp = round((GO_Transf/GO_Transf.sum())*100, 1)
GO_Transp = pd.DataFrame(GO_Transp)

GCOMP_Transp = round((GCOMP_Transf/GCOMP_Transf.sum())*100, 1)
GCOMP_Transp = pd.DataFrame(GCOMP_Transp)

GO_Transp.rename(columns={'GOf':'GOp'}, inplace=True)
GCOMP_Transp.rename(columns={'GCOMPf':'GCOMPp'}, inplace=True)

GO_Trans = pd.concat([GCOMP_Transf, GCOMP_Transp, GO_Transf, GO_Transp], axis=1)

GO_Trans['TOTALf'] = (GO_Transf['GOf'] + GCOMP_Transf['GCOMPf'])

GO_Trans['TOTALf'].fillna((GCOMP_Transf.GCOMPf), inplace=True)

GO_Trans['TOTALp'] = round(((GO_Trans.TOTALf/GO_Trans.TOTALf.sum())*100), 1)

GO_Trans.sort_values(['GOf'], ascending=False, inplace=True)

GO_Trans.fillna(0, inplace=True)

GO_Transplot = GO_Trans.head(20)
sns.barplot(data = GO_Transplot, x = 'GOp', y = GO_Transplot.index, palette = 'spring')
plt.title('GROSS OVERLOADING PER TRANSPORTER')
plt.ylabel('Transporter')
plt.xlabel('Gross Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER TRANSPORTER.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GO_Trans.loc['TOTALS']=round(GO_Trans.sum(), 0)

GO_Trans

GO_Trans.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROSS OVERLOADING PER TRANSPORTER.xlsx')

# GROUP AXLE OVERLOADING (GAO) IS OVERLOADING BASED ON GROUPED AXLES
# CALCULATING OVERLOADING ON GA1 (GA1O)
Q3['GA1Oa'] = 0
GA1Oa = Q3['Configuration']!="3C"
Q3['GA1Oa'] = (Q3.GA1 - 1.05 * 8000)

Q3['GA1Ob'] = 0
GA1Ob = Q3['Configuration']=="3C"
Q3['GA1Oa'] = (Q3.GA1 - 1.05 * 10000)

Q3['GA1O'] = (Q3.GA1Oa + Q3.GA1Ob)

GA1COMP = Q3['GA1O']<=0
Q3.loc[GA1COMP, 'GA1O']=0 # GA1O Is overloading on GA1

# DROPPING DUMMY VARIABLES FOR GA1O
Q3.drop(['GA1Oa', 'GA1Ob'], axis=1, inplace=True)

# CALCULATING OVERLOADING ON GA2 (GA2O)
Q3['GA2O_2A'] = 0
GA2O_2A = Q3['Configuration']=="2A"
Q3.loc[GA2O_2A, 'GA2O_2A'] = (Q3.GA2 - 1.05 * 10000)
GA2ACOMP = Q3['GA2O_2A']<=0
Q3.loc[GA2ACOMP, 'GA2O_2A']=0

Q3['GA2O_3A'] = 0
GA2O_3A = Q3['Configuration']=="3A"
Q3.loc[GA2O_3A, 'GA2O_3A'] = (Q3.GA2 - 1.05 * 18000)
GA3ACOMP = Q3['GA2O_3A']<=0
Q3.loc[GA3ACOMP, 'GA2O_3A']=0

Q3['GA2O_3C'] = 0
GA2O_3C = Q3['Configuration']=="3C"
Q3.loc[GA2O_3C, 'GA2O_3C'] = (Q3.GA2 - 1.05 * 18000)
GA3CCOMP = Q3['GA2O_3C']<=0
Q3.loc[GA3CCOMP, 'GA2O_3C']=0

Q3['GA2O_3D'] = 0
GA2O_3D = Q3['Configuration']=="3D"
Q3.loc[GA2O_3D, 'GA2O_3D'] = (Q3.GA2 - 1.05 * 18000)
GA3DCOMP = Q3['GA2O_3D']<=0
Q3.loc[GA3DCOMP, 'GA2O_3D']=0

Q3['GA2O_4A'] = 0
GA2O_4A = Q3['Configuration']=="4A"
Q3.loc[GA2O_4A, 'GA2O_4A'] = (Q3.GA2 - 1.05 * 10000)
GA4ACOMP = Q3['GA2O_4A']<=0
Q3.loc[GA4ACOMP, 'GA2O_4A']=0

Q3['GA2O_5C'] = 0
GA2O_5C = Q3['Configuration']=="5C"
Q3.loc[GA2O_5C, 'GA2O_5C'] = (Q3.GA2 - 1.05 * 10000)
GA5CCOMP = Q3['GA2O_5C']<=0
Q3.loc[GA5CCOMP, 'GA2O_5C']=0

Q3['GA2O_5D'] = 0
GA2O_5D = Q3['Configuration']=="5D"
Q3.loc[GA2O_5D, 'GA2O_5D'] = (Q3.GA2 - 1.05 * 9000)
GA5DCOMP = Q3['GA2O_5D']<=0
Q3.loc[GA5DCOMP, 'GA2O_5D']=0

Q3['GA2O_6G'] = 0
GA2O_6G = Q3['Configuration']=="6G"
Q3.loc[GA2O_6G, 'GA2O_6G'] = (Q3.GA2 - 1.05 * 16000)
GA6GCOMP = Q3['GA2O_6G']<=0
Q3.loc[GA6GCOMP, 'GA2O_6G']=0

Q3['GA2O_6C'] = 0
GA2O_6C = Q3['Configuration']=="6C"
Q3.loc[GA2O_6C, 'GA2O_6C'] = (Q3.GA2 - 1.05 * 18000)
GA6CCOMP = Q3['GA2O_6C']<=0
Q3.loc[GA6CCOMP, 'GA2O_6C']=0

Q3['GA2O_6A'] = 0
GA2O_6A = Q3['Configuration']=="6A"
Q3.loc[GA2O_6A, 'GA2O_6A'] = (Q3.GA2 - 1.05 * 18000)
GA6ACOMP = Q3['GA2O_6A']<=0
Q3.loc[GA6ACOMP, 'GA2O_6A']=0

Q3['GA2O_7A'] = 0
GA2O_7A = Q3['Configuration']=="7A"
Q3.loc[GA2O_7A, 'GA2O_7A'] = (Q3.GA2 - 1.05 * 16000)
GA7ACOMP = Q3['GA2O_7A']<=0
Q3.loc[GA7ACOMP, 'GA2O_7A']=0

Q3['GA2O'] = (Q3.GA2O_2A + Q3.GA2O_3A + Q3.GA2O_3C + Q3.GA2O_3D + Q3.GA2O_4A + Q3.GA2O_5C + Q3.GA2O_5D + Q3.GA2O_6G + Q3.GA2O_6C + Q3.GA2O_6A + Q3.GA2O_7A) # GA2O Is overloading on GA2

# DROPPING DUMMY VARIABLES FOR GA2 OVERLOADING

Q3.drop(['GA2O_2A', 'GA2O_3A', 'GA2O_3C', 'GA2O_3D', 'GA2O_4A', 'GA2O_5C', 'GA2O_5D', 'GA2O_6G', 'GA2O_6C', 'GA2O_6A', 'GA2O_7A'], axis=1, inplace=True)

# CALCULATING OVERLOADING ON GA3 (GA3O)
Q3['GA3O_4A'] = 0
GA3O_4A = Q3['Configuration']=="4A"
Q3.loc[GA3O_4A, 'GA3O_4A'] = (Q3.GA3 - 1.05 * 18000)
GA4ACOMP = Q3['GA3O_4A']<=0
Q3.loc[GA4ACOMP, 'GA3O_4A']=0

Q3['GA3O_5C'] = 0
GA3O_5C = Q3['Configuration']=="5C"
Q3.loc[GA3O_5C, 'GA3O_5C'] = (Q3.GA3 - 1.05 * 22000)
GA5CCOMP = Q3['GA3O_5C']<=0
Q3.loc[GA5CCOMP, 'GA3O_5C']=0

Q3['GA3O_5D'] = 0
GA3O_5D = Q3['Configuration']=="5D"
Q3.loc[GA3O_5D, 'GA3O_5D'] = (Q3.GA3 - 1.05 * 9000)
GA5DCOMP = Q3['GA3O_5D']<=0
Q3.loc[GA5DCOMP, 'GA3O_5D']=0

Q3['GA3O_6G'] = 0
GA3O_6G = Q3['Configuration']=="6G"
Q3.loc[GA3O_6G, 'GA3O_6G'] = (Q3.GA3 - 1.05 * 24000)
GA6GCOMP = Q3['GA3O_6G']<=0
Q3.loc[GA6GCOMP, 'GA3O_6G']=0

Q3['GA3O_6C'] = 0
GA3O_6C = Q3['Configuration']=="6C"
Q3.loc[GA3O_6C, 'GA3O_6C'] = (Q3.GA3 - 1.05 * 24000)
GA6CCOMP = Q3['GA3O_6C']<=0
Q3.loc[GA6CCOMP, 'GA3O_6C']=0

Q3['GA3O_6A'] = 0
GA3O_6A = Q3['Configuration']=="6A"
Q3.loc[GA3O_6A, 'GA3O_6A'] = (Q3.GA3 - 1.05 * 8000)
GA6ACOMP = Q3['GA3O_6A']<=0
Q3.loc[GA6ACOMP, 'GA3O_6A']=0

Q3['GA3O_7A'] = 0
GA3O_7A = Q3['Configuration']=="7A"
Q3.loc[GA3O_7A, 'GA3O_7A'] = (Q3.GA3 - 1.05 * 16000)
GA7ACOMP = Q3['GA3O_7A']<=0
Q3.loc[GA7ACOMP, 'GA3O_7A']=0

Q3['GA3O'] = (Q3.GA3O_4A + Q3.GA3O_5C + Q3.GA3O_5D + Q3.GA3O_6G + Q3.GA3O_6C + Q3.GA3O_6A + Q3.GA3O_7A) # GA3O Is overloading on GA3

# DROPPING DUMMY VARIABLES FOR GA3O OVERLOADING

Q3.drop(['GA3O_4A', 'GA3O_5C', 'GA3O_5D', 'GA3O_6G', 'GA3O_6C', 'GA3O_6A', 'GA3O_7A'], axis=1, inplace=True)

# CALCULATING OVERLOADING ON GA4 (GA4O)
Q3['GA4O_5D'] = 0
GA4O_5D = Q3['Configuration']=="5D"
Q3.loc[GA4O_5D, 'GA4O_5D'] = (Q3.GA4 - 1.05 * 18000)
GA5DCOMP = Q3['GA4O_5D']<=0
Q3.loc[GA5DCOMP, 'GA4O_5D']=0

Q3['GA4O_6A'] = 0
GA4O_6A = Q3['Configuration']=="6A"
Q3.loc[GA4O_6A, 'GA4O_6A'] = (Q3.GA4 - 1.05 * 18000)
GA6ACOMP = Q3['GA4O_6A']<=0
Q3.loc[GA6ACOMP, 'GA4O_6A']=0

Q3['GA4O_7A'] = 0
GA4O_7A = Q3['Configuration']=="7A"
Q3.loc[GA4O_7A, 'GA4O_7A'] = (Q3.GA4 - 1.05 * 16000)
GA7ACOMP = Q3['GA4O_7A']<=0
Q3.loc[GA7ACOMP, 'GA4O_7A']=0

Q3['GA4O'] = (Q3.GA4O_5D + Q3.GA4O_6A + Q3.GA4O_7A) # GA4O Is overloading on GA4

# DROPPING DUMMY VARIABLES FOR GA4 OVERLOADING
Q3.drop(['GA4O_5D', 'GA4O_6A', 'GA4O_7A'], axis=1, inplace=True)

# CALCULATED GROUP AXLE OVERLOADING (GAO)
Q3['GAO'] = (Q3.GA1O + Q3.GA2O + Q3.GA3O + Q3.GA4O) # GAO

# DROPPING DUMMY VARIABLES FOR GROUPED AXLE OVERLOADING (GAO)
Q3.drop(['GA1O', 'GA2O', 'GA3O', 'GA4O'], axis=1, inplace=True)

#Grouped Axle Overloading/Compliance Analysis
Q3.sort_values(['GAO'], ascending=False, inplace=True)

Q3_GAO = round(pd.DataFrame(Q3[Q3.GAO>0]), 1)
Q3_GACOMP = round(pd.DataFrame(Q3[Q3.GAO<=0]), 1)

#Returning Non-Overloading to zeros
GACOMP = Q3['GAO']<=0
Q3.loc[GACOMP, 'GAO']=0

round(Q3_GAO.describe(), 1)

Q3_GAO.head()

#Grouped Axle Overloading per Axle Configuration
GAO_Axf = Q3_GAO.groupby('Configuration')['GAO'].count()
GAO_Axf = pd.DataFrame(GAO_Axf)

GACOMP_Axf = Q3_GACOMP.groupby('Configuration')['GAO'].count()
GACOMP_Axf = pd.DataFrame(GACOMP_Axf)

GAO_Axf.rename(columns={'GAO':'GAOf'}, inplace=True)
GACOMP_Axf.rename(columns={'GAO':'GACOMPf'}, inplace=True)

GAO_Axp = round((GAO_Axf/GAO_Axf.sum())*100, 1)
GAO_Axp = pd.DataFrame(GAO_Axp)

GACOMP_Axp = round((GACOMP_Axf/GACOMP_Axf.sum())*100, 1)
GACOMP_Axp = pd.DataFrame(GACOMP_Axp)

GAO_Axp.rename(columns={'GAOf':'GAOp'}, inplace=True)
GACOMP_Axp.rename(columns={'GACOMPf':'GACOMPp'}, inplace=True)

GAO_Ax = pd.concat([GACOMP_Axf, GACOMP_Axp, GAO_Axf, GAO_Axp], axis=1)

GAO_Ax['TOTALf'] = (GAO_Axf['GAOf'] + GACOMP_Axf['GACOMPf'])

GAO_Ax['TOTALf'].fillna((GACOMP_Axf.GACOMPf), inplace=True)

GAO_Ax['TOTALp'] = round(((GAO_Ax.TOTALf/GAO_Ax.TOTALf.sum())*100), 1)

GAO_Ax.sort_values(['GAOf'], ascending=False, inplace=True)

GAO_Ax.fillna(0, inplace=True)

sns.barplot(data = GAO_Ax, x = 'GAOp', y = GAO_Ax.index, palette = 'rainbow')
plt.title('GROUP AXLE OVERLOADING PER AXLE CONFIGURATION')
plt.ylabel('Axle Configuration')
plt.xlabel('Group Axle Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER AXLE CONFIGURATION.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GAO_Ax.loc['TOTALS']=round(GAO_Ax.sum(), 0)

GAO_Ax

GAO_Ax.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER AXLE CONFIGURATION.xlsx')

#Grouped Axle Overloading per Origin
GAO_Orgf = Q3_GAO.groupby('Origin')['GAO'].count()
GAO_Orgf = pd.DataFrame(GAO_Orgf)

GACOMP_Orgf = Q3_GACOMP.groupby('Origin')['GAO'].count()
GACOMP_Orgf = pd.DataFrame(GACOMP_Orgf)

GAO_Orgf.rename(columns={'GAO':'GAOf'}, inplace=True)
GACOMP_Orgf.rename(columns={'GAO':'GACOMPf'}, inplace=True)

GAO_Orgp = round((GAO_Orgf/GAO_Orgf.sum())*100, 1)
GAO_Orgp = pd.DataFrame(GAO_Orgp)

GACOMP_Orgp = round((GACOMP_Orgf/GACOMP_Orgf.sum())*100, 1)
GACOMP_Orgp = pd.DataFrame(GACOMP_Orgp)

GAO_Orgp.rename(columns={'GAOf':'GAOp'}, inplace=True)
GACOMP_Orgp.rename(columns={'GACOMPf':'GACOMPp'}, inplace=True)

GAO_Org = pd.concat([GACOMP_Orgf, GACOMP_Orgp, GAO_Orgf, GAO_Orgp], axis=1)

GAO_Org['TOTALf'] = (GAO_Orgf['GAOf'] + GACOMP_Orgf['GACOMPf'])

GAO_Org['TOTALf'].fillna((GACOMP_Orgf.GACOMPf), inplace=True)

GAO_Org['TOTALp'] = round(((GAO_Org.TOTALf/GAO_Org.TOTALf.sum())*100), 1)

GAO_Org.sort_values(['GAOf'], ascending=False, inplace=True)

GAO_Org.fillna(0, inplace=True)

GAO_Orgplot = GAO_Org.head(20)
sns.barplot(data = GAO_Orgplot, x = 'GAOp', y = GAO_Orgplot.index, palette = 'summer')
plt.title('GROUP AXLE OVERLOADING PER ORIGIN')
plt.ylabel('Origin')
plt.xlabel('Group Axle Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER ORIGIN.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GAO_Org.loc['TOTALS']=round(GAO_Org.sum(), 0)

GAO_Org

GAO_Org.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER ORIGIN.xlsx')

#Grouped Axle Overloading per Destination
GAO_Desf = Q3_GAO.groupby('Destination')['GAO'].count()
GAO_Desf = pd.DataFrame(GAO_Desf)

GACOMP_Desf = Q3_GACOMP.groupby('Destination')['GAO'].count()
GACOMP_Desf = pd.DataFrame(GACOMP_Desf)

GAO_Desf.rename(columns={'GAO':'GAOf'}, inplace=True)
GACOMP_Desf.rename(columns={'GAO':'GACOMPf'}, inplace=True)

GAO_Desp = round((GAO_Desf/GAO_Desf.sum())*100, 1)
GAO_Desp = pd.DataFrame(GAO_Desp)

GACOMP_Desp = round((GACOMP_Desf/GACOMP_Desf.sum())*100, 1)
GACOMP_Desp = pd.DataFrame(GACOMP_Desp)

GAO_Desp.rename(columns={'GAOf':'GAOp'}, inplace=True)
GACOMP_Desp.rename(columns={'GACOMPf':'GACOMPp'}, inplace=True)

GAO_Des = pd.concat([GACOMP_Desf, GACOMP_Desp, GAO_Desf, GAO_Desp], axis=1)

GAO_Des['TOTALf'] = (GAO_Desf['GAOf'] + GACOMP_Desf['GACOMPf'])

GAO_Des['TOTALf'].fillna((GACOMP_Desf.GACOMPf), inplace=True)

GAO_Des['TOTALp'] = round(((GAO_Des.TOTALf/GAO_Des.TOTALf.sum())*100), 1)

GAO_Des.sort_values(['GAOf'], ascending=False, inplace=True)

GAO_Des.fillna(0, inplace=True)

GAO_Desplot = GAO_Des.head(20)
sns.barplot(data = GAO_Desplot, x = 'GAOp', y = GAO_Desplot.index, palette = 'rainbow')
plt.title('GROUP AXLE OVERLOADING PER DESTINATION')
plt.ylabel('Destination')
plt.xlabel('Group Axle Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER DESTINATION.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GAO_Des.loc['TOTALS']=round(GAO_Des.sum(), 0)

GAO_Des

GAO_Des.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER DESTINATION.xlsx')

#Grouped Axle Overloading per Transporter
GAO_Transf = Q3_GAO.groupby('Transporter')['GAO'].count()
GAO_Transf = pd.DataFrame(GAO_Transf)

GACOMP_Transf = Q3_GACOMP.groupby('Transporter')['GAO'].count()
GACOMP_Transf = pd.DataFrame(GACOMP_Transf)

GAO_Transf.rename(columns={'GAO':'GAOf'}, inplace=True)
GACOMP_Transf.rename(columns={'GAO':'GACOMPf'}, inplace=True)

GAO_Transp = round((GAO_Transf/GAO_Transf.sum())*100, 1)
GAO_Transp = pd.DataFrame(GAO_Transp)

GACOMP_Transp = round((GACOMP_Transf/GACOMP_Transf.sum())*100, 1)
GACOMP_Transp = pd.DataFrame(GACOMP_Transp)

GAO_Transp.rename(columns={'GAOf':'GAOp'}, inplace=True)
GACOMP_Transp.rename(columns={'GACOMPf':'GACOMPp'}, inplace=True)

GAO_Trans = pd.concat([GACOMP_Transf, GACOMP_Transp, GAO_Transf, GAO_Transp], axis=1)

GAO_Trans['TOTALf'] = (GAO_Transf['GAOf'] + GACOMP_Transf['GACOMPf'])

GAO_Trans['TOTALf'].fillna((GACOMP_Transf.GACOMPf), inplace=True)

GAO_Trans['TOTALp'] = round(((GAO_Trans.TOTALf/GAO_Trans.TOTALf.sum())*100), 1)

GAO_Trans.sort_values(['GAOf'], ascending=False, inplace=True)

GAO_Trans.fillna(0, inplace=True)

GAO_Transplot = GAO_Trans.head(20)
sns.barplot(data = GAO_Transplot, x = 'GAOp', y = GAO_Transplot.index, palette = 'spring')
plt.title('GROUP AXLE OVERLOADING PER TRANSPORTER')
plt.ylabel('Transporter')
plt.xlabel('Group Axle Overloading Tally (%)')
plt.savefig('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER TRANSPORTER.jpg', dpi = 500, bbox_inches = 'tight', pad_inches = 0.5, transparent = True)

GAO_Trans.loc['TOTALS']=round(GAO_Trans.sum(), 0)

GAO_Trans

GAO_Trans.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/GROUP AXLE OVERLOADING PER TRANSPORTER.xlsx')

#Top 20 Gross Overloading HGV
Q3.sort_values(['GO'], ascending=False, inplace=True)
GO20 = Q3.head(20)
GO20

GO20.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/TOP 20 GROSS OVERLOADING HGV.xlsx')

#Top 20 Group Axle Overloading HGV
Q3.sort_values(['GAO'], ascending=False, inplace=True)
GAO20 = Q3.head(20)
GAO20

GAO20.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/TOP 20 GROUP AXLE OVERLOADING HGV.xlsx')

#ANALYSED HGV CLEAN DATA
Q3.sort_values(['GO'], ascending=False, inplace=True)
Q3.to_excel('C:/Users/ACAPE CONSULTANT/Desktop/Pythonbased/Static1/CleanData.xlsx')
