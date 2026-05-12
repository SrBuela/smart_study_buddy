from beanie import Document


class Note(Document):

    title: str
    content: str
    owner_email: str