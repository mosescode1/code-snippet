
const hambugerBtn = document.querySelector('#hamburger');
const nav = document.querySelector('nav');
const closeNav = document.querySelector('.close__nav');
const loginNav = document.querySelector("#login");
const loginBttn = document.querySelector("#loginBtn");
const loginFormUsename = document.querySelector("#login__username");
const loginFormPassword = document.querySelector("#login__password");
const loginSection = document.querySelector(".login");

const closeLoginNav = document.querySelector(".close__login");

const BaseUrl = "http://127.0.0.1:5000";
// const BaseUrl = 'https://t86hc55r-5000.euw.devtunnels.ms/'
class App {
	constructor() {
		hambugerBtn.addEventListener('click', this.handleHamburger);
		closeNav.addEventListener('click', this.handleCloseBtn);
		loginBttn.addEventListener('click', this.handleLogin)
		loginNav.addEventListener("click", this.handleLoginNav)
		closeLoginNav.addEventListener("click", this.handleCloseBtnNav)
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

	handleLoginNav() {
		loginSection.classList.remove("hidden");
	}

	handleCloseBtnNav() {
		loginSection.classList.add("hidden");
	}

	async handleLogin(e) {
		e.preventDefault();

		if (!loginFormPassword.value || !loginFormUsename.value) return;


		const loginData = {
			username: loginFormUsename.value,
			password: loginFormPassword.value,
		}

		const user = await loginFunc(BaseUrl, loginData);
		if (user) {
			localStorage.setItem("user", JSON.stringify(user));
			location.href = "dashboard.html";
		}
	}
}
const app = new App();


// Login Function

const loginFunc = async (BaseUrl, loginData) => {
	try {
		const response = await fetch(`${BaseUrl}/auth/login`, {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(loginData)
		})

		const data = await response.json();
		if (data.status === 'fail') {
			console.log("failed");
			return
		} else {
			return data;
		}

	} catch (err) {
		console.log(err)
	}

}