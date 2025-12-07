## Autoloader Update Lab

This lab demonstrates how to use Databricks Autoloader to ingest and update JSON files in a Delta table. The main goal is to ensure that each record, identified by its `id`, is kept up-to-date in the table whenever a newer entry for the same `id` arrives.

### Task Description

1. The folder `volume_path` contains JSON files with the following structure:
	 ```json
	 {
		 "id": 19,
		 "name": "name_2537",
		 "timestamp": "2025-11-19T02:23:51.680159"
	 }
	 ```
2. Ingest all files into a Delta table, using the `id` field as the unique identifier.
3. If a newer entry for an existing `id` is detected (based on the `timestamp`), update the corresponding record in the table.

### Data Generation

To test your implementation, use the notebook `Data_Generator.py`. This notebook generates sample JSON files and writes them to the input folder. Each file contains a random record, and the generator ensures unique timestamps for each entry.

**Steps to use the Data Generator:**
1. Open `Data_Generator.py` in Databricks.
2. Specify the catalog, schema, and volume using the provided widgets.
3. Run the notebook to generate 10 sample JSON files in the input folder.

You can then run the Autoloader lab to ingest and update these records in your Delta table.
