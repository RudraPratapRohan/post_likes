@app.get("/users/{user_id_str}/liked-posts")
def get_liked_posts(user_id_str: str):
    db = SessionLocal()
    result = (
        db.query(Post.post_str_id)
        .join(Like)
        .filter(Like.user_id_str == user_id_str)
        .all()
    )
    return [r[0] for r in result]
