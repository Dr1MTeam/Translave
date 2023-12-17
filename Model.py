import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os

class Model:
    def __init__(self, model_name, model_dir_name = "m_mT5", tokenizer_dir_name = "tok_mT5", cache_dir="cache"):
        cwd = os.path.dirname(os.path.abspath(__file__))
        self.models_dir = os.path.join(cwd, "models")
        self.cache_dir = os.path.join(self.models_dir, "cache")
        self.model_dir = os.path.join(self.models_dir, model_dir_name)
        self.tokenizer_dir = os.path.join(self.models_dir, tokenizer_dir_name)
        self.model_name = model_name

        # Пытаемся загрузить модель
        self.load_model()
        self.load_tekenizer()
        self.to_device()

    def load_model(self):
        try:
            # Пытаемся загрузить модель из локальной директории
            print('Loading from:', self.model_dir)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_dir, local_files_only=True)
        except OSError:
            print('Failed to load from:', self.model_dir)
            # Если произошло исключение (например, директории или файлов нет), загружаем по имени
            m_cache = os.path.join(self.cache_dir, "mcache")
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name, cache_dir=m_cache)
            self.model.save_pretrained(self.model_dir)
    def load_tekenizer(self):
        try:
            # Пытаемся загрузить модель из локальной директории
            print('Loading from:', self.tokenizer_dir)
            self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_dir, local_files_only=True, legacy=False)
        except OSError:
            print('Failed load from:', self.tokenizer_dir)
            #Если произошло исключение (например, директории или файлов нет), загружаем по имени
            t_cache = os.path.join(self.cache_dir, "tcache")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, cache_dir=t_cache, legacy=False)
            self.tokenizer.save_pretrained(self.tokenizer_dir)
    def to_device(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(self.device)
        print('Loaded on:', self.device.type)

    def encode_str(self, text, seq_len):
        # Tokenize,pad to max length and encode to ids
        # Returns tensor with tocken ids"""
        input_ids = self.tokenizer.encode(
            text=text,
            return_tensors = 'pt',
            padding = 'max_length',
            truncation = True,
            max_length = seq_len)
        return input_ids[0]
    def translate(self, mode, Sentence, variation=1):
        input_ids = self.encode_str(
        text = mode+' '+Sentence,
        seq_len = self.model.config.max_length)
        input_ids = input_ids.unsqueeze(0).cuda()
        output_tokens = self.model.generate(input_ids, num_beams=10, num_return_sequences=variation, length_penalty = 1, no_repeat_ngram_size=2)
        translated_Sentence = []
        for token_set in output_tokens:
            translated_Sentence.append(self.tokenizer.decode(token_set, skip_special_tokens=True))
            
        return translated_Sentence
    def close(self):
        self.model.close()
    
# Пример использования



def main():

    test = Model(model_name="Translave")
    mode = '<eng.rus>' # По идее из списка выбирается
    Sentence = ' this is test sentence'
    print(test.translate(mode, Sentence))

if __name__ == "__main__":
    main()