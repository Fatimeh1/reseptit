import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)
    
    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_recipe(title, ingredients, user_id, classes):
    sql = """INSERT INTO recipes (title, ingredients, user_id) 
             VALUES (?, ?, ?)"""
    db.execute(sql, [title, ingredients, user_id])

    recipe_id = db.last_insert_id() 

    sql = "INSERT INTO recipe_classes (recipe_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value]) 

def add_comment(recipe_id, user_id, comment):
    sql = """INSERT INTO comments (recipe_id, user_id, comment) 
             VALUES (?, ?, ?)"""
    db.execute(sql, [recipe_id, user_id, comment])

def get_comments(recipe_id):
    sql = """SELECT comments.comment,
                    users.id user_id,
                    users.username
            FROM comments, users
            WHERE comments.user_id = users.id AND 
                    comments.recipe_id = ?
            ORDER BY comments.id DESC"""
    return db.query(sql, [recipe_id])

def get_images(recipe_id):
    sql = "SELECT id FROM images WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def add_image(recipe_id, image):
    sql = "INSERT INTO images (recipe_id, image) VALUES (?, ?)"
    db.execute(sql, [recipe_id, image]) 

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def get_classes(recipe_id):
    sql = "SELECT title, value FROM recipe_classes WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

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
    result = db.query(sql, [recipe_id])
    return result[0] if result else None

def update_recipe(recipe_id, title, ingredients, classes):
    sql = """UPDATE recipes SET title = ?,
                                ingredients = ?
                            WHERE id = ?"""
    db.execute(sql , [title, ingredients, recipe_id])

    sql = "DELETE FROM recipe_classes WHERE recipe_id = ?"
    db.execute(sql , [recipe_id])

    sql = "INSERT INTO recipe_classes (recipe_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

def remove_recipe(recipe_id):
    sql = "DELETE FROM recipe_classes WHERE recipe_id = ?"
    db.execute(sql , [recipe_id])
    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql , [recipe_id])

def find_recipes(query):
    sql = """SELECT id, title 
             FROM recipes
             WHERE title LIKE ? OR ingredients LIKE ?
             ORDER BY id DESC"""
    like = "%" + query +"%"
    return db.query(sql, [like, like])
                                
