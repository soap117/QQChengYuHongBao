import re
dict_normalize = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a', 'ō':'o', 'ó':'o', 'ǒ':'o', 'ò':'o', 'ē':'e', 'é':'e', 'ě':'e', 'è':'e','ī':'i', 'í':'i', 'ǐ':'i', 'ì':'i',
'ū':'u', 'ú':'u', 'ǔ':'u', 'ù':'u', 'ǖ':'v', 'ǘ':'v','ǚ':'v', 'ǜ':'v'}
diction_raw = open('all.txt', 'r', encoding='UTF-8').readlines()
diction_fpy = {}
import pickle
for line in diction_raw:
    temp = re.search('拼音：', line)
    if temp != None:
        chengyu = line[0: temp.regs[0][0]]
        chengyu = chengyu.replace(' ', '')
        py = re.findall('拼音：(.*)释义', line)
        if len(py)==0:
            continue
        else:
            py = py[0]
        for k in range(len(py)):
            if py[k] in dict_normalize.keys():
                py = py.replace(py[k], dict_normalize[py[k]])
        pys = re.split('[ \u3000]', py)
        for t in range(len(pys)-1, 0, -1):
            if len(pys[t])==0:
                del pys[t]
        fpy = pys[0]
        spy = ''
        for single_py in pys:
            if len(single_py)>0:
                spy += single_py[0]
        if fpy not in diction_fpy.keys():
            diction_fpy[fpy] = [(chengyu, spy)]
        else:
            diction_fpy[fpy].append((chengyu, spy))
pickle.dump(diction_fpy, open('fpy.pkl', 'wb'))


