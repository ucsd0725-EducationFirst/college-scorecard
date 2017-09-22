#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

with open("Most-Recent-Cohorts-All-Data-Elements.csv") as file:
	data = file.readlines()
data = [l.strip() for l in data]
fields = data[0].split(",")[1:]
data = [l.split(",") for l in data[1:]]

"""
Regions:

0	U.S. Service Schools
1	New England (CT, ME, MA, NH, RI, VT)
2	Mid East (DE, DC, MD, NJ, NY, PA)
3	Great Lakes (IL, IN, MI, OH, WI)
4	Plains (IA, KS, MN, MO, NE, ND, SD)
5	Southeast (AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)
6	Southwest (AZ, NM, OK, TX)
7	Rocky Mountains (CO, ID, MT, UT, WY)
8	Far West (AK, CA, HI, NV, OR, WA)
9	Outlying Areas (AS, FM, GU, MH, MP, PR, PW, VI)

LOCALE

11	City: Large (population of 250,000 or more)
12	City: Midsize (population of at least 100,000 but less than 250,000)
13	City: Small (population less than 100,000)
21	Suburb: Large (outside principal city, in urbanized area with population of 250,000 or more)
22	Suburb: Midsize (outside principal city, in urbanized area with population of at least 100,000 but less than 250,000)
23	Suburb: Small (outside principal city, in urbanized area with population less than 100,000)
31	Town: Fringe (in urban cluster up to 10 miles from an urbanized area)
32	Town: Distant (in urban cluster more than 10 miles and up to 35 miles from an urbanized area)
33	Town: Remote (in urban cluster more than 35 miles from an urbanized area)
41	Rural: Fringe (rural territory up to 5 miles from an urbanized area or up to 2.5 miles from an urban cluster)
42	Rural: Distant (rural territory more than 5 miles but up to 25 miles from an urbanized area or more than 2.5 and up to 10 miles from an urban cluster)
43	Rural: Remote (rural territory more than 25 miles from an urbanized area and more than 10 miles from an urban cluster)

Fields to get:

INSTNM - school name
UGDS - Student population size
UGDS_MEN - percent male
UGDS_WOMEN - percent female

Location

CITY
STABBR
ZIP
INSTURL
LOCALE
REGION
LATITUDE
LONGITUDE

SAT Scores

SATVR25 377
SATVRMID 424
SATVR75 470

SATMT25 370
SATMTMID 420
SATMT75 470

SATWR25 370
SATWR75 470
SATWRMID 420

SAT_AVG 827

ACT Scores

ACTCM25 15
ACTCMMID 17
ACTCM75 19

ACTEN25 14
ACTENMID 17
ACTEN75 19

ACTMT25 15
ACTMTMID 17
ACTMT75 18

ACTWR25 NULL
ACTWRMID NULL
ACTWR75 NULL

Tuition

TUITIONFEE_IN
TUITIONFEE_OUT

PCTPELL - pell grant rate
GRAD_DEBT_MDN - median debt of graduated

Repayment

RPY_1YR_RT
RPY_3YR_RT
RPY_5YR_RT
RPY_7YR_RT

Starting Salary

MN_EARN_WNE_P6
MD_EARN_WNE_P6
PCT10_EARN_WNE_P6
PCT25_EARN_WNE_P6
PCT75_EARN_WNE_P6
PCT90_EARN_WNE_P6

Eventual salary

MN_EARN_WNE_P10
MD_EARN_WNE_P10
PCT10_EARN_WNE_P10
PCT25_EARN_WNE_P10
PCT75_EARN_WNE_P10
PCT90_EARN_WNE_P10
"""

schools = {}

# fields_to_get = {"CIP30CERT1":True,"CIP30CERT2":True,"CIP30ASSOC":True,"CIP30CERT4":True,"CIP30BACHL":True,"CIP31CERT1":True,"CIP31CERT2":True,"CIP31ASSOC":True,"CIP31CERT4":True,"CIP31BACHL":True,"CIP38CERT1":True,"CIP38CERT2":True,"CIP38ASSOC":True,"CIP38CERT4":True,"CIP38BACHL":True,"CIP39CERT1":True,"CIP39CERT2":True,"CIP39ASSOC":True,"CIP39CERT4":True,"CIP39BACHL":True,"CIP40CERT1":True,"CIP40CERT2":True,"CIP40ASSOC":True,"CIP40CERT4":True,"CIP40BACHL":True,"CIP41CERT1":True,"CIP41CERT2":True,"CIP41ASSOC":True,"CIP41CERT4":True,"CIP41BACHL":True,"CIP42CERT1":True,"CIP42CERT2":True,"CIP42ASSOC":True,"CIP42CERT4":True,"CIP42BACHL":True,"CIP43CERT1":True,"CIP43CERT2":True,"CIP43ASSOC":True,"CIP43CERT4":True,"CIP43BACHL":True,"CIP44CERT1":True,"CIP44CERT2":True,"CIP44ASSOC":True,"CIP44CERT4":True,"CIP44BACHL":True,"CIP45CERT1":True,"CIP45CERT2":True,"CIP45ASSOC":True,"CIP45CERT4":True,"CIP45BACHL":True,"CIP46CERT1":True,"CIP46CERT2":True,"CIP46ASSOC":True,"CIP46CERT4":True,"CIP46BACHL":True,"CIP47CERT1":True,"CIP47CERT2":True,"CIP47ASSOC":True,"CIP47CERT4":True,"CIP47BACHL":True,"CIP48CERT1":True,"CIP48CERT2":True,"CIP48ASSOC":True,"CIP48CERT4":True,"CIP48BACHL":True,"CIP49CERT1":True,"CIP49CERT2":True,"CIP49ASSOC":True,"CIP49CERT4":True,"CIP49BACHL":True,"CIP50CERT1":True,"CIP50CERT2":True,"CIP50ASSOC":True,"CIP50CERT4":True,"CIP50BACHL":True,"CIP51CERT1":True,"CIP51CERT2":True,"CIP51ASSOC":True,"CIP51CERT4":True,"CIP51BACHL":True,"CIP52CERT1":True,"CIP52CERT2":True,"CIP52ASSOC":True,"CIP52CERT4":True,"CIP52BACHL":True,"CIP54CERT1":True,"CIP54CERT2":True,"CIP54ASSOC":True,"CIP54CERT4":True,"CIP54BACHL":True,"STABBR":True}

# fields_to_get = {"PCIP01":True,"PCIP03":True,"PCIP04":True,"PCIP05":True,"PCIP09":True,"PCIP10":True,"PCIP11":True,"PCIP12":True,"PCIP13":True,"PCIP14":True,"PCIP15":True,"PCIP16":True,"PCIP19":True,"PCIP22":True,"PCIP23":True,"PCIP24":True,"PCIP25":True,"PCIP26":True,"PCIP27":True,"PCIP29":True,"PCIP30":True,"PCIP31":True,"PCIP38":True,"PCIP39":True,"PCIP40":True,"PCIP41":True,"PCIP42":True,"PCIP43":True,"PCIP44":True,"PCIP45":True,"PCIP46":True,"PCIP47":True,"PCIP48":True,"PCIP49":True,"PCIP50":True,"PCIP51":True,"PCIP52":True,"PCIP54":True,"STABBR":True}

# fields_to_get = {"INSTNM": True,"UGDS": True,"UGDS_MEN": True,"UGDS_WOMEN": True,"CITY": True,"STABBR": True,"ZIP": True,"INSTURL": True,"LOCALE": True,"REGION": True,"LATITUDE": True,"LONGITUDE": True,"SATVR25": True,"SATVR75": True,"SATMT25": True,"SATMT75": True,"SATWR25": True,"SATWR75": True,"SATVRMID": True,"SATMTMID": True,"SATWRMID": True,"SAT_AVG": True,"ACTCM25": True,"ACTCM75": True,"ACTEN25": True,"ACTEN75": True,"ACTMT25": True,"ACTMT75": True,"ACTWR25": True,"ACTWR75": True,"ACTCMMID": True,"ACTENMID": True,"ACTMTMID": True,"ACTWRMID": True,"TUITIONFEE_IN": True,"TUITIONFEE_OUT": True,"PCTPELL": True,"GRAD_DEBT_MDN": True,"RPY_1YR_RT": True,"RPY_3YR_RT": True,"RPY_5YR_RT": True,"RPY_7YR_RT": True,"MN_EARN_WNE_P6": True,"MD_EARN_WNE_P6": True,"PCT10_EARN_WNE_P6": True,"PCT25_EARN_WNE_P6": True,"PCT75_EARN_WNE_P6": True,"PCT90_EARN_WNE_P6": True,"MN_EARN_WNE_P10": True,"MD_EARN_WNE_P10": True,"PCT10_EARN_WNE_P10": True,"PCT25_EARN_WNE_P10": True,"PCT75_EARN_WNE_P10": True,"PCT90_EARN_WNE_P10": True}

for d in data:
	_id = int(d[0])
	s = {}
	for i in range(0, len(fields)):
		f = fields[i]
		if fields_to_get.get(f):
			s[f] = d[i+1]
	schools[_id] = s

import json
with open("schools_percentages.json", "w") as file:
	json.dump(schools, file)