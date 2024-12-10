# University Timetable Web Application

A simple web-based timetable application that allows university students to view their class schedules based on their classification (Freshmen, Sophomore, Junior). The app connects to a PostgreSQL database to retrieve and display the relevant course details.

**Description**

This project is a Flask web application that displays a timetable of courses based on the student's classification. The app allows users to select their classification and view the courses available for that classification, showing the course name, the day of the week, and the time. It uses Flask for the backend and connects to a PostgreSQL database to store and retrieve timetable data.

**Steps Followed During Development**

1. **Creating AWS account**
   - Entered all of the details (email, password, card)
   - Configuration (Creating IAM user, MFA, adjusting settings for easier use)

2. **Creating EC2 and Configuring**
   - Creating EC2 instance, Ubuntu
   - Make sure to save your public key .pem
   - Configuration (adjusting ports and ip addresses to ensure we can connect trough ModaXterm, and can connect to our DB)
   - Allow Trafic from anywhere and specify IP range to be able to connect your instance
   - Add ports 8000, All traffic, 80, 22, 443, 5432
   - Configure security groups:
       - specify IP range, if you whant to allow only specific IPs or just 0.0.0.0/0 to allow anyone
       - add a security group with port 5432 to connect to your PostgreSQL RDS

3. **Creating RDS**
   - Choose PostrgeSQL as a Database
   - Connect with your instance
       - make sure that they are in the same security group (in my case there were not, and this is why I could not connect) and connected (all the protocals are correct)
       - and make sure it is public

4. **Create a seccion in Modaxterm and Connect to EC2 incstance**
   - New Seccion -> name: ubuntu -> add public IP of your instance
         - It is in Details
   - Add the public key file .pem you saved while creating EC2

5. **SetUp DBeaver**
   - New connection -> Choose PostgreSQL
   - For host enter endpoint of your RDS (in security)
   - Add username and password you used when creating RDS, you can find it in configurations
         -  if you frogot the password, like me, you can enter Modify and Reset it

6. **Update EC2 and Install neaded Dependencies**:
   - Run the following
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip postgresql-client -y
     ```

7. **Connect to RDS PostgreSQL**:
   - Connect to the RDS instance using psql:
     ```bash
     psql -h <RDS_End_Point> -U <RDS_User> -d <RDS_Database_Name>
     ```
   - Instead of <RDS_End_Point> write your own endpoint, same with <RDS_User> and <RDS_Database_Name>

8. **Create database table**:
   - Connect to the RDS instance using psql:
     ```sql
     CREATE TABLE timetable(id SERIAL PRIMARY KEY, course_name VARCHAR(100), classification VARCHAR(20),day VARCHAR(20), time VARCHAR(20));
     ```
   - And Insert the data
      ```sql
     INSERT INTO timetable (course_name, classification, day, time) VALUES ('COSC2610 Operating Systems', 'Sophomore', 'Tuesday', '2:00pm'), ('COSC3410 Computer Security', 'Junior', 'Thursday', '4:30pm'), ('COSC3500 IT Project Management', 'Junior', 'Wednesday', '4:30pm'), ('ECON3000 Basic Economic Modelling', 'Junior', 'Monday', '11:30am'), ('ARHS2210 Intercultural History of Art', 'Sophomore', 'Tuesday', '4:30pm'), ('ARHS1050 Art Appretiation', 'Freshmen', 'Thursday', '11:30am');
     ```
   -Now you can leave with \q

9. **Create Project Directory and Flask Application**:
   - Create the project directory and Python file:
     ```bash
     mkdir feruzas_project
     cd feruzas_project
     touch app.py
     ```
   - Fill in the python code
     ```bash
     nano app.py
     ```

10. **Create `index.html` Template**:
   - create a directory named templates inside of project file, in index.html is our first page with a form where users can choose classification, in timetable.html wpould be our output from database based on classification chosen
     ```bash
     mkdir templates
     cd templates
     nano index.html
     nano timetable.html
     ```
   - make sure that html files are inside of template directory which is inside project derectory

11. **Virtual Environment Set Up**:
   - Set up and activate the virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - if its not installed run:
      ```bash
     sudo apt install pyhton3.12-venv
     ```
   - Here you might encounter lockfile error, like me, it is due to other process currently running apt. Run:
     ```bash
     ps aux | grep '[a]pt'
     sudo apt update
     ```
  - Now run this command again and it will work (worked for me):
      ```bash
     sudo apt install pyhton3.12-venv
     ```
  - Then you can run:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

12. **Run Flask Application**:
    - get to your project directory
      ```bash
      cd feruzas_project
      ```
    - Run the Flask app:
      ```bash
      python app.py
      ```
    - You can view it by going through this link
      http://<public_Ip_of_your_instance>:8000

13. **If you encountered errors with pg8000**
   - Run: `pip install flask pg8000`.

14. **Final Adjustments**
   - Styled the web pages using basic CSS for a cleaner user interface.
   - Ensured the app is responsive and looks good on different screen sizes.

## Screenshots

![Screenshot 1]()
![Screenshot 2]()

