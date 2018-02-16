// Get the modal
var current_modal = document.getElementById('currentModal') ;

// Get the button that opens the modal
var current = document.getElementById("current_question") ;

var past = document.getElementById("past_question1") ;

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0] ;

var res = document.getElementById("Results") ;

 var yes = document.getElementById("Yes") ;
  var no = document.getElementById("No") ;
  var abs = document.getElementById("Abstained") ;
  var res = document.getElementById("Results") ;

var yes_result = 0
var no_result = 0
var abs_result = 0

// When the user clicks Yes, increment yes_results by 1
  yes.onclick = function() {
    yes_result += 1 ;
  }

  // When the user clicks No, increment no_results by 1
  no.onclick = function() {
    no_result += 1 ;
  }

  // When the user clicks Abstained, increment abs_results by 1
  abs.onclick = function() {
    abs_result += 1;
  }

// When the user clicks Results, show vote results
res.onclick = function() {
 alert("Yes: " + yes_result + '\n' +
 "No: " + no_result + '\n' +
 "Abstained: " + abs_result) ;
}

// When the user clicks the button, open the modal
current.onclick = function() {
  current_modal.style.display = "block" ;

  document.getElementById("question_name").innerHTML = "Question:" + document.getElementById("current_question").innerHTML ;
  document.getElementById("question_type").innerHTML = "Type of question:" + document.getElementById("hola").innerHTML ;
}

past.onclick = function() {
  current_modal.style.display = "block" ;

  document.getElementById("question_name").innerHTML = "Question:" + document.getElementById("past_question1").innerHTML ;
  document.getElementById("question_type").innerHTML = "Type of question: Enmienda" ;
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  current_modal.style.display = "none" ;
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == current_modal) {
    current_modal.style.display = "none" ;
  }
}