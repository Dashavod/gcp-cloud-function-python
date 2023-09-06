
def get_template(company, type:str, industries=None):
    with open(f"templates/prompts/{type}.txt", "r") as f:
        template = f.read()
    match(type):
        case "companyInfo":
            new = template.replace('**your_company**', company)
            return new.replace('**your_industries**', industries)
        case "emailsTemplate":
            return template.replace('**your_email**', company)
        case "cosmoDesc":
            return template.replace('**your_question**', company)
    return template
