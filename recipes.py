import db

def add_recipe(title, ingredients, user_id):
    sql = """INSERT INTO recipes (title, ingredients, user_id) 
             VALUES (?, ?, ?)"""
    db.execute(sql, [title, ingredients, user_id])

def get_recipes():
    sql = "SELECT id, title, FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipes(recipe_id):
    sql = """SELECT resipes.title,
                    recipes.ingredients, 
                    users.username
            FROM recipes, users
            WHERE recipes.user_id = users.id AND 
                    recipes.id = ?"""
    return db.query (sql, recipe_id)[0]
