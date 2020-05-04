

function submit_by_category(cat_value) {
  cat_value = cat_value.getAttribute('value');
  // $('#category_srch_form').remove('<input>');
  var input = $("<input>")
             .attr("type", "hidden")
             .attr("name", "browse_category").val(cat_value);
  $('#category_srch_form').append(input);
  $("#category_srch_form").submit();
  // console.log(cat_value);
  // console.log("called");
}
$(document).ready(function(){

  // $("#cat_bttn").click(function(){
  //   $('#category_srch_form').remove('<input>');
  //   console.log($(this).attr('value'));
  //   var input = $("<input>")
  //              .attr("type", "hidden")
  //              .attr("name", "browse_category").val($(this).attr('value'));
  //   $('#category_srch_form').append(input);
  //   $("#category_srch_form").submit();
    // $.ajax({
    //     url: $("#category_srch_form").attr('action'),
    //     type: 'post',
    //     dataType: 'json',
    //     data: $('form#myForm').serialize(),
    //     success: function(data) {
    //                // ... do something with the data...
    //              }
    // });
  // });

});
