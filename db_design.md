# Veritabanı Tasarımı (Database Design)

## 📌 Genel Yapı

Bu veritabanı, eğitim takibi sisteminde öğrenci, eğitim modülü ve performans bilgilerini kayıt altına almak amacıyla oluşturulmuştur. Temizlenmiş veri setindeki sütunlara dayanarak aşağıdaki tablolar oluşturulmuştur.

---

## 📊 Tablolar ve Açıklamaları

### 1. Students (Öğrenciler)
| Kolon Adı           | Veri Türü   | Açıklama                         |
|---------------------|-------------|----------------------------------|
| student_id          | INT         | Öğrenciye özel kimlik numarası  |
| gender              | VARCHAR(10) | Öğrencinin cinsiyeti            |
| nationality         | VARCHAR(50) | Uyruk bilgisi                    |
| place_of_birth      | VARCHAR(50) | Doğum yeri                       |

---

### 2. Education (Eğitim Bilgisi)
| Kolon Adı             | Veri Türü   | Açıklama                                      |
|-----------------------|-------------|-----------------------------------------------|
| education_id          | INT         | Eğitim kaydı kimliği                          |
| student_id            | INT         | Öğrenci kimliği (foreign key)                |
| educational_stage     | VARCHAR(50) | Eğitim aşaması (ör. Lise, Üniversite)         |
| class_grade           | INT         | Sınıf seviyesi                                |
| section_id            | VARCHAR(10) | Sınıf/seviye kodu                             |

---

### 3. Performance (Performans ve Davranış)
| Kolon Adı              | Veri Türü   | Açıklama                                      |
|------------------------|-------------|-----------------------------------------------|
| performance_id         | INT         | Performans kaydı ID                           |
| student_id             | INT         | Öğrenci kimliği (foreign key)                |
| raised_hands           | INT         | Derste el kaldırma sayısı                     |
| visited_resources      | INT         | Kaynak ziyaret sayısı                          |
| discussion             | INT         | Sınıf içi tartışma katılım sayısı             |
| parent_answering_survey| VARCHAR(10)| Veli anketine cevap verildi mi?              |
| student_absence_days   | VARCHAR(20)| Devamsızlık durumu                            |
| grade_level            | FLOAT       | Başarı seviyesi (not ortalaması)             |

---

## 🔁 İlişkiler
- `student_id`, tüm tablolarda birleştirici birincil anahtardır (foreign key olarak kullanılır).
- `Students`, `Education` ve `Performance` tabloları arasında bire çok (1:N) ilişkiler bulunmaktadır.

