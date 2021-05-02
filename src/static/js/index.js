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
        <span class="chart-description">${chartDescription}</span>        
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
    // Plot the graph
    return new Chart(ctxBirthChartMoon, birthMoonChartParam);
}

/**
    * Plot a graph of the premature deaths per months
    * @param {list} deaths - List of the prematures deaths for each months, for instance [0, 2, ......] corresponds to 0 death in january, 2 deaths in february, ....
 */
function prematureDeathsByMonths(deaths){
    
    let barChartData = {
        labels: ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],
        datasets: [{
            type: 'bar',
            label: 'Décès Prématurés',
            id: "y-axis-0",
            backgroundColor: "red",
            data: deaths
        }]
    };


    let ctxPrematureDeathsByMonths = document.getElementById("premature-deaths-by-months");
    return new Chart(ctxPrematureDeathsByMonths, {
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

/**
    * Plot a graph of the premature deaths per family
    * @param {list} family_dead - List of the deaths for each family
    * @param {list} family_alive - List of the living for each family
    * Non fini !
*/

function prematureDeathsByFam(family_dead, family_alive){
    
    var barChartData = 
    {
        labels: ['Galak','Réglisse','Myrtille','Vincent','Panade','Rubarbe','Bimbo','Nostalgie','Nubia','Margot','Nourrice','Orange','Olympe','Ford','Ruby','Cote d’Or','Sorbet','Paupiette','Nounou','Odile','Oasis','Potache','Nash','Mirabelle','Pascaline','Renaud','Neslie','Ayham','Minnie','Narcisse','Maserati','Origami','Paula','Mamamia','Peluche','Nima','Clarabelle','Onyx','Papyrus','Nancy','Mushroom','Nassma','Ferraris','Madona','Jonquille','Citron','Pissenlit','Pink','Météorite','Saturne','Madi','Moon','Meringue','Ovalie','Oreo','Majestic','Bessie','Micheline','Mazda','Mastar','Ciboulette','Motorola','Plume','Panda','Agapanthe','Nitendo','Provence','Céline','Perle','Nora','Moka','Poire','Olive','Pomme','Ophélie','Norma','Lindt','Mercedes','Trompette','Ocarina','Oméga','Betty','Pupuce','Pamela','Blondie','Citroenne','Nya','Ninon','Mélasse','Nolvenn','Orage','KitKat','Moussaka','Summer','Nice','Tournesol','Noisette','Ophia','Paquerette','Banane','Midas','Ninette','Mystic','Caprice','Dottie','Origan','Mimosa','Ollande','Naomi','Snow','Star','Numerobis','Mosaic','Nuggets','Sonette','Kinder','Lotus','Nadine','Benoît','Orchidée','Okaly','Malaisie','Milka','Nela','Penny','Rustique','Fraise','Normande','Blanche','Moutarde','Macaroni','Moselle','Mandala','Margueritte','Neptune','Papaye','Maite','Naza','Toblerone','Rosette','Iris','Nairobi','Mina','Raymonde','Otaria','Sauterelle','Sidonie','Prune','Bleuet','Noire','Magma','Sky','Fiesta','Neda','Jeep','Nouille','Lila','Nina','Nathalia','Tonnerre','Lavande','Naya','Nilla','Hélène','Unknown'],
        datasets: [
            {
                type: 'bar',
                label: 'Décès Prématurés',
                id: "y-axis-0",
                backgroundColor: "green",
                data: family_dead,
            },
            {
                type: 'bar',
                label: 'Vivants',
                id: "y-axis-0",
                backgroundColor: "blue",
                data: family_alive,
            }
        ]
    };
  
  
    var ctx = document.getElementById("premature-deaths-by-family");
    var ch = new Chart(ctx, 
        {
            type: 'bar',
            data: barChartData,
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
        });
}

// Listen the button to change the graph disposition
document.getElementById("list-icon").addEventListener("click", () => toggleChartsDisposition("list"));
document.getElementById("grid-icon").addEventListener("click", () => toggleChartsDisposition("grid"));


const birth_moon_label = graph_data["birth_moon_label"];
const birth_moon_by_years = graph_data["birth_moon_by_years"];
const deaths = graph_data["deaths"];
const family_dead = graph_data["family_dead"];
const family_alive = graph_data["family_alive"];


// Adding graph to html, (adding section with a title and a canvas for the graph)
addGraphHTML(
    "birth-chart-moon",
    "Naissance selon le cycle lunaire",
    "Un graphique des naissances en fonction de la phase de la lune, ce graph est la pour confirmer ou infirmer une croyance selon laquelle, il y aurai plus de naissances en phase de pleine lune",
    "/static/images/moon.jpg"
);
addGraphHTML(
    "premature-deaths-by-months",
    "Morts Prématurés par mois",
    "Un graphique des morts prématurés en fonction des mois de l'année, une veau mort prématurérément est un veau qui est né prématurément et mort dans les semaines après celle-ci", 
    "/static/images/death.jpg"
);
addGraphHTML(
    "premature-deaths-by-family",
    "Morts Prématurés par familles",
    "Un graphique des décès prématurés et des vivants pour chaque familles",
    "/static/images/vaches.jpg"
);

// Plot the graphs
let moonChart = plotBirthChartMoon(birth_moon_by_years, birth_moon_label);
prematureDeathsByMonths(deaths);
prematureDeathsByFam(family_dead, family_alive);