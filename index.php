<!DOCTYPE html>
<html>
<?php
session_start();
if(empty($_SESSION['userScore'])) $_SESSION['userScore'] = 0;
if(empty($_SESSION['compScore'])) $_SESSION['compScore'] = 0;

?>
<head>
	<title></title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="font-awesome-4.7.0/css/font-awesome.min.css">
	<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>
</head>

<body>

<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">OpenCurrents RPS</a>
      <p class="navbar-text">Created by Hank C</p>
    </div>
  </div>
</nav>

<div class="container">
  <div class="row">

  	<div class="col-md-12">
	    <div class="jumbotron">
		  <h1>Hello, user!</h1>
		  <p>This is a simple rock paper scissors game, simply make your choice and hit the Go! button to battle the computer! This page was developed for opencurrents code challenge.</p>
		  <p><a class="btn btn-primary btn-lg" href="https://github.com/opencurrents/software-challenge" role="button" target="_blank">Learn more</a></p>
		</div>
	</div>

	<form action="" method="post">
		<div class="col-md-4">
		</div>
		<div class="col-md-4 c">
			<label class="radio-inline ri">
				<input type="radio" name="choice" id="inlineRadio1" value="1"><b>Rock</b><br>
				<div>
					<i class="fa fa-cube fa-5x" aria-hidden="true"></i>
				</div>
			</label>
			<label class="radio-inline ri">
				<input type="radio" name="choice" id="inlineRadio2" value="2">Paper<br>
				<div>
					<i class="fa fa-file-o fa-5x" aria-hidden="true"></i>
				</div>
			</label>
			<label class="radio-inline ri">
				<input type="radio" name="choice" id="inlineRadio3" value="3">Scissors<br>
				<div>
					<i class="fa fa-scissors fa-5x" aria-hidden="true"></i>
				</div>
			</label>
		</div>
		<div class="col-md-4">
		</div>

		<div class="col-md-5">
		</div>
		<div class="col-md-2 c">
			<br>
			<button name="submit" type="submit" class="btn btn-info"><i class="fa fa-play" aria-hidden="true"></i> Go!</button>
		</div>
		<div class="col-md-5">
		</div>
	</form>

	<div class="col-md-12">
		<hr>
	</div>

	<div class="col-md-4"></div>
	<div class="col-md-4 c">
		<?php
		//FINAL 
		// 0 == Tie
		// 1 == Loss
		// 2 == Win
		//RSP
		// 1 == Rock
		// 2 == Paper
		// 3 == Scissors
		$userScore = 0;
		$compScore = 0;
		if(!empty($_POST)) {
			if(!empty($_POST['choice'])){

				$user = $_POST['choice'];
				$comp = rand(1,3);

				if($comp == 1){
					$compText = 'Rock';
				}elseif($comp == 2){
					$compText = 'Paper';
				}elseif($comp == 3){
					$compText = 'Scissors';
				}

				if($user == 1){
					$userText = 'Rock';
					if($comp == 1){
						$final = 0;
					}elseif($comp == 2){
						$final = 1;
					}elseif($comp == 3){
						$final = 2;
					}
				}elseif($user == 2){
					$userText = 'Paper';
					if($comp == 1){
						$final = 2;
					}elseif($comp == 2){
						$final = 0;
					}elseif($comp == 3){
						$final = 1;
					}
				}elseif($user == 3){
					$userText = 'Scissors';
					if($comp == 1){
						$final = 1;
					}elseif($comp == 2){
						$final = 2;
					}elseif($comp == 3){
						$final = 0;
					}
				}

				if($final == 0){
					$finalText = '<span class="label label-warning">Tie</span>';
					$pointsF = 0.5;
					$pointsA = 0.5;
				}elseif($final == 1){
					$finalText = '<span class="label label-danger">Loss</span>';
					$pointsF = 0;
					$pointsA = 1;
				}elseif($final == 2){
					$finalText = '<span class="label label-success">Win</span>';
					$pointsF = 1;
					$pointsA = 0;
				}
				$_SESSION['userScore'] = $_SESSION['userScore'] + $pointsF;
				$_SESSION['compScore'] = $_SESSION['compScore'] + $pointsA;

				echo '<div class="col-md-6">
							<h2>User Score</h2>
							<h3>'. $_SESSION['userScore'] .'</h3>
						</div>
						<div class="col-md-6">
							<h2>Computer Score</h2>
							<h3>' . $_SESSION['compScore'] .'</h3>
					  </div>';

				echo '<table class="table table-striped"> 
						<thead> 
							<tr> 
								<th>Computer</th> 
								<th>User</th> 
								<th>Result</th> 
								<th>Points</th> 
							</tr> 
						</thead> 
						<tbody> 
							<tr> 
								<td>' . $compText .'</td> 
								<td>' . $userText . '</td> 
								<td>' . $finalText . '</td> 
								<td>' . (string)$pointsF . '</td> 
							</tr> 
						</tbody> 
					</table>';
			}else{
				echo '<div class="alert alert-danger alert-dismissible" role="alert">
					  	<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
					  	<strong>Error!</strong> Please Make a Selection
					  </div>';
			}
		}
	?>


	</div>
	<div class="col-md-4"></div>



  </div>
</div>
</body>

</html>
