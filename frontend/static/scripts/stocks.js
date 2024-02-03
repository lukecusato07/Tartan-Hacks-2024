console.log("loaded js");
var chosen_market;
var current_stocks;
var current_tickers;

function changeMarket() {
        chosen_market = document.getElementById("market_selector").value;

        fetch("https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/" + chosen_market)
        .then((response) => response.json())
        .then((json) => {
                current_stocks = json;
                current_tickers = current_stocks.map((stock) => stock.symbol);
                console.log(current_tickers);
                search_fill();
                document.getElementById('search_bar_div').classList.remove("d-none");
        })
        .catch((error) => {
                console.error("Fetch error:", error);
        });

        chosen_market = " " + chosen_market.split("/")[0].toUpperCase();
        document.getElementById("form_part_2_title"). innerHTML = chosen_market;
}

async function search_fill() {
        var select = document.getElementById('datalistOptions'); 
        await remove_prev_options(select);

        for(var i = 0; i < Object.keys(current_stocks).length; i++) {
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