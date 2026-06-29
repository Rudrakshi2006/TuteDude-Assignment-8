# Flask Registration Form

## Objective

This project demonstrates a simple Flask web application that accepts user details through a registration form and displays the submitted information on a confirmation page.

---

## Technologies Used

- Python 3.x
- Flask
- HTML

---

## Project Structure

```
Flask_Registration/
│
├── app.py
│
└── templates/
    ├── register.html
    └── success.html
|__README.md
|
```


---

## Features

- Create a Flask application
- Display a registration form
- Accept user input:
  - Name
  - City
  - Phone Number
- Handle form submission using Flask routes
- Display the submitted details on a confirmation page

---

## Prerequisites

- Python 3.x installed
- Flask installed

Install Flask using:

```bash
pip install flask
```

---

## How to Run

1. Open the project folder in Terminal or Command Prompt.
2. Run the application:

```bash
python app.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Expected Output

1. Registration form is displayed in the browser.
2. User enters Name, City, and Phone Number.
3. User clicks the **Register** button.
4. A confirmation page displays the entered details.

---

## Sample Output

### Registration Form

```
User Registration Form

Name: __________

City: __________

Phone Number: __________

[ Register ]
```

### Confirmation Page

```
Registration Successful!

Name: Rudrakshi
City: Pune
Phone Number: 9876543210
```

---

## Learning Outcomes

- Creating a Flask application
- Using HTML templates
- Creating Flask routes
- Handling form submission using POST method
- Retrieving form data using `request.form`
- Passing data from Flask to HTML templates using `render_template`

---
