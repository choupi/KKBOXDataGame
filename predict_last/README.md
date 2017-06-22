### gen_feat2_last.py
Generate features for predict if the user continue to watch last video
> # userid, continueLast, nextVideo, lastVideo, lastWatchTime/totalWatchTime, lastWatchTime, lastWatchTime/averageWatchTime, lastWatchCount/averageWatchCount, trainEndTS-lastWatchTS, lastWatchTSInterval, userCount, averageWatchTime, averageWatchCount
> 00058293,0,00000251,00000495,0.0403225806452,5,0.000231145335093,0.162704804673,21600,3600,859.0,21631.412107,12.2922,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
> 00097263,1,00000110,00000110,0.000103460762506,4,0.000198649352303,0.0787571801937,1940400,0,21533.0,20135.983096,12.697255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

### tr_last.py
predict if the user continue to watch last video

> 0.7993162887
> [ 0.2169829   0.07557875  0.05802927  0.0370475   0.35711346  0.07511886
>   0.04651444  0.06384661  0.06976822]
> [[13045 31986]
>  [  196 17080]]
>              precision    recall  f1-score   support
> 
>           0       0.99      0.29      0.45     45031
>           1       0.35      0.99      0.51     17276
> 
> avg / total       0.81      0.48      0.47     62307

> $ cat t_feat2_last.csv |awk -F, '{print $2}'|sort|uniq -c|sort -nr|head
>    8615 00000029
>    3705 00000669
>    2597 00000391
>    2556 00000110
>    1714 00000389
>    1540 00000482
>    1415 00000670
>    1127 00000251
>     938 00000664
>     798 00000087

