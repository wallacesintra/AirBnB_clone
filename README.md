# AirBnB_clone

## Project Description

Airbnb Clone Console is a command-line interface (CLI) application that provides a way to manage and interact with a database of properties and users. The application is built using Python.

## Installation

1. clone the repository:

    ```bash
    gh repo clone wallacesintra/AirBnB_clone

    ```

2. navigate to the project directory

3. start the console application:

    ```bash
    python3 console.py

    ```

## Project Features

* create, update and delete properties
* view and filter property by price, location, ...
* manage users accounts
* review and rating system for the properties

## Usage

after starting the application, interact with it using the command line interface.

* create a new property:

    ```bash
    create property --name "property-name" --price property-price(should be an integer) --location "property-location"
    ```

* update a property:

    ```bash
    update property --id property-id(should be an integer) --name "updated-name-of-the-property"
    ```

other commands type `help` in the terminal
