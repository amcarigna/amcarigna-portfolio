projects = [
    {
        "image": "/static/images/rest.png",
        "name": "Course List API",
        "techs": [
            "Python",
            "Flask",
            "Peewee"
        ],
        "description": """Currently runs locally from terminal. REST API built with Flask on top of Peewee for database
        management. Created in a Treehouse course. The API provides methods to get, post, put, and delete courses and
        course reviews from a database. The Peewee database also provides a User table which is used as the basis to
        authenticate access to certain methods with the argon2 package. Courses and their reviews are linked with
        foreign keys.""",
        # "live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/course-list-api"
    },
    {
        "image": "/static/images/pet.png",
        "name": "Pet Adoption",
        "techs": [
            "Python",
            "Flask",
            "SQLAlchemy"
        ],
        "description": """Pet Adoption Website. Locally hosted web app built with Flask and SQLAlchemy. (Not associated
        with any real pet adoption agency.) This simple application provides basic CRUD operations for a database
        designed to hold pet information (name, breed, age, weight, color, etc.).""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/pet-adoption"
    },
    {
        "image": "/static/images/alchemy.png",
        "name": "Book Database App",
        "techs": [
            "Python",
            "SQLAlchemy"
        ],
        "description": """A Simple Book Database App. Runs in terminal with Python. Built on SQLAlchemy. This simple
        application provides basic CRUD operations for a database designed to hold book information (title, author,
        publication date, price).""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/simple-book-db-app"
    },
    {
        "image": "/static/images/book.png",
        "name": "Book Analysis with Pandas",
        "techs": [
            "Python",
            "Pandas",
            "Jupyter Notebook"
        ],
        "description": """In this project, I got some practice in using pandas to query a .csv database for information
        about a kaggle dataset from goodreads. I analyzed the database to discover: the most popular book, the relative
        popularity of long and short books, which reviews can be trusted, what it means for a book to be considered
        'good,' which authors are the most prolific, and book statistics (length, publisher, published date, etc).""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/pandas-book-analysis"
    },
    {
        "image": "/static/images/cleaning.png",
        "name": "Data Cleaning with Pandas",
        "techs": [
            "Python",
            "Pandas",
            "Jupyter Notebook"
        ],
        "description": """In this project, I cleaned up a small dataset containing a list of Pokemon and their
        attributes. The .csv file had many mistakes and errors to be cleaned, including: bad data types (strings in
        numeric columns and vice versa), duplicate data, missing data, bad data formatting (e.g., wrong case or bad
        punctuation), typos, and hanging whitespace. Then, I saved the cleaned up dataset to a new .csv file. In order
        to do this, I also created functions to search the dataframe a little more easily, and a function to move rows
        around to preserve the order of the Pokemon after deletions.""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/pandas-data-cleaning"
    },
    {
        "image": "/static/images/phantom.svg",
        "name": "Deep Back Projection",
        "techs": [
            "Python",
            "PyTorch",
            "MATLAB"
        ],
        "description": """Joint work with classmate for Purdue University course project for BME 595. The topic of this
        project is medical imaging reconstruction. For instance, we may be given an x-ray of a skull, and our objective
        would be to mathematically reconstruct the skull. In this project, we use a convolutional neural network to
        accurately carry out this task. Image credit to Larry Shepp and Benjamin F. Logan.""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/deep-back-projection"
    },
    {
        "image": "/static/images/keras.png",
        "name": "Exercises in Keras",
        "techs": [
            "Python",
            "Keras"
        ],
        "description": """A collection of deep learning tasks completed in Keras for MA598, at Purdue University.
        Includes: 1) Training a convolutional neural network (CNN) on CIFAR-10, a database of images of common items. 2)
        Training a recurrent neural network (RNN) on jena climate data. 3) A continuous bag of words (CBOW) embedding of
        IMDB film review data used to train a dense neural network. 4) A Skip Gram embedding of IMDB film review data
        used to train a dense neural network. 5) Training an autoencoder on CIFAR-10, a database of images of common
        items, and then 6) using the autoencoder from the last part to train another autoencoder on the same
        dataset.""",
        # "live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/keras-exercises"
    },
    {
        "image": "/static/images/portfolio.png",
        "name": "Portfolio",
        "techs": [
            "Python",
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "description": """This is the project that created the webpage you are on right now! It uses Flask to create a
        simple webpage for exhibiting current and prior projects. Most of the work in creating the webpage was done
        using HTML, but some Python functionality was used, including for the storage of this paragraph.""",
        "live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/amcarigna-portfolio"
    },
    {
        "image": "/static/images/power_rankings.png",
        "name": "Power-Rankings",
        "techs": [
            "Python",
            "Pandas",
            "NumPy"
        ],
        "description": """A python application for generating power rankings for a sports league. Currently in
        development. Developed with using the NFL (American Football) in mind. At the moment, it functions more like a
        package because it is missing a user interface. I've been using Jupyter Notebook to run functions
        from it. The necessary functions are all present and work properly. The most important function is
        models.build_league(), which will build a computer model of a league for the first time, or load previous league
        data.""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/power-rankings"
    },
    {
        "image": "/static/images/mtg.png",
        "name": "MTG-Inventory",
        "techs": [
            "Python"
        ],
        "description": """This project is in early development. The goal of the project is to create an application to
        add, search, update, and delete trading cards from one's inventory. It uses Scryfall API to get trading card
        information. The purpose of this project is two-fold: First, to be able to store inventory digitally and locally
        without needing to subscribe to some online service. Second, to see if the features provided by those online
        services can be improved upon.""",
        #"live": "https://python-portfolio-f63j.onrender.com/",
        "repo": "https://github.com/amcarigna/mtg-inventory"
    },
    {
        "image": "/static/images/stargazer-screenshot.png",
        "name": "Stargazer Log",
        "techs": [
            "JavaScript",
            "HTML",
            "CSS"
        ],
        "description": """This project served as an introduction to using Git and Github. Before this, I was aware
        generally of version control, its purpose, and rough logic behind how it works. But using Git and Github always
        intimidated me, and I avoided it. Now I am comfortable using its basic features and ready to learn other
        ones.""",
        "live": "https://amcarigna.github.io/stargazers-log/",
        "repo": "https://github.com/amcarigna/stargazers-log"
    }
]