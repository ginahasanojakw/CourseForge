# === Stage 20: Add duplicate detection for newly created records ===
# Project: CourseForge
class DuplicateChecker:
    def __init__(self, db):
        self.db = db

    async def check_content_duplication(self, content_type: str, new_data: dict) -> bool:
        if content_type == "module":
            query = f"SELECT id FROM {content_type}s WHERE title = %(title)s OR description LIKE '%{new_data['description']}%'"
        elif content_type in ["lesson", "exercise"]:
            query = f"SELECT id FROM {content_type}s WHERE parent_id = %(parent_id)s AND (title = %(title)s OR content LIKE '%{new_data.get('content', '')}%')"
        else:
            return False

        try:
            async with self.db.cursor() as cursor:
                await cursor.execute(query, {"title": new_data.get("title", ""), "description": new_data.get("description", ""), "parent_id": new_data.get("parent_id")})
                existing = await cursor.fetchone()
                return existing is not None
        except Exception:
            return False

    async def check_user_duplication(self, username: str) -> bool:
        query = "SELECT id FROM users WHERE email = %(email)s OR username = %(username)s"
        try:
            async with self.db.cursor() as cursor:
                await cursor.execute(query, {"email": username.lower(), "username": username})
                existing = await cursor.fetchone()
                return existing is not None
        except Exception:
            return False

    async def check_progress_duplication(self, user_id: int, course_id: int) -> bool:
        query = "SELECT id FROM progress WHERE user_id = %(user_id)s AND course_id = %(course_id)s"
        try:
            async with self.db.cursor() as cursor:
                await cursor.execute(query, {"user_id": user_id, "course_id": course_id})
                existing = await cursor.fetchone()
                return existing is not None
        except Exception:
            return False
