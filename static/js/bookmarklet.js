if (!($ = window.jQuery)) { // typeof jQuery=='undefined' works too  
	script = document.createElement( 'script' );  
	script.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js';   
	script.onload=makeApiCall;  
	document.body.appendChild(script);  
}   
else {  
    makeApiCall();  
}  
  
function makeApiCall() {  
	console.log('Making API Call');
	console.log(theSuperprettyUrl);
	
	$.get(theSuperprettyUrl, function() {
		console.log( "Success" );
	})
	.done(function(data) {
		console.log(data);
	})
	.fail(function(xhr, status, error) {
		console.log( "Error" );
	});
} 