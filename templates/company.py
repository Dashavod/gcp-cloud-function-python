template_basic = {
    "site": "youtube.com",
    "headline": "YouTube is a global video-sharing platform where users can watch, upload, and share videos.",
    "founded": 2005,
    "name": "Youtube",
    "country": "United States",
    "headquarters": "San Bruno, California",
    "region": [
        "Global"
    ],
    "industries": ["Finance","Insurance"],
    "company_type": "for profit",
    "technologies": [
        "AI",
        "Cloud",
        "Big Data"
    ],
    "mission": "Give everyone a voice and show them the world",
    "values": "Creativity, Community, and Responsibility",
    "revenue": "1500000",
    "number_of_employees": 150,
    "info": "YouTube is a global video-sharing platform where users can watch, upload, and share videos. Founded in 2005, the platform has grown to become one of the largest video-sharing websites in the world. YouTube offers a wide range of content, including music videos, educational videos, movie trailers, and more. The platform also allows users to create their own channels and upload their own videos. YouTube is committed to giving everyone a voice and showing them the world, and is focused on developing innovative solutions to meet the needs of its users. YouTube has been recognized for its commitment to creativity, community, and responsibility, and was named one of the world's most innovative companies."
}
class Company:
    def __init__(self, data=None):
        self.site = ""
        self.headline = ""
        self.founded = 0
        self.name = ""
        self.country = ""
        self.headquarters = ""
        self.region = []
        self.industries = ""
        self.company_type = ""
        self.technologies =[]
        self.mission = ""
        self.values = ""
        self.revenue = ""
        self.number_of_employees = 0
        self.info = ""
        if data: [setattr(self, key, data[key]) for key in data]
        print(f'Company {self.__dict__} created')
