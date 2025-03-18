import sqlite3

from Tutorial_28.model.Post import Post


class PostDao:
    def __init__(self, db_name="posts.db"):
        """Initialize database connection and create table if not exists."""
        self.connection = sqlite3.connect("posts.db",check_same_thread=False)
        self.cursor = self.connection.cursor()


        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def generate_id(self):
        """Generate a new ID based on the highest existing ID."""
        self.cursor.execute("SELECT MAX(id) FROM post")
        max_id = self.cursor.fetchone()[0]
        return 1 if max_id is None else max_id + 1

    def create_post(self, title, content):
        """Insert a new post into the database with manually assigned ID."""
        new_id = self.generate_id()
        self.cursor.execute(
            "INSERT INTO post (id, title, content) VALUES (?, ?, ?)",
            (new_id, title, content)
        )
        self.connection.commit()
        return new_id

    def get_post_by_id(self, post_id):
        """Retrieve a post by its ID."""
        self.cursor.execute("SELECT * FROM post WHERE id = ?", (post_id,))
        row = self.cursor.fetchone()
        return Post(*row) if row else None

    def get_all_posts(self):
        """Retrieve all posts."""
        self.cursor.execute("SELECT * FROM post")
        rows = self.cursor.fetchall()
        return [Post(*row) for row in rows]

    def update_post(self, post_id, title, content):
        """Update an existing post."""
        self.cursor.execute(
            "UPDATE post SET title = ?, content = ? WHERE id = ?",
            (title, content, post_id)
        )
        self.connection.commit()

    def delete_post(self, post_id):
        """Delete a post by ID."""
        self.cursor.execute("DELETE FROM post WHERE id = ?", (post_id,))
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()