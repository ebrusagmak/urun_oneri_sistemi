import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df=pd.read_excel('alisveris_sepeti.xlsx')
veriler=df.values.tolist()

veriler = [satir[0].split(",") for satir in veriler]
# print(veriler)

te=TransactionEncoder()
veri_encoded=te.fit_transform(veriler)
# print(veri_encoded)

dataframe=pd.DataFrame(veri_encoded,columns=te.columns_)
# print(dataframe)

fazla_kullanılan_ürünler=apriori(dataframe,min_support=0.03,use_colnames=True)

# print(fazla_kullanılan_ürünler)

birlikte_kullanilma=association_rules(fazla_kullanılan_ürünler,metric='lift',min_threshold=1)


def urun_oner(sepet_urunu, kurallar, top_n=3):
    ilgili_kurallar = kurallar[kurallar['antecedents'].apply(lambda x: sepet_urunu in x)]
    siralanmis = ilgili_kurallar.sort_values('lift', ascending=False)
    onerilen_urunler = []
    for _, row in siralanmis.iterrows():
        for urun in row['consequents']:
            if urun != sepet_urunu and urun not in onerilen_urunler:
                onerilen_urunler.append(urun)
        if len(onerilen_urunler) >= top_n:
            break
    return onerilen_urunler[:top_n]

print(urun_oner('chocolate', birlikte_kullanilma, top_n=5))