const lightThemePath = "/static/css/theme/light.css";
const darkThemePath = "/static/css/theme/darkmode.css";

/**
    * Toogle the theme
*/
const toggleTheme = () => {
    // get the element containing the style of the theme
    styleTag = document.getElementById("base-stylesheet");

    if (styleTag.href.includes(lightThemePath)) {
        styleTag.href = darkThemePath;
        // change Icon to display a sun
        document.getElementById("theme-icon").className = "fa fa-sun-o";
        setCookie("theme", "dark", "Fri, 31 Dec 9999 23:59:59 GMT");
    }

    else {
        styleTag.href = lightThemePath;
        // Change icon to display a moon
        document.getElementById("theme-icon").className = "fa fa-moon-o";
        setCookie("theme", "light", "Fri, 31 Dec 9999 23:59:59 GMT");
    }
};


// From the mozilla documentation https://developer.mozilla.org/en-US/docs/web/api/document/cookie
const getCookie = (name) => {
    cookie = document.cookie.split("; ").find(row => row.startsWith(name + "="));
    if (cookie != undefined) {
        return cookie.split("=")[1];
    }
    return null;
}

const setCookie = (name, value, expiration) => {
    document.cookie = name + "=" + value + "; expires=" + expiration + ";";
}



let theme = getCookie("theme");

// When page loads set theme according to cookie, if it exists
if (theme != null) {
    styleTag = document.getElementById("base-stylesheet");
    if (theme === "light" && !styleTag.href.includes("/static/css/theme/light.css"))
    {
        styleTag.href = "/static/css/theme/light.css";
        document.getElementById("theme-icon").className = "fa fa-moon-o";
    }
    else if (theme === "dark" && !styleTag.href.includes("/static/css/theme/darkmode.css"))
    {
        styleTag.href = "/static/css/theme/darkmode.css";
        document.getElementById("theme-icon").className = "fa fa-sun-o";
    }
}
