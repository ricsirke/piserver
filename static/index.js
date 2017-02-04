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
    
    
});





