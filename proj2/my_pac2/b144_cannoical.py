import re

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

list_url = ["https://www.b144.co.il/",
"https://private.b144.co.il/",
"https://www.b144.co.il/maps/map/",
"https://www.b144.co.il/zipcode/",
"https://www.b144.co.il/?city=תל-אביב-יפו",
"https://www.b144.co.il/Top/מסעדות/תל-אביב-יפו/",
"https://www.b144.co.il/מוסכים/",
"https://www.b144.co.il/מוסכים/אזור-תל-אביב-והמרכז/",
"https://www.b144.co.il/מוסכים/תל-אביב-יפו/",
"https://www.b144.co.il/מוסכים/תל-אביב-יפו/שכונת-מונטיפיורי/",
"https://www.b144.co.il/מוסכים/מוסך-מורשה/",
"https://www.b144.co.il/מוסכים/מוסך-מורשה/אזור-תל-אביב-והמרכז/",
"https://www.b144.co.il/מוסכים/מוסך-מורשה/תל-אביב-יפו/",
"https://www.b144.co.il/b144_sip/481404134470655D4A120D164570605F/",
"https://www.b144.co.il/b144_sip/businessreviews/481404134470655D4A120D164570605F/",
"https://www.b144.co.il/b144_sip/businessgallery/481404134470655D4A120D164570605F/",
"https://www.b144.co.il/b144_sip/businessproducts/481404134470655D4A120D164570605F/",
"https://private.b144.co.il/privateResults/אבי-כהן/",
"https://private.b144.co.il/bezeq_phone/401C0413477866584F120310/",
"https://www.b144.co.il/Magazine/",
"https://www.b144.co.il/Magazine/עיצוב-שיער-ומספרות/",
"https://www.b144.co.il/Magazine/עיצוב-שיער-ומספרות/טיפים-לשמירה-על-שיער-בריא/",
"https://www.b144.co.il/Coupons/",
"https://www.b144.co.il/Coupons/?_business=עיצוב-שיער-ומספרות",
"https://www.b144.co.il/Coupons/?_business=עיצוב-שיער-ומספרות&_city=אזור-תל-אביב-והמרכז",
"https://www.b144.co.il/Coupons/?_business=עיצוב-שיער-ומספרות&_city=תל-אביב-יפו",
"https://www.b144.co.il/Coupons/?_business=ציוד-לוטרינרים",
"https://www.b144.co.il/PriceLists/",
"https://www.b144.co.il/PriceLists/ב/",
"https://www.b144.co.il/PriceList/בתי-דפוס/",
"https://www.b144.co.il/PriceList/בתי-דפוס/כרטיסי-ביקור/",
"https://www.b144.co.il/Tips/",
"https://www.b144.co.il/Tips/עיצוב-שיער-ומספרות/",
"https://www.b144.co.il/indexes/",
"https://www.b144.co.il/indexes/ב/",
"https://www.b144.co.il/indexes/clients/",
"https://www.b144.co.il/indexes/clients/ב/",
"https://www.b144.co.il/indexes/n_members/",
"https://www.b144.co.il/indexes/n_members/?area=-36",
"https://www.b144.co.il/indexes/n_members/?area=-36&city=5000",
"https://www.b144.co.il/indexes/n_members/?area=-36&city=5000&letter=ב",
"https://www.b144.co.il/chains/",
"https://www.b144.co.il/chains/בתי-מרקחת/",
"https://www.b144.co.il/סניפים/בתי-מרקחת/סופר-פארם/",
"https://www.b144.co.il/סניפים/בתי-מרקחת/סופר-פארם/אזור-תל-אביב-והמרכז/",
"https://www.b144.co.il/סניפים/בתי-מרקחת/סופר-פארם/ירושלים/",
"https://www.b144.co.il/b144_sip/401C041340766D5C4B140514/",
"https://www.b144.co.il/indexes/maps/",
"https://www.b144.co.il/indexes/maps/מפת-תל-אביב-יפו/",
"https://www.b144.co.il/maps/תל-אביב-יפו/",
"https://www.b144.co.il/maps/תל-אביב-יפו/גבעת-כח/",
"https://www.b144.co.il/maps/תל-אביב-יפו/רמת-אביב-ג-שכונה/",
"https://www.b144.co.il/indexes/cities/",
"https://www.b144.co.il/indexes/cities/ב/",
"https://www.b144.co.il/indexes/באר-שבע/",
"https://www.b144.co.il/indexes/באר-שבע/ב/",
"https://www.b144.co.il/indexes/Neighbourhoods/",
"https://www.b144.co.il/maps/תל-אביב-יפו/רמת-אביב-ג/",
"https://www.b144.co.il/indexes/Areas/",
"https://www.b144.co.il/indexes/אזור-תל-אביב-והמרכז/",
"https://www.b144.co.il/indexes/אזור-תל-אביב-והמרכז/ב/",
]

for x in list_url :

    driver.get("view-source:" + x)

    text = driver.page_source
#print(text)
# הוצאת הכתובת של SEOPageCanonical
    pattern = r'"SEOPageCanonical":"(.*?)"'
    match = re.search(pattern, text)

    if match:
        url = match.group(1)
        print("SEOPageCanonical URL:", url)

    driver.get(x)
    text = driver.page_source
# הוצאת הכתובת של canonical רגיל
    pattern2 = r'<link\s+rel="canonical"\s+href="(.*?)"\s*/?>'
    match2 = re.search(pattern2, text)

    if match2:
        url2 = match2.group(1)
        print("Canonical URL:", url2)

    if match and match2 and url == url2:
        print(x + " is good")
    else:
        print(x + "  is not good")


input("x")
