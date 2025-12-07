# Databricks notebook source
# MAGIC %md
# MAGIC # Autoloader with updating of files
# MAGIC
# MAGIC The folder ```volume_path``` contains JSON files with the following structure: 
# MAGIC
# MAGIC
# MAGIC ```
# MAGIC {
# MAGIC "id": 19,
# MAGIC "name": "name_2537",
# MAGIC "timestamp": "2025-11-19T02:23:51.680159"
# MAGIC }
# MAGIC ```
# MAGIC
# MAGIC
# MAGIC Ingest all files into a table, using the ID as an identifier. If a newer entry for the ID is written, update it in the table. 
# MAGIC
# MAGIC Use the notebook ```Data_Generator``` to generate new files to test your implementation.

# COMMAND ----------

dbutils.widgets.text("catalog", "", "Catalog")
dbutils.widgets.text("schema", "", "Schema")
dbutils.widgets.text("volume", "", "Volume")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
volume = dbutils.widgets.get("volume")

base_path = f"/Volumes/{catalog}/{schema}/{volume}"
volume_path = f"{base_path}/input"