// utils
function __getEl(id){
        return document.getElementById(id);
    }


// led
$(function(){ 
    var doLedReq = function(data){
        var r = new XMLHttpRequest();
        
        r.open( "POST" , "/led", true);
        r.setRequestHeader('Content-type', 'application/json');
        r.send(JSON.stringify(data));
        
        r.onreadystatechange = function () {
		if (r.readyState == 4 && r.status == 200) {
			//data = r.responseText;
            //alert(data);
		}
		else if (r.readyState == 4 && r.status == 500) {
			alert ("server error");
			return;
		}
		else if (r.readyState == 4 && r.status != 200 && r.status != 500 ) { 
			alert ("Something went wrong!   status:" + r.status);
			return; }
        }
    }

    __getEl("btnLedStop").onclick = function(){
        var data = { "dev": "led", "op": "stop" };
        doLedReq(data);
    };

    __getEl("btnOnoff").onclick = function(){
        var data = { "dev": "led", "op": "toogle" };
        doLedReq(data);
    };

    __getEl("btnLedPlus").onclick = function(){
        var data = { "dev": "led", "op": "setLum", "incr": 20 };
        doLedReq(data);
    };

    __getEl("btnLedMin").onclick = function(){
        var data = { "dev": "led", "op": "setLum", "incr": -20 };
        doLedReq(data);
    };
    
    __getEl("btnStrob").onclick = function(){
        // not the best source TODO
        var spd = parseInt(__getEl("strobVal").innerHTML);
        var data = { "dev": "led", "op": "strob", "spd": spd };
        doLedReq(data);
    };
    
    __getEl("rngStrobVal").onchange = function(){
        __getEl("strobVal").innerHTML=this.value;
    };
});


// temphum
$(function(){
    function onTempHumLoad(){
            var temphum = JSON.parse(this.responseText);
            
            __getEl("temp").innerHTML = temphum.temp;
            __getEl("hum").innerHTML = temphum.hum;
            
            console.log(this.responseText);
        }
    
    var doTempHumXhr = function(){
        var r = new XMLHttpRequest();
        
        r.addEventListener("load", onTempHumLoad);
        r.open( "GET" , "/temphum", true);
        r.send();
    };
    
    doTempHumXhr();
    
    __getEl("btnTempHumRefresh").onclick = function(){
        doTempHumXhr();
    };
    
    var data = [
        {"hum": 22.5, "t": "2017-02-04 11:30:01.554436", "temp": 22.5},
        {"hum": 22.5, "t": "2017-02-04 12:00:01.554436", "temp": 22.0},
        {"hum": 22.5, "t": "2017-02-04 12:30:01.554436", "temp": 22.0},
        {"hum": 22.5, "t": "2017-02-04 13:00:01.554436", "temp": 22.5},
        {"hum": 22.5, "t": "2017-02-04 13:30:01.554436", "temp": 23.0},
        {"hum": 22.5, "t": "2017-02-04 14:00:01.554436", "temp": 23.0},
        {"hum": 22.5, "t": "2017-02-04 14:30:01.554436", "temp": 23.0},
        {"hum": 22.5, "t": "2017-02-04 15:00:01.554436", "temp": 23.5},
        {"hum": 22.5, "t": "2017-02-04 15:30:01.554436", "temp": 23.5},
        {"hum": 22.5, "t": "2017-02-04 16:00:01.554436", "temp": 24.0},
    ];
    
    data = data.map(function(d){
        d["t"] = new Date(d["t"]);
        return d;
    })
    
    var svg = d3.select("svg"),
        margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")"),
        x_ax = d3.scaleTime()
                 .rangeRound([0, width])
                 .domain(d3.extent(data, function(d){ return d["t"]; })),
        y_ax = d3.scaleLinear()
                 .rangeRound([0, height])
                 .domain(d3.extent(data, function(d){ return d["temp"]; })),
        lineGen = d3.line()
                    .x(function(d){ return x_ax(d["t"]); })
                    .y(function(d){ return y_ax(d["temp"]); });
              
        // line draw      
        g.append("path")
         .datum(data)
         .attr("fill", "none")
         .attr("stroke", "steelblue")
         .attr("stroke-linejoin", "round")
         .attr("stroke-linecap", "round")
         .attr("stroke-width", 1.5)
         .attr("d", lineGen);
        
        // x axis draw
        g.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x_ax))
        // .select(".domain")
          // .remove();
        
        // y axis draw
        g.append("g")
          .call(d3.axisLeft(y_ax))
        .append("text")
          .attr("fill", "#000")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .text("Temperature");
});





