from src.spark.load_data import load_customers

customers = load_customers()

customers.show(5)

customers.printSchema()

print(customers.count())