
# Ecommerce Website with Django Backend

This project is a forked repository that originally contained only the frontend of an ecommerce website. I have added backend functionality using the Django framework. The backend is equipped with CRUD functionality, user management, real-time order management, and uses PostgreSQL as the database.

## Features

- **CRUD Functionality**: Create, Read, Update, and Delete products and other resources.
- **User Management**: User authentication and authorization.
- **Real-Time Order Management**: Handle orders in real-time.
- **PostgreSQL Database**: Robust database for handling complex queries and large data sets.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kpaatmik/Ecommerce.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Ecommerce
    ```
3. Set up a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
6. Set up the database:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Create a superuser to access the admin panel:
    ```sh
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the website at `http://127.0.0.1:8000`.
- Access the admin panel at `http://127.0.0.1:8000/admin` to manage users, products, and orders.

## Contributing

If you have any ideas or modifications for this project, feel free to fork the repository and make a pull request. Here’s how you can do it:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Add some feature"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Open a pull request.

## Contact

For any inquiries, feel free to reach out:

- **Name**: K P Aatmik
- **LinkedIn**: [linkedin.com/in/k-p-aatmik/](https://www.linkedin.com/in/k-p-aatmik/)
- **GitHub**: [github.com/kpaatmik](https://github.com/kpaatmik)


