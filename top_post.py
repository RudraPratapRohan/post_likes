@app.get("/posts/top")
def get_top_posts(limit: int = Query(5, gt=0)):
    db = SessionLocal()
    result = (
        db.query(Post.post_str_id, func.count(Like.id).label("like_count"))
        .join(Like)
        .group_by(Post.id)
        .order_by(desc("like_count"))
        .limit(limit)
        .all()
    )
    return [{"post_str_id": r[0], "like_count": r[1]} for r in result]
