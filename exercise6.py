import json

with open('ptt_0726_s.json','r',encoding='utf-8') as f:
    ptt=json.load(f)
    #sorted(ptt,key=lambda info:info['h_推文總數']['推'])
    size=len(ptt)
    for i in range(size-1):
        if len(list(ptt[i][r'h_推文總數'])) == 0:
            ptt[i][r'h_推文總數'][r'推'] = 0
        if len(list(ptt[i+1][r'h_推文總數'])) == 0:
            ptt[i+1][r'h_推文總數'][r'推'] = 0
        try:
            if ptt[i][r'h_推文總數'][r'推'] <= ptt[i+1][r'h_推文總數'][r'推']:
                a = ptt[i]
                ptt[i] = ptt[i+1]
                ptt[i+1] = a
        except:
            print(ptt[i][r'h_推文總數'])
            print(ptt[i+1][r'h_推文總數'])
            input()
    
with open('newsort_ptt.json','w',encoding='utf-8') as f2:
        f2.write(json.dumps(ptt,ensure_ascii=False,indent=4))


f = open("newsort_ptt.json", "r" ,encoding='utf-8')
print(f.read())