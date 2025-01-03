from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Query

from post_service.models import PostCreate, PostResponse

router = APIRouter()

posts = []


@router.get("/", response_model=List[PostResponse])
async def get_posts(
    limit: int = Query(32, ge=1, le=64, title="Limit", description="Limit the number of posts"),
    search: Optional[str] = Query(None, min_length=1, max_length=128, title="Search", description="Search posts"),
):
    searched_posts = posts
    if search:
        searched_posts = [post for post in posts if search.lower() in post.get("title").lower()]
    return searched_posts[:limit]


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(
    post_id: int = Path(..., ge=0, title="Post ID", description="The ID of the post"),
):
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    return posts[post_id]


@router.post("/", response_model=PostResponse)
async def create_post(post: PostCreate):
    new_post = {"id": len(posts), **post.model_dump()}
    posts.append(new_post)
    return new_post


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: int = Path(..., ge=0, title="Post ID", description="The ID of the post"),
    updated_post: PostCreate = ...,
):
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post.created_at = posts[post_id].get("created_at")
    posts[post_id] = {"id": post_id, **updated_post.model_dump()}
    return posts[post_id]


@router.delete("/{post_id}", response_model=PostResponse)
async def delete_post(
    post_id: int = Path(..., ge=0, title="Post ID", description="The ID of the post"),
):
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.pop(post_id)
