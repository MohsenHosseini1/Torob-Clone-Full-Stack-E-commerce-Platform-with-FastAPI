# Torob-Clone-Full-Stack-E-commerce-Platform-with-FastAPI
This project is a comprehensive implementation of a Torob-like e-commerce platform, featuring a robust backend and a RESTful API. It provides a solid foundation for building a price comparison and product listing website, similar to Torob.com, an Iranian online marketplace.

Key Features:
- User Management: Supports user registration, login, and account management with secure password hashing.
- Product Operations: Enables adding, viewing, searching, and managing products.
- Category System: Implements a flexible product categorization system.
- User Interactions: Includes features like product liking and user-specific product listings.
- RESTful API: Built with FastAPI, offering efficient endpoints for all e-commerce operations.
- Database Integration: Utilizes PostgreSQL for data storage, with YAML-based configurable connection settings.

Backend Functionality:
- User authentication and session management
- Product CRUD operations
- Category management and product filtering
- User-specific actions (liking products, viewing owned products)

API Endpoints:
- POST /add: Add a new product
- GET /view1: Retrieve all products
- GET /choose/{product_id}: Get details of a specific product
- GET /search: Search for products by name
- GET /info: Retrieve user information
- GET /myproduct: Get products owned by a user

Technology Stack:
- Backend: Python
- Web Framework: FastAPI
- Database: PostgreSQL
- ORM: Raw SQL queries via psycopg2
- Configuration: YAML for database settings

The application combines a command-line interface for backend operations with a modern FastAPI layer, allowing for flexible use and easy integration with front-end systems. It's designed with modularity and scalability in mind, making it suitable for both educational purposes and as a starting point for production systems.

This project serves as an excellent template for developers looking to understand the intricacies of building e-commerce platforms, from database design to API implementation.

Developed by Mohsen Hosseini
