function changeColor() {
	var theme = document.getElementById("theme");
	var themeValue = theme.options[theme.selectedIndex].value;
	var rootVariables = document.querySelector(":root");

	if (themeValue == "Purple") {
		rootVariables.style.setProperty('--currentColor', 'var(--purpleColor)');
		rootVariables.style.setProperty('--currentTransperant', 'var(--purpleTransperant)');
	}
	else if (themeValue == "Red") {
		rootVariables.style.setProperty('--currentColor', 'var(--redColor)');
		rootVariables.style.setProperty('--currentTransperant', 'var(--redTransperant)');
	}
	else if (themeValue == "Orange") {
		rootVariables.style.setProperty('--currentColor', 'var(--orangeColor)');
		rootVariables.style.setProperty('--currentTransperant', 'var(--orangeTransperant)');
	}
	else if (themeValue == "Green") {
		rootVariables.style.setProperty('--currentColor', 'var(--greenColor)');
		rootVariables.style.setProperty('--currentTransperant', 'var(--greenTransperant)');
	}
	else if (themeValue == "Blue") {
		rootVariables.style.setProperty('--currentColor', 'var(--blueColor)');
		rootVariables.style.setProperty('--currentTransperant', 'var(--blueTransperant)');
	}
	else if (themeValue == "Brown") {
		rootVariables.style.setProperty('--currentColor', 'var(--brownColor)');
		rootVariables.style.setProperty('--currentTransperant', 'var(--brownTransperant)');
	}
}

window.onload = function () {
	// Try to read from local storage, otherwise set to default
	let currentTheme = localStorage.getItem("mytheme") || "Red";
	const themeSelector = document.getElementById("theme");

	// Set the theme that we read from local storage
	setTheme("Red", currentTheme);
	themeSelector.value = currentTheme;
	changeColor();

	// Add change event listener
	themeSelector.addEventListener("change", function (e) {
		// Get the user's choice from the event object `e`.
		const newTheme = e.currentTarget.value;
		// Set the theme
		setTheme(currentTheme, newTheme);
	});

	function setTheme(oldTheme, newTheme) {
		const body = document.getElementsByTagName("body")[0];
		// Remove old theme scope from body's class list
		body.classList.remove(oldTheme);
		// Add new theme scope to body's class list
		body.classList.add(newTheme);
		// Set it as current theme
		currentTheme = newTheme;
		// Store the new theme in local storage
		localStorage.setItem("mytheme", newTheme);
	}
};
