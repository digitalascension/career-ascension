import mysql.connector as conn
import json


class OmniDB:
    def __init__(self, host, user, passwd, database):
        try:
            self.omnidb = conn.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database)
        except conn.InterfaceError as e:
            print(e)


    # Get a model with a specific name
    def get_model(self):
        model_cursor = self.omnidb.cursor()
        sql = 'SELECT * FROM ModelData'
        try:
            model_cursor.execute(sql)
            result = model_cursor.fetchall()
            return result
        except conn.OperationalError:
            return None

    # Search OMNIDB for models with names that match a search value.
    def search_omni(self, value):
        models = []
        model_cursor = self.omnidb.cursor()
        sql = "SELECT * FROM ModelData WHERE ModelName LIKE \"%{0}%\"".format(value)
        try:
            model_cursor.execute(sql)
        except conn.Error as e:
            return e
        result = model_cursor.fetchall()
        for r in result:
            models.append(
                {
                    'Name': r[1],
                    'CreatedBy': r[2],
                    'LastUpdated': str(r[3]),
                    'Tags': r[4],
                    'URL': r[5]
                }
            )
        # Serialize to JSON and then return.
        jsonResult = json.dumps(models)
        return jsonResult

    # Get the latest models that have been entered in the database.
    def get_latest_models(self):
        model_cursor = self.omnidb.cursor()
        sql = 'SELECT * FROM ModelData WHERE datediff(CURDATE(), LastUpdated ) < 5 ORDER BY LastUpdated DESC'
        model_cursor.execute(sql)
        result = model_cursor.fetchall()
        return result
