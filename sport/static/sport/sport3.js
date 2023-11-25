// --- CAROUSEL IN CREDIT SECTION --- //
document.addEventListener('DOMContentLoaded', function() {
	event.preventDefault();

	//getting the carousel 'slides' in credits page
	const slide1 = document.getElementById('kasia');
	const slide2 = document.getElementById('monika');
	const slide3 = document.getElementById('tomek');
	const slides = [slide1, slide2, slide3];
	const slideWidth = slide1.getBoundingClientRect().width;

	//getting the buttons in credits page
	const previousButton 	= document.getElementById('plans-carousel-previous-button');
	const nextButton 		= document.getElementById('plans-carousel-next-button');

	//moving the plan slides wih previous/next buttons
	nextButton.addEventListener('click', () => {
		slides.scrollLeft += planWidth;
	});
	previousButton.addEventListener('click', () => {
		slides.scrollLeft -= planWidth;
	});


})