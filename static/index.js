$(function(){
    function __getEl(id){
        return document.getElementById(id);
    }

    var doLedXhr = function(data){
        var r = new XMLHttpRequest();
        
        r.open( "POST" , "/led", true);
        r.setRequestHeader('Content-type', 'application/json');
        r.send(JSON.stringify(data));
        
        r.onreadystatechange = function () {
		if (r.readyState == 4 && r.status == 200) {
			data = r.responseText;
			// returns "ok"
            //alert(data);
		}
		//test if fail
		else if (r.readyState == 4 && r.status == 500) {
			alert ("server error");
			return ("fail");
		}
		//else 
		else if (r.readyState == 4 && r.status != 200 && r.status != 500 ) { 
			alert ("Something went wrong!   status:" + r.status);
			return ("fail"); }
	}
    }

    var doLedAjax = function(data){
	$.ajax({
            url: "http://localhost:5000/led",
            method: "POST",
            data: data,
            success: function(result){
                console.log(result);
                }
        })
    };

    var doLedReq = function(data){
        doLedXhr(data);
    }


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





