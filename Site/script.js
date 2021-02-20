const isMobile = screen.height > screen.width;
const mainNav = document.querySelector("#main-nav");

if(isMobile) {
	configMobile();
}

function configMobile() {
	const navHamburger = document.querySelector("#nav-hamburger");
	navHamburger.style.display = "inline";

	const content = document.querySelector("#content");
	content.style.margin = "50px";
	content.style.textAlign = "start";

	const team = document.querySelectorAll("div.person");
	team.forEach((person) => {
		person.style.display = "block";
		person.style.textAlign = "center";
	});

	const portraits = document.querySelectorAll("img.portrait");
	portraits.forEach((portrait) => {
		portrait.style.width = "250px";
		portrait.style.height = "250px";
		portrait.style.borderRadius = "500px";
		console.log(portrait);
	});

	mainNav.style.fontSize = "3rem";
	toggleNav();
}

function toggleNav() {
	if(mainNav.style.display == "none") {
		mainNav.style.display = "block";
	} else {
		mainNav.style.display = "none";
	}
}