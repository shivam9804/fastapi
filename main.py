from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog from db'}
    else:
        return {'data': f'{limit} blog from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}

@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1','2'},'limit':limit,'id':id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog is created with title as {blog.title}'}

# if __name__ == '__main__':
#     uvicorn.run(app, host='1270.0.0.1', port=8080)