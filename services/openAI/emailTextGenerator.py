from aihub.kernel import kernel
from db.firestore import add_document_to_firestore
from templates.email import Email
from templates.templates import get_template


def emailTextGenerator(data,user):
    template = get_template(data, "emailTemplate")
    response = kernel(template, user, 0.27)
    try:
        res = eval(response)
    except Exception as e:
        print(f"OpenAI provide information with wrong stucture, please retry\n {e}")
        return f"OpenAI provide information with wrong stucture, please retry\n {e}"
    email = Email(res)
    add_document_to_firestore(email, "Emails")
    return email