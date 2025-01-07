# Checkup: Health and Wellness Application

**Checkup** is a desktop application designed to help users monitor their nutritional intake and activity levels. Built with **Python** and **Tkinter**, it leverages the `customtkinter` library for a modern user interface and integrates with a **Microsoft Access database** to manage user data and provide personalized health recommendations.

---

## Features

### 1. User Authentication
- Sign in, register, or log in as a guest for personalized experiences.

### 2. Data Input
- Users can input personal details, including:
  - Age
  - Height
  - Weight
  - Gender
  - Activity level

### 3. Health Metrics Calculation
- Automatically calculates and displays:
  - **Daily Caloric Needs**  
  - **Macronutrient Intake** (Carbohydrates, Protein)  
  - **Micronutrient Needs** (Magnesium, Sodium, Calcium, Potassium, Phosphorus, Water)

### 4. Database Integration
- All user credentials and health data are securely stored in a **Microsoft Access database** for easy retrieval and updates.

---

## Prerequisites

Before running the application, ensure the following dependencies are installed:

- **Python 3.x**  
- **Tkinter**  
- **customtkinter**  
- **pyodbc**  
- **Pillow (PIL)**  

Use the following command to install dependencies:  
```bash
pip install customtkinter pyodbc pillow
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/checkup.git
   cd checkup
   ```

2. Update the **Microsoft Access database path**:
   - Locate the database file provided in the repository.
   - Modify the file path in the code to point to your local machine's path.

3. Replace the **default image** shown in the program:
   - The repository includes a placeholder image. Replace it with your preferred photo if necessary.

4. Run the application:
   ```bash
   python main.py
   ```

---

## Notes

- The application comes with the full source code, including the database and placeholder image files.
- Ensure you have **read/write access** to the database file location for proper functionality.

---

## Screenshots

![Screenshot 1](./screenshots/home.png)  
*Home screen displaying user metrics.*

![Screenshot 2](./screenshots/input.png)  
*Data input screen for user details.*

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contribution

Contributions are welcome! Feel free to fork the repository, make updates, and submit a pull request.

---

*Built with 💻 and 💙 by [Your Name].*
