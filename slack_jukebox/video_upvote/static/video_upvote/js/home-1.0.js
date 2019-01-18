function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
        }
    }
});

function upvote(event){
	console.log($('[name="csrfmiddlewaretoken"]').val())
	console.log("chakka");
	console.log(event.currentTarget.dataset.id); 
	elm = $(event.currentTarget);
	if(elm.hasClass("active")){    //upvote button changing css
		data = JSON.stringify({
			data: event.currentTarget.dataset.id,
			vote: 'down'			//undo previous vote
		});
	}
	else {
		data = JSON.stringify({
			data: event.currentTarget.dataset.id,
			vote: 'up'				////vote
		});
	}
  $.ajax({
  type: "POST",
  url: '/upvote',
  data: data,
  success: function(response){
  	console.log(response.data);
	if(response.data == "vote added"){
		elm.addClass("active");
	}
	else if(response.data == "vote removed"){
		elm.removeClass("active");
		elm.addClass("upvote")

	}
	else if(response.data == "invalid login"){
		alert("Please login to vote");
	}
  }
});
}

function showUpvotes(event){
	console.log("event");
	$('#'+event.currentTarget.dataset.target).show();
	 //show upvote list
	 event.stopPropagation();
	event.preventDefault();
}
$('.upvote-list-container').click(function(event){
	event.stopPropagation();
});

document.addEventListener("click", function(event){
  $('.upvote-list-container').hide();
});