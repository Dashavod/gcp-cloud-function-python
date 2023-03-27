
def get_template(company, type:str, industries=None):
    with open(f"templates/prompts/{type}.txt", "r") as f:
        template = f.read()
        new = template.replace('**your_company**', company)
        print("new", new)
    match(type):
        case "companyInfo":
            print("temp comp")
            return new.replace('**your_industries**', industries)
        case "emailTemplate":
            return new
    return template
