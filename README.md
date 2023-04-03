# Big-Data
Tugas - Reynaldi Fakhri Pratama

## Chapter 3
Deep Dive Into Apache Spark

### Python
**1. Acccumulator (kode 1)**
<table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Acccumulator/Accumulator.py#L1-L4 </td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/d93010843196ea7f1f110b6fe0c06a02680159e3/Acccumulator/Accumulator.png"></td>
 </tr>
 <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. Sc =>  variabel yang merujuk pada objek SparkContext 
      </p>
      <p>
         2. Parallelize => fungsi dalam SparkContext yang   digunakan untuk membuat RDD (Resilient Distributed Datasets) dari koleksi 
      </p>
      <p>
      3. Accumulator => merupakan variabel yang dapat diakumulasikan, yaitu memiliki operasi “+” yang komutatif dan asosiatif. 
      </p>
      <p>
       4. Lambda => merupakan kata kunci yang digunakan untuk membuat fungsi anonim. Fungsi ini adalah fungsi satu baris kecil yang tidak memiliki nama.
      </p>
      <p>
          5. Value => nilai dari context
      </p>
   </td>
 </tr>
</table>
<b>2. BroadCast (kode 2)</b>
<table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/BroadCast/BroadCast.py#L1-L2</td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/BroadCast/Broadcast.png"></td>
 </tr>
 <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. Broadcast =>  fungsi yang dapat digunakan untuk menunjukkan bahwa dataset cukup kecil dan harus disiarkan. Ini berarti bahwa dataset akan dikirim ke setiap node dalam cluster hanya sekali, daripada mengirimkan salinan dengan tugas. Ini dapat membantu mengurangi biaya komunikasi dan meningkatkan kinerja.
      </p>
      <p>
         2. List => digunakan untuk membuat objek daftar, yang merupakan koleksi item yang terurut.
      </p>
      <p>
         3. Range => digunakan untuk menghasilkan urutan angka.
      </p>
   </td>
 </tr>
</table>
<b>3. Log Analytics (kode 3)</b>
<table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Log%20Analytics/LogAnalytics.py#L1-L14 </td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Log%20Analytics/LogAnalytics.png"></td>
 </tr>
 <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. TextFile =>  fungsi yang digunakan untuk membaca file teks dan mengembalikan RDD yang mewakili data dalam file tersebut
      </p>
      <p>
         2. Filter => fungsi transformasi yang digunakan untuk mengembalikan RDD baru dengan subset data yang memenuhi kondisi tertentu
      </p>
      <p>
      3. Cache => fungsi transformasi yang dapat digunakan pada DataFrame, Dataset, atau RDD ketika Anda ingin melakukan lebih dari satu tindakan.  
      </p>
      <p>
       4. Count => fungsi aksi yang digunakan untuk menghitung jumlah baris dalam DataFrame, Dataset, atau RDD.
      </p>
   </td>
 </tr>
</table>
<b>4. Pair RDD (kode 4)</b>
    <table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Pair%20RDD/PairRDD.py#L1-L11 </td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Pair%20RDD/PairRDD.png"></td>
 </tr>
 <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. map => mengubah setiap elemen RDD menjadi elemen baru dengan menerapkan fungsi pada elemen tersebut
      </p>
      <p>
         2. collect => mengembalikan semua elemen RDD sebagai daftar ke driver
      </p>
      <p>
         3. len => mengembalikan panjang objek yang dapat diukur, seperti daftar atau string
      </p>
      <p>
         4. keys => mengembalikan daftar kunci dari kolom MapType di spark
      </p>
      <p>
         4. values => mengembalikan daftar nilai dari kolom MapType di spark
      </p>
   </td>
 </tr>
</table>
<b>5. Understanding RDDs (kode 5)</b>
    <table border="0">
 <tr>
    <td><b style="font-size:30px" width="20%">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Understanding%20RDDs/UnderstandingRDDs.py#L1-L40 </td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Understanding%20RDDs/UnderstandingRDDs.png"></td>
 </tr>
 <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. defaultParallelism => digunakan untuk mendapatkan jumlah partisi yang digunakan oleh spark
      </p>
      <p>
         2. getNumPartitions => digunakan untuk mendapatkan jumlah partisi dari RDD
      </p>
      <p>
         3. mapPartitionsWithIndex => digunakan untuk mengubah setiap partisi RDD menjadi elemen baru dengan menerapkan fungsi pada partisi tersebut
      </p>
      <p>
         4. repartition => digunakan untuk mengubah jumlah partisi RDD
      </p>
      <p>
         5. coalesce => digunakan untuk mengubah jumlah partisi RDD dengan mempertahankan jumlah partisi yang ada
      </p>
      <p>
         6. toDebugString => digunakan untuk mendapatkan informasi tentang RDD
      </p>
   </td>
 </tr>
</table>
<b>6. Word Count (kode 6)</b>
    <table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Word%20Count/WordCount.py#L1-L8 </td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/Word%20Count/Word%20Count.png"></td>
 </tr>
 <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <!-- jelaskan mengenai flatMap, reduceByKey, split -->
      <p>
         1. flatMap => digunakan untuk mengubah setiap elemen RDD menjadi elemen baru dengan menerapkan fungsi pada elemen tersebut
      </p>
      <p>
         2. reduceByKey => digunakan untuk menggabungkan semua elemen RDD dengan fungsi yang sama dengan kunci yang sama
      </p>
      <p>
         3. split => digunakan untuk memecah string menjadi daftar string
      </p>
   </td>
 </tr>
</table>

### Scala

**1. System Commands Output**
<table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/System%20Commands%20Output/SystemCommandsOutput.scala#L1-L3</td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/System%20Commands%20Output/SystemCommandsOutput.png"></td>
 </tr>
 <!-- <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. Sc =>  variabel yang merujuk pada objek SparkContext 
      </p>
      <p>
         2. Parallelize => fungsi dalam SparkContext yang   digunakan untuk membuat RDD (Resilient Distributed Datasets) dari koleksi 
      </p>
      <p>
      3. Accumulator => merupakan variabel yang dapat diakumulasikan, yaitu memiliki operasi “+” yang komutatif dan asosiatif. 
      </p>
      <p>
       4. Lambda => merupakan kata kunci yang digunakan untuk membuat fungsi anonim. Fungsi ini adalah fungsi satu baris kecil yang tidak memiliki nama.
      </p>
      <p>
          5. Value => nilai dari context
      </p>
   </td>
 </tr> -->
</table><br>

**2. System Commands ReturnCode**
<table border="0">
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/System%20Commands%20ReturnCode/SystemCommandsReturnCode.scala#L1-L3 </td>
    <td><img alt="Dark" src="https://github.com/renaldi-oss/big-data/blob/148578888a4bef43d8c0d8c23929cc22e5108477/System%20Commands%20ReturnCode/SystemCommandsReturnCode.png"></td>
 </tr>
 <!-- <tr>
   <td colspan="2">
      <b style="font-size:30px">Penjelasan</b>
      <p>
         1. sys.process adalah perintah untuk mengimpor modul sys.process dari Scala. Module ini digunakan untuk menjalankan dan mengontrol proses eksternal dari program
      </p>
   </td>
 </tr> -->
</table>
