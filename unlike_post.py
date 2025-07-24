@app.delete("/posts/{post_str_id}/like")
def unlike_post(post_str_id: str, like: LikeAction):
    db = SessionLocal()
    post = db.query(Post).filter_by(post_str_id=post_str_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    like_entry = db.query(Like).filter_by(post_id=post.id, user_id_str=like.user_id_str).first()
    if not like_entry:
        return {"status": "not_liked_previously"}

    db.delete(like_entry)
    db.commit()
    return {"status": "unliked"}
