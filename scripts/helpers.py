import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class_freq_num = 25


def check_dataframe(dataframe):
    print("Number of Features : {0} \n Lenght of Dataframe {1}".format(dataframe.shape[1], dataframe.shape[0]))

    print("\nIs data frame has null value? : ", dataframe.isnull().any())

    print("\nHow many missing values are in which columns? :", "\n", dataframe.isnull().sum())

    cat_names = [col for col in dataframe.columns if dataframe[col].dtype == "O"]
    num_names = [col for col in dataframe.columns if dataframe[col].dtype != "O"]

    print("\nHow many columns are in the object type? : ", len(cat_names), "\n", cat_names)

    print("\nHow many columns are in the numerical type? : ", len(num_names), "\n", num_names)


def get_cat_and_num_cols(dataframe, number_of_unique_classes=class_freq_num):
    """
        -> Kategorik ve sayısal değişkenleri belirler.

        :param dataframe: İşlem yapılacak dataframe
        :param number_of_unique_classes: Değişkenlerin sınıflarının frekans sınırı
        :return: İlk değer olarak kategorik sınıfların adını, ikinci değer olarak sayısal değişkenlerin adını döndürür.

    """

    categorical_columns = [col for col in dataframe.columns
                           if len(dataframe[col].unique()) <= number_of_unique_classes]

    numeric_columns = [col for col in dataframe.columns if len(dataframe[col].unique()) > number_of_unique_classes
                       and dataframe[col].dtype != "O"]

    return categorical_columns, numeric_columns


def cats_summary(dataframe, categorical_cols):
    var_count = 0  # Kaç kategorik değişken olduğu raporlanacak

    for var in categorical_cols:
        print(pd.DataFrame({var: dataframe[var].value_counts(),
                            "Ratio (%)": 100 * dataframe[var].value_counts() / len(dataframe)}),
              end="\n\n\n")
        var_count += 1

    print('%d categorical variables have been described' % var_count, end="\n\n")
