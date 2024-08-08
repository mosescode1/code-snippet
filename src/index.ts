import './css/index.css'
const hambugerBtn = document.querySelector("#hamburger") as HTMLElement;
const nav = document.querySelector("nav") as HTMLElement;
const closeNav = document.querySelector(".close__nav") as HTMLElement;


class App{
	constructor() {
		hambugerBtn.addEventListener("click", this.handleHamburger);
		closeNav.addEventListener("click", this.handleCloseBtn);
	}

	private handleHamburger() {
		nav.style.display = "block";
		hambugerBtn.style.display = "none";
		closeNav.style.display = "block";

	}

	private handleCloseBtn() {
		nav.style.display = "none";
		closeNav.style.display = 'none';
		hambugerBtn.style.display = 'block';
	}
}


const app = new App();
