import xml.etree.ElementTree as ET
import pandas as pd


def Get_XML_Data(df):
    # Load the XML file - Update the path
    tree = ET.parse('/Users/XYZ/Desktop/pegelstaende_neu.xml')
    root = tree.getroot()

    # Create empty lists to store data
    no_list, psmgr_list, pegelname_list, messwert_list, km_list, pnp_list, datum_list, uhrzeit_list, pegelnummer_list = ([] for _ in range(9))

    # Iterate through the XML elements and extract data
    for item in root.findall('.//gewaesser/item'):
        no_list.append(item.find('no').text)
        psmgr_list.append(item.find('psmgr').text)
        pegelname_list.append(item.find('pegelname').text)
        messwert_list.append(item.find('messwert').text)
        km_list.append(item.find('km').text)
        pnp_list.append(item.find('pnp').text)
        datum_list.append(item.find('datum').text)
        uhrzeit_list.append(item.find('uhrzeit').text)
        pegelnummer_list.append(item.find('pegelnummer').text)  

    # Create a Pandas DataFrame
    df = pd.DataFrame({
        'No': no_list,
        'PSMGR': psmgr_list,
        'Pegelname': pegelname_list,
        'Messwert': messwert_list,
        'KM': km_list,
        'PNP': pnp_list,
        'Datum': datum_list,
        'Uhrzeit': uhrzeit_list,
        'Pegelnummer': pegelnummer_list
    })
    return df

def get_output_schema():       
  return pd.DataFrame({
    'No': prep_string(),
    'PSMGR': prep_string(),
    'Pegelname': prep_string(),
    'Messwert': prep_string(),
    'KM': prep_string(),
    'PNP': prep_string(),
    'Datum': prep_string(),
    'Uhrzeit': prep_string(),
    'Pegelnummer': prep_string()
})
