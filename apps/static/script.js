$(document).ready(function() {
    $('form').on('submit', function(event) {       
      $.ajax({
         data : {
            value1 : $('#value1').val(),            
                },
            type : 'POST',
            url : '/process'
           })           
       .done(function(data) {                 
        $('#input_is').text(data['response']).show();      
     });
     event.preventDefault();
     });     
});