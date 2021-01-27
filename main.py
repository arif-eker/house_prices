#
#
#

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scripts.helpers as hlp

pd.set_option('display.max_rows', 10)
pd.pandas.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: '%.3f' % x)

# train ve test setlerinin bir araya getirilmesi.
train = pd.read_csv("datasets/house_price_train.csv")

test = pd.read_csv("datasets/house_price_test.csv")

# Veriyi birleştiriyoruz.
# Çünkü trainde yapacağımız işlemler testte de aynı anda olsun ki ileride birleştirmede büyük sıkıntılar yaşamayalım.
# Daha sonra ikisi tekrardan ayrılacak.

df_merge = pd.concat([train, test], ignore_index=True)

df = df_merge.copy()

hlp.check_dataframe(df)
df.drop("Id", axis=1, inplace=True)
cat_cols, num_cols = hlp.get_cat_and_num_cols(df)

hlp.cats_summary(df, cat_cols)
