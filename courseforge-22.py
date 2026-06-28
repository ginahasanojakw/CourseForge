# === Stage 22: Add favorite records and quick favorite listing ===
# Project: CourseForge
class FavoriteManager(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content_type = db.Column(db.String(20))  # module, lesson, exercise
    content_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Favorite({self.user_id}, {self.content_type}:{self.content_id})>"

def add_favorite(user_id: int, ctype: str, cid: int):
    fav = Favorite(user_id=user_id, content_type=ctype, content_id=cid)
    db.session.add(fav)
    db.session.commit()
    return fav

def get_user_favorites(user_id: int):
    return [f for f in Favorite.query.filter_by(user_id=user_id).all()]
