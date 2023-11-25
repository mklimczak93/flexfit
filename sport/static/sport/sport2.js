// --- CAROUSEL IN PLANS SECTION --- //

document.addEventListener('DOMContentLoaded', function() {
	event.preventDefault();

	//getting the carousel 'slides' in plans page
	const plan1 = document.getElementById('plan1');
	const plan2 = document.getElementById('plan2');
	const plan3 = document.getElementById('plan3');
	const plan4 = document.getElementById('plan4');
	const plan5 = document.getElementById('plan5');
	const plans = [plan1, plan2, plan3, plan4, plan5];
	const plansDiv = document.getElementById('plans-list');
	const planWidth = plan1.getBoundingClientRect().width;

	//getting the buttons in plans page
	const previousButton 	= document.getElementById('plans-carousel-previous-button');
	const nextButton 		= document.getElementById('plans-carousel-next-button');

	//moving the plan slides wih previous/next buttons
	nextButton.addEventListener('click', () => {
		//plans.style.transform = 'translateX(' + planWidth + ')'
		plansDiv.scrollLeft += planWidth;
	});
	previousButton.addEventListener('click', () => {
		//plans.style.transform = 'translateX(' + planWidth + ')'
		plansDiv.scrollLeft -= planWidth;
	});

})