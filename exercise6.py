import json

ptt = open('ptt_0726_s.json','r', encoding='utf-8')
ptt = json.loads(ptt.read())
hot = []
for i in range(len(ptt)):
    hot = ptt[i]["h_推文總數"]
    all = hot.get("all", None)
    if all is not None:
        pass
    else:
        hot['all'] = 0
    print(all)