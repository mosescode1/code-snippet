const hambugerBtn = document.querySelector('#hamburger');
const nav = document.querySelector('nav');
const closeNav = document.querySelector('.close__nav');

class App {
	constructor() {
		hambugerBtn.addEventListener('click', this.handleHamburger);
		closeNav.addEventListener('click', this.handleCloseBtn);
	}

	handleHamburger() {
		nav.style.display = 'block';
		hambugerBtn.style.display = 'none';
		closeNav.style.display = 'block';
	}

	handleCloseBtn() {
		nav.style.display = 'none';
		closeNav.style.display = 'none';
		hambugerBtn.style.display = 'block';
	}
}

const app = new App();
