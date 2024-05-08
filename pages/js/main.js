// header and footer

$(function() {
    $("#header").load("header.html");
    $("#footer").load("footer.html");
});

// header and footer



window.onload = function () {
    pieChartDraw();
}


// annual calendar start

// Get all elements with the specified class name
var elements = document.getElementsByClassName('annual_calendar');

// Iterate through each element and perform appendChild
for (var i = 0; i < elements.length; i++) {
    let colStyle = 'width:12px; height:13px; background-Color:#b3b3b3; border-radius:2px;';

    // get information of current date
    let today = new Date();

    let today_day = today.getDay();
    console.log(today_day);

    // create default annual calander
    tbody = document.createElement('table');
    tbody.style = 'border-spacing:5px;';

    const day_arr = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'];
    const week_arr = [];

    for(let i=0; i<52; i++) {
        week_arr.push(i);
    }

    for(let i=0; i<day_arr.length; i++) {
        let row = document.createElement('tr');
        row.className = day_arr[i];

        for(let j=0; j<week_arr.length; j++) {

            if(j>50) {
                if(i>today_day) {
                    break;
                }
            }

            let col = document.createElement('td');
            col.className = week_arr[j] + ', ' + day_arr[i];

            col.style = colStyle;
            row.appendChild(col);
        }

        tbody.appendChild(row);
    }

    elements[i].appendChild(tbody);
}

// annual calendar end




// ajaxs
function handleClick() {
    // You can add more JavaScript functionality here

    console.log("clicked!");

    $.ajax({
        method:"GET",
        url:"http://0.0.0.0:8000/readAllDisciplines",
        success : function(response) {
            console.log(response)
        }
    })
}







// pie chart start

let pieChartData = {
    labels: ['NVDA', 'NASDAQ', 'CASH', 'AAPL', 'AMD', 'MSFT'],
    datasets: [{
        data: [14, 15, 11, 1, 1, 1],
        backgroundColor: ['rgb(255, 99, 132)', 'rgb(255, 159, 64)', 'rgb(255, 205, 86)', 'rgb(75, 192, 192)', 'rgb(54, 162, 235)', 'rgb(153, 102, 255)']
    }] 
};

let pieChartDraw = function () {
    let ctx = document.getElementById('pieChartCanvas').getContext('2d');
    
    window.pieChart = new Chart(ctx, {
        type: 'pie',
        data: pieChartData,
        options: {
            responsive: false
        }
    });
};

function get_price_with_ticker() {
    console.log('clicked')
    

    $.ajax({
        method:"GET",
        url:"http://127.0.0.1:8000/prices/"+"nvda,aapl",
        success : function(response) {
            console.log(response)
        }
    })
}

// pie chart end