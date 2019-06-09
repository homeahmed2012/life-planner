$.ajax({
        url:"http://localhost:3000/goals",
        type:"GET",
        success: function(data, textStatus, jqXHR){
           for(var i = 0; i < data.length; i++){
            $('#glist').append('<li>'+data[i].title+'</li>');
           }
        }
});