@app.post("/posts")
def create_post(post: PostCreate):
    db = SessionLocal()
    existing = db.query(Post).filter_by(post_str_id=post.post_str_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Post ID already exists")
    new_post = Post(post_str_id=post.post_str_id, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {
        "internal_db_id": new_post.id,
        "post_str_id": new_post.post_str_id,
        "status": "created"
    }
