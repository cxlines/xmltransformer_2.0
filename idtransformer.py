import csv
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import os

# Specify the path to your .csv file
csv_file_path = r'C:\Users\mulle\Desktop\JASPRAVIM25\marian11_app\xmltransformer\mz001.csv'
# Initialize variables
dateSMR = None
castka1Value = None
castka2Value = None
castka3Value = None
castka4Value = None
castka5Value = None
castka6Value = None
castkaDifference = None

# Read the .csv file with the correct delimiter
with open(csv_file_path, mode='r', encoding='latin1') as file:
    csv_reader = csv.reader(file, delimiter=';')  # Specify ';' as the delimiter

    # Get the first row to find dateSMR
    first_row = next(csv_reader, None)  # Read the first row
    print(f"First row: {first_row}")  # Debugging line

    if first_row and len(first_row) >= 7:  # Ensure there are at least 7 columns
        dateSMR = first_row[6]  # Get the value in the 7th column (index 6)
    else:
        print(f"Row 1 does not have at least 7 columns. Found {len(first_row)} columns.")

    # Check the first row for castka6Value
    if first_row and len(first_row) >= 4 and first_row[0] == '700':
        castka6Value = float(first_row[2])  # Get the value in the 3rd column (index 2) and convert to float

    # Find the rows for all other castka values
    for row in csv_reader:
        if row and len(row) >= 4:  # Ensure there are at least 4 columns
            # Find castka1Value
            if castka1Value is None and row[0] == '1490' and row[3].startswith('472'):
                castka1Value = float(row[2])  # Convert to float

            # Find castka2Value
            if castka2Value is None and row[0] == '1490' and row[3].startswith('527'):
                castka2Value = float(row[2])  # Convert to float

            # Find castka3Value
            if castka3Value is None and row[0] == '879':
                castka3Value = float(row[2])  # Convert to float

            # Find castka4Value
            if castka4Value is None and row[0] == '1497':
                castka4Value = float(row[2])  # Convert to float

            # Find castka5Value
            if castka5Value is None and row[0] == '701':
                castka5Value = float(row[2])  # Convert to float

            # Stop searching if all values are found
            if (
                    castka1Value is not None and
                    castka2Value is not None and
                    castka3Value is not None and
                    castka4Value is not None and
                    castka5Value is not None and
                    castka6Value is not None
            ):
                break

# Calculate castkaDifference
if castka6Value is not None and castka5Value is not None:
    castkaDifference = round(castka6Value - castka5Value, 2)  # Limit to 2 decimal places

# Format dateSMR to MM/YYYY
if dateSMR is not None:
    parts = dateSMR.split('.')
    if len(parts) == 2:
        dateSMR = f"{parts[1]}/{parts[0]}"  # Format as MM/YYYY
        dateMR = f"{parts[1]}{parts[0]}"    # Format as MMYYYY

# Calculate the sum of all castka values
castkaSums = sum(filter(None,[castka1Value, castka2Value, castka3Value, castka4Value, castka5Value, castka6Value, castkaDifference]))

# Print the variables
if dateSMR is not None:
    print(f"The value of dateSMR is: {dateSMR}")
else:
    print("The value of dateSMR could not be determined.")

if dateSMR is not None:
    print(f"The value of dateMR is: {dateMR}")
else:
    print("The value of dateMR could not be determined.")

if castka1Value is not None:
    print(f"The value of castka1Value is: {castka1Value}")
else:
    print("The value of castka1Value could not be determined.")

if castka2Value is not None:
    print(f"The value of castka2Value is: {castka2Value}")
else:
    print("The value of castka2Value could not be determined.")

if castka3Value is not None:
    print(f"The value of castka3Value is: {castka3Value}")
else:
    print("The value of castka3Value could not be determined.")

if castka4Value is not None:
    print(f"The value of castka4Value is: {castka4Value}")
else:
    print("The value of castka4Value could not be determined.")

if castka5Value is not None:
    print(f"The value of castka5Value is: {castka5Value}")
else:
    print("The value of castka5Value could not be determined.")

if castka6Value is not None:
    print(f"The value of castka6Value is: {castka6Value}")
else:
    print("The value of castka6Value could not be determined.")

if castkaDifference is not None:
    print(f"The value of castkaDifference is: {castkaDifference:.2f}")
else:
    print("The value of castkaDifference could not be determined.")

    # XML template
xml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<MoneyData ICAgendy="" KodAgendy="" HospRokOd="" HospRokDo="" description="interné doklady" ExpZkratka="_ID">
    <SeznamIntDokl>
        <IntDokl>
            <Doklad></Doklad>
            <Popis>hrubé mzdy {dateSMR}</Popis>
            <DatUcPr>2023-12-31</DatUcPr>
            <DatPln>2023-12-31</DatPln>
            <DatumKV>2023-12-31</DatumKV>
            <CisloZapoc>0</CisloZapoc>
            <VarSym>HM{dateMR}</VarSym>
            <Adresa>
                <ObchNazev>Zamestnanci</ObchNazev>
                <ICO>212121</ICO>
            </Adresa>
            <Cleneni>21P 00</Cleneni>
            <Vyroba>0</Vyroba>
            <ZpVypDPH>1</ZpVypDPH>
            <SSazba>10</SSazba>
            <ZSazba>20</ZSazba>
            <SouhrnDPH>
                <Zaklad0>{castkaSums:.2f}</Zaklad0>
                <Zaklad5>0</Zaklad5>
                <Zaklad22>0</Zaklad22>
                <DPH5>0</DPH5>
                <DPH22>0</DPH22>
            </SouhrnDPH>
            <Celkem>{castkaSums:.2f}</Celkem>
            <DRada>ZVL</DRada>
            <RozuctPolozka>
                <Popis>FP na stravu zo SF</Popis>
                <UcMD>472000</UcMD>
                <UcD>331000</UcD>
                <Castka>{castka1Value:.2f}</Castka>
                <ParSym>HM{dateMR}</ParSym>
                <TypCena>0</TypCena>
                <SazbaDPH>0</SazbaDPH>
            </RozuctPolozka>
            <RozuctPolozka>
                <Popis>FP na stravu z nákladov</Popis>
                <UcMD>527000</UcMD>
                <UcD>331000</UcD>
                <Castka>{castka2Value:.2f}</Castka>
                <ParSym>HM{dateMR}</ParSym>
                <TypCena>0</TypCena>
                <SazbaDPH>0</SazbaDPH>
            </RozuctPolozka>
            <RozuctPolozka>
                <Popis>tvorba SF</Popis>
                <UcMD>527000</UcMD>
                <UcD>472000</UcD>
                <Castka>{castka3Value:.2f}</Castka>
                <ParSym>HM{dateMR}</ParSym>
                <TypCena>0</TypCena>
                <SazbaDPH>0</SazbaDPH>
            </RozuctPolozka>
            <RozuctPolozka>
                <Popis>náhrada príjmu za PN</Popis>
                <UcMD>527000</UcMD>
                <UcD>331000</UcD>
                <Castka>{castka4Value:.2f}</Castka>
                <ParSym>HM{dateMR}</ParSym>
                <TypCena>0</TypCena>
                <SazbaDPH>0</SazbaDPH>
            </RozuctPolozka>
            <RozuctPolozka>
                <Popis>hrubé mzdy {dateSMR}</Popis>
                <UcMD>521000</UcMD>
                <UcD>331000</UcD>
                <Castka>{castka5Value:.2f}</Castka>
                <ParSym>HM{dateMR}</ParSym>
                <TypCena>0</TypCena>
                <SazbaDPH>0</SazbaDPH>
            </RozuctPolozka>
            <RozuctPolozka>
                <Popis>hrubé mzdy dohody {dateSMR}</Popis>
                <UcMD>521000</UcMD>
                <UcD>331000</UcD>
                <Castka>{castkaDifference:.2f}</Castka>
                <ParSym>HM{dateMR}</ParSym>
                <TypCena>0</TypCena>
                <SazbaDPH>0</SazbaDPH>
            </RozuctPolozka>
        </IntDokl>
    </SeznamIntDokl>
</MoneyData>
"""
# Output to file
output_path = os.path.join(os.getcwd(), "ID.xml")
with open(output_path, "w", encoding="utf-8") as xml_file:
    xml_file.write(xml_template)

print(f"XML output saved to {output_path}")