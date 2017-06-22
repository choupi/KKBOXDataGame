import sys
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

X=[]
Y=[]
LB=[]
# feat train
with open(sys.argv[1], 'rb') as f:
    for l in f:
        sl=l.strip().split(',')
        LB.append(sl[0])
        Y.append(int(sl[1]))
        X.append(map(float, sl[4:13]))
        #X.append(map(float, sl[4:]))

#clf = LogisticRegression(penalty='l1')
TH=0.1
clf = RandomForestClassifier(n_estimators=500, max_depth=10)
#clf = RandomForestClassifier(n_estimators=2000, max_depth=9)
clf.fit(X, Y)
print clf.score(X, Y)
#print clf.coef_
print clf.feature_importances_ 
Ypp=clf.predict_proba(X)
Yp=[]
for i in xrange(len(Ypp)):
    if Ypp[i][1]>TH: Yp.append(1)
    else: Yp.append(0)
#for i in xrange(len(Yp)): print Yp[i]
print confusion_matrix(Y, Yp)
print classification_report(Y, Yp)
#for i in xrange(len(Yp)):
#    if Yp[i]!=Y[i] and Y[i]==1:
#        print LB[i], Y[i], X[i]

X=[]
LB=[]
VL=[]
# feat test
with open(sys.argv[2], 'rb') as f:
    for l in f:
        sl=l.strip().split(',')
        LB.append(sl[0])
        VL.append(sl[3])
        X.append(map(float, sl[4:13]))

Ypp=clf.predict_proba(X)
print 'user_id,title_id'
Yp=[]
for i in xrange(len(Ypp)):
    if Ypp[i][1]>TH: 
        v=VL[i]
    else: 
        v='00000029'
    print '%s,%s'%(LB[i], v)
