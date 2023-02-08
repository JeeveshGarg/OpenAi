# # !pip install -U spacy
# # !python -m spacy download en_core_web_sm

# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation as pun
# from heapq import nlargest
# stopwords = list(STOP_WORDS)
# nlp = spacy.load('en_core_web_sm')

# # with open('input_for_summary.txt') as f:
# #     text = f.read()


# # doc = nlp(text)
# def summmary_generator(text):
#     doc = nlp(text)
#     tokens = [token.text for token in doc]
#     # print(tokens)
#     punctuation = pun + '\n'
#     # punctuation
#     word_frequencies = {}
#     for word in doc:
#         if word.text.lower() not in stopwords:
#             if word.text.lower() not in punctuation:
#                 if word.text not in word_frequencies.keys():
#                     word_frequencies[word.text] = 1
#         else:
#             if word.text in word_frequencies:
#                 word_frequencies[word.text] += 1
#     # print(word_frequencies)

#     max_frequency = max(word_frequencies.values())
#     max_frequency
#     for word in word_frequencies.keys():
#         word_frequencies[word] = word_frequencies[word]/max_frequency
#     # print(word_frequencies)
#     sentence_tokens = [sent for sent in doc.sents]
#     # print(sentence_tokens)

#     sentence_scores = {}
#     for sent in sentence_tokens:
#         for word in sent:
#             if word.text.lower() in word_frequencies.keys():
#                 if sent not in sentence_scores.keys():
#                     sentence_scores[sent] = word_frequencies[word.text.lower()]
#                 else:
#                     sentence_scores[sent] += word_frequencies[word.text.lower()]
#     sentence_scores

    
#     select_length = int(len(sentence_tokens)*0.3)
#     select_length
#     summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
#     summary
#     final_summary = [word.text for word in summary]
#     summary = ' '.join(final_summary)
#     flashcards = summary.split(".") 
    
#     return summary,flashcards


# prompt = '''
#             Mahatma Gandhi was a great patriotic Indian, if not the greatest. He was a man of an unbelievably great personality. He certainly does not need anyone like me praising him. Furthermore, his efforts for Indian independence are unparalleled. Most noteworthy, there would have been a significant delay in independence without him. Consequently, the British because of his pressure left India in 1947. In this essay on Mahatma Gandhi, we will see his contribution and legacy.
#             First of all, Mahatma Gandhi was a notable public figure. His role in social and political reform was instrumental. Above all, he rid the society of these social evils. Hence, many oppressed people felt great relief because of his efforts. Gandhi became a famous international figure because of these efforts. Furthermore, he became the topic of discussion in many international media outlets.

# Mahatma Gandhi made significant contributions to environmental sustainability. Most noteworthy, he said that each person should consume according to his needs. The main question that he raised was “How much should a person consume?”. Gandhi certainly put forward this question.

# Furthermore, this model of sustainability by Gandhi holds huge relevance in current India. This is because currently, India has a very high population. There has been the promotion of renewable energy and small-scale irrigation systems. This was due to Gandhiji’s campaigns against excessive industrial development.

# Mahatma Gandhi’s philosophy of non-violence is probably his most important contribution. This philosophy of non-violence is known as Ahimsa. Most noteworthy, Gandhiji’s aim was to seek independence without violence. He decided to quit the Non-cooperation movement after the Chauri-Chaura incident. This was due to the violence at the Chauri Chaura incident. Consequently, many became upset at this decision. However, Gandhi was relentless in his philosophy of Ahimsa.

# Secularism is yet another contribution of Gandhi. His belief was that no religion should have a monopoly on the truth. Mahatma Gandhi certainly encouraged friendship between different religions.
# Legacy of Mahatma Gandhi
# Mahatma Gandhi has influenced many international leaders around the world. His struggle certainly became an inspiration for leaders. Such leaders are Martin Luther King Jr., James Beve, and James Lawson. Furthermore, Gandhi influenced Nelson Mandela for his freedom struggle. Also, Lanza del Vasto came to India to live with Gandhi.
# The United Nations has greatly honored Mahatma Gandhi. UN has made 2nd October as “the International Day of Nonviolence.” Furthermore, many countries observe 30th January as School Day of Nonviolence and Peace.

# The awards given to Mahatma Gandhi are too many to discuss. Probably only a few nations remain which have not awarded Mahatma Gandhi.

# In conclusion, Mahatma Gandhi was one of the greatest political icons ever. Most noteworthy, Indians revere by describing him as the “father of the nation”. His name will certainly remain immortal for all generations.
#         '''

# print(summmary_generator(prompt))

# # with open("summary_text.txt", "w") as file:
# #     file.write(summary)

import nltk
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import re
def summmary_generator(text):
    cnt = text.count('.')
    bad_chars = ['!', "*", "@","#","$","%","/"]
    filtered_string = ''.join(map(lambda x: x if x not in bad_chars else '', text))
    filtered_string.replace("  ", " ")
    # print(filtered_string)
    parser = PlaintextParser.from_string(filtered_string, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    line = 0
    if(cnt<3):
        line = cnt
    elif(cnt<5):
        line = cnt/2
    elif(cnt<10):
        line = cnt/3
    else:
        line = cnt/4
        
    summary = summarizer(parser.document, line)
    dp = []
    for i in summary:
        lp = str(i) 
        dp.append(lp)
    final_sentence = ' '.join(dp)
    flashcards = final_sentence.split(".")
    flashcards = flashcards[:-1]
    flash = []
    for f in flashcards:
        flash.append(f.replace("\n", ""))
    summary = final_sentence
    
    return summary,flash