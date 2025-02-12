Berikut adalah contoh Technical Report untuk proyek baru Anda (dengan nama proyek "Tax:red[Twelve]") menggunakan template yang telah Anda berikan:

---

# Technical Report: Tax:red[Twelve]

## 🔑 Keywords
**LangChain, Pinecone, OpenAI GPT, Streamlit, Web Scraping, CNN Indonesia, PPN 12 Persen, Retrieval-Augmented Generation (RAG), Conversational AI, Async Python**

---

## 1. Overview  
Proyek ini bertujuan untuk membangun sebuah sistem percakapan (chatbot) dan modul pengumpulan data berita yang fokus pada informasi terkait PPN 12 Persen. Sistem ini mengintegrasikan model bahasa OpenAI melalui LangChain, penyimpanan vektor menggunakan Pinecone, serta model embeddings multilingual (intfloat/multilingual-e5-large) dari HuggingFace.  
Selain fitur tanya jawab berbasis retrieval, proyek ini juga menyediakan modul web scraping yang mengambil artikel berita dari CNN Indonesia dengan tag “ppn-12-persen” dan menyimpan data (judul, konten, link, timestamp) ke dalam format CSV. Antarmuka pengguna dibangun menggunakan Streamlit dengan dukungan asynchronous agar pengalaman interaksi menjadi responsif dan efisien.

---

## 2. Motivation  
Banyak pihak yang membutuhkan informasi dan analisis terkini mengenai PPN 12 Persen, baik untuk keperluan perpajakan maupun riset pasar. Di sisi lain, terdapat kebutuhan untuk mengumpulkan data berita dari sumber terpercaya seperti CNN Indonesia guna memperoleh gambaran dan konteks perkembangan informasi seputar topik tersebut.  
Dengan menggabungkan teknologi conversational AI dan web scraping, sistem ini diharapkan dapat:
- Menyediakan jawaban yang relevan dan terpersonalisasi bagi pertanyaan seputar PPN 12 Persen.
- Mengumpulkan dan mengarsipkan berita terbaru sebagai basis data yang dapat digunakan untuk analisis lebih lanjut.
- Meningkatkan efisiensi dan kecepatan akses informasi bagi pengguna.

---

## 3. Success Metrics  
- **Kualitas Jawaban:**  
  - Jawaban yang diberikan chatbot harus relevan dan tepat sasaran apabila pertanyaan berkaitan dengan PPN 12 Persen.  
- **Waktu Respons:**  
  - Sistem harus mampu memberikan jawaban dalam waktu maksimal 3 detik untuk menjamin pengalaman pengguna yang responsif.
- **Akurasi Data Scraping:**  
  - Modul scraping harus dapat mengambil setidaknya 90% artikel yang tersedia per halaman dari CNN Indonesia dengan tag “ppn-12-persen”.
- **User Engagement:**  
  - Umpan balik positif dari pengguna terkait kemudahan penggunaan antarmuka dan relevansi informasi yang dihasilkan.

---

## 4. Requirements & Constraints  

### 4.1 Functional Requirements  
- **Conversational Retrieval Chain:**  
  - Sistem harus mengintegrasikan LangChain dengan Pinecone sebagai vectorstore serta OpenAI GPT sebagai model LLM.  
  - Penggunaan prompt template yang memastikan chatbot hanya menjawab pertanyaan jika terdapat konteks relevan mengenai PPN 12 Persen.
- **Antarmuka Pengguna:**  
  - Implementasi UI berbasis Streamlit yang mendukung input obrolan (chat) dan menampilkan riwayat percakapan secara real time.
- **Web Scraping:**  
  - Modul scraping menggunakan Selenium dan BeautifulSoup untuk mengambil data berita (judul, konten, link, timestamp) dari CNN Indonesia dengan query “ppn-12-persen”.  
  - Data yang dikumpulkan disimpan dalam format CSV untuk keperluan analisis dan referensi lebih lanjut.

### 4.2 Constraints  
- **Keterbatasan Data Index:**  
  - Pinecone index (“rag-ppn-12”) harus telah dibuat dan terisi dengan data relevan agar proses retrieval berjalan dengan baik.
- **Ketergantungan Eksternal:**  
  - Responsivitas sistem bergantung pada kestabilan API OpenAI, performa Pinecone, serta struktur halaman CNN Indonesia yang dapat berubah sewaktu-waktu.
- **Batasan Topik:**  
  - Sistem hanya akan memberikan jawaban jika pertanyaan berkaitan dengan topik PPN 12 Persen; untuk pertanyaan di luar topik, sistem akan merespons dengan pesan default.
- **Penggunaan Asynchronous:**  
  - Implementasi asynchronous diperlukan untuk menghindari blocking terutama pada proses chat dan scraping, sehingga memastikan pengalaman pengguna yang mulus.

### 4.3 In-Scope & Out-of-Scope  
**In-Scope:**  
- Pengembangan chatbot untuk pertanyaan seputar PPN 12 Persen dengan retrieval chain berbasis LangChain dan Pinecone.  
- Pembuatan modul web scraping untuk mengumpulkan berita terkait dari CNN Indonesia.  
- Integrasi antarmuka pengguna berbasis Streamlit yang mendukung asynchronous execution.

**Out-of-Scope:**  
- Penerjemahan otomatis berita atau konten yang telah di-scrape ke dalam bahasa lain.  
- Penanganan pertanyaan yang tidak berkaitan dengan topik PPN 12 Persen (ditangani dengan pesan default).

---

## 5. Methodology  

### 5.1 Problem Statement  
Proyek ini dirancang untuk menjawab kebutuhan akan sistem informasi terintegrasi yang dapat:  
- Menjawab pertanyaan secara real time terkait informasi PPN 12 Persen melalui chatbot.  
- Mengumpulkan berita terkini dari CNN Indonesia yang membahas topik PPN 12 Persen guna mendukung analisis data dan pembuatan laporan.

### 5.2 Data & Teknik  
- **Sumber Data:**  
  - Data percakapan dihasilkan oleh LLM OpenAI berdasarkan konteks yang diambil dari Pinecone vectorstore.  
  - Data berita dikumpulkan secara otomatis melalui teknik web scraping menggunakan Selenium dan BeautifulSoup.
- **Teknik Pemodelan:**  
  - **Prompt Engineering:**  
    - Menggunakan template yang menginstruksikan LLM untuk hanya memberikan jawaban jika terdapat konteks relevan, serta menolak menjawab pertanyaan di luar topik.  
  - **Retrieval-Augmented Generation (RAG):**  
    - Integrasi retrieval chain untuk mengambil informasi kontekstual sebelum menghasilkan jawaban.
- **Integrasi UI:**  
  - Penggunaan Streamlit untuk antarmuka pengguna yang interaktif, mendukung input chat dan streaming output secara asynchronous.
- **Pengembangan Web Scraping:**  
  - Menggunakan Selenium untuk memuat halaman web dan BeautifulSoup untuk mengekstrak data artikel secara sistematis.

### 5.3 Implementasi  
- **Inisialisasi Komponen:**  
  - Memuat variabel lingkungan untuk API key (Pinecone dan OpenAI).  
  - Inisialisasi Pinecone dengan index yang sudah dibuat dan penggunaan model embeddings dari HuggingFace.
- **Chatbot dan Retrieval Chain:**  
  - Pembuatan prompt template untuk memastikan chatbot hanya merespons jika terdapat informasi relevan.  
  - Implementasi fungsi asynchronous untuk memproses input pengguna dan menyimpan chat history.
- **Modul Web Scraping:**  
  - Penggunaan Selenium untuk mengakses halaman CNN Indonesia dengan tag “ppn-12-persen”.  
  - Ekstraksi konten artikel menggunakan BeautifulSoup dan penyimpanan data ke dalam CSV.
- **Integrasi UI dengan Streamlit:**  
  - Tampilan halaman utama dengan judul “Tax:red[Twelve]” dan komponen input chat.  
  - Penyajian output obrolan menggunakan fungsi streaming untuk respons real time.

---

## 6. Results and Analysis  

### 6.1 Pengujian Chatbot  
- **Akurasi Jawaban:**  
  - Uji coba awal menunjukkan bahwa chatbot memberikan jawaban yang relevan apabila pertanyaan berkaitan dengan PPN 12 Persen.  
  - Untuk pertanyaan di luar topik, sistem konsisten menampilkan pesan default: “Saya tidak memiliki informasi untuk menjawab pertanyaan ini.”
- **Waktu Respons:**  
  - Penggunaan asynchronous processing memastikan respons rata-rata berada di bawah 3 detik.
- **Analisis Chat History:**  
  - Riwayat percakapan tersimpan dengan baik dan dapat digunakan untuk evaluasi serta perbaikan lebih lanjut.

### 6.2 Evaluasi Modul Web Scraping  
- **Ketersediaan Data:**  
  - Modul scraping berhasil mengambil data dari 11 halaman (misalnya, page 1 hingga 11) dengan mengumpulkan judul, konten, link, dan timestamp.  
- **Kualitas Data:**  
  - Artikel yang di-scrape sebagian besar memuat konten yang lengkap; namun, beberapa halaman dapat mengalami perubahan struktur HTML yang mempengaruhi akurasi ekstraksi.
- **Kinerja:**  
  - Penggunaan Selenium disertai dengan wait time memastikan stabilitas, meskipun terdapat potensi penundaan apabila halaman web lambat dimuat.

### 6.3 Observasi Umum  
- Integrasi antara retrieval chain dan UI Streamlit telah berjalan dengan baik dan memberikan pengalaman interaktif bagi pengguna.  
- Kinerja web scraper cukup memadai, namun pemeliharaan berkala diperlukan untuk mengantisipasi perubahan struktur situs target.

---

## 7. Conclusion  
Proyek "Tax:red[Twelve]" berhasil mengintegrasikan dua komponen utama:  
1. Sebuah sistem conversational AI yang menggunakan LangChain, Pinecone, dan OpenAI GPT untuk memberikan jawaban seputar PPN 12 Persen secara real time.  
2. Modul web scraping yang mengumpulkan berita terkini dari CNN Indonesia terkait topik PPN 12 Persen dan mengarsipkannya dalam format CSV untuk analisis lebih lanjut.

Keberhasilan proyek ini ditandai dengan akurasi jawaban yang baik, waktu respons yang cepat, serta kemampuan untuk mengumpulkan data berita secara otomatis.  
Untuk pengembangan selanjutnya, beberapa saran perbaikan antara lain:
- Optimalisasi kualitas data dalam Pinecone vectorstore dengan memperbarui embedding secara berkala.
- Penguatan modul scraping agar lebih adaptif terhadap perubahan struktur situs.
- Penambahan fitur analitik atau dashboard untuk memvisualisasikan tren berita terkait PPN 12 Persen.

Dengan demikian, proyek ini tidak hanya memberikan solusi informasi berbasis chatbot tetapi juga mendukung kebutuhan analisis data berita secara komprehensif dalam konteks PPN 12 Persen.

---

Silakan ditinjau kembali dan disesuaikan dengan detail tambahan atau penyesuaian lain sesuai kebutuhan proyek Anda.
