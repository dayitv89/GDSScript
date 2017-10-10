// CJS is an extension of chrome to run your custom js code on some site. I used this to change default github header color black to navy blue color.
// set jquery 2.1.0 for host github.com
$(document).ready(function() {
	$('header').css('background-color', '#00478e');
});
