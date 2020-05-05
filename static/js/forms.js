

function submit_by_category(cat_value) {
  // Excecutes on click browse by category
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

function show_project_details(project) {
  // $('#category_srch_form').remove('<input>');
  card = "<div class='card mb-3'><div class='card-body'><h5 \
  class='card-title'>Card title</h5><p class='card-text'>\
  This is a wider card with supporting text below as a natural\
   lead-in to additional content. This content is a little bit \
   longer.</p><p class=card-text'><small class='text-muted'>\
   </small></p></div></div>";
  $(project).closest('div-proj').append(card);
  // console.log(cat_value);
  // console.log("called");
}

$(document).ready(function(){

});
