from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy.stats import shapiro
from scipy.stats import levene
from scipy.stats import bartlett
from scipy.stats import ttest_ind
from pandas import DataFrame
from statsmodels.sandbox.stats.multicomp import MultiComparison
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def my_shapiro(df, yname):
    x = list(df.columns)
    x.remove(yname)
    
    for i in x:
        for u in df[i].unique():
            s = shapiro(df[yname][df[i]==u])
            print("%s:%s" % (i, u), end=" ")
            print(s)
            print("=" * 35)
            print("%s:%s 수준의 검정통계량: %0.2f, p-value: %0.2f" 
                    % (i, u, s.statistic, s.pvalue))
            print("-" * 35)
            if s.pvalue > 0.05:
                print("[O] 정규성을 충족함")
            else:
                print("[X] 정규성을 충족하지 않음")
            print("-" * 35)
            print()
            
def my_hmvar(df, yname):
    x = list(df.columns)
    x.remove(yname)
    
    params = []
    for i in x:
        u = list(df[i].unique())
        
        for j in u:
            params.append(df[yname][df[i] == j])
        
        lev = levene(*params)
        print("%s:%s" % (yname, i), end=" ")
        print(lev)
        print("=" * 35)
        print("%s:%s Levene 검증에 의한 등분산성 확인: %0.3f, p-value: %0.3f" 
                    % (yname, i, lev.statistic, lev.pvalue))
        print("-" * 35)
        
        if lev.pvalue > 0.05:
            print("[O] 등분산성을 충족함")
        else:
            print("[X] 등분산성을 충족하지 않음")
        print("-" * 35)
        print()
        
        lev = bartlett(*params)
        print("%s:%s" % (yname, i), end=" ")
        print(lev)
        print("=" * 35)
        print("%s:%s Bartlett 검증에 의한 등분산성 확인: %0.3f, p-value: %0.3f" 
                    % (yname, i, lev.statistic, lev.pvalue))
        print("-" * 35)
        
        if lev.pvalue > 0.05:
            print("[O] 등분산성을 충족함")
        else:
            print("[X] 등분산성을 충족하지 않음")
        print("-" * 35)
        print()

def my_group_count(df, yname):
    x = list(df.columns)
    x.remove(yname)
    x1 = x[:]
    x.append(x1)
    
    for i in x:
        tmp = df.groupby(i).count()
        tmp_values = tmp[tmp.columns[-1]].unique()
        print('group by', i)
        print("=" * 35)
        print(tmp)
        print("-" * 35)
        
        if len(tmp_values) > 1:
            print("[X] 집단별 표본수 상이")
        else:
            print("[O] 집단별 표본수 동일")
                
        print()
        
def my_tukey_hsd(df, yname):
    x = list(df.columns)
    x.remove(yname)

    for i in range(0, len(x)):
        for name, gdf in df.groupby(x[i]):
            j = (i + 1) % len(x)
            print('{0}:{1}'.format(x[i], name), pairwise_tukeyhsd(gdf[yname], gdf[x[j]]))
            print()
            
def my_bonferroni(df, yname):
    x = list(df.columns)
    x.remove(yname)

    for i in range(0, len(x)):
        for name, gdf in df.groupby(x[i]):
            j = (i + 1) % len(x)
            comp = MultiComparison(df[yname], df[x[j]])
            result = comp.allpairtest(ttest_ind)
            print('{0}:{1}'.format(x[i], name), result[0])
            print()