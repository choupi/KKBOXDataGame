import sys

u_dict={}
# noseen
with open(sys.argv[1], 'rb') as f:
    for l in f:
        sl=l.strip().split(',')
        u_dict[sl[0]]=sl[1]

# seen
with open(sys.argv[2], 'rb') as f:
    for l in f:
        if 'user' in l:
            print l.strip()
            continue
        sl=l.strip().split(',')
        if sl[1]=='00000029': v=u_dict[sl[0]]
        else: v=sl[1]
        #else: v='00000029'
        print '%s,%s'%(sl[0], v)
