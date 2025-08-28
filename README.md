# Django HTMX Word Cloud Generator

A simple yet powerful web application that dynamically generates a word cloud from a given text without a full page refresh. This project demonstrates the integration of Django for the backend, HTMX for seamless frontend updates, and Bootstrap 5 for a clean, responsive design.

![Project Screenshot](https://placehold.co/800x450/6366f1/white?text=Word+Cloud+App)

---

## ✨ Features

* **Dynamic Content:** Generates a word cloud on-demand with a single button click.
* **No Page Reload:** Uses HTMX to fetch and display the word cloud, providing a smooth, single-page application feel.
* **Responsive Design:** Styled with Bootstrap 5, ensuring the application looks great on all devices, from desktops to mobile phones.
* **Easy to Customize:** The Python backend logic for word cloud generation can be easily modified to change colors, shapes, and excluded words.
* **Loading Indicator:** Provides visual feedback to the user while the word cloud is being generated.

---

## 🛠️ Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, Bootstrap 5
* **Dynamic Behavior:** HTMX
* **Word Cloud Generation:** `wordcloud`, `matplotlib`

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.8+ and pip installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    * On macOS and Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    Create a `requirements.txt` file with the following content:
    ```txt
    Django>=4.0
    django-htmx
    wordcloud
    matplotlib
    numpy
    Pillow
    ```
    Then, install the packages:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## Usage

1.  Navigate to the main page of the application (e.g., `http://127.0.0.1:8000/wordcloud/`).
2.  Click the "Generate Word Cloud" button.
3.  A loading spinner will appear, and shortly after, the generated word cloud image will be displayed in the container below the button.

---

## 📂 Project Structure

Here is a brief overview of the key files in the project:

```
your_project/
├── your_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── partials/
│   │   │   └── wordcloud_image.html  # HTMX partial template
│   │   └── wordcloud_template.html   # Main page template
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                     # App-level URLs
│   ├── utils.py                    # Word cloud generation logic
│   └── views.py                    # Main view logic
├── your_project/
│   ├── settings.py                 # Project settings
│   └── urls.py                     # Project-level URLs
└── manage.py
