@app.post("/posts/{post_str_id}/like")
def like_post(post_str_id: str, like: LikeAction):
    db = SessionLocal()
    post = db.query(Post).filter_by(post_str_id=post_str_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    existing_like = db.query(Like).filter_by(post_id=post.id, user_id_str=like.user_id_str).first()
    if existing_like:
        return {"status": "already_liked"}

    new_like = Like(post_id=post.id, user_id_str=like.user_id_str)
    db.add(new_like)
    db.commit()
    return {"status": "liked"}
