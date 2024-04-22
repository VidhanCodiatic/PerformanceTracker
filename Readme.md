# PerformanceTracker

PerformanceTracker is a Django application designed to track performance metrics such as cost, revenue, and profit.

## Installation

# Method One :-

To install and run PerformanceTracker locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NitinV84/PerformanceTracker.git
    cd PerformanceTracker
    ```

2. **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

5. **Generate Random Revenue for DailyPerformance:**

    ```bash
    python manage.py generate_random_revenue
    ```

6. **Run celery task for Dailyperformance :**

    ```bash
    celery -A PerformanceTracker worker --loglevel=info
    ```

7. **Access the application at [http://localhost:8000](http://localhost:8000).**

8. **Create and Update DailyPerformance and HourlyPerformance:**

    ```bash
    dailyperformance/
    dailyperformance/<int:pk>/
    hourlyperformance/
    hourlyperformance/<int:pk>/
    ```

# Method Two :-

1. **Create a virtual environment and activate:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

2. **Build docker image:**

    ```bash
    docker-compose build
    ```

3. **Run docker:**

    ```bash
    docker-compose up
    ```

4. **Stop docker:**

    ```bash
    docker-compose down
    ```


## Challenges Faced and Overcame

During the development of the PerformanceTracker project, several challenges were encountered, along with their resolutions:

### Challenge 1: Implementing the slow_iteration.py Script with Celery

**Description:** Implementing the `slow_iteration.py` script with Celery presented challenges in efficiently iterating over a limited queryset while introducing a delay using `time.sleep(60)`.

**Solution:** To overcome this challenge, the `slow_iteration.py` script was designed to utilize Celery tasks for asynchronous execution. The DailyPerformance queryset was limited to 50 records to prevent excessive resource consumption. Within the Celery task, each record was iterated over, and a 60-second delay was introduced using `time.sleep(60)`. By leveraging Celery's task scheduling capabilities, the script was able to iterate over the queryset asynchronously while maintaining the desired delay.

To incorporate time-based scheduling for the `slow_iteration.py` script, Celery Beat was configured. This allowed the script to run at a specific time each day, ensuring consistent and timely execution.

## Usage

Once the server is running, you can access the PerformanceTracker application in your web browser.

## Contributing

We welcome contributions from the community! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Nitin Verma](LICENSE) license.
