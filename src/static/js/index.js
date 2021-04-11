let ctxBirthChartMoon = document.getElementById('birth-chart-moon-cycle').getContext('2d');
const changeChartsDisposition = (dispositionName) => {
  if (dispositionName === "list")
  {
    document.documentElement.style.setProperty("--chart-width", "100%");
  }
  else if (dispositionName === "grid")
  {
    document.documentElement.style.setProperty("--chart-width", "50%");
  }
}


document.getElementById("list-icon").addEventListener("click", () => changeChartsDisposition("list"));
document.getElementById("grid-icon").addEventListener("click", () => changeChartsDisposition("grid"));



const plotBirthChartMoon = (data, label) => {

    new Chart(ctxBirthChartMoon, {
        type: 'bar',
        responsive: false,
        maintainAspectRatio : false,
        data: {
            labels: label,
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


function stacked_bar_plot(listes_familles, Vivants, Morts_nés, Décès){
  Chart.defaults.global.elements.line.fill = false;
  var barChartData = {
    labels: listes_familles,
    datasets: [{
      type: 'bar',
      label: 'Vivants',
      id: "y-axis-0",
      backgroundColor: "green",
      data: Vivants
    }, {
      type: 'bar',
      label: 'Morts_nés',
      id: "y-axis-0",
      backgroundColor: "red",
      data: Morts_nés
    },{
      type: 'bar',
      label: 'Décès',
      id: "y-axis-0",
      backgroundColor: "orange",
      data: Décès
    }]
  };


  var ctx = document.getElementById("myChart");
  var ch = new Chart(ctx, {
    type: 'bar',
    data: barChartData,
    options: {
      title: {
        display: true,
        text: "Chart.js Bar Chart - Stacked"
      },
      tooltips: {
        mode: 'label'
      },
      responsive: true,
      scales: {
        xAxes: [{
          stacked: true
        }],
        yAxes: [{
          stacked: true,
          position: "left",
          id: "y-axis-0",
        }, {
          stacked: false,
          position: "right",
          id: "y-axis-1",
        }]
      }
    }
  });
}