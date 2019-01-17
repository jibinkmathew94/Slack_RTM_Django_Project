function upvote(event){
	console.log("chakka");
	console.log(event.currentTarget.dataset.id);
	data = JSON.stringify({ data: event.currentTarget.dataset.id })
	console.log(data);
  $.ajax({
  type: "POST",
  url: 'upvote',
  data: data,
  success: function(data){
	console.log(data);
  }
});
}