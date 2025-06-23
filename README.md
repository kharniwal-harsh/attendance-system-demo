# Advanced Attendance System

A modern face recognition-based attendance management system for educational institutions. This project is ideal for college projects and demonstrates role-based access, intuitive management, and accurate identification using multiple images.

## Features

1. **Role-based access** for administrators and lecturers.
2. **Manage classes, add students, view attendance records** through an intuitive interface.
3. **Capture and store multiple images** for accurate identification.
4. **Export attendance records** to Excel.
5. **User-friendly dashboard** for both admin and lecturer roles.
6. **Great for college projects** and demonstrations.

## Project Structure

```
├── app.py
├── database.py
├── encode_faces.py
├── init_db.py
├── migrate_data.py
├── requirements.txt
├── static/
│   ├── attendance_sheets/
│   ├── class_photos/
│   ├── img/
│   └── student_photos/
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── landing.html
│   └── ...
└── ...
```

## Setup Procedure

Follow these steps to set up and run the project:

1. **Clone or Download the Repository**
   ```
   git clone https://github.com/kharniwal-harsh/attendance-system-demo
   ```
2. **Set Up the Database**
   - Run the database initialization script:
     ```
     python init_db.py
     ```
3. **Launch the Application**
   - Start the Flask app:
     ```
     python app.py
     ```
   - Visit the application in your browser:
     ```
     http://localhost/{your-project-folder-name}
     ```

## User Guide

### 1. Login as Administrator
- **Email:** `admin@gmail.com`
- **Password:** `@admin_`

Once logged in, you can:
- Add students
- Manage courses, units, and venues

⚠️ **Important:**
- Ensure to add at least two students and capture five clear images for each.
- Poor image quality will affect recognition accuracy. You can retake any image by clicking on it.

### 2. Login as Lecturer
- Create a lecturer account via the admin panel or use a pre-existing one.
- Select lecture user type to be able to login as lecturer.

If you have issues using this email and password, create your lecturer on the admin panel.

- **Email:** `mark@gmail.com`
- **Password:** `@mark_`

As a lecturer:
- Select a course, unit, and venue on the home page.
- Launch the Face Recognition feature to begin attendance.

#### Additional Features for the Lecturer Panel
- Export the attendance to an Excel sheet.
- Other simple features are available for managing the lecture panel.

---

For any issues or contributions, please open an issue or pull request on the [GitHub repository](https://github.com/kharniwal-harsh/attendance-system-demo).
