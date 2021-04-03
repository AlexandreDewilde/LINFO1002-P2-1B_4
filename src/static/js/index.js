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