import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('test.csv')

plt.subplots(figsize=(12,13))
plt.xticks(rotation='90')
sns.barplot(x=name,y=value)

misisng_column = (df.isna().sum()/df.shape[0]).sort_values(ascending=False)
missing_column_name = misisng_column[misisng_column>0].index
#'''
#According to data discription,N/A in 
#'PoolQC': no pool
#'MiscFeature': no Miscellaneous feature not covered in other categories
#'Alley': no Alley access
#'Fence': no fence
#'FireplaceQu':No Fireplace
#'LotFrontage', minimum is 21, I guess the data is really missing, not 0
#####df['LotFrontage'].min()
#'GarageCond':No Garage
#'GarageQual':No Garage
#'GarageYrBlt':no Garage
#####df[df['GarageYrBlt'].isna() | ( df['GarageQual'].isna()) | df['GarageYrBlt'].isna()][df['GarageYrBlt'].notna() | ( df['GarageQual'].notna()) | df['GarageYrBlt'].notna()]
#'GarageFinish':no Garage
#'GarageType':No garage
#'BsmtCond': no basement
#'BsmtQual'no basement
#'BsmtExposure':no basement
#'BsmtFinType1':no basement
#'BsmtFinType2'no basement
#'MasVnrType'：no Masonry veneer
#'MasVnrArea': no Masonry veneer
#'MSZoning': missing
#'BsmtHalfBath': missing, because there are 2 N/A, but the rest are 0:1364,1:91, 2:2 and doesn't agree with the number of no basement
#'Utilities': missing, because there are 2N/A, the rest are all 'AllPub'        
#'Functional':missing, 
#'BsmtFullBath':missing
#'BsmtFinSF2':missing        #df['BsmtFinSF2'].value_counts().sum()
#'BsmtFinSF1':missing
#'Exterior1st':missing
#'Exterior2nd':missing
#'BsmtUnfSF':missing
#'TotalBsmtSF':missing
#'SaleType':missing
#'GarageArea':missing
#'GarageCars':missing 
#'''

#'''
#Accoring to the previous, ['MSZoning', 'BsmtHalfBath', 'Utilities','Functional', 'BsmtFullBath', 'BsmtFinSF2', 'BsmtFinSF1', 'Exterior2nd','BsmtUnfSF', 'TotalBsmtSF', 'SaleType', 'Exterior1st', 'KitchenQual','GarageArea', 'GarageCars'], may have missing data
#But, there are 4 missing in 'MSZoning', and all the other properties missed at most two values, and all in same two data, we can dump those two.
#'''

for i in sorted(['BsmtHalfBath', 'Utilities','Functional', 'BsmtFullBath', 'BsmtFinSF2', 'BsmtFinSF1', 'Exterior2nd','BsmtUnfSF', 'TotalBsmtSF', 'SaleType', 'Exterior1st', 'KitchenQual','GarageArea', 'GarageCars']):
    print(i,': ',list(df[df[i].isna()].index))
#'''#660 data appears 6 times, and all in basement related items. We can drop it.'''
df = df.drop(660)
#'''the other data with missing value in it, appear at most 2 times, not need to drop it, we can fill it with other values.'''

#'''for numerice missing, we can fill with medium, and for object data, we can fill with the most data 
