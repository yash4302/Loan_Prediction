function changeColor() {
	var theme = document.getElementById("theme");
	var themeValue = theme.options[theme.selectedIndex].value;
	var rootVariables = document.querySelector(":root");
	var colorPicker = document.getElementById("colorPicker");
	colorPicker.disabled = true;
	colorPicker.style.display = "none";

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
	else if (themeValue == "Random") {
		colorPicker.disabled = false;
		colorPicker.style.display = "inline-block";
		var color = colorPicker.value;
		rootVariables.style.setProperty('--currentColor', color);
		rootVariables.style.setProperty('--currentTransperant', color+'20');
	}
}

function getColor_setTheme() {
	var colorPicker = document.getElementById("colorPicker");
	var color = colorPicker.value;

	var rootVariables = document.querySelector(":root");
	rootVariables.style.setProperty('--currentColor', color);
	rootVariables.style.setProperty('--currentTransperant', color+'20');
}

window.onload = function () {
	// Try to read from local storage, otherwise set to default
	var themeSelector = document.getElementById("theme");
	var currentTheme;

	if (theme == "Random") {
		currentTheme = localStorage.getItem("mytheme") || document.getElementById("colorPicker").value;
	} else {
		currentTheme = localStorage.getItem("mytheme") || "Red";
	}
	
	let currentColor = localStorage.getItem("mycolor") || "#000000";
	const colorSelector = document.getElementById("colorPicker");

	// Set the theme that we read from local storage
	setColor("#000000", currentColor);
	setTheme("Red", currentTheme);
	themeSelector.value = currentTheme;
	colorSelector.value = currentColor;
	changeColor();

	// Add change event listener
	themeSelector.addEventListener("change", function (e) {
		// Get the user's choice from the event object `e`.
		const newTheme = e.currentTarget.value;
		// Set the theme
		setTheme(currentTheme, newTheme);
	});

	// Add change event listener
	colorSelector.addEventListener("change", function (e) {
		// Get the user's choice from the event object `e`.
		const newColor = e.currentTarget.value;
		// Set the theme
		setColor(currentColor, newColor);
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

	function setColor(oldColor, newColor) {
		const body = document.getElementsByTagName("body")[0];
		// Remove old theme scope from body's class list
		body.classList.remove(oldColor);
		// Add new theme scope to body's class list
		body.classList.add(newColor);
		// Set it as current theme
		currentColor = newColor;
		// Store the new theme in local storage
		localStorage.setItem("mycolor", newColor);
	}
};
