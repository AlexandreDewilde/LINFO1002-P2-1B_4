let ctxBirthChartMoon = document.getElementById('birth-chart-moon-cycle').getContext('2d');


const plotBirthChartMoon = (data) => {

    new Chart(ctxBirthChartMoon, {
        type: 'bar',
        responsive: true,
        maintainAspectRatio :false,
        data: {
            labels: [...Array(30).keys()],
            datasets: [{
                label: 'Naissances par jour du cycle lunaire',
                data: data,
                backgroundColor: "#C0756F",
                borderColor: "#C0756F",
                borderWidth: 1
            }]
        }
    });
}