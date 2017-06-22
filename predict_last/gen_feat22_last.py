import sys

VL={'00000669':0,
    '00000482':1,
    '00000670':2,
    '00000251':3,
    '00000664':4,
    '00000483':5,
    '00000049':6,
    '00000360':7,
    '00000409':8,
    '00000372':9,
    '00000484':10,
    '00000667':11,
    '00000118':12,
    '00000088':13,
    '00000212':14,
    '00000491':15,
    '00000317':16}
v_dict={}
# video stat
with open(sys.argv[1], 'rb') as f:
    for l in f:
        sl=l.strip().split(',')
        v_dict[sl[0]]=map(float, sl[1:])

ul_dict={}
# label
with open(sys.argv[2], 'rb') as f:
    for l in f:
        if 'user' in l: continue
        sl=l.strip().split(',')
        ul_dict[sl[0]]=sl[1]

u_dict={}
u_last={}
#event 
with open(sys.argv[3], 'rb') as f:
    for l in f:
        if 'user_id' in l: continue
        sl=l.strip().split(',')
        if sl[1] not in u_dict: u_dict[sl[1]]={}
        if sl[2] not in u_dict[sl[1]]: u_dict[sl[1]][sl[2]]=[]
        try: u_dict[sl[1]][sl[2]].append(int(sl[3]))
        except: pass
        if sl[1] not in u_last: u_last[sl[1]]=[]
        u_last[sl[1]].append((sl[2], int(sl[0])))
        #elif  int(sl[0])>u_last[sl[1]][1]: u_last[sl[1]]=(sl[2], int(sl[0]))

for u in u_dict:
    #vlist=sorted([(v,sum(u_dict[u][v])/v_dict[v][1]) for v in u_dict[u]], key=lambda x:x[1], reverse=True)
    #vcnt=sum([len(u_dict[u][v]) for v in u_dict[u]])
    vl_list=sorted(u_last[u], key=lambda x:x[1])

    #v_last=u_last[u][0]
    v_last=vl_list[-1][0]
    s=sum([sum(u_dict[u][v]) for v in u_dict[u]])
    vlen=len(u_dict[u])
    vl_s=sum(u_dict[u][v_last])
    vl_m=vl_s/v_dict[v_last][1]
    vl_l=len(u_dict[u][v_last])
    vl_c=vl_l/v_dict[v_last][2]
    #vl_t=1475305200-u_last[u][1]
    vl_t=1475305200-vl_list[-1][1]
    vl_tint=vl_list[-1][1]-vl_list[0][1]
    if vl_tint==0: vl_tint=1
    for i in vl_list:
        if i[0]==v_last: 
            vl_st=i[1]
            break
    vl_int=vl_list[-1][1]-vl_st
    i='0'
    #if ul_dict[u] in u_dict[u]: i='1'
    if ul_dict[u]==v_last: i='1'
    v1=0
    v2=0
    if v_dict[v_last][1]>v_dict[v_last][3]: v1=1
    if v_dict[v_last][2]>v_dict[v_last][4]: v2=1
    r=[u, i, ul_dict[u], v_last]+map(str, [vl_s/float(s), vl_s, vl_m, vl_l, vl_c, vl_t, vl_tint, vl_int, float(vl_int)/vl_tint, v_dict[v_last][0], v_dict[v_last][1], v_dict[v_last][2], v1, v2 ])
    print ','.join(r)

