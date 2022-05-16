import transformers
import torch as th
from transformers import T5Tokenizer, T5Model,T5ForConditionalGeneration,T5Config


def predictor(text):

            model = T5ForConditionalGeneration.from_pretrained('app/model')

            tokenizer = T5Tokenizer.from_pretrained("t5-small")
            #config = T5Config.from_pretrained("t5-small")
            tokenized_text = tokenizer(str(text),padding='max_length', max_length=127, truncation=True)
            source_ids = th.tensor([tokenized_text['input_ids']])
            source_mask = th.tensor([tokenized_text['attention_mask']])
            generated_ids = model.generate(
                    input_ids = source_ids,
                    attention_mask = source_mask, 
                    max_length=127,
                    num_beams=5,
                    repetition_penalty=1, 
                    length_penalty=1, 
                    early_stopping=True,
                    no_repeat_ngram_size=2
                )
            pred = tokenizer.decode(generated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
            return pred

text=" Khalistan flags were found tied on the main entrance gates and walls of Himachal Pradesh legislative assembly at Tapovan in Kangra district on Sunday. Slogans were also written on the walls of the assembly complex. The flags have now been removed by the administration. Assembly complex at Dharamshala is used only during winter session in December."
