# Using the functions in the data folder
## hikmah.data.etl
### load_tables

1. Import the library 

   ````python
   from hikmah.data.etl import load_tables
   ````

2. **jsonl_to()** 

   ```python
   data = load_tables.jsonl_to(<jsonl_file_path>,<destination_type: 'list' or 'pandas'>)
   # Returns: dictionary list or pandas dataframe
   ```

   