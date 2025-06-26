# 🛒 Ürün Öneri Sistemi (Market Sepeti Analizi)

Bu projede, kullanıcıların alışveriş sepeti verilerini analiz ederek, birlikte en sık alınan ürünleri tespit eden ve **ürün önerisi** sunan basit bir sistem geliştirdim.  
Veriler Excel dosyasından alınmıştır ve analiz süreci Python kullanılarak yürütülmüştür.

## 🚀 Kullanılan Teknolojiler

- Python 🐍
- pandas
- mlxtend (Apriori ve Association Rules)


## 📊 Nasıl Çalışır?

1. Excel formatındaki alışveriş verileri içeri aktarılır.
2. Veriler, sepetteki ürünler listesi haline dönüştürülür.
3. `TransactionEncoder` ile veriler binary forma çevrilir.
4. `apriori` algoritması ile sık kullanılan ürün kombinasyonları çıkarılır.
5. `association_rules` ile ürünler arasındaki ilişki kuralları oluşturulur.
6. Kullanıcının girdiği ürüne göre, en yüksek lift değerine sahip olan ürünler önerilir.

## 🧠 Örnek Kullanım

```python
print(urun_oner('milk', birlikte_kullanilma, top_n=5))
