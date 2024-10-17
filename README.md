
# Laptop Store - Flask Web Application

Welcome to the **Elaptops** web application, a platform built using Flask for selling laptops online. This repository contains the codebase for the website, which allows users to browse laptops, view product details, and proceed with purchasing through a secure checkout system.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Demo

https://elaptops.onrender.com/

## Features

- **Product Listings**: Browse a variety of laptops.
- **Search**: Search laptops based on their names or their brands.
- **Product Details Page**: View individual laptop details with high-resolution images and descriptions.
- **Shopping Cart**: Add laptops to a shopping cart and review the order before purchase.
- **Checkout System**: A secure checkout system with payment gateway integration.
- **User Authentication**: Sign up, log in, and manage orders as a registered user.
- **Wishlist**: Save products to a wishlist for later viewing.
- **Responsive Design**: Optimized for desktop and mobile devices.
  
## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript 
- **Database**: SQLite
- **Templating Engine**: Jinja2 (Flask's templating engine)
- **Authentication**: Flask-Login (User authentication)
- **Payment Gateway**: Stripe
- **Other Libraries**: 
  - Flask-WTF (Form handling)
  - Flask-Migrate (Database migrations)

## Setup and Installation

### Prerequisites

Make sure you have the following installed on your local machine:

- Python 3.x
- Flask
- SQLite (or another database system)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hillcrest01/elaptops
   cd elaptops
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the project root and configure the following variables:

   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///laptops.db
   STRIPE_PUBLIC_KEY=your_stripe_public_key
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

5. **Set up the database**:
   Initialize the database using Flask-Migrate:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Flask development server**:
   ```bash
   flask run
   ```

7. Visit `http://127.0.0.1:5000` in your browser to view the application.


## How to Use

1. **Browsing Products**:
   - Navigate to the homepage to view available laptops. 
   - Use the search and filter features to find laptops that match your needs.

2. **Adding to Cart**:
   - Click on any laptop to view details and add it to your cart.

3. **Checkout Process**:
   - Review items in your cart and proceed to checkout, where you'll be asked to provide payment details via Stripe/PayPal.
   
4. **User Authentication**:
   - Sign up or log in to save products to your wishlist and track your orders.

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
