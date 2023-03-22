from aihub.kernel import kernel
from db.firestore import add_document_to_firestore
from services.openAI.companyInfoGenerator import companyInfoGenerator
from services.openAI.emailTextGenerator import emailTextGenerator
from templates.email import Email
from templates.templates import get_template


def openai_request(body, user, template = "company"):
    match(template):
        case "company":
            return companyInfoGenerator(body,user)
        case "email":
            return emailTextGenerator(body,user)
        case _:
            return{"error": "Incorrect type template, please change and try again"}
