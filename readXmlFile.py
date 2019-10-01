# This script reads an xml file and prints the content of a tag based on its attribute
'''
sample xml

<?xml version='1.0'?>
<DATA>
	<ROW>
		<COLUMN NAME="LOG_ID"><![CDATA[99999999999]]></COLUMN>
		<COLUMN NAME="SESSION_ID"><![CDATA[0845-0845-0845-0845]]></COLUMN>
		<COLUMN NAME="TIMESTAMP"><![CDATA[30-AUG-11 01.59.59.699000000 PM]]></COLUMN>
		<COLUMN NAME="CONTENT"><![CDATA[{
  "message": "Hello",
  "data": "Helloo Data"
}]]></COLUMN>
		<COLUMN NAME="SENDER_TIMESTAMP"><![CDATA[30-AUG-11 01.59.59.699000000 PM]]></COLUMN>
	</ROW>
</DATA>
</xml>

'''
from bs4 import BeautifulSoup
infile = open("aa.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
titles = soup.find_all('COLUMN')
#print(titles)
count=0
for title in titles:
    #print(title.get_text())
    if(str(title.attrs['NAME']) == "CONTENT"):
        print(title.get_text()+",")
        count+=1
        #print("********************************************************************************")
        #print(",")
    #print(title.get_text())
#print(count)
