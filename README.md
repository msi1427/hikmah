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
   from hikmah.data import <modules>
   ```
   

# How to Contribute?

This repo is not aimed to contain anything that are explicitly implemented in different libraries. Things that are preferred in this repo are:

- Handling unstable and erroneous implementations in different libraries (if possible also contribute to their main repos).
- Implementing a faster and stable version of what already exists. (An empirical explanation should be provided)
- There are ML and math concepts which are theoretical but does not have a good implementation. Those things can be added.
- Things that can be automated but have not yet been considered by others.
- --- To be continued ---