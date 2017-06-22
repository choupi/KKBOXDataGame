import sys
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

VL=['00000669', '00000664', '00000628', '00000265', '00000391', '00000110', '00000673']
#VL=['00000669', '00000664', '00000628', '00000265', '00000391', '00000110', '00000673', '00000482', '00000267', '00000587']
#VL=['00000669', '00000664', '00000628']

X=[]
Y=[]
LB=[]
# feat train
with open(sys.argv[1], 'rb') as f:
    for l in f:
        sl=l.strip().split(',')
        if sl[1]=='1': continue
        if sl[2] not in VL: continue
        Y.append(sl[2])
        LB.append(sl[0])
        X.append(map(float, sl[4:]))

print len(Y)
#clf = LogisticRegression(penalty='l1')
TH=0.5
#clf = RandomForestClassifier(n_estimators=100, max_depth=18)
clf = RandomForestClassifier(n_estimators=500, max_depth=18)
#clf = RandomForestClassifier(n_estimators=2000, max_depth=18)
clf.fit(X, Y)
print clf.score(X, Y)
#print clf.coef_
print clf.feature_importances_ 
Yp=clf.predict(X)
#Ypp=clf.predict_proba(X)
#Yp=[]
#for i in xrange(len(Ypp)):
#    if Ypp[i][1]>TH: Yp.append(1)
#    else: Yp.append(0)
#for i in xrange(len(Yp)): print Yp[i]
print confusion_matrix(Y, Yp)
print classification_report(Y, Yp)
#for i in xrange(len(Yp)):
#    if Yp[i]!=Y[i] and Y[i]==1:
#        print LB[i], Y[i], X[i]

X=[]
LB=[]
# feat test
with open(sys.argv[2], 'rb') as f:
    for l in f:
        sl=l.strip().split(',')
        LB.append(sl[0])
        X.append(map(float, sl[4:]))

Yp=clf.predict(X)
print 'user_id,title_id'
for i in xrange(len(Yp)):
    print '%s,%s'%(LB[i], Yp[i])
