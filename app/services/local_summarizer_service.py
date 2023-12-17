from transformers import MBartTokenizer, MBartForConditionalGeneration

from app.services.base_summarizer_service import BaseSummarizerService


class LocalSummarizerService(BaseSummarizerService):
    def __init__(self):
        # Подготовка модели и токенайзера
        model_name = "IlyaGusev/mbart_ru_sum_gazeta" # https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta
        self.tokenizer = MBartTokenizer.from_pretrained(model_name)
        self.model = MBartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text):
        # Конфигурирование токенайзера
        input_ids = self.tokenizer(
            [text],
            max_length=600,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )["input_ids"]

        output_ids = self.model.generate(
            input_ids=input_ids,
            no_repeat_ngram_size=4
        )[0]

        summary = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        return summary
