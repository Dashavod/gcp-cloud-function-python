from services.openAI.companyInfoGenerator import companyInfoGenerator
from services.openAI.emailTextGenerator import emailTextGenerator



def openai_request(body, user):
    print(body["template"])
    match(body["template"]):
        case "company":
            return companyInfoGenerator(body,user)
        case "email":
            return emailTextGenerator(body,user)
        case _:
            return{"error": "Incorrect type template, please change and try again"}
