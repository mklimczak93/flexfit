// --- MAIN --- //

document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#class-search-button').addEventListener('click', makeSearchViewVisible);
	//document.querySelector('#class-details-button').addEventListener('click', makeClassDetailsVisible);
	//document.querySelector('#edit-profile-button').addEventListener('click', makeEditProfileVisible);
	//document.querySelector('#profile-calendar-button').addEventListener('click', makeProfileCalendarVisible);


    // By default, load the feed
    makeSearchViewVisible();
  });


// --- SWITCHING WINDOWS --- //
// --- STANDARD USER --- //
function makeSearchViewVisible() {
	console.log("Search view visible");
	document.querySelector('#class-search').style.display = 'flex';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';
}

function makeEditProfileVisible() {
	console.log("Profile editing visible");
	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'flex';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';
}

function makeProfileCalendarVisible() {
	event.preventDefault();
	console.log("Profile calendar visible");
	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'flex';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';
}

function makeClassesListVisible() {
	event.preventDefault();
	console.log("List of classes visible");
	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'flex';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';

}
// --- STUDIO --- //

function makeAddClassPanelVisible() {
	event.preventDefault();
	console.log("Add class panel visible");
	document.querySelector('#studio-edit').style.display = 'none';
	document.querySelector('#studio-overview').style.display = 'none';
	document.querySelector('#add-classes').style.display = 'flex';
	document.querySelector('#studio-classes-calendar').style.display = 'none';
	document.querySelector('#studio-classes-list').style.display = 'none';
	document.querySelector('#studio-credits').style.display = 'none';
}

function makeStudioOverviewVisible() {
	event.preventDefault();
	console.log("Studio overview panel visible");
	document.querySelector('#studio-edit').style.display = 'none';
	document.querySelector('#studio-overview').style.display = 'flex';
	document.querySelector('#add-classes').style.display = 'none';
	document.querySelector('#studio-classes-calendar').style.display = 'none';
	document.querySelector('#studio-classes-list').style.display = 'none';
	document.querySelector('#studio-credits').style.display = 'none';
}

function makeStudioEditVisible() {
	event.preventDefault();
	console.log("Studio overview panel visible");
	document.querySelector('#studio-edit').style.display = 'flex';
	document.querySelector('#studio-overview').style.display = 'nne';
	document.querySelector('#add-classes').style.display = 'none';
	document.querySelector('#studio-classes-calendar').style.display = 'none';
	document.querySelector('#studio-classes-list').style.display = 'none';
	document.querySelector('#studio-credits').style.display = 'none';
}

function makeStudioCalendarVisible() {
	event.preventDefault();
	console.log("Studio calendar visible");
	document.querySelector('#studio-overview').style.display = 'none';
	document.querySelector('#add-classes').style.display = 'none';
	document.querySelector('#studio-classes-calendar').style.display = 'flex';
	document.querySelector('#studio-classes-list').style.display = 'none';
	document.querySelector('#studio-credits').style.display = 'none';
}

function makeStudioListVisible() {
	event.preventDefault();
	console.log("Studio classes list visible");
	document.querySelector('#studio-overview').style.display = 'none';
	document.querySelector('#add-classes').style.display = 'none';
	document.querySelector('#studio-classes-calendar').style.display = 'none';
	document.querySelector('#studio-classes-list').style.display = 'flex';
	document.querySelector('#studio-credits').style.display = 'none';

}

function makeStudioCreditsVisible() {
	event.preventDefault();
	console.log("Studio credits panel visible");
	document.querySelector('#studio-overview').style.display = 'none';
	document.querySelector('#add-classes').style.display = 'none';
	document.querySelector('#studio-classes-calendar').style.display = 'none';
	document.querySelector('#studio-classes-list').style.display = 'none';
	document.querySelector('#studio-credits').style.display = 'flex';

}

// --- END OF STUDIO --- //
// --- USER PROFILE --- //

function makeClassDetailsVisible(id) {
	event.preventDefault();
	console.log("Class details visible");
	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'flex';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';

	//getting right divs
	const classDetialsHalf1 	= document.getElementById("class-details-half1");
	const classDetialsHalf2 	= document.getElementById("class-details-half2");

	//getting a list of ID classes of which the user is signed up for
	fetch(`/signed_up_classes_list`)
	.then(response => response.json())
	.then(signedUpClassesList => {
		console.log(signedUpClassesList);

		//getting the chosen class data
		//document.location.href = "{% url 'show_chosen_class' class_id=class.id %}"
		fetch(`show_chosen_class/${id}`)
		.then(response => response.json())
		.then(chosenClass => {
			console.log(chosenClass.id);

			//filling in first half of the div with class data
			classDetialsHalf1.innerHTML =
			`
			<div class="profile-menu">
				<div class="profile-menu-div" style="padding: 0px;">
					<img src="${chosenClass.photo}" class="class-photo" alt="class photo">
					<h3 style="margin:10px;">${chosenClass.name}</h3>
					<div style="width:100%; display:flex; flex-direction:row; justify-content:space-around; padding-bottom: 0px;">
						<div class="small-middle">
							<h5>
								<i class="fa-solid fa-location-dot"></i>
								Location
							</h5>
							<h6>${chosenClass.address}</h6>
						</div>
						<div class="small-middle">
							<h5>
								<i class="fa-solid fa-calendar-days"></i>
								Time & date
							</h5>
							<h6>${chosenClass.date}</h6>
							<h6>${chosenClass.hour}</h6>
						</div>
						<div class="small-middle">
							<h5>
								<i class="fa-solid fa-clock"></i>
								Duration
							</h5>
							<h6>${chosenClass.duration} min</h6>
						</div>
					</div>
				</div>

				<div class="profile-menu-div">
					<div class="small-middle">
						<button id="class_sign_up_button" class="invis-button" >

						</button>
					</div>
					<div class="small-middle">
						<button class="invis-button" onclick="makeSearchViewVisible()">
							<h5>
								<i class="fa-solid fa-magnifying-glass"></i>
							</h5>
							<h5>Find other classes</h5>
						</button>
					</div>
				</div>
				<div class="profile-menu-div">
					<button class="invis-button" onclick="goToExplanation()">
						<h5>How FlexFit works</h5>
					</button>
				</div>
			</div>
			`;


			//filling in second half of the div with class data
			classDetialsHalf2.innerHTML =
			`
			<div class="calendar-heading-div">
				<h3 style="padding: 5px;">${chosenClass.name}</h3>
			</div>
			<div class="class-descr-div">
				<div style="width:100%;">
					<h4 style="margin-left: 0px; margin-bottom: 5px;"> Class information:</h4>
				</div>
				<div style="height: 100px;  overflow-y: scroll;" id="descitpion-div">
					<p>${chosenClass.description}</p>
				</div>
				<div style="width:100%; tex-align:left">
					<p onclick="makeWholeDiv()" style="justify-self:start; color:grey; text-size:8px;" id = "read-more-button">Read more</p>
				</div>
				<div style="width:100%; margin: 20px;">
					<h4 style="margin-left: 0px; margin-bottom: 5px;"> ${chosenClass.name} rating:</h4>
					<div style="width: 100%; display: flex; flex-direction: row; gap: 8px; padding-top: 15px;">

						<div style="width: 30%; padding-top: 10px;">
							<h1 style="font-size: 1.75rem;">${chosenClass.rating}</h1>
							<div class="five-stars" style="width: 1.75 rem; margin-top: -10px;">
								<i class="fa-solid fa-star" style="font-size: 7px;"></i>
								<i class="fa-solid fa-star" style="font-size: 7px;"></i>
								<i class="fa-solid fa-star" style="font-size: 7px;"></i>
								<i class="fa-solid fa-star" style="font-size: 7px;"></i>
								<i class="fa-solid fa-star" style="font-size: 7px;"></i>
							</div>
							<p>${chosenClass.rating_amount} ratings</p>
						</div>

						<div style="width: 50%; padding-right: 20px;">
							<div style="display: flex; flex-direction: row; justify-content: space-around;">
								<p>5</p>
								<div class="empty-bar">
									<div class="color-bar" id="fives">
									</div>
								</div>

							</div>
							<div style="display: flex; flex-direction: row; justify-content: space-around;">
								<p>4</p>
								<div class="empty-bar">
									<div class="color-bar" id="fours">
									</div>
								</div>
							</div>
							<div style="display: flex; flex-direction: row; justify-content: space-around;">
								<p>3</p>
								<div class="empty-bar">
									<div class="color-bar" id="threes">
									</div>
								</div>
							</div>
							<div style="display: flex; flex-direction: row; justify-content: space-around;">
								<p>2</p>
								<div class="empty-bar">
									<div class="color-bar" id="twos">
									</div>
								</div>
							</div>
							<div style="display: flex; flex-direction: row; justify-content: space-around;">
								<p>1</p>
								<div class="empty-bar">
									<div class="color-bar" id="ones">
									</div>
								</div>
							</div>

						</div>
					</div>

				</div>


				<!-- Class reviews to follow -->

				<div id="class_reviews" style="width:100%; margin: 10px;">
					<h4 style="margin-left: 0px; margin-bottom: 15px;"> ${chosenClass.name} reviews:</h4>



				</div>
			</div>
			`;


			//checking if the chosen class ID is in already signed up classes
			//& switching the signup button for cancel function
			const check = signedUpClassesList.includes(chosenClass.id);
			console.log(check);
			const classSignUpButton = document.getElementById("class_sign_up_button")

			if (signedUpClassesList.includes("user_not_logged_in")) {
				classSignUpButton.innerHTML =
					`
					<h5>
						<i class="fa-solid fa-right-to-bracket"></i>
					</h5>
					<h5>Register to sign up for the class</h5>
					`;
					classSignUpButton.setAttribute('onClick', "goToRegister()");
			}else{
				//if class ID already in signedup list
				if (check === true) {
					classSignUpButton.innerHTML =
					`
					<h5>
						<i class="fa-solid fa-xmark"></i>
					</h5>
					<h5>Cancel the sign up</h5>
					`;
					classSignUpButton.setAttribute('onClick', "cancelClass("+ chosenClass.id +")");


				} else {
					//if class ID NOT in the signedup list
					classSignUpButton.innerHTML =
					`
					<h5>
						<i class="fa-solid fa-right-to-bracket"></i>
					</h5>
					<h5>Sign up</h5>
					`;
					classSignUpButton.setAttribute('onClick', "signUpForClass("+ chosenClass.id +")");

				};
			};

			//reviews
			const classReviewsDiv = document.getElementById('class_reviews');
			const reviews = chosenClass.reviews;
			if (reviews.length === 0) {
				classReviewsDiv.innerHTML =
				`
				<h4 style="margin-left: 0px; margin-bottom: 15px;"> ${chosenClass.name} reviews:</h4>
				<div class="review">
					<p>There are no reviews for this class yet.</p>
				</div>
				`
			} else {
				console.log(chosenClass.id)
				fetch(`/class_reviews/${chosenClass.id}`)
				.then(response => response.json())
				.then(reviews_objects => {
					reviews_objects.forEach(review => {

						const reviewDiv = document.createElement("div");
						reviewDiv.innerHTML =
						`
						<div class="review" >
							<div style="width: 100%; display: flex; flex-direction:row;justify-content: space-between;">
								<h6>On ${review.date} ${review.author} said:</h6>
								<h6>${review.rate}<i class="fa-solid fa-star"></i></h6>
							</div>

							<div style="margin-top:10px;">
								<p>${review.description}</p>
							</div>
						</div>
						`;
						classReviewsDiv.appendChild(reviewDiv);
					});


				})

			};

			//adding rating spread to the graph
			document.getElementById("fives").style.width = chosenClass.fives + '%';
			document.getElementById("fours").style.width = chosenClass.fours + '%';
			document.getElementById("threes").style.width = chosenClass.threes + '%';
			document.getElementById("twos").style.width = chosenClass.twos + '%';
			document.getElementById("ones").style.width = chosenClass.ones + '%';

		});
	});
}

function makeWholeDiv() {
	let descriptionDiv = document.getElementById("descitpion-div");
	let readMoreButton = document.getElementById("read-more-button")
	descriptionDiv.style.height = "auto";
	if (descriptionDiv.style.height === "auto") {
		readMoreButton.onclick = function () {
			descriptionDiv.style.height = "100px";
		};
	} else {
		readMoreButton.onclick = function () {
			descriptionDiv.style.height = "auto";
		};
	};
}

function makeAddReviewPanelVisible(classID) {
	event.preventDefault();
	console.log("Add review panel visible");

	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'flex';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';


	//sending the id data
	fetch('/add_review', {
		method: 'POST',
		credentials: 'same-origin',
		headers: {
		"X-CSRFToken": csrftoken,
		"Accept": "application/json",
		'Content-Type': 'application/json'
    	},
		body: JSON.stringify({
			class_id: classID
		})
	  })
	  .then(response => response.json())
	  .then(result => {
		  // Print result
		  console.log(result);
	  });

	  //document.getElementById("class_review_submit_button").onsubmit = makeClassDetailsVisible(classID)
	  let submitInputButton = document.getElementById("class_review_submit_button");
	  submitInputButton.setAttribute('onSubmit', "makeClassDetailsVisible("+ classID +")");

}


// --- LINK TO FLEXFIT EXPLANATION --- //
function goToExplanation() {
	console.log(document.location.href);
	window.location.assign(document.location.href + "/credits");
}

function goToRegister() {
	console.log(document.location.href);
	window.location.assign(document.location.href + "/register");
}

function signUpForClass(classID) {
	console.log(classID);

	//sending the data
	fetch('/class_signup', {
		method: 'POST',
		body: JSON.stringify({
			class_id: classID
		})
	  })
	  .then(response => response.json())
	  .then(result => {
		  // Print result
		  console.log(result);
	  });
	//alert("Hey, you have signed up for the class! See you then!");
	//creating custom popup/modal instead of just alert
	let signingUpPopup = document.createElement("div");
	signingUpPopup.id = "signing_up_popup_id"
	console.log("Created div")
	//adding CSS with class
	signingUpPopup.classList.add("signing_up_popup");
	//adding a message
	signingUpPopup.innerHTML =
		`
		<div>
			<h3>Hey you!</h3>
			<br>
			<p>You have just signed up for the class!</p>
			<p>See you then and there!</p>
		</div>
		<br>
		<div style="width: 100%; display: flex; justify-content: center;">
			<button id="OK-sign-up-button" class="sign-up-button" onclick="hideThePopUp()">OK!</button>
		</div>
		`
	//actually showing it
	event.preventDefault();
	document.getElementById("container2").appendChild(signingUpPopup);
	signingUpPopup.style.display = 'block';


	//switching it back to signup
	const classSignUpButton = document.getElementById("class_sign_up_button")
	classSignUpButton.innerHTML =
	`
	<h5>
		<i class="fa-solid fa-xmark"></i>
	</h5>
	<h5>Cancel the sign up</h5>
	`;
	classSignUpButton.setAttribute('onClick', "cancelClass("+ classID +")");

	//hiding it
	document.getElementById("OK-sign-up-button").onclick = function() {
		signingUpPopup.style.display = 'none';
		//refreshing site
		document.location.reload()
	}





}


function cancelClass(classID) {
	console.log(classID);

	//sending the data
	fetch('/class_cancel', {
		method: 'POST',
		body: JSON.stringify({
			class_id: classID
		})
	  })
	  .then(response => response.json())
	  .then(result => {
		  // Print result
		  console.log(result);
	  });
	//alert("Hey, you have signed up for the class! See you then!");
	//creating custom popup/modal instead of just alert
	let signingUpPopup = document.createElement("div");
	signingUpPopup.id = "signing_up_popup_id"
	console.log("Created div")
	//adding CSS with class
	signingUpPopup.classList.add("signing_up_popup");
	//adding a message
	signingUpPopup.innerHTML =
		`
		<div>
			<h3>Hey you!</h3>
			<br>
			<p>You have cancelled the sign up.</p>
			<p>Take care!</p>
		</div>
		<br>
		<div style="width: 100%; display: flex; justify-content: center;">
			<button id="OK-sign-up-button" class="sign-up-button" onclick="hideThePopUp()">OK!</button>
		</div>
		`
	//actually showing it
	event.preventDefault();
	document.getElementById("container2").appendChild(signingUpPopup);
	signingUpPopup.style.display = 'block';

	//switching it back to signup
	const classSignUpButton = document.getElementById("class_sign_up_button")
	classSignUpButton.innerHTML =
	`
	<h5>
		<i class="fa-solid fa-right-to-bracket"></i>
	</h5>
	<h5>Sign up</h5>
	`;
	classSignUpButton.setAttribute('onClick', "signUpForClass("+ classID +")");

	//hiding it
	document.getElementById("OK-sign-up-button").onclick = function() {
		signingUpPopup.style.display = 'none';
		//refreshing site
		document.location.reload()
	}



}


function hideThePopUp() {
	document.getElementById("signing_up_popup_id").style.display = 'none';
	//refreshing site
	document.location.reload()
}

function hideAnyPopUp(id) {
	document.getElementById(id).style.display = 'none';
}

// --- NAVBAR MENU --- //
document.addEventListener('DOMContentLoaded', function() {
	event.preventDefault();
	const toggleButton = document.getElementsByClassName('toggle-button')[0]
	const navbarLinks = document.getElementsByClassName('navbar-links')[0]

	toggleButton.addEventListener('click', () => {
		console.log('ToggleButton doing something');
		navbarLinks.classList.toggle('active')
	})
})


// --- CALENDAR VIEW - NEXT MONTH --- //
document.addEventListener('DOMContentLoaded', function() {
	event.preventDefault();
	const previousMonthButton 	= document.getElementById("previous-month-button");
	const nextMonthButton 		= document.getElementById("next-month-button");
	const calendarDiv 			= document.getElementById("calendar");
	const year 					= document.querySelector('#year-number').value;
	const month 				= document.querySelector('#calendar').value;
	const previousMonth 		= month - 1;

	previousMonthButton.addEventListener('click', () => {
		console.log(year, month);
		calendarDiv.innerHTML =
		`
		<div class="calendar-title">
                    <button class="small-button" id="previous-month-button">
                        <i class="fa-solid fa-caret-left"></i>
                    </button>
                    <h3>${previousMonth} ${year}</h3>
                    <button class="small-button" id="next-month-button">
                        <i class="fa-solid fa-caret-right"></i>
                    </button>
                </div>
                <div class="calendar-days">
                    <!-- days of the week -->
                    <div class="day-name"> Mon </div>
                    <div class="day-name"> Tue </div>
                    <div class="day-name"> Wed </div>
                    <div class="day-name"> Thu </div>
                    <div class="day-name"> Fri </div>
                    <div class="day-name"> Sat </div>
                    <div class="day-name"> Sun </div>
                    <!-- previous month days -->

                    <div class="day2"> {{i}} </div>

                    <!-- current month days -->

                    <div class="today" id="{{i}}">{{i}}</div>

                    <div class="day" id="{{i}}">{{i}}</div>

                    <!-- future month days -->

                    <div class="day2">{{i}}</div>

                </div>
		`;
	});
})

// --- CALENDAR VIEW - SHOW CLASSES FOR THE DAY --- //
function showClassesForTheDay(day_var) {
	//event.preventDefault();

	//getting current date
	const date 			= new Date();
	const currentYear 	= date.getFullYear();
	let currentMonth 	= date.getMonth()+1;
	const currentDay	= date.getDate();

	//getting user's classes
	fetch(`/show_classes_for_day`)
	.then(response => response.json())
	.then(classes => {
		const givenDay = day_var;
		//format example 2023-05-23
		if (currentMonth.length = 1){
			currentMonth = '0' + String(currentMonth)
		}
		const givenDate = currentYear + '-' + currentMonth + '-' + givenDay;
		//setting basic case
		document.querySelector('#class-info-calendar').innerHTML =
			`
			<h5>You haven't signed up for any classes for this day.</h5>
			`
		classes.forEach (element => {
			const elementDate = element.time.slice(0, 10)
			console.log(elementDate, givenDate)
			if (elementDate === givenDate) {
				const elementTime = element.time.slice(11, 16)
				document.querySelector('#class-info-calendar').innerHTML =
				`
				<div>
					<h5>${elementTime}</h5>
					<h6>${element.duration} min</h6>
				</div>
				<div>
					<h4>${element.name}</h4>
					<h6 style="font-weight: 400;">
						${element.get_class_rating}
						<i class="fa-solid fa-star"></i>
					</h6>
				</div>
				<div>
					<h5>${element.studio.name}</h5>
					<h6>${element.address}</h6>
				</div>
				<div>
					<button class="sign-up-button" id="class-details-button">See details</button>
				</div>
				`;
			}

		})


	})


}


// --- CREDITS VIEW ---//
function seeCreditsPanel() {
	console.log("Credits panel visible");

	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'flex';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'none';
}

// --- ADD CREDITS VIEW ---//
function showAddCreditsView() {
	console.log("Add credits view visible");
	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'flex';
	document.querySelector('#change-plan').style.display = 'none';
}

// --- CHANGE PLAN VIEW ---//
function showChangePlanView() {
	console.log("Change plan view visible");
	document.querySelector('#class-search').style.display = 'none';
	document.querySelector('#class-details').style.display = 'none';
	document.querySelector('#edit-profile').style.display = 'none';
	document.querySelector('#profile-calendar').style.display = 'none';
	document.querySelector('#classes_list').style.display = 'none';
	document.querySelector('#review-panel').style.display = 'none';
	document.querySelector('#credits-panel').style.display = 'none';
	document.querySelector('#add-credits-panel').style.display = 'none';
	document.querySelector('#change-plan').style.display = 'flex';
}

// --- SHOWING ELEMENT AFTER RESOLVE ---//
function showElement(element, mSeconds) {
    return new Promise((resolve, reject) => {
        element.classList.remove('none');
        element.classList.add('block');
        setTimeout( () => {
            element.classList.remove('block');
            element.classList.add('none');
            resolve();
        }, mSeconds);
    });
}
// --- CHANGE CURRENT PLAN ---//
function changeCurrentPlan(planNo) {
	console.log(planNo)
	console.log('start sending plan info');
	//sending new planNo
	fetch('/change_plan', {
		method: 'POST',
		credentials: 'same-origin',
		headers: {
		"X-CSRFToken": csrftoken,
		"Accept": "application/json",
		'Content-Type': 'application/json'
    	},
		body: JSON.stringify({
			"plan_no": planNo
		})
	  })
	  .then(response => response.json())
	  .then(result => {
		// Print result
		console.log(result);

	  });

	//showing right divs
	//document.location.reload()
	seeCreditsPanel()
	//let planDivContent = document.getElementById("credits-plan-div").innerHTML;
	//planDiv.reload()
	//jquery
	//$("#credits-plan-div").load(window.location.href + " credits-plan-div");
	//setInterval(function() {
		//document.getElementById('credits-plan-div').innerHTML = planDivContent;
		//}, 1000);

	// I KNOW I SHOULD NOT HARDCODE STUFF HERE,
	// BUT I CANNOT REFRESH JUST THE DIV, SO HERE IT COMES, SORRYYYYY //
	let creditsTitle =  document.getElementById("credits-title");
	let creditsPrice =  document.getElementById("price");

	let planNo2 = planNo.replace('/mo','');
	creditsTitle.innerHTML =
	`
	${planNo2}
	`;
	if (planNo2 === '9 credits/mo') {
		creditsPrice.innerHTML =
		`
		39 pln/mo
		`;
	} else if (planNo2 === '25 credits/mo') {
		creditsPrice.innerHTML =
		`
		59 pln/mo
		`;
	} else if (planNo2 === '47 credits/mo') {
		creditsPrice.innerHTML =
		`
		79 pln/mo
		`;
	} else if (planNo2 === '64 credits/mo') {
		creditsPrice.innerHTML =
		`
		99 pln/mo
		`;
	} else if (planNo2 === '80 credits/mo') {
		creditsPrice.innerHTML =
		`
		119 pln/mo
		`;
	};

}

//--- POPUP DO YOU WANT TO CHANGE YOUR PLAN --- //
function popUpChangePlan(planNo) {
	console.log(planNo);
	//creating custom popup/modal instead of just alert
	let changePlanPopup = document.createElement("div");
	changePlanPopup.id = "change_plan_popup_id"
	console.log("Created div")
	//adding CSS with class
	changePlanPopup.classList.add("signing_up_popup");
	//adding a message
	changePlanPopup.innerHTML =
		`
		<div>
			<div class="full-row">
				<h3>Hey you!</h3>
				<button class="simple" onclick="hideAnyPopUp('change_plan_popup_id')" id="x-button-popup">
					<i class="fa-solid fa-xmark"></i>
				</button>
			</div>
			<br>
			<p>Do you want to change your plan for the one below?</p>
			<br>
			<div class="plan-name-tag">${planNo}</div>
		</div>
		<br>
		<div style="width: 100%; display: flex; justify-content: center;">
			<button id="change-plan-button" class="sign-up-button">Change!</button>
		</div>
		`

	//actually showing it
	event.preventDefault();
	document.getElementById("container2").appendChild(changePlanPopup);
	changePlanPopup.style.display = 'block';

	//setting onclick attribute
	let changeButton = document.getElementById("change-plan-button")
	//changeButton.setAttribute('onClick', "changeCurrentPlan("+ planNo +")");
	//changeButton.addEventListener("click", changeCurrentPlan(planNo))
	//changeButton.onclick = function(planNo) {
	//	changeCurrentPlan(planNo);
	//	changePlanPopup.style.display = 'none';
	//}
	//changeButton.addEventListener('click', (planNo) => {
	//	changeCurrentPlan(planNo);
	//	changePlanPopup.style.display = 'none';
	//});
	changeButton.addEventListener('click', function(sth) {
		changeCurrentPlan(planNo);
		changePlanPopup.style.display = 'none';
		//navigating back to credits section & refreshing data

	});

	//hiding it
	document.getElementById("change-plan-button").onclick = function() {
		changePlanPopup.style.display = 'none';
	}
	document.getElementById("x-button-popup").onclick = function() {
		changePlanPopup.style.display = 'none';
	}


}


// --- SHOW MAP --- //
//center of the map - Warsaw
let center = [21.01, 52.23]
document.addEventListener('DOMContentLoaded', function() {
	var map = tt.map({
		key: "gMhmRVyr2CeKgo9xRFR0r40VPf1A5BIt",
		container: "map",
		center: center,
		zoom: 12,
		style: 'static/fitflex_map.json',
	});


	//creating marker per class
	//getting user's classes
	fetch(`/show_all_classes`)
	.then(response => response.json())
	.then(classes => {
		classes.forEach (givenClass => {
			//logging the locations' coordinates & adapting their format
			console.log(givenClass.location)
			const givenLocation = givenClass.location.split(',');

			//creating individaul divs for markers
			var element = document.createElement("div")
			element.innerHTML =
			`
			<i class="fa-solid fa-location-dot"></i>
			`;
			element.className = "marker";
			//creating markers
			var marker = new tt.Marker({ element: element })
  			.setLngLat(givenLocation)
  			.addTo(map);

			//creating popups
			var popupOffsets = {
				top: [0, 0],
				bottom: [0, -70],
				"bottom-right": [0, -70],
				"bottom-left": [0, -70],
				left: [25, -35],
				right: [-25, -35],
			  };
			var customPopup =
			`<div class="popup-info">`+
			`<img src="${givenClass.photo}" class="profile-picture" style="height:50px;width:50px;margin:10px;">`+
			`<div>`+
			`<h3 style="color:black"> ${givenClass.name} </h3>` +
			`<h5 style="color:black"> ${givenClass.address} </h5>`+
			`</div></div>`

			var popup = new tt.Popup({ offset: popupOffsets }).setHTML(customPopup);

			//popup marker connection
			marker.setPopup(popup);
	});

	});

})

