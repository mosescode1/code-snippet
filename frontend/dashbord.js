const user = document.querySelector(".username");
const addSnippetbtn = document.querySelector(".snippetBtn");
const main = document.querySelector(".main_body");


const BaseUrl = "http://127.0.0.1:5000";


class Dashboard {
	constructor() {
		this.user = JSON.parse(localStorage.getItem("user"));
		this.displayUser();
		this.getSnippet();
	}

	displayUser() {
		user.innerHTML = `${this.user.data.username}`;
	}

	displayUserSnippets() {

	}

	createSnippet() {

	}

	deleteSnippet() {

	}

	editSnippet() {

	}

	async getSnippet() {
		const params = {
			page: 1,
			limit: 7,
		};

		const queryString = new URLSearchParams(params).toString();
		const response = await fetch(BaseUrl + `/snippets?${queryString}`,)
		const data = await response.json()
		this._displaySnippets(data);
	}

	_displaySnippets(data) {

		data.forEach(snippet => {
			const value = this._snippets(snippet.snippet_type, snippet.snippet_code)
			main.insertAdjacentHTML("beforeend", value);
		});
	}

	_snippets(snippetTitle, snippetCode) {
		const innerHTML = `	<div
							class="flex items-center gap-4 bg-[#111a22] px-4 min-h-[72px] py-2">
							<div
								class="text-white flex items-center justify-center rounded-lg bg-[#243647] shrink-0 size-12"
								data-icon="CodeSimple"
								data-size="24px"
								data-weight="regular">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="24px"
									height="24px"
									fill="currentColor"
									viewBox="0 0 256 256">
									<path
										d="M93.31,70,28,128l65.27,58a8,8,0,1,1-10.62,12l-72-64a8,8,0,0,1,0-12l72-64A8,8,0,1,1,93.31,70Zm152,52-72-64a8,8,0,0,0-10.62,12L228,128l-65.27,58a8,8,0,1,0,10.62,12l72-64a8,8,0,0,0,0-12Z"></path>
								</svg>
							</div>
							<div class="flex flex-col justify-center">
								<p
									class="text-white text-base font-medium leading-normal line-clamp-1">
									${snippetTitle}
								</p>
								<p
									class="text-[#93adc8] text-sm font-normal leading-normal line-clamp-2">
									${snippetCode}
								</p>
							</div>
						</div>`;
		return innerHTML;
	}

}



const dash = new Dashboard();