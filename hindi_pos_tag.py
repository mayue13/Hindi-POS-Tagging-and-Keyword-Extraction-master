from nltk.tag import tnt
from nltk.corpus import indian
import nltk
#download(nltk)

def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

text1 = "इराक के विदेश मंत्री ने अमरीका के उस प्रस्ताव का मजाक उड़ाया है , जिसमें अमरीका ने संयुक्त राष्ट्र के प्रतिबंधों को इराकी नागरिकों के लिए कम हानिकारक बनाने के लिए कहा है ।"
text="प्रेम के अनेक रूप हैं। उन में सबसे श्रेष्ठ देश प्रेम है। वो भूमि जहॉ हमारा जन्म होता है। जिसकी गोद में पलकर हम बड़े होते हैं।"
model = hindi_model()
new_tagged = (model.tag(nltk.word_tokenize(text)))
print(new_tagged)

with open("result/output.txt","a",encoding='utf-8') as output_file:
    output_file.write("\n[INPUT]\n")
    output_file.write(text)
    output_file.write("\n[OUTPUT]\n")
    output_file.write(str(new_tagged))
