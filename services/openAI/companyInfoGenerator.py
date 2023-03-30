from aihub.kernel import kernel
from db.firestore import add_document_to_firestore
from templates.company import Company
from templates.templates import get_template


def companyInfoGenerator(body,user):
    industries = body["industries"]
    print(','.join(industries))
    template = get_template(body["message"] ,"companyInfo",','.join(industries))
    response = kernel(template, user, 0.27)
    try:
        res = eval(response)
    except Exception as e:
        print(f"OpenAI provide information with wrong stucture, please retry\n {e}")
        return f"OpenAI provide information with wrong stucture, please retry\n {e}"
    company = Company(res)
    add_document_to_firestore(company, "Organizations")
    return company.__dict__