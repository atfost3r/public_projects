#! python3

# readCencusExcel.py - Tabulates population and the number of cencus tracts for each country

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

#TODO: Fill in countryData with each contry's population and tracts.
print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    state   = sheet['B' + str(row)].value
    county  = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value
    #Make sure the key for this state exists. 
    countyData.setdefault(state, {})
    #Make sure the key for this country in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)
 
# Open a new text file and write the contents of countryData to it. 
print('Writing results...')
resultFile = open('censes2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
