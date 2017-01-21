$(function(){
    
    var btnOnoffHandler = function(){
        $.ajax({
            url: "http://localhost:5000/led",
            method: "POST",
            data: { "target": "led", "op": "toogle" },
            success: function(result){
                console.log(result);
                }
        })
    };
    
    $("#btnOnoff").click(btnOnoffHandler);
    
    
    
    
});





