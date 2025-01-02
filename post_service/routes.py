from typing import List

from fastapi import APIRouter, HTTPException

from post_service.models import Post

router = APIRouter()

posts = []


@router.get("/", response_model=List[Post])
async def get_posts():
    return posts


@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int):
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    return posts[post_id]


@router.post("/", response_model=Post)
async def create_post(post: Post):
    posts.append(post)
    return post


@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, updated_post: Post):
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post.created_at = posts[post_id].created_at
    posts[post_id] = updated_post
    return updated_post


@router.delete("/{post_id}", response_model=Post)
async def delete_post(post_id: int):
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.pop(post_id)
