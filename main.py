from __future__ import print_function
import requests
import csv
import time

fileCsv=input("enter name of csv:")
fileCsv=fileCsv + ".csv"
with open(fileCsv, newline='') as fh:
    rd = csv.DictReader(fh, delimiter=',')
    b = []
    c=0
    for row in rd:
        # print(row['Frontside'])
        b.append(str(row['Frontside']))
        c=c+1
print(b)
print(c)
print("len List total World",str(len(b)))
notFount1 = []
notFount2 = []
counter = 0
for item in b:
    counter = counter + 1
    linkDic="https://d27ucmmhxk51xv.cloudfront.net/media/english/ameProns/"+item+".mp3?version=1.1.92"
    doc = requests.get(linkDic)
    print(str(counter) + " ==>> ", doc.status_code)
    if doc.status_code == 200:
        diri = item + ".mp3"
        with open(diri, 'wb') as f:
            f.write(doc.content)

    if doc.status_code != 200:
        notFount1.append(item)
        print("first Try")
        print("List first Try ;) *** 111 *** ===>>",notFount1)
        linkDic = "https://d27ucmmhxk51xv.cloudfront.net/media/english/ameProns/" + item +"1"+ ".mp3?version=1.1.92"
        doc = requests.get(linkDic)
        print(str(counter) + " ==>> ", doc.status_code)
        print("______1_______sleep_______15s___________")
        time.sleep(15)
        if doc.status_code == 200:
            diri = item + ".mp3"
            with open(diri, 'wb') as f:
                f.write(doc.content)
        if doc.status_code != 200:
            notFount2.append(item)
            print("second Try !! :( so soory man")
            print("List second Try So Bad *** 222 *** ===>>",notFount2)
            print("____2_______sleep_______30s___________")
            time.sleep(30)
    print("________totla_______sleep_______5s___________")
    time.sleep(5)

print("\n ------------------------finish-----------------------------\n")
print("len List first Try 111 =====>>>> ",str(len(notFount1)))
print("len List second Try 222 =====>>>> ",str(len(notFount2)))
print("FFFFFinally List first Try ;) *** 111 ***  ===>>",notFount1)
print("FFFFFinally List second Try :( OOOPPPSSS *** 222 ***  ===>>",notFount2)