# src/prompt_manager.py

class PromptManager:
    @staticmethod
    def get_system_prompt():
        """
        Sistemin temel rolünü tanımlar.
        Rapordaki 'System 2' (Yavaş ve Mantıksal Düşünme) yapısını simüle eder.
        """
        return """
        Sen otonom bir araç için gelişmiş bir 'Sürüş Karar Asistanı'sın. 
        Görevin, sağlanan trafik görüntüsünü analiz etmek ve güvenli sürüş için stratejik kararlar üretmektir.
        Doğrudan direksiyonu kontrol etmiyorsun, ancak kontrol algoritmalarına (MPC/PID) üst düzey komutlar veriyorsun.
        """

    @staticmethod
    def get_cot_prompt():
        """
        Chain-of-Thought (CoT) yapısını zorunlu kılan prompt.
        Rapor referansı: Algı -> Muhakeme -> Tahmin -> Planlama
        """
        return """
        Lütfen aşağıdaki görüntüyü şu 4 aşamalı mantık zincirini (CoT) kullanarak analiz et:

        1. ALGI (Perception): Görüntüdeki kritik nesneleri (araçlar, yayalar, trafik ışıkları, şeritler) ve konumlarını listele.
        2. MUHAKEME (Reasoning): Bu nesnelerin mevcut durumu nedir? (Örn: Yaya yola bakıyor, araç fren lambalarını yaktı).
        3. TAHMİN (Prediction): Önümüzdeki 2-3 saniye içinde ne olması muhtemel? (Örn: Yaya yola atlayabilir).
        4. KARAR (Decision): Ego-araç ne yapmalı? (Hızlan, Yavaşla, Dur, Şerit Değiştir). Kararını net bir komutla bitir.
        
        Çıktıyı JSON formatında ver.
        """