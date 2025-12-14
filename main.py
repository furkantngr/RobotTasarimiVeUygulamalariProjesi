# main.py
import os
from src.vlm_engine import VLMEngine

def main():
    # 1. Motoru Başlat
    engine = VLMEngine(model_name="llava")
    
    # 2. Test Görselini Seç (Buraya 'assets' klasörüne koyduğun bir resmin adını yaz)
    image_path = "assets/test_image.jpg" 

    if not os.path.exists(image_path):
        print(f"❌ Hata: '{image_path}' bulunamadı. Lütfen assets klasörüne bir resim ekleyin.")
        return

    # 3. Analizi Gerçekleştir
    result = engine.analyze_scene(image_path)

    # 4. Sonucu Yazdır
    print("\n" + "="*50)
    print("🤖 OTONOM SÜRÜŞ KARAR MEKANİZMASI RAPORU")
    print("="*50)
    print(result)
    print("="*50)

if __name__ == "__main__":
    main()