import db

def add_recipe(title, ingredients, user_id):
    sql = """INSERT INTO recipes (title, ingredients, user_id) 
             VALUES (?, ?, ?)"""
    db.execute(sql, [title, ingredients, user_id])

def get_recipes():
    sql = "SELECT id, title, ingredients FROM recipes ORDER BY id DESC"
    
    return db.query(sql)