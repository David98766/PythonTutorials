from Project_Start.model.Blog import Blog

class BlogDao:
    def __init__(self):
        self.blogs = [
            Blog(1, "My Day",
                 "Today I had a great day", "Adam"),
            Blog(2, "My Day Number 2",
                 "I had another great day", "Adam")
        ]
    def getAllBlogs(self):
        return self.blogs

    def getBlogByID(self, blogId):
        for blog in self.blogs:
            if blog.blogId == blogId:
                return blog
        return None
