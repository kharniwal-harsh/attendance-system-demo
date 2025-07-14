# Attendies – Smart Attendance Management System 🎓

[![View Live Demo](https://img.shields.io/badge/View-Live%20Demo-blue?style=for-the-badge)](https://kharniwal-harsh.github.io/attendance-system-demo/)

🚀 About the Project
Attendies is a smart attendance management system that streamlines the process of taking attendance in classrooms using:

🎥 Face recognition (via dlib & face_recognition) for live webcam or group photo attendance

📝 Manual fallback marking to ensure no student is missed

📊 Detailed dashboards with Excel export and notifications for low attendance

Designed to reduce manual workload and save time for educators.

## Project Screenshots

Below are screenshots of the main features and pages of the project:

1. **Landing Page**
   
   ![Landing Page](project%20pic/landing_page.png)
   > The welcoming landing page introduces the system and its features.

2. **Login Page**
   
   ![Login Page](project%20pic/login_page.png)
   > Secure login for administrators and lecturers.

3. **Dashboard Page**
   
   ![Dashboard Page](project%20pic/dashboard_page.png)
   > Overview of attendance statistics and quick access to management features.

4. **Profile Page**
   
   ![Profile Page](project%20pic/profile_page.png)
   > User profile management for updating personal details and password.

5. **Create Class Page**
   
   ![Create Class Page](project%20pic/create_class_page.png)
   > Interface for administrators to create and manage classes.

6. **Register Student Page**
   
   ![Register Student Page](project%20pic/register_student_page.png)
   > Add new students and capture multiple images for face recognition.

7. **View Students Page**
   
   ![View Students Page](project%20pic/view_students_page.png)
   > List and manage all registered students in the system.

8. **Manual Attendance Page**
   
   ![Manual Attendance Page](project%20pic/manual_attendance_page.png)
   > Mark attendance manually for students in a class.

9. **Image-based Attendance Page**
   
   ![Image-based Attendance Page](project%20pic/imagebased_attendance_page.png)
   > Mark attendance by uploading or capturing student images.

10. **Webcam Attendance Page**
   
   ![Webcam Attendance Page](project%20pic/live_webcam_attendance_page.png)
   > Take attendance using live webcam face recognition.

11. **View Attendance Page**
   
   ![View Attendance Page](project%20pic/view%20attendance_page.png)
   > View and export attendance records for analysis.

## Features

1. **Role-based access** for administrators and lecturers.
2. **Manage classes, add students, view attendance records** through an intuitive interface.
3. **Capture and store multiple images** for accurate identification.
4. **Export attendance records** to Excel.
5. **User-friendly dashboard** for both admin and lecturer roles.


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

📚 Once logged in, you can:
Add students (capture at least 5 clear face images)

Create & manage classes

Mark attendance via:

📸 Live webcam face recognition

🖼️ Uploading a group image

✍️ Manual marking

Export attendance to Excel

Send notifications to students with <75% attendance

⚠️ Important:
Ensure to register students with multiple clear face images for best recognition results. Poor images may lead to low accuracy.

As a lecturer:
- Select a course, unit, and venue on the home page.
- Launch the Face Recognition feature to begin attendance.

#### Additional Features for the Lecturer Panel
- Export the attendance to an Excel sheet.
- Other simple features are available for managing the lecture panel.

---

For any issues or contributions, please open an issue or pull request on the [GitHub repository](https://github.com/kharniwal-harsh/attendance-system-demo).
