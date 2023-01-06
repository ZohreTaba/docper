from src.init import create_app

app = create_app()







# @app.get('/blog')
# def index(limit=10, published: bool = True):
#     #only get 10 published blog
#     if published:
#         return {'data': f'{limit} published blog from database' }
#     else:
#         return {'data': f'{limit} unpublished blog from database'}
#
# @app.get('/about')
# def about():
#     return {'data': "about page"}
#
# @app.get('/blog/{id}')
# def show(id: int):
#     return {'data': id}
#
#
# class Blog(BaseModel):
#     title: str
#     body: str
#     published: bool
#
#
# @app.post('/blog')
# def create_blog(blog: Blog):
#     return blog
