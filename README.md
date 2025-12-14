# 🚗 Otonom Sürüş İçin Görme-Dil Modeli (VLM) Tabanlı Karar Mekanizması

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Ollama](https://img.shields.io/badge/Backend-Ollama-orange)
![Model](https://img.shields.io/badge/Model-LLaVA%20%2F%20BakLLaVA-green)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

## 📋 Proje Özeti
Bu proje, otonom araç teknolojilerinde **Yüksek Seviyeli Karar Verme (High-Level Decision Making)** katmanını simüle etmek amacıyla geliştirilmiş hibrit bir yapay zeka sistemidir.

Geleneksel "Modüler" sistemlerin esneklik sorunları ve "Uçtan Uca" (End-to-End) sistemlerin açıklanabilirlik (black-box) problemlerine çözüm olarak; **Görme-Dil Modellerinin (Vision-Language Models - VLM)** sağduyu ve muhakeme yeteneklerini kullanır. Proje, Daniel Kahneman'ın *"Hızlı ve Yavaş Düşünme"* teorisini otonom sürüşe uyarlayarak, VLM'i **"Sistem 2" (Bilişsel/Mantıksal)** karar verici olarak konumlandırır.

## 🚀 Temel Özellikler

* [cite_start]**Zincirleme Düşünce (Chain-of-Thought - CoT):** Model, sadece bir komut üretmez; karara varmadan önce *Algı -> Muhakeme -> Tahmin -> Planlama* adımlarını izler[cite: 106].
* **Açıklanabilir Yapay Zeka (XAI):** Her kararın nedenini ve mantıksal dayanağını (Rationale) raporlar. [cite_start]Kaza sonrası analizler için kritik önem taşır[cite: 202].
* **VLM Entegrasyonu:** Görsel veriyi analiz etmek için LLaVA (Large Language-and-Vision Assistant) modelini kullanır.
* **Otomatik Loglama:** Üretilen tüm kararlar ve analizler zaman damgasıyla `logs/` klasörüne kaydedilir.

## 🛠️ Mimari Yaklaşım

Proje, literatürdeki **DriveAgent-R1** ve **CoT4AD** mimarilerinden esinlenerek tasarlanmıştır.

1.  **Girdi:** Araç kamerasından alınan anlık trafik görüntüsü.
2.  **VLM Motoru (Beyin):** Görüntüyü işler ve anlamsal bağlamı (semantic context) çıkarır.
3.  **Prompt Mühendisliği:** Modelin halüsinasyon görmesini engellemek için yapılandırılmış CoT istemleri kullanılır.
4.  **Çıktı:** JSON formatında yapılandırılmış sürüş kararı (Örn: "Hızlan", "Yavaşla", "Dur").

---

## 📦 Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### 1. Gereksinimler
* Python 3.8 veya üzeri
* [Ollama](https://ollama.com/) (Yerel LLM sunucusu)

### 2. Kütüphanelerin Yüklenmesi
```bash
git clone [https://github.com/kullaniciadi/vlm-autonomous-decision.git](https://github.com/kullaniciadi/vlm-autonomous-decision.git)
cd vlm-autonomous-decision
pip install -r requirements.txt
```
### 3. Modelin İndirilmesi (Ollama)
Bu proje görsel yetenekleri için LLaVA modelini kullanır:
```bash
ollama pull llava
```
