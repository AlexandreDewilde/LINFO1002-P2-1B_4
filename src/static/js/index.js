// From chart js documentation https://www.chartjs.org/docs/2.7.2/general/responsive.html
function resizeCharts() {
    for (var id in Chart.instances) {
        Chart.instances[id].resize();
    }
}

/**
  * Change the disposition of graph in the page
  * @param {string} dispositionName - The new disposition to adopt : list or grid
*/
const toggleChartsDisposition = (dispositionName) => {
    
    if (dispositionName === "list")
    {
        document.documentElement.style.setProperty("--chart-width", "90%");
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

/**
    * Add a container for graph in the html in the charts container section
    * @param {string} chartName- Name of the chart, it will be the name of the canvas containing the graph
    * @param {string} chartTitle - Name of the chart, to display
*/
const addGraphHTML = (chartName, chartTitle, chartDescription, chartImgDescriptionPath) => {
    // Get cards section
    let cardsSection = document.querySelector(".cards");
    cardsSection.innerHTML += `
    <a href="#${chartName}-section">
        <section class="card">
            <img class="card-picture" src="${chartImgDescriptionPath}" alt="moon pictures">
            <div class="card-description">
                <span class="card-title">${chartTitle}</span>
                <span class="card-sub-description">${chartDescription}</span>
            </div>
        </section>
    </a>
    `
    // Get the first chart container in the page
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

/**
    * Plot a stacked bar chart of the birth per moon phase, with years stacked
    * @param {map} data - A map with years as key and the birth per moon phase as value
    * @param {list} labels - The labels for each bars of the chart
*/
const plotBirthChartMoon = (data, labels) => {
    // Get the canvas where to plot the chart
    let ctxBirthChartMoon = document.getElementById('birth-chart-moon').getContext('2d');
    let datasets = [];
    for (let [key, value] of Object.entries(data)) {
        datasets.push({
            label: key,
            data: value,
            stack: `${data.length}`,
            backgroundColor: "#388E8E",
            borderColor: "#388E8E",
        });
    }

    const birthMoonChartParam = {
        type: 'bar',
        data: {
            labels: labels,
            datasets: datasets,
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    stacked: true,
                },
                y: {
                    beginAtZero: true,
                    stacked: true,
                }
            }
            
        }
    };
    // Plot the graph
    return new Chart(ctxBirthChartMoon, birthMoonChartParam);
}

/**
    * Plot a graph of the premature deaths per months
    * @param {list} deces - List of the deaths for each months
 */
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

// Listen the button to change the graph disposition
document.getElementById("list-icon").addEventListener("click", () => toggleChartsDisposition("list"));
document.getElementById("grid-icon").addEventListener("click", () => toggleChartsDisposition("grid"));


const birth_moon_label = graph_data["birth_moon_label"];
const birth_moon_by_years = graph_data["birth_moon_by_years"];
const deaths = graph_data["deaths"];


// Adding graph to html, (adding section with a title and a canvas for the graph)
addGraphHTML("birth-chart-moon", "Naissance selon le cycle lunaire", "Un graphique des naissances en fonction de la phase lunaire", "/static/images/moon.jpg");
addGraphHTML("premature-deaths-by-months", "Morts Prématurés par mois", "Un graphique des morts en fonction des mois de l'année", "/static/images/death.jpg");


// Plot the graphs
let moonChart = plotBirthChartMoon(birth_moon_by_years, birth_moon_label);
prematureDeathsByMonths(deaths);