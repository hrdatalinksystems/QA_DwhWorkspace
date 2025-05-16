# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "deb2abfb-31aa-454c-993b-67c10a8141ac",
# META       "default_lakehouse_name": "SalesLakehouse",
# META       "default_lakehouse_workspace_id": "a050afdf-29d9-476c-bc35-3ac5262a365a",
# META       "known_lakehouses": [
# META         {
# META           "id": "deb2abfb-31aa-454c-993b-67c10a8141ac"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE TEST (
# MAGIC     Id decimal(10),
# MAGIC     Name string
# MAGIC )

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO TEST (Id, Name) VALUES
# MAGIC (1, 'Raj'),
# MAGIC (2, 'Aliya')
# MAGIC ;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM test")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM test

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
