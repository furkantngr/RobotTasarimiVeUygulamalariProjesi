# src/vlm_engine.py
import ollama
from .prompt_manager import PromptManager

class VLMEngine:
    def __init__(self, model_name="llava"):
        self.model = model_name
        self.prompt_manager = PromptManager()

    def analyze_scene(self, image_path):
        """
        Görüntüyü alır ve VLM modeline gönderir.
        """
        print(f"🔄 [Sistem] Görüntü işleniyor: {image_path}...")
        print(f"🧠 [Sistem] '{self.model}' modeli ile mantıksal analiz (CoT) başlatılıyor...")

        try:
            # Ollama Python kütüphanesi ile görüntüyü ve promptu gönderiyoruz
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        'role': 'system',
                        'content': self.prompt_manager.get_system_prompt(),
                    },
                    {
                        'role': 'user',
                        'content': self.prompt_manager.get_cot_prompt(),
                        'images': [image_path]
                    }
                ]
            )
            return response['message']['content']

        except Exception as e:
            return f"Hata oluştu: {str(e)}"