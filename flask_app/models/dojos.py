from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojos:
    DB = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod # ALL DOJOS/READ
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod # READ ONE
    def get_one(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0]) 
    
    @classmethod # ALL NINJAS FROM 1 DOJO
    def ninjas_in_dojo(cls, dojos_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        data = {'id':dojos_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        one_dojo = cls(results[0])
        for row in results:
            ninjas_data = {'id':row['ninjas.id'], 'first_name':row['first_name'], 'last_name':row['last_name'], 'age':row['age'], 'created_at':row['ninjas.created_at'], 'updated_at':row['ninjas.updated_at'], 'dojos_id':row['dojos_id']}
            one_ninja = ninjas.Ninja(ninjas_data)
            one_dojo.ninjas.append(one_ninja)
        return one_dojo

    @classmethod # SAVE/CREATE A DOJO
    def save_dojo(cls, data):
        query = """INSERT INTO dojos (name)
                VALUES (%(name)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result