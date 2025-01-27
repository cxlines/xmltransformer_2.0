import csv
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import os

# Specify the path to your .csv file
csv_file_path = r'C:\Users\mulle\Desktop\JASPRAVIM25\marian11_app\xmltransformer\mz001.csv'

# Initialize variables
castka3Sum = 0
castka46Sum = 0
castka5Sum = 0
castka7Sum = 0
castka8Sum = 0
castka9Sum = 0
castka10Sum = 0
castka11Sum = 0
castka12Sum = 0
cast1 = 0
cast2 = 0
cast3 = 0
cast4 = 0
cast5 = 0
cast6 = 0
cast7 = 0
cast8 = 0
cast9 = 0
cast10 = 0

# Process the .csv file
with open(csv_file_path, mode='r', encoding='latin1') as file:
    csv_reader = csv.reader(file, delimiter=';')  # Specify ';' as the delimiter

    for row in csv_reader:
        if row and len(row) >= 7:  # Ensure there are at least 4 columns
            if row and len(row) >= 7:  # Ensure there are at least 7 columns
                dateSMR = row[6]  # Get the value in the 7th column (index 6)
            else:
                print(f"Row 1 does not have at least 7 columns. Found {len(row)} columns.")
            # Assign variables based on conditions
            if row[0] == '803' and row[3] == '527':
                castka3Sum = float(row[2])
            if row[0] == '803' and row[3].startswith('301'):
                castka46Sum = float(row[2])
            if row[0] == '804' and row[3] == '527':
                castka5Sum = float(row[2])
            if row[0] == '805' and row[3] == '527':
                castka7Sum = float(row[2])
            if row[0] == '805' and row[3].startswith('301'):
                castka8Sum = float(row[2])
            if row[0] == '1200':
                castka9Sum = float(row[2])
            if row[0] == '1498':
                castka10Sum = float(row[2]) * -1
            if row[0] == '3000':
                castka11Sum = float(row[2])
            if row[0] == '3001':
                castka12Sum = float(row[2])
            if row[0] == '800' and row[3] == '524':
                cast1 = float(row[2])
            if row[0] == '891' and row[3] == '524':
                cast2 = float(row[2])
            if row[0] == '894' and row[3] == '524':
                cast3 = float(row[2])
            if row[0] == '895' and row[3] == '524':
                cast4 = float(row[2])
            if row[0] == '896' and row[3] == '524':
                cast5 = float(row[2])
            if row[0] == '897' and row[3] == '524':
                cast6 = float(row[2])
            if row[0] == '800' and row[3] == '331':
                cast7 = float(row[2])
            if row[0] == '892' and row[3] == '331':
                cast8 = float(row[2])
            if row[0] == '893' and row[3] == '331':
                cast9 = float(row[2])
            if row[0] == '894' and row[3] == '331':
                cast10 = float(row[2])

# Calculate castka1Sum and castka2Sum
castka1Sum = cast1 + cast2 + cast3 + cast4 + cast5 + cast6
castka2Sum = cast7 + cast8 + cast9 + cast10
castka1p2 = castka1Sum + castka2Sum
castka3p4 = castka3Sum + castka46Sum
castka5p6 = castka5Sum + castka7Sum
castka7p8 = castka7Sum + castka8Sum
castka9p10 = castka9Sum + castka10Sum
castka11p12 = castka11Sum + castka12Sum
# Format dateSMR to MM/YYYY
if dateSMR is not None:
    parts = dateSMR.split('.')
    if len(parts) == 2:
        dateSMR = f"{parts[1]}/{parts[0]}"  # Format as MM/YYYY
        dateMR = f"{parts[1]}{parts[0]}"    # Format as MMYYYY


# Print the values
print(f"The value of castka3Sum is: {castka3Sum:.2f}")
print(f"The value of castka46Sum is: {castka46Sum:.2f}")
print(f"The value of castka5Sum is: {castka5Sum:.2f}")
print(f"The value of castka7Sum is: {castka7Sum:.2f}")
print(f"The value of castka8Sum is: {castka8Sum:.2f}")
print(f"The value of castka9Sum is: {castka9Sum:.2f}")
print(f"The value of castka10Sum is: {castka10Sum:.2f}")
print(f"The value of castka11Sum is: {castka11Sum:.2f}")
print(f"The value of castka12Sum is: {castka12Sum:.2f}")
print(f"The value of cast1 is: {cast1:.2f}")
print(f"The value of cast2 is: {cast2:.2f}")
print(f"The value of cast3 is: {cast3:.2f}")
print(f"The value of cast4 is: {cast4:.2f}")
print(f"The value of cast5 is: {cast5:.2f}")
print(f"The value of cast6 is: {cast6:.2f}")
print(f"The value of cast7 is: {cast7:.2f}")
print(f"The value of cast8 is: {cast8:.2f}")
print(f"The value of cast9 is: {cast9:.2f}")
print(f"The value of cast10 is: {cast10:.2f}")
print(f"The value of castka1Sum is: {castka1Sum:.2f}")
print(f"The value of castka2Sum is: {castka2Sum:.2f}")
print(f'dateSMR: {dateSMR}')
print(f'dateMR: {dateMR}')

# XML template
xml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<MoneyData ICAgendy="" KodAgendy="" HospRokOd="" HospRokDo="" description="pohľadávky a záväzky" ExpZkratka="_PH+ZV" >
    <SeznamZavazku>
        <Zavazek>
            <Doklad></Doklad>
            <DRada>MZAV2</DRada>
            <Popis>sociálne poistenie 12/2023</Popis>
            <PrDokl>SP122023</PrDokl>
            <VarSym>122023</VarSym>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatVyst>2023-12-31</DatVyst>
            <DatSpl>2024-01-31</DatSpl>
            <DatPln>2023-12-31</DatPln>
            <Doruceno>2023-12-31</Doruceno>
            <Dbrpis>0</Dbrpis>
            <Adresa>
                <ObchNazev>Sociálna poisťovňa</ObchNazev>
                <ICO>30807484</ICO>
            </Adresa>
            <UcPokl>BU 01</UcPokl>
            <Cleneni>21P 00</Cleneni>
            <PlnenDPH>0</PlnenDPH>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castka1p2}</Zaklad0> 
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
                <SeznamDalsiSazby>
                    <DalsiSazba>
                        <Popis>druhá znížená</Popis>
                        <HladinaDPH>1</HladinaDPH>
                        <Sazba>5</Sazba>
                        <Zaklad>0</Zaklad>
                        <DPH>0</DPH>
                    </DalsiSazba>
                </SeznamDalsiSazby>
            </SouhrnDPH>
            <Celkem>{castka1p2}</Celkem> 
            <UhZbyva>{castka1p2}</UhZbyva> 
            <PUZbyva>{castka1p2}</PUZbyva> 
            <ZjednD>0</ZjednD>
            <SeznamRozuctPolozek>
                <RozuctPolozka>
                    <Popis>sociálne poistenie 12/2023 - zamestnávateľ</Popis>
                    <UcMD>524000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka1Sum}</Castka> 
                    <ParSym>SP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
                <RozuctPolozka>
                    <Popis>sociálne poistenie 12/2023 - zamestnanec</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka2Sum}</Castka> 
                    <ParSym>SP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
            </SeznamRozuctPolozek>
        </Zavazek>
        <Zavazek>
            <Doklad></Doklad>
            <DRada>MZAV2</DRada>
            <Popis>zdravotné poistenie 12/2023</Popis>
            <PrDokl>VSZP122023</PrDokl>
            <VarSym>122023</VarSym>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatVyst>2023-12-31</DatVyst>
            <DatSpl>2024-01-25</DatSpl>
            <DatPln>2023-12-31</DatPln>
            <Doruceno>2023-12-31</Doruceno>
            <Dbrpis>0</Dbrpis>
            <Adresa>
                <ObchNazev>Všeobecná zdravotná poisťovňa, a.s.</ObchNazev>
                <ICO>35937874</ICO>
            </Adresa>
            <UcPokl>BU 01</UcPokl>
            <Cleneni>21P 00</Cleneni>
            <PlnenDPH>0</PlnenDPH>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castka3p4}</Zaklad0> 
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
            </SouhrnDPH>
            <Celkem>{castka3p4}</Celkem>
            <UhZbyva>{castka3p4}</UhZbyva>
            <PUZbyva>{castka3p4}</PUZbyva>
            <ZjednD>0</ZjednD>
            <SeznamRozuctPolozek>
                <RozuctPolozka>
                    <Popis>zdravotné poistenie 12/2023 - zamestnávateľ</Popis>
                    <UcMD>524000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka3Sum}</Castka> 
                    <ParSym>VSZP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
                <RozuctPolozka>
                    <Popis>zdravotné poistenie 12/2023 - zamestnanec</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka46Sum}</Castka>
                    <ParSym>VSZP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
            </SeznamRozuctPolozek>
        </Zavazek>
        <Zavazek>
            <Doklad></Doklad>
            <DRada>MZAV2</DRada>
            <Popis>zdravotné poistenie 12/2023</Popis>
            <PrDokl>DOZP122023</PrDokl>
            <VarSym>122023</VarSym>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatVyst>2023-12-31</DatVyst>
            <DatSpl>2024-01-25</DatSpl>
            <DatPln>2023-12-31</DatPln>
            <Doruceno>2023-12-31</Doruceno>
            <Dbrpis>0</Dbrpis>
            <Adresa>
                <ObchNazev>DÔVERA zdravotná poisťovňa, a. s.</ObchNazev>
                <ICO>35942436</ICO>
            </Adresa>
            <UcPokl>BU 01</UcPokl>
            <Cleneni>21P 00</Cleneni>
            <PlnenDPH>0</PlnenDPH>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castka5p6}</Zaklad0> 
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
            </SouhrnDPH>
            <Celkem>{castka5p6}</Celkem>
            <UhZbyva>{castka5p6}</UhZbyva>
            <PUZbyva>{castka5p6}</PUZbyva>
            <ZjednD>0</ZjednD>           
            <SeznamRozuctPolozek>
                <RozuctPolozka>
                    <Popis>zdravotné poistenie 12/2023 - zamestnávateľ</Popis>
                    <UcMD>524000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka5Sum}</Castka>
                    <ParSym>DOZP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
                <RozuctPolozka>
                    <Popis>zdravotné poistenie 12/2023 - zamestnanec</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka46Sum}</Castka> 
                    <ParSym>DOZP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
            </SeznamRozuctPolozek>
        </Zavazek>
        <Zavazek>
            <Doklad></Doklad>
            <DRada>MZAV2</DRada>
            <Popis>zdravotné poistenie 12/2023</Popis>
            <PrDokl>UNZP122023</PrDokl>
            <VarSym>122023</VarSym>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatVyst>2023-12-31</DatVyst>
            <DatSpl>2024-01-25</DatSpl>
            <DatPln>2023-12-31</DatPln>
            <Doruceno>2023-12-31</Doruceno>
            <Dbrpis>0</Dbrpis>
            <Adresa>
                <ObchNazev>Union zdravotná poisťovňa, a.s.</ObchNazev>
                <ICO>36284831</ICO>
            </Adresa>
            <UcPokl>BU 01</UcPokl>
            <Cleneni>21P 00</Cleneni>
            <PlnenDPH>0</PlnenDPH>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castka7p8}</Zaklad0> 
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
            </SouhrnDPH>
            <Celkem>{castka7p8}</Celkem>
            <UhZbyva>{castka7p8}</UhZbyva>
            <PUZbyva>{castka7p8}</PUZbyva>
            <ZjednD>0</ZjednD>
            <SeznamRozuctPolozek>
                <RozuctPolozka>
                    <Popis>zdravotné poistenie 12/2023 - zamestnávateľ</Popis>
                    <UcMD>524000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka7Sum}</Castka> 
                    <ParSym>UNZP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
                <RozuctPolozka>
                    <Popis>zdravotné poistenie 12/2023 - zamestnanec</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>336000</UcD>
                    <Castka>{castka8Sum}</Castka>
                    <ParSym>UNZP122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
            </SeznamRozuctPolozek>
        </Zavazek>
        <Zavazek>
            <Doklad></Doklad>
            <DRada>MZAV2</DRada>
            <Popis>daň zo mzdy 12/2023</Popis>
            <PrDokl>DU122023</PrDokl>
            <VarSym>122023</VarSym>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatVyst>2023-12-31</DatVyst>
            <DatSpl>2024-01-25</DatSpl>
            <DatPln>2023-12-31</DatPln>
            <Doruceno>2023-12-31</Doruceno>
            <Dbrpis>0</Dbrpis>
            <Adresa>
                <ObchNazev>Daňový úrad</ObchNazev>
                <ICO>1212121</ICO>
            </Adresa>
            <UcPokl>BU 01</UcPokl>
            <Cleneni>21P 00</Cleneni>
            <PlnenDPH>0</PlnenDPH>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castka9p10}</Zaklad0> 
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
            </SouhrnDPH>
            <Celkem>{castka9p10}</Celkem>
            <UhZbyva>{castka9p10}</UhZbyva>
            <PUZbyva>{castka9p10}</PUZbyva>
            <ZjednD>0</ZjednD>
            <SeznamRozuctPolozek>
                <RozuctPolozka>
                    <Popis>daň zo mzdy 12/2023</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>342000</UcD>
                    <Castka>{castka9Sum}</Castka> 
                    <ParSym>DU122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
                <RozuctPolozka>
                    <Popis>daňový bonus 12/2023</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>342000</UcD>
                    <Castka>{castka10Sum}</Castka> 
                    <ParSym>DU122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
            </SeznamRozuctPolozek>
        </Zavazek>
        <Zavazek>
            <Doklad></Doklad>
            <DRada>MZAV2</DRada>
            <Popis>mzdy na účet 12/2023</Popis>
            <PrDokl>MZ122023</PrDokl>
            <VarSym>122023</VarSym>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatVyst>2023-12-31</DatVyst>
            <DatSpl>2024-01-25</DatSpl>
            <DatPln>2023-12-31</DatPln>
            <Doruceno>2023-12-31</Doruceno>
            <Dbrpis>0</Dbrpis>
            <Adresa>
                <ObchNazev>Zamestnanci</ObchNazev>
                <ICO>212121</ICO>
            </Adresa>
            <UcPokl>BU 01</UcPokl>
            <Cleneni>21P 00</Cleneni>
            <PlnenDPH>0</PlnenDPH>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castka11p12}</Zaklad0> 
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
            </SouhrnDPH>
            <Celkem>{castka11p12}</Celkem>
            <UhZbyva>{castka11p12}</UhZbyva>
            <PUZbyva>{castka11p12}</PUZbyva>
            <ZjednD>0</ZjednD>
            <SeznamRozuctPolozek>
                <RozuctPolozka>
                    <Popis>mzdy na účet 12/2023</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>331331</UcD>
                    <Castka>{castka11Sum}</Castka> 
                    <ParSym>MZ122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
                <RozuctPolozka>
                    <Popis>mzdy v hotovosti 12/2023</Popis>
                    <UcMD>331000</UcMD>
                    <UcD>331331</UcD>
                    <Castka>{castka12Sum}</Castka> 
                    <ParSym>MZ122023</ParSym>
                    <TypCena>0</TypCena>
                    <SazbaDPH>0</SazbaDPH>
                </RozuctPolozka>
            </SeznamRozuctPolozek>
        </Zavazek>
    </SeznamZavazku>
</MoneyData>
"""
# Output to file
output_path = os.path.join(os.getcwd(), "ZAV.xml")
with open(output_path, "w", encoding="utf-8") as xml_file:
    xml_file.write(xml_template)

print(f"XML output saved to {output_path}")
