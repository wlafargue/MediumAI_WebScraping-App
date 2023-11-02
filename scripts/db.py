from pymongo import MongoClient

class Database:
    """Class for managing a Mongo database."""

    def __init__(self, host="localhost", port=27017, database="my_db"):
        """ Initialize the Database Class.

        Args:
            host (str): hostname; default=localhost
            port (int): port; default=27017
            database (str): name of database; default=my_db
        """
        self.init_db(host, port, database)

    def init_db(self, host, port, database):
        """
        Initialize a Mongo database.

        Args:
            host (str): hostname
            port (int): port
            database (str): name of database
        """
        self.host = host
        self.port = port
        self.db_name = database

        self.client = MongoClient(self.host, self.port)
        self.db = self._client[self.db_name]
    
    def init_collection(self, collection):
        """ Initialize a collection to the existing database.

        Args:
            collection (str): name of collection

        Returns:
            Collection object
        """
        return self.db[self.collection]
    
    def find_one(self, collection, query):
        """ Return a single document.

        Args:
            collection (str): name of collection
            query (dict): querying a specific element to match
        
        Returns:
            Result of query
        """
        return self.db[collection].find_one(query)
    
    def update_many(self, collection, query, values, upsert=True):
        """ Return a single document.

        Args:
            collection (str): name of collection
            query (dict): querying a specific element
            values (dict): new values
            upsert (bool): if True, update and insert values; default=True

        Returns:
            Result of query
        """
        return self.db[collection].update_many(query, values, upsert=upsert)
