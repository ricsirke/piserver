$(function(){

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

    


    var btnOnoffHandler = function(){
        var data = { "dev": "led", "op": "toogle" };
        doLedAjax(data);
    };


    var btnLedPlusHandler = function(){
        var data = { "dev": "led", "op": "setLum", "incr": 20 };
        doLedAjax(data);
    };


    var btnLedMinHandler = function(){
        var data = { "dev": "led", "op": "setLum", "incr": -20 };
        doLedAjax(data);
    };
    
    $("#btnOnoff").click(btnOnoffHandler);
    $("#btnLedPlus").click(btnLedPlusHandler);
    $("#btnLedMin").click(btnLedMinHandler);
    
    
    
    
});





