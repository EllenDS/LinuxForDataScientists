#! /usr/bin/python3.8

import csv
from reportlab.pdfgen import canvas
from reportlab.lib import colors

Bitcoin = []
Ether = []
Litecoin = []
Bitcoin_Cash = []
Binance_Coin = []
EOS = []
XRP = []
Lumens = []
Chainlink = []
Polkadot = []
Yearn_finance = []
US_Dollar = []
United_Arab_Emirates_Dirham = []
Argentine_Peso = []
Australian_Dollar = []
Bangladeshi_Taka = []
Bahraini_Dinar = []
Bermudian_Dollar = []
Brazil_Real = []
Canadian_Dollar = []
Swiss_Franc = []
Chilean_Peso = []
Chinese_Yuan = []
Czech_Koruna = []
Danish_Krone = []
Euro = []
British_Pound_Sterling = []
Hong_Kong_Dollar = []
Hungarian_Forint = []
Indonesian_Rupiah = []
Israeli_New_Shekel = []
Indian_Rupee = []
Japanese_Yen = []
South_Korean_Won = []
Kuwaiti_Dinar = []
Sri_Lankan_Rupee = []
Burmese_Kyat = []
Mexican_Peso = []
Malaysian_Ringgit = []
Nigerian_Naira = []
Norwegian_Krone = []
New_Zealand_Dollar = []
Philippine_Peso = []
Pakistani_Rupee = []
Polish_Zloty = []
Russian_Ruble = []
Saudi_Riyal = []
Swedish_Krona = []
Singapore_Dollar = []
Thai_Baht = []
Turkish_Lira = []
New_Taiwan_Dollar = []
Ukrainian_hryvnia = []
Venezuelan_bolívar_fuerte = []
Vietnamese_đồng = []
South_African_Rand = []
IMF_Special_Drawing_Rights = []
Silver_Troy_Ounce = []
Gold_Troy_Ounce = []
Bits = []
Satoshi = []

coin = ["Bitcoin"]
crypto = ["Ether", "Litecoin", "Bitcoin_Cash", "Binance_Coin", "EOS", "XRP", "Lumens", "Chainlink", "Polkadot", "Yearn_finance", "Bits", "Satoshi"]
fiat = ["US_Dollar", "United_Arab_Emirates_Dirham", "Argentine_Peso", "Australian_Dollar", "Bangladeshi_Taka", "Bahraini_Dinar", "Bermudian_Dollar", "Brazil_Real", 
"Canadian_Dollar", "Swiss_Franc", "Chilean_Peso", "Chinese_Yuan", "Czech_Koruna", "Danish_Krone", "Euro", "British_Pound_Sterling", "Hong_Kong_Dollar", "Hungarian_Forint", "Indonesian_Rupiah",
"Israeli_New_Shekel", "Indian_Rupee", "Japanese_Yen", "South_Korean_Won", "Kuwaiti_Dinar", "Sri_Lankan_Rupee", "Burmese_Kyat", "Mexican_Peso", "Malaysian_Ringgit", "Nigerian_Naira",
"Norwegian_Krone", "New_Zealand_Dollar", "Philippine_Peso", "Pakistani_Rupee", "Polish_Zloty", "Russian_Ruble", "Saudi_Riyal", "Swedish_Krona", "Singapore_Dollar", "Thai_Baht",
"Turkish_Lira", "New_Taiwan_Dollar", "Ukrainian_hryvnia", "Venezuelan_bolívar_fuerte", "Vietnamese_đồng", "South_African_Rand", "IMF_Special_Drawing_Rights"]
commodity = ["Silver_Troy_Ounce", "Gold_Troy_Ounce"]

with open('transformed_data.csv','rt')as file:
   csv_rows = csv.reader(file)
   for row in csv_rows:     
        if row[0] == "Bitcoin":
            Bitcoin.append(row[1])
        elif row[0] == "Ether":
            Ether.append(row[1])
        elif row[0] == "Litecoin":
            Litecoin.append(row[1])
        elif row[0] == "Bitcoin Cash":
            Bitcoin_Cash.append(row[1])
        elif row[0] == "Binance Coin":
            Binance_Coin.append(row[1])
        elif row[0] == "EOS":
            EOS.append(row[1])
        elif row[0] == "XRP":
            XRP.append(row[1])
        elif row[0] == "Lumens":
            Lumens.append(row[1])
        elif row[0] == "Chainlink":
            Chainlink.append(row[1])
        elif row[0] == "Polkadot":
            Polkadot.append(row[1])
        elif row[0] == "Yearn finance":
            Yearn_finance.append(row[1])
        elif row[0] == "US Dollar":
            US_Dollar.append(row[1])
        elif row[0] == "United Arab Emirates Dirham":
            United_Arab_Emirates_Dirham.append(row[1])
        elif row[0] == "Argentine Peso":
            Argentine_Peso.append(row[1])    
        elif row[0] == "Australian Dollar":
            Australian_Dollar.append(row[1])
        elif row[0] == "Bangladeshi Taka":
            Bangladeshi_Taka.append(row[1])
        elif row[0] == "Bahraini Dinar":
            Bahraini_Dinar.append(row[1])
        elif row[0] == "Bermudian Dollar":
            Bermudian_Dollar.append(row[1])
        elif row[0] == "Brazil Real":
            Brazil_Real.append(row[1])
        elif row[0] == "Canadian Dollar":
            Canadian_Dollar.append(row[1])
        elif row[0] == "Swiss Franc":
            Swiss_Franc.append(row[1])
        elif row[0] == "Chilean Peso":
            Chilean_Peso.append(row[1])
        elif row[0] == "Chinese Yuan":
            Chinese_Yuan.append(row[1])
        elif row[0] == "Czech Koruna":
            Czech_Koruna.append(row[1])
        elif row[0] == "Danish Krone":
            Danish_Krone.append(row[1])
        elif row[0] == "Euro":
            Euro.append(row[1])
        elif row[0] == "British Pound Sterling":
            British_Pound_Sterling.append(row[1])
        elif row[0] == "Hong Kong Dollar":
            Hong_Kong_Dollar.append(row[1])
        elif row[0] == "Hungarian Forint":
            Hungarian_Forint.append(row[1])
        elif row[0] == "Indonesian Rupiah":
            Indonesian_Rupiah.append(row[1])
        elif row[0] == "Israeli New Shekel":
            Israeli_New_Shekel.append(row[1])
        elif row[0] == "Indian Rupee":
            Indian_Rupee.append(row[1])
        elif row[0] == "Japanese Yen":
            Japanese_Yen.append(row[1])
        elif row[0] == "South Korean Won":
            South_Korean_Won.append(row[1])
        elif row[0] == "Kuwaiti Dinar":
            Kuwaiti_Dinar.append(row[1])
        elif row[0] == "Sri Lankan Rupee":
            Sri_Lankan_Rupee.append(row[1])
        elif row[0] == "Burmese Kyat":
            Burmese_Kyat.append(row[1])
        elif row[0] == "Mexican Peso":
            Mexican_Peso.append(row[1])
        elif row[0] == "Malaysian Ringgit":
            Malaysian_Ringgit.append(row[1])
        elif row[0] == "Nigerian Naira":
            Nigerian_Naira.append(row[1])
        elif row[0] == "Norwegian Krone":
            Norwegian_Krone.append(row[1])
        elif row[0] == "New Zealand Dollar":
            New_Zealand_Dollar.append(row[1])
        elif row[0] == "Philippine Peso":
            Philippine_Peso.append(row[1])
        elif row[0] == "Pakistani Rupee":
            Pakistani_Rupee.append(row[1])
        elif row[0] == "Polish Zloty":
            Polish_Zloty.append(row[1])
        elif row[0] == "Russian Ruble":
            Russian_Ruble.append(row[1])
        elif row[0] == "Saudi Riyal":
            Saudi_Riyal.append(row[1])
        elif row[0] == "Swedish Krona":
            Swedish_Krona.append(row[1])
        elif row[0] == "Singapore Dollar":
            Singapore_Dollar.append(row[1])
        elif row[0] == "Thai Baht":
            Thai_Baht.append(row[1])
        elif row[0] == "Turkish Lira":
            Turkish_Lira.append(row[1])
        elif row[0] == "New Taiwan Dollar":
            New_Taiwan_Dollar.append(row[1])
        elif row[0] == "Ukrainian hryvnia":
            Ukrainian_hryvnia.append(row[1])
        elif row[0] == "Venezuelan bolívar fuerte":
            Venezuelan_bolívar_fuerte.append(row[1])
        elif row[0] == "Vietnamese đồng":
            Vietnamese_đồng.append(row[1])
        elif row[0] == "South African Rand":
            South_African_Rand.append(row[1])
        elif row[0] == "IMF Special Drawing Rights":
            IMF_Special_Drawing_Rights.append(row[1])
        elif row[0] == "Silver - Troy Ounce":
            Silver_Troy_Ounce.append(row[1])
        elif row[0] == "Gold - Troy Ounce":
            Gold_Troy_Ounce.append(row[1])
        elif row[0] == "Bits":
            Bits.append(row[1])
        elif row[0] == "Satoshi":
            Satoshi.append(row[1])


report_euro = float(Euro[-1]) - float(Euro[0])
report_USD = float(US_Dollar[-1]) - float(US_Dollar[0])
report_pound = float(British_Pound_Sterling[-1]) - float(British_Pound_Sterling[0])
report_yen = float(Japanese_Yen[-1]) - float(Japanese_Yen[0])
report_yuan = float(Chinese_Yuan[-1]) - float(Chinese_Yuan[0])
report_shekel = float(Israeli_New_Shekel[-1]) - float(Israeli_New_Shekel[0])
report_silver = float(Silver_Troy_Ounce[-1]) - float(Silver_Troy_Ounce[0])
report_gold = float(Gold_Troy_Ounce[-1]) - float(Gold_Troy_Ounce[0])


fileName = 'report.pdf'
documentTitle = 'Currency report'
title = 'Linux for Data Scientists'
subTitle = 'Bitcoin Evaluation'
textLines = [
    'Evolution of currencies compared to Bitcoin',
    'Euro:   '+ str(report_euro),
    'US_Dollar:   ' + str(report_USD),
    'British Poun Sterling:   ' + str(report_pound),
    'Japanese Yen:   ' + str(report_yen),
    'Chinese Yuan:   ' + str(report_yuan),
    'Israeli New Shekel:   ' + str(report_shekel),
    'Silver Troy Ounce:   ' + str(report_silver),
    'Gold Troy Ounce:   ' + str(report_gold),
]
  

pdf = canvas.Canvas(fileName)
  
pdf.setTitle(documentTitle)
  
pdf.setFont('Courier-Bold', 24)
pdf.drawCentredString(300, 770, title)
  
pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)
  
pdf.line(30, 710, 550, 710)
  
text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.black)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)
  

pdf.save()

