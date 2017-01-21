$(function(){
    function __getEl(id){
        return document.getElementById(id);
    }

    var doLedXhr = function(data){
        var r = new XMLHttpRequest();
        r.open( "POST" , "/led", true);
        
        //params = '=' + data + '&amp;pwd=' + data
        r.send(data);
        
        r.onreadystatechange = function () {
		if (r.readyState == 4 && r.status == 200) {
			data = r.responseText;
			alert(data);
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
    
    
});





