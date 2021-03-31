toggleTheme = () => {
    styleTag = document.getElementById("base-stylesheet");
    if (styleTag.href.includes("/static/css/light.css")) {
        styleTag.href = "/static/css/darkmode.css";
        setCookie("theme", "dark", "Fri, 31 Dec 9999 23:59:59 GMT");
        document.getElementById("checkbox-theme").checked = true;
    } 
    else {
        styleTag.href = "/static/css/light.css";
        setCookie("theme", "light", "Fri, 31 Dec 9999 23:59:59 GMT");
        document.getElementById("checkbox-theme").checked = false;
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

if (theme != null) {
    styleTag = document.getElementById("base-stylesheet");
    if (theme === "light" && !styleTag.href.includes("/static/css/light.css"))
    {
        styleTag.href = "/static/css/light.css";
        document.getElementById("checkbox-theme").checked = false;
    }
    else if (theme === "dark" && !styleTag.href.includes("/static/css/darkmode.css"))
    {
        styleTag.href = "/static/css/darkmode.css";
        document.getElementById("checkbox-theme").checked = true;
    }
}