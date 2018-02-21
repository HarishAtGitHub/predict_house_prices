$( document ).ready(function() {
$('#estimatorform').submit(function(event) {
event.preventDefault();
    $.ajax({
        url: '/ml/api/v1.0/price',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
        bedrooms: jQuery("#bedrooms").val(),
        bathrooms: jQuery("#bathrooms").val(),
        sqft_living: jQuery("#sqft_living").val(),
        sqft_lot: jQuery("#sqft_lot").val(),
        floors: jQuery("#floors").val(),
        zipcode: jQuery("#zipcode").val()
        }),
        success: function(data) {
                   jQuery('.pricenumber').text(data)
        },
        error: function(xhr, resp, text) {
             console.log(xhr, resp, text);
        }
    });
});
})