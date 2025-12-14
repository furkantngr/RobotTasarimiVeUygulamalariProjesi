🚗 Otonom Sürüş İçin VLM Tabanlı Karar Destek Mekanizması

(VLM-Based Decision Making Mechanism for Autonomous Driving)

"Algılayan araçlardan, düşünen ve anlayan araçlara..."

📋 Proje Özeti ve Kapsam

Bu proje, geleneksel otonom sürüş algoritmalarının (kural tabanlı veya uçtan uca kara kutu modelleri) yetersiz kaldığı karmaşık trafik senaryolarında, Büyük Dil Modelleri (LLM) ve Görme-Dil Modellerini (VLM) bir "Yüksek Seviyeli Karar Verici" (High-Level Decision Maker) olarak konumlandıran hibrit bir mimari sunmaktadır.

Projenin temel amacı, aracın sadece çevresel nesneleri algılamasını değil, olaylar arasında nedensel ilişkiler kurmasını (örneğin: "Top yola yuvarlandı -> Çocuk çıkabilir -> Yavaşla") sağlamaktır.

🏗 Mimari Yaklaşım: Sistem 1 ve Sistem 2

Bu projede, Nobel ödüllü Daniel Kahneman'ın "Hızlı ve Yavaş Düşünme" teorisi otonom sürüşe uyarlanmıştır:

🧠 Sistem 2 (VLM Ajanı - Yavaş Düşünme): Karmaşık ve belirsiz durumlarda devreye giren, stratejik kararlar alan ve muhakeme yeteneği olan katman. (Örn: "Agresif sürücüden kaçınmak için şerit değiştir.").

🛡️ Sistem 1 (Güvenlik Katmanı - Hızlı Düşünme): Deterministik, milisaniye hassasiyetinde çalışan ve VLM'in olası halüsinasyonlarını filtreleyen güvenlik bariyeri (Safety Guard/LLM-Hinted RL).

✨ Temel Özellikler

Zincirleme Düşünce (Chain-of-Thought - CoT): Model, "Fren yap" demeden önce neden fren yapması gerektiğini adım adım açıklar (Şeffaflık).

Halüsinasyon Filtresi: LLM'in ürettiği aksiyonlar, fiziksel kurallar ve sensör verileriyle (mesafe, hız) çapraz kontrolden geçirilir.

Senaryo Bazlı Simülasyon: Okul bölgesi, agresif sürücü ve otoyol senaryoları üzerinde karar mekanizması testi.

📂 Proje Yapısı

.
├── main.py                 # Simülasyonu başlatan ana dosya
├── config.py               # Model konfigürasyonları
├── requirements.txt        # Gerekli kütüphaneler
├── modules/
│   ├── perception.py       # (Mock) Sensör ve sahne verisi üretici
│   ├── vlm_agent.py        # Karar veren LLM/VLM Ajanı (Reasoning)
│   └── safety_guard.py     # Kararları denetleyen Güvenlik Katmanı
└── assets/
    └── architecture.png    # Mimari diyagram


🚀 Kurulum ve Çalıştırma

Repoyu klonlayın:

git clone [https://github.com/kullaniciadi/llm-autonomous-driving.git](https://github.com/kullaniciadi/llm-autonomous-driving.git)
cd llm-autonomous-driving


Gereksinimleri yükleyin:

pip install -r requirements.txt


Simülasyonu başlatın:

python main.py


🧪 Deneysel Senaryolar (Demo)

Bu repo, raporda belirtilen teorik riskleri analiz etmek için aşağıdaki senaryoları simüle eder:

Senaryo

VLM Tespiti (Sistem 2)

Güvenlik Müdahalesi (Sistem 1)

Sonuç

Okul Bölgesi

"Çocuk çıkabilir, riskli bölge."

Hız Sınırı Kontrolü (Max 30km/s)

✅ Güvenli Yavaşlama

Agresif Sürücü

"Arkada taciz eden araç var, yol ver."

Şerit Müsaitliği Kontrolü

✅ Şerit Değiştirme

Hatalı Karar (Test)

"Yol boş, hızlan." (Halüsinasyon)

Ön Engel Mesafe < 10m

🛑 ACİL FREN (Müdahale)

📚 Literatür ve Referanslar

Bu çalışma, aşağıdaki temel literatür üzerine inşa edilmiştir (Tam liste proje raporundadır):

GAIA-1: Otonom sürüş için üretken dünya modelleri.

DriveGPT: Sürüş davranışlarının tokenizasyonu ve tahmini.

DiLu Framework: Kapalı döngü öğrenme ve bellek yönetimi.

DriveAgent-R1: Aktif algı ve hibrit düşünme.

🔗 Katkı ve İletişim

Bu proje, [Ders Adı/Proje Adı] kapsamında geliştirilmiştir.

Geliştirici: [Adın Soyadın]

İletişim: [E-posta Adresin]

Not: Bu proje bir "Proof of Concept" (Kavram Kanıtı) çalışmasıdır ve gerçek araçlarda doğrudan kullanım için tasarlanmamıştır.
