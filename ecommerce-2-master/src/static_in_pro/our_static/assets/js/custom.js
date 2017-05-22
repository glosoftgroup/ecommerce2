    
function addTocart(id, name, imageurl, id2){
    var item_name = name;
    var imagepath = imagepath;
    $.ajax({
        type: "GET", // "POST"
        url: "{% url 'cart' %}",
        data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                item: id2,
                qty:1
        },
        success: function(data) {
            console.log(data);
            updateCartItemCount();
            updateMinicart();
            $('.p-message').html(data.flash_message);
            $('.p-namex').html('Name: '+ name);
            $('.p-imagex').attr('src', imageurl);
            $('.p-price').html('Price: KShs'+ data.line_total);
            $('.p-quantity').html('Qty: '+data.item_quantity);

            $('#myModal').modal();
            toastr.success(data.flash_message, 'Success', { showDuration: 2000,hideDuration: 1000, timeOut: 2000,});           
        }, 
        error: function(response, error) {
            // console.log(response)
            console.log(error);
            toastr.error('cannot process', 'Error', {timeOut: 500});
        }
    });        
}
function updateCartItemCount(){
    var badge = $("#notify");
    var my_count = $("#my-count");

    $.ajax({
        type: "GET",
        url: "{% url 'item_count' %}",
        success: function(data){
            badge.text(data.count);
            // console.log(data.count);
            my_count.text(data.count);
            /**- if cart qty is 0-**/
            if(data.count == 0){
              $('.cart-block-content').fadeOut(function(){
                $('.cart-block-content').html('Cart is empty').fadeIn();
              });                 
            }
        },
        error: function(data, error) {
            console.log(data);
            console.log(error);
        }

    });

 }
function updateMinicart(){      
    $(".cart-block").html('&nbsp;').load("{% url 'minicart' %}");
}
function removeCartItem(id){
    // alert(id);
    $.ajax({
        type: "GET",
        url: "{% url 'cart' %}",
        data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                item: id,
                qty:1,
                delete:'True'
        },
        success: function(data){
            var item_id = $(".remove-item-"+id);
            item_id.fadeOut(function(){
                updateCartItemCount();
                $('.total-price').html(data.subtotal);
                // $('.cart-title').html(data.count + ' Items in my cart');
                // updateMinicart();
            });

            // alert('deleted')
            console.log('deleted');
        },
        error: function(data, error) {
            console.log(data);
            console.log(error);
        }

    });
}
