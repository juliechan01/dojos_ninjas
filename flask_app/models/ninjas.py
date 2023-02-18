from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojos

class Ninja:
    DB = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']
    
    @classmethod # READ ONE
    def get_one(cls, id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod # SAVE/CREATE
    def save_ninja(cls, data):
        query = """INSERT INTO ninjas (dojos_id, first_name, last_name, age)
                VALUES (%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod # UPDATE
    def update(cls, data):
        query = """UPDATE ninjas 
                SET first_name = %(first_name)s, 
                last_name = %(last_name)s, 
                age = %(age)s
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @classmethod # DELETE
    def delete(cls, id):
        query = """
                DELETE FROM ninjas
                WHERE id = %(id)s;
        """
        data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results