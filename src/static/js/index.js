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
        // This function is needed to resized the chart
        resizeCharts();
    }

    else if (dispositionName === "grid")
    {
        document.documentElement.style.setProperty("--chart-width", "48%");
        // Resize the graphs
        resizeCharts();
    }
}


/**
    * Add a container for graph in the html in the charts container section
    * @param {string} chartName- Name of the chart, it will be the name of the canvas containing the graph
    * @param {string} chartTitle - Name of the chart, to display
    * @param {string} chartDescription - Description of the chart
    * @param {string} path to the image to represent the chart
    * @param {string} chartConclusion, a conclusion for the chart
*/
const addGraphHTML = (chartName, chartTitle, chartDescription, chartImgDescriptionPath, chartConclusion) => {
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
    </a>`

    // Get the first chart container in the page
    let chartContainerElement = document.querySelector(".charts-container");
    chartContainerElement.innerHTML += `
    <section id="${chartName}-section" class="chart-section">
        <h2 class="chart-title">${chartTitle}</h2>
        <div class="chart-description">
            <h3>Description</h3>
            ${chartDescription}
        </div>        
        <div class="chart-container">
            <canvas id="${chartName}"></canvas>
        </div>
        <div class="chart-conclusion">
            <h3>Conclusion</h3>
            ${chartConclusion}
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
        let color = `rgba(${(255-(key-1990)/30 * 150 )}, 100, ${((key-1990)/30 * 150 + 105)}, 1.0)`;
        datasets.push({
            label: key,
            data: value,
            stack: `${data.length}`,
            backgroundColor: color,
            borderColor: color,
            hoverBackgroundColor: color
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
            title: {
                display: false,
                text: "Naissances selon la phase lunaire"
            },
            legend: {
                labels: {
                    filter: () => {
                        return document.documentElement.clientWidth > 500;
                    }
                }
            },
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
    // Plot the graph and return it
    return new Chart(ctxBirthChartMoon, birthMoonChartParam);
}


/**
    * Plot a graph of the premature deaths per months
    * @param {map} prematureDeathsMontlyByYears - map of the prematureDeath with years as key and value a list of deaths by months with idx corresponding to the months in order
 */
function prematureDeathsByMonths(prematureDeathsMontlyByYears){

    let datasets = [];
    for (let [key, value] of Object.entries(prematureDeathsMontlyByYears))
    {
        let color = `rgba(${(255-(key-1990)/30 * 150)}, 150, ${((key-1990)/30 * 50 + 205)}, 1.0)`;
        datasets.push({
            label: key,
            data: value,
            stack: `${prematureDeathsMontlyByYears.length}`,
            backgroundColor: color,
            borderColor: color,
            hoverBackgroundColor: color
        });
    }
    
    let barChartData = {
        labels: ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],
        datasets: datasets
    };
    

    let ctxPrematureDeathsByMonths = document.getElementById("premature-deaths-by-months");
    return new Chart(ctxPrematureDeathsByMonths, {
        type: 'bar',
        data: barChartData,
        options: {
            title: {
                display: false,
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

/**
    * Plot a graph of the premature deaths per family
    * @param {list} labels - list of families names
    * @param {list} family_dead - List of the deaths for each family
    * @param {list} family_alive - List of the living for each family
*/

function prematureDeathsByFam(labels, family_dead, family_alive){
    
    let prematureDeathByFamData = 
    {
        labels: labels,
        datasets: [
            {
                type: 'bar',
                label: 'Décès Prématurés',
                id: "y-axis-0",
                backgroundColor: "rgba(50, 50, 200)",
                data: family_dead,
            },
            {
                type: 'bar',
                label: 'Vivants',
                id: "y-axis-0",
                backgroundColor: "rgba(120, 120, 255)",
                data: family_alive,
            }
        ]
    };
  
  
    let prematureDeathsByFamCanvas = document.getElementById("premature-deaths-by-family");
    return new Chart(prematureDeathsByFamCanvas, 
        {
            type: 'bar',
            data: prematureDeathByFamData,
            options: 
            {
                title: 
                {
                    display: true,
                    text: "Décès Prématurés par familles"
                },
                responsive: true,
                maintainAspectRatio: false,
                scales: 
                {
                xAxes: [
                    {
                        stacked: true
                    }],
                yAxes: [
                    {
                        stacked: true,
                        position: "left",
                        id: "y-axis-0",
                    }]
                }
            }
        }
    );
}


// Listen the button to change the graph disposition
document.getElementById("list-icon").addEventListener("click", () => toggleChartsDisposition("list"));
document.getElementById("grid-icon").addEventListener("click", () => toggleChartsDisposition("grid"));


const birth_moon_labels = graph_data["birth_moon_labels"];
const birthMoonByYears = graph_data["birth_moon_by_years"];
const prematureDeathsMontlyByYears = graph_data["premature_deaths_montly_by_months"];
const familiesLabels = graph_data["families_labels"];
const familiesDeaths = graph_data["families_deaths"];
const familiesAlives = graph_data["families_alives"];


// Adding graph to html, (adding section with a title and a canvas for the graph)
addGraphHTML(
    "birth-chart-moon",
    "Naissance selon le cycle lunaire",
    "<p>Ceci est un graphique des naissances par années en fonction de la phase de la lune</p> <p>Le graphique tente de confirmer / infirmer une croyance selon laquelle, il y aurait plus de naissances en phase de pleine lune </p>",
    "/static/images/moon.jpg",
    "En conclusion, on ne peut pas conclure qu'il y a plus de naissances en fonction de certaines phases de la lune"
);
addGraphHTML(
    "premature-deaths-by-months",
    "Morts Prématurés par mois",
    "<p>Ceci est un graphique des morts prématurés en fonction des mois de l'année pour toutes les années, le but de ce graphique est de constater si il y a une tendance dans les morts prématurés, si cela arrivent plus souvent certains mois que d'autres.</p>\n <p>NB: un veau mort prématurément est un veau qui est né avec la complication \"né prématurément\" et qui est mort dans les semaines après sa naissance</p>", 
    "/static/images/death.jpg"
);
addGraphHTML(
    "premature-deaths-by-family",
    "Morts Prématurés par familles",
    "<p>Ceci est un graphique des décès prématurés et des vivants pour chaque familles</p><p>Le graphique tente de voir si certaines familles ont des tendances génétique à avoir des morts prématurés</p> <p>NB: un veau mort prématurément est un veau qui est né avec la complication \"né prématurément\" et qui est mort dans les semaines après sa naissance</p>",
    "/static/images/vaches.jpg"
);

// Plot the graphs
let moonChart = plotBirthChartMoon(birthMoonByYears, birth_moon_labels);
prematureDeathsByMonths(prematureDeathsMontlyByYears);
prematureDeathsByFam(familiesLabels, familiesDeaths, familiesAlives);