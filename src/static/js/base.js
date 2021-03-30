// TODO create a cookie for light theme and dark theme


toggleTheme = () => {
    styleTag = document.getElementById("base-stylesheet");
    styleTag.href = styleTag.href.includes("/static/css/light.css") ? "/static/css/darkmode.css" : "/static/css/light.css";
};
