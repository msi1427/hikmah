**Hikmah** is defined in Arabic as *'coming to know the essence of beings as they really are'*. This repo aims to generalize common artificial intelligence and data science implementations for research, development and production and will be built upon multiple libraries. <br/>
Any sort of contribution is welcomed.

# Build from Sources

1. Clone the repo

   ```bash
   git clone https://github.com/msi1427/hikmah.git
   cd hikmah
   ```

2. Initialize and activate a virtual environment

   ```bash
   virtualenv --no-site-packages env
   source env/bin/activate
   ```

3. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Import the library 

   ```python
   import hikmah
   ```

   *Use data functions* (More on [data.md](https://github.com/msi1427/hikmah/blob/main/data/data.md))
   
   ```python
   from hikmah.text import <module_name>
   ```
   
   *Use text functions* (More on [text.md](https://github.com/msi1427/hikmah/blob/main/text/text.md))

