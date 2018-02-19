// Get the modal
  var modal = document.getElementById('myModal') ;

  // Get the button that opens the modal
  var btn = document.getElementById("myBtn") ;

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0] ;

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
  btn.onclick = function() {
    modal.style.display = "block" ;

    document.getElementById("current_question_name").innerHTML = "Question:" + document.getElementById("myBtn").innerHTML ;
    document.getElementById("current_question_type").innerHTML = "Type of question: default" ;
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none" ;
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none" ;
    }
  }