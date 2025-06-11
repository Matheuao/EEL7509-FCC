from transformers import BarkModel
import torch
from transformers import AutoProcessor
from IPython.display import Audio

class TTS():

    def __init__(self):
        
        self.model, self.processor, self.device = self.build_model()

    def build_model(self):
        model = BarkModel.from_pretrained("suno/bark-small")

        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
        
        processor = AutoProcessor.from_pretrained("suno/bark")

        return model, processor, device

    def run_inference(self, text):
        inputs = self.processor(text_prompt)
        speech_output = self.model.generate(**inputs.to(self.device))
        sampling_rate = self.model.generation_config.sample_rate

        return speech_output, sampling_rate

text_prompt = "Agora vamos tentar gerar fala, com o bark, um modelo de inteligência artificial"

obj = TTS()
audio, sr =obj.run_inference(text_prompt)
Audio(audio[0].cpu().numpy(), rate=sr)