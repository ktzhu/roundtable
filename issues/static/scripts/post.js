jQuery.fn.delay = function(time,func){
    return this.each(function(){
        setTimeout(func,time);
    });
};

$(function() {

$(".submit").click(function() {

var name = $("#name").val();
var email = $("#email").val();
	var comment = $("#comment").val();
    var dataString = 'name='+ name + '&email=' + email + '&comment=' + comment;
	
	if(name=='' || email=='' || comment=='')
     {
    alert("Whoops. You didn't fill out the form!");
     }
	else
	{
	$("#flash").show();
	$("#flash").fadeIn(400).html('<img src="images/ajax-loader.gif" align="absmiddle">&nbsp;<span class="loading">Loading Post…</span>');
$.ajax({
		type: "POST",
  url: "postajax.php",
   data: dataString,
  cache: false,
  success: function(html){
 
  $("ol#update").append(html);
  $("ol#update li:last").fadeIn("slow");
  document.getElementById('email').value='';
   document.getElementById('name').value='';
    document.getElementById('comment').value='';
	$("#name").focus();
 
  $("#flash").hide();
	
  }
 });

$.ajax({
  type: "POST",
  url: "featureajax.php",
  data: dataString,
  cache: false,
  success: function(html) {
    $("#featchpost .info").fadeIn("slow");
    $("ul#recent").append(html);
    $("ul#recent").delay(5000, function(){$("ul#recent").fadeOut(5000)});
    document.getElementById('comment').value='';
  $("#flash").hide();
  }

});
 
}
return false;
	});
});