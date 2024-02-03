console.log("loaded js");
var chosen_market;
var nasdaq_stocks, nyse_stocks, current_stocks;

const NASDAQ_URL = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_full_tickers.json";
const NYSE_URL = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_full_tickers.json";

function preloadData() {
    Promise.all([
        fetch(NASDAQ_URL).then(response => response.json()),
        fetch(NYSE_URL).then(response => response.json())
    ])
    .then(data => {
        nasdaq_stocks = data[0];
        nyse_stocks = data[1];
        console.log("Preloaded NASDAQ and NYSE data");
    })
    .catch(error => {
        console.error("Preload error:", error);
    });
}

function changeMarket() {
    chosen_market = document.getElementById("market_selector").value;

    // Use preloaded data based on chosen market
    current_stocks = chosen_market === "NASDAQ" ? nasdaq_stocks : nyse_stocks;

    search_fill();
    document.getElementById('search_bar_div').classList.remove("d-none");

    chosen_market = " " + chosen_market.split("/")[0].toUpperCase();
    document.getElementById("form_part_2_title").innerHTML = chosen_market;
}

async function search_fill() {
    var select = document.getElementById('datalistOptions'); 
    await remove_prev_options(select);

    for(var i = 0; i < current_stocks.length; i++) {
        var option = document.createElement('option');
        var name = current_stocks[i].name + " (" + current_stocks[i].symbol + ")";
        option.innerHTML = name;
        option.value = name;
        select.appendChild(option);
    }
}

function remove_prev_options(select) {
    while (select.options.length > 0) {                
        select.remove(0);
    }        
}

function show_submit_button() {
    document.getElementById('submit_button_div').classList.remove("d-none");
}

preloadData();
