# from psycopg2 import connect
# host = 'localhost'
# user = "postgres"
# password = '12345'
# db = 'oqtepa'
# def get_categories():
#     con = connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db
#     )
#     cursor = con.cursor()
#     con.autocommit = True
#     sql = """
#               select * from categories
#               """
#     cursor.execute(sql)
#     res = []
#     for i in cursor.fetchall():
#         res.append(i)
#     con.close()
#     return res
#
#
# # print(get_categories())
