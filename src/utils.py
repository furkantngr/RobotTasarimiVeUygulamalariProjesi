# src/utils.py
import os
import datetime
from PIL import Image, ImageDraw, ImageFont

class Utils:
    @staticmethod
    def validate_image(image_path):
        """
        Dosya yolunun geçerli olup olmadığını kontrol eder.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Hata: '{image_path}' bulunamadı.")
        
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        ext = os.path.splitext(image_path)[1].lower()
        if ext not in valid_extensions:
            raise ValueError(f"Hata: Desteklenmeyen dosya formatı ({ext}). Sadece JPG ve PNG kullanın.")
        return True

    @staticmethod
    def save_log(result_text, image_name):
        """
        Modelin ürettiği kararı zaman damgasıyla bir metin dosyasına kaydeder.
        Bu, rapordaki 'Açıklanabilirlik' (Explainability) ilkesi için gereklidir.
        """
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"{log_dir}/decision_log_{timestamp}.txt"

        with open(log_filename, "w", encoding="utf-8") as f:
            f.write(f"--- OTONOM SÜRÜŞ KARAR GÜNLÜĞÜ ---\n")
            f.write(f"Tarih: {datetime.datetime.now()}\n")
            f.write(f"İncelenen Görsel: {image_name}\n")
            f.write("-" * 30 + "\n")
            f.write(result_text)
        
        print(f"✅ [Log] Karar raporu kaydedildi: {log_filename}")

    @staticmethod
    def visualize_result(image_path, decision_text):
        try:
            img = Image.open(image_path)
            draw = ImageDraw.Draw(img)
            
           
            try:
            
                font = ImageFont.truetype("arial.ttf", 20)
            except IOError:
                font = ImageFont.load_default()
                
                
            draw.text((10, 10), "AI ANALIZI TAMAMLANDI", fill="red", font=font)
            
            output_dir = "output"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            base_name = os.path.basename(image_path)
            save_path = os.path.join(output_dir, f"analyzed_{base_name}")
            img.save(save_path)
            print(f"🖼️ [Görsel] İşlenmiş görüntü kaydedildi: {save_path}")
            
        except Exception as e:
            print(f"⚠️ Görsel işleme hatası: {e}")