<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cheryl Machingura - Data Scientist Portfolio</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

  <!-- Custom CSS -->
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f6f8;
    }

    header {
      text-align: center;
      padding: 20px;
      background-color: #3498db;
      color: white;
    }

    header img {
      border-radius: 50%;
      width: 150px;
      height: 150px;
      object-fit: cover;
    }

    h1 {
      margin-top: 10px;
      font-family: 'Poppins', sans-serif;
      font-size: 2.5em;
    }

    h2 {
      font-family: 'Poppins', sans-serif;
      color: #3498db;
      margin-top: 40px;
    }

    section {
      margin: 20px;
    }

    .project-card {
      background-color: white;
      padding: 20px;
      text-align: center;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      margin: 10px;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: pointer;
    }

    .project-card:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }

    .project-card img {
      width: 100%;
      height: auto;
      border-radius: 10px;
    }

    .project-card a {
      text-decoration: none;
      color: #3498db;
      font-weight: bold;
    }

    .form-container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .form-container label {
      font-size: 1.1em;
      color: #333;
    }

    .form-container input, .form-container textarea {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border-radius: 5px;
      border: 1px solid #ccc;
      font-size: 1em;
    }

    .form-container button {
      padding: 10px 20px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 1.1em;
    }

    .form-container button:hover {
      background-color: #2980b9;
    }

    footer {
      text-align: center;
      margin-top: 40px;
      background-color: #3498db;
      color: white;
      padding: 20px;
    }

    footer a {
      color: white;
      text-decoration: none;
    }

  </style>
</head>

<body>
  <!-- Header Section -->
  <header>
    <img src="https://github.com/CherylMachingura/cheryltaf85.github.io/blob/main/Cheryl%20professional%20picture.jpeg?raw=true" alt="Cheryl's Professional Photo" />
    <h1>Welcome to My Portfolio</h1>
    <p>Hi there, I'm Cheryl! Welcome to my portfolio.</p>
  </header>

  <!-- About Me Section -->
  <section>
    <h2><i class="fas fa-user-circle"></i> About Me</h2>
    <p>💡 &nbsp;I am a **Principal Program Manager** at **Discover Financial Services**, currently transitioning into **data science** and **data modeling** roles.</p>
    <p>🎓 &nbsp;I hold an **MBA in Business Analytics** from **Texas Woman's University** and am completing my **Master's in Data Science** from **Bellevue University**.</p>
    <p>🌱 &nbsp;I am passionate about **machine learning**, **predictive analytics**, and solving **real-world business problems** such as **customer churn**, **fraud detection**, and **credit risk modeling**.</p>
    <p>✍️ &nbsp;In my free time, I enjoy creating impactful **data visualizations**, contributing to **data science communities**, and working on **side projects**.</p>
    <p>💬 &nbsp;Feel free to reach out to me for **collaborations**, **job opportunities**, or just for an engaging **data science discussion**.</p>
    <p>✉️ &nbsp;You can shoot me an email at **[cherylmachingura.pm@gmail.com](mailto:cherylmachingura.pm@gmail.com)**. I’ll get back to you as soon as possible.</p>
    <p>📄 &nbsp;Please check out my **[Résumé](https://drive.google.com/file/d/1CgTBBelcsjjc-4VOdApL9c76vvTL49Fe/view?usp=sharing)** for more details about me.</p>
  </section>

  <!-- Projects Section -->
  <section>
    <h2><i class="fas fa-project-diagram"></i> Projects</h2>
    
    <div class="project-card">
      <img src="https://via.placeholder.com/150" alt="Customer Churn">
      <h3>Customer Churn Prediction</h3>
      <p>Predict customer churn in the financial industry using machine learning.</p>
      <a href="https://github.com/cheryltaf85/Customer-Churn-Prediction">View Project</a>
    </div>

    <div class="project-card">
      <img src="https://via.placeholder.com/150" alt="Credit Risk">
      <h3>Credit Risk Modeling for Loan Approvals</h3>
      <p>Predict the risk of loan defaults using machine learning.</p>
      <a href="https://github.com/cheryltaf85/Credit-Risk-Modeling">View Project</a>
    </div>

    <div class="project-card">
      <img src="https://via.placeholder.com/150" alt="Fraud Detection">
      <h3>Fraud Detection in Credit Card Transactions</h3>
      <p>Identify fraudulent transactions in real-time using machine learning.</p>
      <a href="https://github.com/cheryltaf85/Fraud-Detection-Credit-Card">View Project</a>
    </div>

    <!-- Add more project cards here, following the same structure -->
  </section>

  <!-- Tech Stack Section -->
  <section>
    <h2><i class="fas fa-cogs"></i> Tech Stack</h2>
    <p>Languages: Python, SQL, R</p>
    <p>Frameworks: TensorFlow, Scikit-Learn</p>
    <p>Tools: Tableau, Power BI, GitHub</p>
  </section>

  <!-- Contact Form Section -->
  <section>
    <h2><i class="fas fa-phone"></i> Contact Me</h2>
    <div class="form-container">
      <form action="https://formspree.io/f/your-form-id" method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Your Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer>
    <p>Connect with me on <a href="https://www.linkedin.com/in/cherylmachingura/">LinkedIn</a> or <a href="https://twitter.com/cheryl_taf">Twitter</a></p>
  </footer>
</body>
</html>




