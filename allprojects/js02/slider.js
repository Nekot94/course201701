var slideIndex = 1;
showSlides(slideIndex);
function plusSlide(n) {

	showSlides(slideIndex += n);

}
function currentSlide(n) {

	showSlides(slideIndex = n);

}
function showSlides(n) {

	var i = 0;
	var slides = document.getElementsByClassName('slide');
	var dots = document.getElementsByClassName('dot'); 
	if (n > slides.length) {
		slideIndex = 1;


	}
	if (n < 1) {
		slideIndex = slides.length;
	}
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	slides[slideIndex - 1].style.display = 'block'; 	
	for (i = 0; i < dots.length; i++) {
		dots[i].style.background = '#BBB';
	}
	dots[slideIndex - 1].style.background = '#777'; 
}

