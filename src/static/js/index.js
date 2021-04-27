// From chart js documentation https://www.chartjs.org/docs/2.7.2/general/responsive.html
function resizeCharts() {
    for (var id in Chart.instances) {
        Chart.instances[id].resize();
    }
}


const toggleChartsDisposition = (dispositionName) => {
    
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
        // Resize the graphs
        resizeCharts();
    }
}


const addGraphHTML = (chartName, chartTitle) => {
    let chartContainerElement = document.querySelector(".charts-container");
    chartContainerElement.innerHTML += `
    <section id="${chartName}-section" class="chart">
        <h3 class="chart-title">${chartTitle}</h3>
        <div class="filters-chart" id="filters-chart-${chartName}">
        </div>
        
        <div class="chart-container">
            <canvas id="${chartName}" with="100%"></canvas>
        </div>
    </section>`;
}

const addSelectYearsFilter = (chart, chartName, years, allData, dataByYears) => {
    let chartFilters = document.getElementById(`filters-chart-${chartName}`);

    let yearsOptions = "";
    years.forEach((year) => {
        yearsOptions += `<option value="${year}">${year}</option>\n`
    });

    chartFilters.innerHTML += `
    <select name="years" id="${chartName}-select-years" class="select-years">
        <option value="all">Toutes les années</option>
        ${yearsOptions}
    </select>
    `
    document.getElementById(`${chartName}-select-years`).addEventListener("change", function() {
        chart.data.datasets.forEach(dataset => {
            if (this.value == "all") {
                dataset.data = Object.values(allData);
            }
            else {
                dataset.data = (Object.values(dataByYears[this.value]));
            }
        });
        chart.update();
    });
}


const plotBirthChartMoon = (data, label) => {
    let ctxBirthChartMoon = document.getElementById('birth-chart-moon').getContext('2d');
    let birthMoonChartParam = {
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
    };
    return new Chart(ctxBirthChartMoon, birthMoonChartParam);
}


function prematureDeathsByMonths(deces){
    
  var barChartData = {
    labels: ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],
    datasets: [{
      type: 'bar',
      label: 'Décès Prématurés',
      id: "y-axis-0",
      backgroundColor: "red",
      data: deces
    }]
  };


  var ctx = document.getElementById("premature-deaths-by-months");
  var ch = new Chart(ctx, {
    type: 'bar',
    data: barChartData,
    options: {
      title: {
        display: true,
        text: "Décès Prématurés - Durant L’année"
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        xAxes: [{
          stacked: true
        }],
        yAxes: [{
          stacked: true,
          position: "left",
          id: "y-axis-0",
        }]
      }
    }
  });
}


document.getElementById("list-icon").addEventListener("click", () => toggleChartsDisposition("list"));
document.getElementById("grid-icon").addEventListener("click", () => toggleChartsDisposition("grid"));


const birth_moon_label = graph_data["birth_moon_label"];
const birth_moon = graph_data["birth_moon"];
const birth_moon_by_years = graph_data["birth_moon_by_years"];
const deaths = graph_data["deaths"];


// Adding graph to html, (adding section with a title and a canvas for the graph)
addGraphHTML("birth-chart-moon", "Naissance selon le cycle lunaire");

addGraphHTML("premature-deaths-by-months", "Morts Prématurés par mois");


// Plot the graphs
let moonChart = plotBirthChartMoon(Object.values(birth_moon), birth_moon_label);
addSelectYearsFilter(moonChart, "birth-chart-moon", Object.keys(birth_moon_by_years), birth_moon, birth_moon_by_years);

prematureDeathsByMonths(deaths);