$(document).ready(function(){	//upom clicking "Get 100 tweets" button, display the below
	        // Get the modal

    var modal = document.getElementById('id01');

        // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    	if (event.target == modal) {
    		modal.style.display = "none";
    	}
    }

	$("#searchButton").click(function(data){
        //connect to API in Json format
		$.getJSON("http://localhost:5000/get_api", function(data){


            var items = [];
            //get search bar value
            var value = $("#searchBar").val();

            $.ajax({
                success: function(result){
                    $(".my-new-list").html('')
                    $.each(data, function(key, item){

                        //for all the items in the json data
                        for (var i = 0; i < item.length; i++) {
                            //if the value in the search bar matches transaction id, push details of that transaction
                            if(item[i].id==value) {
                                items.push('<li id= "'+ key + '">' + "ID" +": " + item[i].id + '</li>'+
                                           '<li id="' + key + '">' + "Date of transaction" +": "+ item[i].dateOfTransaction + "</li>" +
                                           '<li id="' + key + '">' + "Merchant" +": "+ item[i].merchant + "</li>" +
                                           '<li id="' + key + '">' + "Description" +": "+ item[i].description + "</li>" +
                                           '<li id="' + key + '">' + "Amount" +": "+ item[i].amount + " " + item[i].currencyCode + "</li>" + "<br>");
                                }

                            //if there is no value in the search bar push all the items
                            else if(value == ''){
                                items.push('<li id= "'+ key + '">' + "ID" +": " + item[i].id + '</li>'+
                                           '<li id="' + key + '">' + "Date of transaction" +": "+ item[i].dateOfTransaction + "</li>" +
                                           '<li id="' + key + '">' + "Merchant" +": "+ item[i].merchant + "</li>" +
                                           '<li id="' + key + '">' + "Description" +": "+ item[i].description + "</li>" +
                                           '<li id="' + key + '">' + "Amount" +": "+ item[i].amount + " " + item[i].currencyCode + "</li>" + "<br>");
                                }

                            }
                    });

                    $('<ul/>', {
                        'class': "my-new-list", html: items.join('')
                    }).appendTo('body');

            }});    

        });
	})
});