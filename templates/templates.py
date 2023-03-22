
def get_template(company,industries,type:str):
    with open(f"templates/prompts/{type}.txt", "r") as f:
        template = f.read()
    match(type):
        case "companyInfo":
            new  = template.replace('**your_company**', company)
            return new.replace('**your_industries**', industries)
        case "emailTemplate":
            return template
    return template
