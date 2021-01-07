# Hotel Bookings
**Analyze and Predict Reservation Cancellations**

![](https://media-cdn.tripadvisor.com/media/photo-o/04/ca/14/23/epic-sana-algarve-hotel.jpg)

Saat ingin berlibur atau terdapat keperluan ke luar kota. Seseorang akan melakukan pemesanan hotel. Hotel sendiri merupakan sebuah tempat yang dapat menampung seseorang untuk sementara waktu. Hotel sendiri terdapat di berbagai wilayah seperti tempat atau destinasi wisata atau pusat bisnis.    Bisnis hotel sendiri sangat menjanjikan terutama untuk wilayah destinasi wisata atau pusat kota, yang 
banyak orang bertujuan untuk berlibur atau memiliki urusan di kota tersebut. Namun dalam bisnis hotel terdapat 
juga berbagai tentangan seperti pembatalan pesanan atau kurang tertariknya atau minat seseorang untuk memesan di hotel tertentu.
Maka untuk meminimalisir adanya pembatalan, maka dapat menggunakan ke ilmuan Data Science untuk memprediksi pembatalan pemesanan,
untuk melakukan analisa dan prediksi pembatalan maka digunakan data historis pemesanan hotel. Project ini menggunakan data pemesanan
di negara Portugal.
<br>

## Problem
Dalam pemesanan hotel, pihak hotel ingin mendapatkan untung sebesar-besarnya dan rugi 
seminimal mungkin. Namun dalam praktiknya kerugian tidak dapat dihindarkan, salah satunya 
adalah dengan adanya pihak yang melakukan pembatalan hotel. Seperti keuntungan potensial yang 
harusnya didapat berkurang akibat ada pemesan yang membatalkan pemesanan, apalagi yang memesan dengan 
jumlah banyak atau kelompok.

## Goals
- Mampu memprediksi tamu yang akan melakukan pembatalan pesanan
- Melakukan strategi untuk mengurangi kerugian akibat dari pembatalan pesanan hotel
- Melakukan analisis mengenai kebiasaan pemesanan pelanggan

## Dataset
Cuplikan dataset
![dataset](https://i.ibb.co/RD7ZtZP/dataset.jpg)
Source : https://www.kaggle.com/jessemostipak/hotel-booking-demand

## Project Framework
> 1. Data Describe
>> - Define Problem
>> - Define Goals
>> - Data Collect and Import
>> - Data Description
> 2. Data Analysis
>> - Exploratory Data Analysis
>> - Data Visualization
> 3. Data Preprocessing
>> - Handling Missing Value
>> - Handling Ouliers
>> - Feature Engineering
> 4. Machine Learning
>> - Scaling
>> - Train Algorithm
>> - Train Algorithm with Hyper Param
>> - Model Evaluation
>> - Model Selection
> 5. Dashboard

## Model
Model yang digunakan adalah Random Forest yang sudah di lakukan hyper parameter tuning. Setelah dievaluasi didapatkan
> Best Threshold = 0.369182, G-Mean = 0.875

| Random Forest |  |
| --- | --- |
| AUC | 0.95 |
| Accuracy | 0.85 |
| Recall | 0.88 |

## Conclusion
- City Hotel lebih mahal dibandingkan dengan Resort Hotel
- Pemesanan cenderung menggunakan TA/TO serta banyak melalui internet atau online
- 67.15% pemesanan yang dibatalkan tidak menggunakan deposit (no deposit)
- Tiap bulan Agustus dan September terjadi lonjakan ADR dari jumlah total maupun reratanya
- 40.9% merupakan wisatawan lokal sedangkan lainnya merupakan manca negara
<hr>

## Dashboard

### Home
![home](https://i.ibb.co/kxQCJL5/home.jpg)

<br>

### Data Visualization
![visual](https://i.ibb.co/vP0MSdT/visual.jpg)

<br>

### Prediction
![pred](https://i.ibb.co/xGkKfWg/pred.jpg)

<hr>

### Source and References
- https://www.sciencedirect.com/science/article/pii/S2352340918315191
- https://www.kaggle.com/jessemostipak/hotel-booking-demand
- https://www.ezeeabsolute.com/blog/best-methods-to-increase-hotel-adr/?utm_source=KPIeBook&utm_medium=blog&utm_campaign=eABlog
- https://www.ezeeabsolute.com/blog/hotel-kpi/
- https://www.xotels.com/en/hotel-management/hotel-business-plan/


