import omise
import json

omise.api_secret = "xxx"
usd = omise.Forex.retrieve("USD")
eur = omise.Forex.retrieve("EUR")
gbp = omise.Forex.retrieve("GBP")
jpy = omise.Forex.retrieve("JPY")
hkd = omise.Forex.retrieve("HKD")
chf = omise.Forex.retrieve("CHF")
aud = omise.Forex.retrieve("AUD")
dkk = omise.Forex.retrieve("DKK")
cny = omise.Forex.retrieve("CNY")

# print(usd)  # สหรัฐอเมริกา USD
# print(eur)  # EUR
# print(gbp)  # สหราชอาณาจักร GBP
# print(jpy)  # ญี่ปุ่น JPY
# print(hkd)  # ฮ่องกง HKD
# print(chf)  # สวิตเซอร์แลนด์ CHF
# print(aud)  # ออสเตรเลีย AUD
# print(dkk)  # เดนมาร์ก DKK
# print(cny)  # จีน CNY

data = {}
data['rate'] = []
data['rate'].append({'USD': usd.rate})
data['rate'].append({'EUR': eur.rate})
data['rate'].append({'GBP': gbp.rate})
data['rate'].append({'JPY': jpy.rate})
data['rate'].append({'HKD': hkd.rate})
data['rate'].append({'CHF': chf.rate})
data['rate'].append({'AUD': aud.rate})
data['rate'].append({'DKK': dkk.rate})
data['rate'].append({'CNY': cny.rate})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('data.json') as json_data:
    for entry in json_data:
        print(entry)
