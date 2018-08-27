$('#ss').click(function(){
    var obj1 = {};
    obj1['date'] = $('#datepicker').val();
    for(var i = 1; i <= 12; i++){
        obj1['q'+i] = $('#q'+i+" input").val();
    }
    console.log(obj1);
    $.ajax({
    url:"http://localhost:3000/posts",
    type:"POST",
    data:JSON.stringify(obj1),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(){
       alert('done');
    }
});
});

$('#q1 input').on('input', function(){
     var self = $('#q1 input');
     var v = self.val();
    //  console.log(v);
    if(isNaN(v)){
        self.css("background-color", "#FFD0D0");
    }else{
        self.css("background-color", "white");
    }
});

$('#add').click(function(){
    var goal = $('#newg');
    var obj2 = {};
    obj2['title'] = goal.val();
    $('#glist').append('<li>'+goal.val()+'</li>');
    goal.val('');
    $.ajax({
        url:"http://localhost:3000/goals",
        type:"POST",
        data:JSON.stringify(obj2),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success: function(data, textStatus, jqXHR){
           alert('done');
        }
    });
});