from services.openAI.companyInfoGenerator import companyInfoGenerator
from services.openAI.emailTextGenerator import emailTextGenerator
from services.openAI.cosmoDescGenerator import CosmoDescGenerator


def openai_request(body, user):
    print(body["template"])
    match(body["template"]):
        case "company":
            return companyInfoGenerator(body,user)
        case "email":
            return emailTextGenerator(body,user)
        case "cosmoDesc":
            return CosmoDescGenerator(body,user)
        case _:
            return{"error": "Incorrect type template, please change and try again"}
