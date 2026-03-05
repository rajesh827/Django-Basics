# Django Basics Lab

This repository contains the implementation of fundamental Django concepts including authentication, form validation, CRUD operations, file uploads, and middleware. The lab focuses on understanding Django's **MVT (Model–View–Template) architecture** and applying server-side validation with database interaction using Django ORM.

---

## Objectives

- Analyze and implement Django’s **MVT (Model–View–Template)** architecture for structured web application development.
- Design and construct **secure server-side logic** for authentication, form handling, and database-driven operations using Django ORM.
- Apply **advanced form validation techniques**, including custom validators and file upload constraints.
- Implement **dynamic web functionalities** such as CRUD operations, middleware integration, and request–response lifecycle management.

---

## Implemented Tasks

### 1. User Authentication
A Django view that accepts **username and password** from a login form and verifies credentials with the **Student table**.  
- If credentials match → Redirect to dashboard  
- If credentials do not match → Display *Invalid username/password*

---

### 2. Patient Form with Validation
Server-side script to create and validate a form and store patient data in the **patients** table.

**Fields**
- Name
- Patient ID
- Mobile
- Gender
- Address
- Date of Birth (DOB)
- Doctor Name

**Validation Rules**
- Name, Mobile, Gender, Doctor Name, DOB → Required
- Mobile → Must be **10 digits** starting with **98, 97, or 96**
- DOB → Must follow **YYYY-MM-DD format**

---

### 3. User Registration Form
HTML form with server-side validation.

**Validation Rules**
- Full Name → Maximum **40 characters**
- Email → Must be a **valid email format**
- Username → Must **start with letters followed by numbers**
- Password → Must be **more than 8 characters**

---

### 4. Image Upload with Validation
A Django view that allows image uploads with restrictions.

**Allowed Formats**
- jpg
- jpeg
- png
- gif

**Validation**
- File size must be **less than 2MB**

---

### 5. Project File Submission Form
Form to submit project files with validation.

**Fields**
- TU Registration Number
- Email Address
- Upload Project File

**Validation Rules**
- All fields are **mandatory**
- Email must be **valid format**
- Allowed file formats:
  - pdf
  - doc
  - docx
  - ppt
  - pptx
  - jpeg
- File size must be **less than 5MB**

---

### 6. Custom Middleware

A custom Django middleware was created to:
- Print incoming **HTTP requests**
- Measure the **time taken to complete each request**

This helps understand the **Django request–response lifecycle**.

---

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

---

## Conclusion

This lab helped in understanding how Django manages web applications using the **MVT architecture**. \
It provided hands-on experience with authentication, form validation, file uploads, middleware, and database operations using Django ORM. 
The experiment demonstrated how Django enables the development of secure and scalable web applications efficiently.

---

## Author

**Rajesh Bhandari**
