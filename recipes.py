import db

def add_recipe(title, ingredients, user_id):
    sql = """INSERT INTO recipes (title, ingredients, user_id) 
             VALUES (?, ?, ?)"""
    db.execute(sql, [title, ingredients, user_id])

def get_recipes():
    sql = "SELECT id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.id,
                    recipes.title,
                    recipes.ingredients, 
                    users.id user_id,
                    users.username
            FROM recipes, users
            WHERE recipes.user_id = users.id AND 
                    recipes.id = ?"""
    return db.query(sql, [recipe_id])[0]

def update_recipe(recipe_id, title, ingredients):
    sql = """UPDATE recipes SET title = ?,
                                ingredients = ?
                            WHERE id = ?"""
    db.execute(sql , [title, ingredients, recipe_id])
                                
