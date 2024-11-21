# Vehicle Management System

A web-based vehicle management system built with Django that allows users to manage vehicles, bookings, and maintenance. The system includes features such as booking vehicles, tracking maintenance schedules, and viewing booking statuses. 

## Features

- **Manage Vehicles**: Add, edit, and view vehicle details including model, registration number, capacity, and status.
- **Vehicle Bookings**: Create, edit, and manage vehicle bookings with customer details, booking status, and dates.
- **Maintenance Records**: Track maintenance activities for each vehicle, including service type, cost, and mileage.
- **Status Indications**: Statuses of bookings are color-coded for better visibility (Confirmed: Green, Pending: Yellow, Completed: Red).
- **User Authentication**: User login and registration to restrict access to certain sections of the system.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- pip (Python package manager)
- Django (version 4.x or higher)
- Database (SQLite by default, can be configured to use PostgreSQL, MySQL, etc.)
- Git (for version control)
- Virtualenv (optional, but recommended)

## Installation

Follow the steps below to set up and run the project locally.

### Step 1: Clone the repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/your-username/vehicle-management.git
```

### Step 2: Create a virtual environment

Navigate to the project directory and create a virtual environment:

```bash
cd vehicle-management
python3 -m venv venv
```

Activate the virtual environment:

- On Windows:

    ```bash
    venv\Scripts\activate
    ```

- On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

### Step 3: Install dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database

By default, the project uses SQLite as the database. If you want to configure another database (e.g., PostgreSQL or MySQL), make sure to update the `DATABASES` setting in `settings.py` accordingly.

### Step 5: Run Database Migrations

Run the migrations to set up the database tables:

```bash
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)

To access the Django admin panel and manage the vehicles and bookings, create a superuser account:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password for the superuser account.

### Step 7: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/`.

### Step 8: Access the Admin Panel (Optional)

You can access the Django admin panel by navigating to `http://127.0.0.1:8000/admin/` and logging in with the superuser credentials you created earlier.

## Usage

- **Home Page**: View a list of all vehicles, bookings, and maintenance records.
- **Bookings List**: Create new bookings, edit existing ones, and view booking status with color-coding.
- **Vehicle Management**: Add, edit, or delete vehicles and view details like model, registration number, and status.
- **Maintenance Tracking**: Record and view maintenance schedules for each vehicle.

## Contributing

If you'd like to contribute to the project, follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m "Add feature"`).
4. Push your changes to your forked repository (`git push origin feature-name`).
5. Create a pull request to merge your changes back into the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
- Replace `your-username` with your actual GitHub username or repository URL.
- If your project has additional dependencies or setup instructions, feel free to add them under the **Installation** section.
- Adjust any configuration settings based on the environment (e.g., production vs. development).
