# Databricks notebook source
# MAGIC %md
# MAGIC # Data Generator
# MAGIC
# MAGIC Create a volume and specify catalog, schema and volume in the widgets.

# COMMAND ----------

dbutils.widgets.text("catalog", "", "Catalog")
dbutils.widgets.text("schema", "", "Schema")
dbutils.widgets.text("volume", "", "Volume")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
volume = dbutils.widgets.get("volume")

volume_path = f"/Volumes/{catalog}/{schema}/{volume}/input"

# COMMAND ----------

# MAGIC %md
# MAGIC The following json generates 10 json files and writes them to the defined volume. After each JSON, it will wait for 10ms to ensure unique timestamps. 

# COMMAND ----------

import random
import json
from datetime import datetime
import time

for i in range(10):
    record = {
        "id": random.randint(1, 20),
        "name": f"name_{random.randint(1000, 9999)}",
        "timestamp": datetime.now().isoformat()
    }
    file_path = f"{volume_path}/record_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.json"
    dbutils.fs.put(file_path, json.dumps(record), overwrite=True)
    time.sleep(0.01)