

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

function popup_proj_details(btn){
  var data = JSON.parse( btn.parentNode.querySelectorAll('script')[0].innerHTML);
  $('.proj-title-pop').text(data.title);
  var text_arr = data.text.split('. ');
  $('.proj-text-pop').empty();
  for (var i = 0; i < text_arr.length; i+=5) {
    var p = document.createElement('p');
    p.setAttribute( "class", "para-tab" );
    var text = text_arr.slice(i, i+5).join('. ');
    if (text.slice(-1) != '.'){
      text = text+".";
    };
    p.innerHTML = text;
    $('.proj-text-pop').append(p);

  }
  $('.proj-img').attr('src', data.image);
  $('.devpost-btn').attr('href', data.url);
  handleTarget($('.devpost-btn'));
  // console.log(data);
}

function handleTarget(btn){
  //change target between _blank and "" based on screen size
  if (window.matchMedia('(max-width: 700px)').matches) {
      btn.setAttribute("target", "");
    console.log(btn.href);
  };
}

// function popup_proj_details(btn){
//   // data = btn.getAttribute('value');
//   //
//   // // console.log(data);
//   // if (data.slice(-1) != '}'){
//   //   data = data.concat('" }')
//   // };
//   // // console.log(data)
//   // // data = JSON.parse(data);
//
// }

function show_project_details_test(project) {
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
  if (window.matchMedia('(max-width: 700px)').matches) {
    $("a").each(function() {
      this.setAttribute("target", "");
    //Do your work
    console.log(this.href);
    })

        // $('.yourselector').attr(target,'')
    }

  // $(document).on('click','.proj-more',function(){
  //   var data = $(this).attr('value');
  //   data = JSON.parse(data);
  //   $('.proj-title-pop').text(data.title);
  //   $('.proj-text-pop').text(data.text);
  //   console.log(data);
  // });

});
