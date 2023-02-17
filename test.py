# import json
# import os
#
# from googletrans import Translator
# from dialogflow import detect_intent_texts
from jsonToStorage import jsonToStore
from kernel import kernel

# with open('train.txt') as f:
#     lines = f.readlines()
# print(lines)
# translator = Translator()
# translated = {translator.translate(phrase, dest="uk") for phrase in lines}
# print([item.text for item in translated])
# [detect_intent_texts("uk-devtorium-q-a-alek","scr5", {item.text}, "uk") for item in translated]
# for str in translated:
#     detect_intent_texts("uk-devtorium-q-a-alek", "scr", {str}, "ua")
#detect_intent_texts("devtorium-bot-e9vy", "scr", translated, "en")
template = {
 "site": "norda.se",
 "headline": "Nordea is a leading Nordic financial services group providing banking, insurance, asset management, and other financial services.",
 "Founded": 182,
 "Headquarters": "Stockholm, Sweden",
 "Region": [
  "Europe",
  "Nordic"
 ],
 "Industries": [
  "Banking",
  "Insurance",
  "Asset Management",
  "Financial Services"
 ],
 "Company type": "for profit",
 "Technologies": [
  "AI",
  "Cloud",
  "Big Data"
 ],
 "Mission": "Provide customers with financial security and peace of mind",
 "Values": "Integrity, Innovation, and Inclusiveness",
 "Revenue": "SEK 517 billion",
 "Number of employees": "33,000",
 "Info": "Nordea is a leading Nordic financial services group providing banking, insurance, asset management, and other financial services. Founded in 1820, the company has grown to become one of the largest financial services groups in the region. Nordea offers a wide range of products and services, including retail banking, corporate banking, private banking, asset management, insurance, and investment banking. The company also provides advice and guidance to customers. Nordea is committed to providing customers with financial security and peace of mind, and is focused on developing innovative solutions to meet the needs of its customers. Nordea has been recognized for its commitment to sustainability, and was named one of the world's most sustainable companies"}
company = "www.skandia.se"
response = kernel(f"{template} \n provide information about {company} in the same format as above", "123456", 0.27)
print(response.replace("\n"," "))
res =eval(response)
url = jsonToStore(res)
print(url)
print(res)