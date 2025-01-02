from typing import List

from fastapi import HTTPException

from post_service.models import Post

posts = []


def get_all_posts() -> List[Post]:
    return posts


def get_post_by_id(post_id: int) -> Post:
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    return posts[post_id]


def create_post(post: Post) -> Post:
    posts.append(post)
    return post


def update_post(post_id: int, updated_post: Post) -> Post:
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post.created_at = posts[post_id].created_at
    posts[post_id] = updated_post
    return updated_post


def delete_post(post_id: int) -> Post:
    if post_id < 0 or post_id >= len(posts):
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.pop(post_id)
