from pymongo import MongoClient

# criando conexão
client = MongoClient("localhost", 27017)

# lista de basse de dados que eu tenho
# print(client.list_database_names())

# crio a base de dados mas como nao mandei nada ainda ele nao cria nada
db = client.Estudo_MongoDb

# pra isso eu insiro os valores

db.teste.insert_one({
    "teste": "teste-feito-16/12/2021"
})

# db.teste.insert_many(
#     [
#         {
#             "id": 1
#         },
#
#         {
#             "id": 12
#         },
#
#         {
#             "id": 500
#         },
#
#         {
#             "id": -222
#         }
#     ]
# )

#
# mydb = myclient['mydatabase']
#
# mycol = mydb["customers"]
#
# print(mydb.list_collection_names())
