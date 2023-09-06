from aihub.kernel import kernel
from db.firestore import add_document_to_firestore
from templates.company import Company
from templates.templates import get_template


def CosmoDescGenerator(body,user):
    template = get_template(body["message"] ,"cosmoDesc")
    response = kernel(template, user, 0.27)

    return {"message": response}