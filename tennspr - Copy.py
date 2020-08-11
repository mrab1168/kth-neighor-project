from typing import List, Any

from bs4 import BeautifulSoup as BS
import pandas as pd
from urllib.request import urlopen

pd.set_option('display.width', 1000)

df = pd.read_csv("URL.csv")
URL_List = df['URL']
# URRL is the list

MTFCCs = []
OIDs = []
GEOIDs = []
STATEs = []

CD116s = []
BASENAMEs = []
NAMEs = []

LSADCs = []
FUNCSTATs = []
AREALANDs = []

AREAWATERs = []
CDSESSNs = []
CENTLATs = []

CENTLONs = []
INTPTLATs = []
INTPTLONs = []
# variables

for URL in URL_List:
    html = urlopen(URL)
    soup = BS(html, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')

            if len(cells) > 1:
                MTFCC = cells[0]
                MTFCCs.append(MTFCC.text.strip())

                OID = cells[1]
                OIDs.append(OID.text.strip())

                GOEID = cells[2]
                GEOIDs.append(GOEID.text.strip())

                STATE = cells[3]
                STATEs.append(int(STATE.text.strip()))

                CD116 = cells[4]
                CD116s.append(CD116.text.strip())

                BASENAME = cells[5]
                BASENAMEs.append(BASENAME.text.strip())

                NAME = cells[6]
                NAMEs.append(NAME.text.strip())

                LSADC = cells[7]
                LSADCs.append(LSADC.text.strip())

                FUNCSTAT = cells[8]
                FUNCSTATs.append(FUNCSTAT.text.strip())

                AREALAND = cells[9]
                AREALANDs.append(AREALAND.text.strip())

                AREAWATER = cells[10]
                AREAWATERs.append(AREAWATER.text.strip())

                CDSESSN = cells[11]
                CDSESSNs.append(CDSESSN.text.strip())

                CENTLAT = cells[12]
                CENTLATs.append(CENTLAT.text.strip())

                CENTLON = cells[13]
                CENTLONs.append(CENTLON.text.strip())

                INTPTLAT = cells[14]
                INTPTLATs.append(INTPTLAT.text.strip())

                INTPTLON = cells[15]
                INTPTLONs.append(INTPTLON.text.strip())

df1 = pd.DataFrame(MTFCCs, index=OIDs, columns=['MTFCC'])
df1['GOEID'] = GEOIDs
df1['STATE'] = STATEs
df1['CD116'] = CD116s
df1['BASENAME'] = BASENAMEs
df1['NAME'] = NAMEs
df1['LSADC'] = LSADCs
df1['FUNCSTAT'] = FUNCSTATs
df1['AREALAND'] = AREALANDs
df1['AREAWATER'] = AREAWATERs
df1['CDSESSN'] = CDSESSNs
df1['CENTLAT'] = CENTLATs
df1['CENTLON'] = CENTLONs
df1['INTPTLAT'] = INTPTLATs
df1['INTPTLON'] = INTPTLONs

print(df1)

df1.to_csv(r'USA.csv')