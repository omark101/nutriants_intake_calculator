# Nutriants_intake_calculator: Health and Wellness Application

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
   git clone https://github.com/omark101/nutriants_intake_calculator.git
   cd nutriants_intake_calculator
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

*Built by Omark101.*
