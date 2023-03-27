from aihub.kernel import kernel
from db.firestore import add_document_to_firestore
from templates.email import Email
from templates.templates import get_template


def emailTextGenerator(data,user):
    template = get_template(data["message"],type="emailsTemplate")
    response = kernel(template, user, 0.8,max_tokens=3634)
    print(response)
    # try:
    #     res = eval(response)
    # except Exception as e:
    #     print(f"OpenAI provide information with wrong stucture, please retry\n {e}")
    #     return f"OpenAI provide information with wrong stucture, please retry\n {e}"
    email = Email({
        "company_name":data["message"],
        "content": response,
        "email_type": "first welcome email"
    })
    add_document_to_firestore(email, "Emails")
    return email.__dict__