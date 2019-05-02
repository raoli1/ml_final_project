import pandas as pd
import sys
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
df=pd.read_csv(sys.argv[1])
df_target=pd.DataFrame(data=df["quidditch_league_player"])
df.drop(["quidditch_league_player"], axis=1,inplace=True)
X=df.values
Y=df_target.values
#VarianceThreshold
'''
selector_VarianceThreshold=VarianceThreshold(threshold=(.8 * (1 - .8)))
X_new=selector_VarianceThreshold.fit_transform(X)
'''
#Select K Best
X_new = SelectKBest(f_classif, k=20).fit_transform(X, Y)

df_new=pd.DataFrame(X_new)
df_new.insert(len(df_new.columns),"quidditch_league_player", df_target)
df_new.to_csv("select_k_best.csv",header=False,index=False)

