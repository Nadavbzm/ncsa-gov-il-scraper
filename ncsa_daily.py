import requests

dayt = 1
montht = 1
yeart = 18
exist = False

#https://www.gov.il/BlobFolder/news/daily030119/he/daily030119.pdf
for year in range(18, 20):
    for montht in range(1, 12):
        for dayt in range(1, 28):
            if dayt<10:
                day = "0" + str(dayt)

            else:
                day = str(dayt)

            if montht<10:
                month = "0" + str(montht)

            else:
                month = str(montht)

            url = f'https://www.gov.il/BlobFolder/news/daily{day}{month}{year}/he/daily{day}{month}{year}.pdf'
            myfile = requests.get(url)

            if not "<!DOCTYPE html>" in str(myfile.content)[0:50]:
                exist = True
                with open(f'roe/daily{day}{month}{year}.pdf', 'wb+') as temp:
                    temp.write(myfile.content)
            print(f'[+] /roe{day}{month}{year}.pdf : {exist}')
            exit = False
