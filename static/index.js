$(function(){
    function __getEl(id){
        return document.getElementById(id);
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

    


    __getEl("btnOnoff").onclick = function(){
        var data = { "dev": "led", "op": "toogle" };
        doLedAjax(data);
    };


    __getEl("btnLedPlus").onclick = function(){
        var data = { "dev": "led", "op": "setLum", "incr": 20 };
        doLedAjax(data);
    };


    __getEl("btnLedMin).onclick = function(){
        var data = { "dev": "led", "op": "setLum", "incr": -20 };
        doLedAjax(data);
    };
    
    
});





