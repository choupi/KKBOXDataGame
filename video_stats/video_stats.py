import sys

u_dict={}
#event 
with open(sys.argv[1], 'rb') as f:
    for l in f:
        if 'user_id' in l: continue
        sl=l.strip().split(',')
        if sl[1] not in u_dict: u_dict[sl[1]]={}
        if sl[2] not in u_dict[sl[1]]: u_dict[sl[1]][sl[2]]=[]
        try: u_dict[sl[1]][sl[2]].append(int(sl[3]))
        except: pass

v_dict={}
for u in u_dict:
    for v in u_dict[u]:
        if v not in v_dict: v_dict[v]=[[], []]
        vm=sum(u_dict[u][v])
        vl=len(u_dict[u][v])
        v_dict[v][0].append(vm)
        v_dict[v][1].append(vl)

for v in v_dict:
    len_u=len(v_dict[v][0])
    avg_vm=sum(v_dict[v][0])/float(len_u)
    avg_vl=sum(v_dict[v][1])/float(len_u)
    vm_list=sorted([vm for vm in v_dict[v][0]], reverse=True)
    vl_list=sorted([vl for vl in v_dict[v][1]], reverse=True)
    max_vm=vm_list[len_u/4]
    max_vl=vl_list[len_u/4]
    #max_vm=max(v_dict[v][0])
    #max_vl=max(v_dict[v][1])
    print '%s,%d,%f,%f,%d,%d'%(v,len_u,avg_vm,avg_vl,max_vm,max_vl)

