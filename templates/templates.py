
def get_template(company, type:str, industries=None):
    with open(f"templates/prompts/{type}.txt", "r") as f:
        template = f.read()
    match(type):
        case "companyInfo":
            print("temp comp")
            new = template.replace('**your_company**', company)
            return new.replace('**your_industries**', industries)
        case "emailsTemplate":
            print("temp comp")
            return template.replace('**your_email**', company)
    return template
