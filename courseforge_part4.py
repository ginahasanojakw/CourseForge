# === Stage 4: Implement create operations for the primary records ===
# Project: CourseForge
class CourseForgeRepository:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS modules (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS lessons (id INTEGER PRIMARY KEY AUTOINCREMENT, module_id INTEGER NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, FOREIGN KEY(module_id) REFERENCES modules(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS exercises (id INTEGER PRIMARY KEY AUTOINCREMENT, lesson_id INTEGER NOT NULL, question TEXT NOT NULL, options TEXT NOT NULL, correct_option_index INTEGER NOT NULL, FOREIGN KEY(lesson_id) REFERENCES lessons(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, exercise_id INTEGER NOT NULL, user_name TEXT NOT NULL, rating INTEGER NOT NULL, comment TEXT, FOREIGN KEY(exercise_id) REFERENCES exercises(id))''')

    def create_module(self, title: str, description: str):
        self.cursor.execute("INSERT INTO modules (title, description) VALUES (?, ?)", (title, description))
        return self.cursor.lastrowid

    def create_lesson(self, module_id: int, title: str, content: str):
        self.cursor.execute("INSERT INTO lessons (module_id, title, content) VALUES (?, ?, ?)", (module_id, title, content))
        return self.cursor.lastrowid

    def create_exercise(self, lesson_id: int, question: str, options: list[str], correct_index: int):
        options_str = "|".join(options)
        self.cursor.execute("INSERT INTO exercises (lesson_id, question, options, correct_option_index) VALUES (?, ?, ?, ?)", (lesson_id, question, options_str, correct_index))
        return self.cursor.lastrowid

    def create_review(self, exercise_id: int, user_name: str, rating: int, comment: str):
        self.cursor.execute("INSERT INTO reviews (exercise_id, user_name, rating, comment) VALUES (?, ?, ?, ?)", (exercise_id, user_name, rating, comment))
        return self.cursor.lastrowid

    def commit(self):
        self.db.commit()
