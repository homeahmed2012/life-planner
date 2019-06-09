var counter  = 1;

$('#ss').click(function () {
    $('#tasks').append("<li class='list-group-item justify-content-between col-3'>"+ $('#name').val() + " : <span class='badge badge-default badge-pill' id='"+counter+"'>" + $('#time').val() +"</span> "+"</li>");
    var scounter = counter;
    counter += 1;
    var myVar = setInterval(function () {
        var count = $('#'+scounter).html();
        if(count > 0 ){
            $('#'+scounter).html(count-1);
        }else{
            clearInterval(myVar);
        }
    }, 1000);
});

