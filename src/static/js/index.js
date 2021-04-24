let ctxBirthChartMoon = document.getElementById('birth-chart-moon-cycle').getContext('2d');

// From chart js documentation https://www.chartjs.org/docs/2.7.2/general/responsive.html
function resizeCharts() {
  for (var id in Chart.instances) {
    Chart.instances[id].resize()
  }
}

const changeChartsDisposition = (dispositionName) => {
  if (dispositionName === "list")
  {
    document.documentElement.style.setProperty("--chart-width", "100%");
    document.documentElement.style.setProperty("--chart-height", "50vh");
    // This function is needed to resized the chart
    resizeCharts();
  }
  else if (dispositionName === "grid")
  {
    document.documentElement.style.setProperty("--chart-width", "48%");
    document.documentElement.style.setProperty("--chart-height", "40vh");
    resizeCharts();
  }
}


document.getElementById("list-icon").addEventListener("click", () => changeChartsDisposition("list"));
document.getElementById("grid-icon").addEventListener("click", () => changeChartsDisposition("grid"));


const plotBirthChartMoon = (data, label) => {

    new Chart(ctxBirthChartMoon, {
        type: 'bar',
        data: {
            labels: label,
            datasets: [{
                label: 'Naissances par jour du cycle lunaire',
                data: data,
                backgroundColor: "#388E8E",
                borderColor: "#388E8E",
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}


function stacked_bar_plot(deces){
  Chart.defaults.global.elements.line.fill = false;
  var barChartData = {
    labels: [1,2,3,4,5,6,7,8,9,10,11,12],
    datasets: [{
      type: 'bar',
      label: 'Décès Prématurés',
      id: "y-axis-0",
      backgroundColor: "red",
      data: deces
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