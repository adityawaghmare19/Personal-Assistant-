<?php

include 'components/connect.php';

session_start();

if(isset($_SESSION['user_id'])){
   $user_id = $_SESSION['user_id'];
}else{
   $user_id = '';
};

if(isset($_POST['submit'])){

   $email = $_POST['email'];
   $email = filter_var($email, FILTER_SANITIZE_STRING);
   $pass = sha1($_POST['pass']);
   $pass = filter_var($pass, FILTER_SANITIZE_STRING);

   $select_user = $conn->prepare("SELECT * FROM `users` WHERE email = ? AND password = ?");
   $select_user->execute([$email, $pass]);
   $row = $select_user->fetch(PDO::FETCH_ASSOC);

   if($select_user->rowCount() > 0){
      $_SESSION['user_id'] = $row['id'];
      header('location:home.php');
   }else{
      $message[] = 'incorrect username or password!';
   }

}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presonal Assistant </title>

    <link rel="shortcut icon" href="assets/img/logo.ico" type="image/x-icon">

    <!-- Bootsrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <!-- Bootsrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">

    <!-- Particle js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"
        type="text/javascript"></script>

    <!-- Texllate  -->
    <link rel="stylesheet" href="assets/vendore/texllate/animate.css">

    <link rel="stylesheet" href="style.css">

    
</head>

<body>
    <section id="Oval" class="mb-4">

        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="d-flex justify-content-center align-items-center" style="height: 60vh;">

                    <canvas id="canvasOne" width="300" height="280" style="position: absolute;"></canvas>

                    <!-- <div id="JarvisHood">

                        <div class="square">
                            <span class="circle"></span>
                            <span class="circle"></span>
                            <span class="circle"></span>
                        </div>

                    </div> -->

                </div>
                <h5 class="text-light text text-center">Welcome to Personal Assistant , Please login </h5>

                <div class="col-md-12 mt-4 pt-4">
                    <div class="text-center">
                        <div id="TextInput" class="d-flex">
                            
                            <form onsubmit="handleLogin(event)">
                                <input type="text" class="login_input" placeholder="Username" required> 
                                <br>
                                <input type="password" class="login_input" placeholder="Password" required>
                                <br>
                                <button type="submit" class="glow-on-hover">Login</button>
                              </form>



                            <button id="SendBtn" class="glow-on-hover" hidden><i class="bi bi-send"></i></button>
                        
                            

                        </div>
                    </div>
                </div>

            </div>
            <div class="col-md-1"></div>
        </div>

    </section>





    <script>
        function handleLogin(event) {
          event.preventDefault(); // Prevent actual form submission
          window.location.href = "index.html"; // Redirect to index.html
        }
      </script>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>

    <!-- Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>

    <!-- Particle js -->
    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <script src='https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js'></script>
    <script src="script.js"></script>

    <!-- Siri wave -->
    <script src="https://unpkg.com/siriwave/dist/siriwave.umd.min.js"></script>

    <!-- Texllate js -->
    <script src="assets/vendore/texllate/jquery.fittext.js"></script>
    <script src="assets/vendore/texllate/jquery.lettering.js"></script>
    <script src="http://jschr.github.io/textillate/jquery.textillate.js"></script>

    <script src="main.js"></script>
    <script src="controller.js"></script>
    <script src="/eel.js"></script>


</body>

</html>