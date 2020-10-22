class Post:
    def __init__(self, title, content, publication_time, creation_time, image, publish_status, approve_status, user_id, category_id):
        self.title = title
        self.content = content
        self.publication_time = publication_time
        self.creation_time = creation_time
        self.image = image
        self.publish_status = publish_status
        self.approve_status = approve_status
        self.user_id = user_id
        self.category_id = category_id